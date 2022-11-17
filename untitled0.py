#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 15:03:09 2022

@author: ubuntu
"""
#!/usr/bin/python2
# -*- coding: utf-8 -*-
# vim: expandtab:ts=4:sw=4
# --------------------------------------------------------
# Author  : Long
# Desc    : upto u
# File    : counter_sample.py
# Software: PyCharm
# Time    : 18-10-29
# Copyright (c) Linkdome Inc.
# --------------------------------------------------------
import math


class LineCounterAntiWander():
    def __init__(self, lines, trust_frames=3, ignore_frames=10, group_time=50):
        # liens = [[line_id, x, y, x, y, x, y], ...]
        self.__cnt_dict = {}
        self.lines = lines
        self.trust_frames = trust_frames
        # self.ignore_frames = ignore_frames
        self.group_time_frames = group_time
        self.cnt_group = {}
        self.crossgroup_result = {}     # [['last_pass_frame_id','cross_id1','cross_id2',...]]
        self.quick_pass_track_id = {}     # {track_id:[start_frame,pass_frame]}
        self.opposite_direction_track_ids = {}
        self.cnt = {}
        self.cross_ids = {}
        self.cross_ids_anti = {}
        self.cross_result = []
        self.cross_result_frame = []
        self.ids_do_cnt = []
        self.ids_to_del = []
        self.ids_wanderer = []
        self.frame_idx = 0
        self.line_ids = []
        # init values
        for line in enumerate(lines):
            line_id = line[0]
            self.line_ids.append(line_id)
            self.cnt.update({line_id: {'enter': 0, 'exit': 0}})
            self.__cnt_dict.update({line_id: {}})
            self.cross_ids.update({line_id: {'enter_ids': [], 'exit_ids': []}})
            self.cross_ids_anti.update({line_id: {'enter_ids': [], 'exit_ids': []}})

            self.cnt_group.update({line_id: 0})
            self.crossgroup_result.update({line_id: []})
        pass

    def get_counter_number(self):
        # {
        #     line_id:
        #         {
        #             'enter_num': 100,
        #             'exit_num': 90,
        #         }
        #     ...
        # }
        return self.cnt.copy()

    def get_cross_result_frame(self):
        # [int(track_id), line_id, self.frame_idx, int(det_idx),0]
        # 0 exit 1 enter
        return self.cross_result_frame

    def remove_cross_result_frame(self,item):
        # item = [int(track_id), line_id, self.frame_idx, int(det_idx),0]
        # 0 exit 1 enter
        self.cross_result_frame.remove(item)
        return True

    def get_current_crossed_ids(self):
        # {
        #     line_id:
        #         {
        #             'enter_ids':[],
        #             'exit_ids':[],
        #         },
        #     ...
        # }
        return self.cross_ids.copy()

    def get_cnt_group(self):
        return self.cnt_group.copy()

    def get_quick_pass_track(self):
        return self.quick_pass_track_id.copy()

    def get_opposite_direction_track(self):
        return self.opposite_direction_track_ids

    def free(self):
        self.__cnt_dict.clear()
        self.cnt.clear()
        self.cross_ids.clear()
        self.cross_ids_anti.clear()

        self.cnt_group.clear()
        self.crossgroup_result.clear()
        self.quick_pass_track_id.clear()
        self.opposite_direction_track_ids.clear()

    def update(self, track_output, frame_idx, track_start_time, pass_time_frames):
        # print track_output
        self.__update_cnt_dict(track_output, frame_idx, track_start_time, pass_time_frames)
        self.__count()
        # print self.get_counter_number()
        # print self.get_current_crossed_ids()

    def __update_cnt_dict(self, track_output, frame_idx, track_start_time, pass_time_frames):
        self.frame_idx = frame_idx
        self.ids_do_cnt = []
        self.ids_to_del = []
        self.track_start_time = track_start_time
        self.pass_time_frames = pass_time_frames

        track_ids = track_output.keys()
        for track_id in track_ids:
            current_track_dict = track_output.get(track_id).get(frame_idx)
            if current_track_dict.get('state') != 2 or current_track_dict.get('update_times') > 0:
                if current_track_dict.get('state') == 3:
                    self.ids_to_del.append(track_id)
                continue
            self.ids_do_cnt.append(track_id)
            track_box = current_track_dict.get('track_box')  # [x,y,w,h]
            # cx = track_box[0] + track_box[2] / 2.
            # cy = track_box[1] + track_box[3] / 2.
            cx = track_box[0] + (track_box[2]-track_box[0])/ 2.
            cy = track_box[1] + (track_box[3]-track_box[1]) / 2.
            # updated_times = int(current_track_dict.get('updatetimes'))
            for line_id in self.line_ids:
                line_tracks_dict = self.__cnt_dict.get(line_id)
                if track_id in line_tracks_dict.keys():
                    track_dict_tmp = line_tracks_dict.get(track_id)
                    track_dict_tmp['last_cx'] = track_dict_tmp['current_cx']
                    track_dict_tmp['last_cy'] = track_dict_tmp['current_cy']
                    track_dict_tmp['current_cx'] = cx
                    track_dict_tmp['current_cy'] = cy
                    track_dict_tmp['confirm_frames'] += 1
                    track_dict_tmp['det_idx'] = current_track_dict.get('det_idx')
                else:
                    # Determine if the track frame is lost near the front of the people wandering around the line, and rebuilt near the line
                    if self.point2line_distance(cx,cy, frame_idx) ==1 and track_id in self.ids_do_cnt:
                        self.ids_do_cnt.remove(track_id)
                        continue

                    # created new track_id info
                    track_dict_tmp = \
                        {
                            'last_cx': cx,
                            'last_cy': cy,
                            'current_cx': cx,
                            'current_cy': cy,
                            'confirm_frames': 0,
                            'enter_frame_idxs': [],
                            'exit_frame_idxs': [],
                            'unconfirmed_enter_frame_idxs': [],
                            'unconfirmed_exit_frame_idxs': [],
                            'det_idx': 0,
                        }
                    line_tracks_dict.update({track_id: track_dict_tmp})
                pass
            pass
        pass  # for track_id in track_ids:

    def point2line_distance(self,x,y, frame_idx):
        # if frame_idx<100:
        #     return 0
        for line in self.lines:
            for j in range(1, len(line) - 2, 2):
                x1=line[j]
                y1=line[j + 1]
                x2=line[j + 2]
                y2=line[j + 3]
                numerator = (x - x1)*(x2 -x1) + (y - y1)*(y2 - y1)  
                if(numerator <=0): #left
                    distance = math.sqrt((x - x1)*(x - x1) + (y - y1)*(y - y1))
                denominator = (x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1)
                if(numerator >= denominator): #right
                    distance = math.sqrt((x - x2)*(x - x2) + (y - y2)*(y - y2))
                r = numerator / denominator # middle
                px = x1 + (x2 - x1) * r
                py = y1 + (y2 - y1) * r
                distance = math.sqrt((x - px)*(x - px) + (y - py)*(y - py))
                # if distance <50:
                #     return 1
                pass
            pass
        return 0

    def __count(self):
        self.cross_result_frame = []
        for line, line_id in zip(self.lines, self.line_ids):
            line_tracks_dict = self.__cnt_dict.get(line_id)
            # self.cross_ids.update({line_id: {'enter_ids': [], 'exit_ids': []}})
            #--------------------new strategy-------------------
            line_crossid_dict = self.cross_ids.get(line_id)
            #------------------------------------------
            #line_crossid_dict['enter_ids'] = []
            #line_crossid_dict['exit_ids'] = []
            line_crossid_dict_anti = self.cross_ids_anti.get(line_id)

            if line_tracks_dict == {}:
                continue

            # delete useless track_id
            for track_id in self.ids_to_del:
                if track_id in line_tracks_dict:
                    line_tracks_dict.pop(track_id)

            # for track_ids need to do counter
            for track_id in self.ids_do_cnt:
                track_dict_tmp = line_tracks_dict.get(track_id)
                x1 = float(track_dict_tmp.get('last_cx'))
                y1 = float(track_dict_tmp.get('last_cy'))
                x2 = float(track_dict_tmp.get('current_cx'))
                y2 = float(track_dict_tmp.get('current_cy'))
                det_idx = track_dict_tmp.get('det_idx')

                line_traj = [x1, y1, x2, y2]
                tmp = 0

                for j in range(1, len(line)-2, 2):
                    cnt_enter, cnt_exit = self.line_count(line_traj, line[j:j+4])
                    if track_dict_tmp.get('confirm_frames') > self.trust_frames:
                        if cnt_enter:
                            tmp += 1
                        elif cnt_exit:
                            tmp -= 1
                        else:
                            unconfirmed_enter_frames = track_dict_tmp.get('unconfirmed_enter_frame_idxs')
                            unconfirmed_exit_frames = track_dict_tmp['unconfirmed_exit_frame_idxs']
                            if len(unconfirmed_enter_frames)-len(unconfirmed_exit_frames) > 0:
                                tmp += 1
                            elif len(unconfirmed_enter_frames)-len(unconfirmed_exit_frames) < 0:
                                tmp -= 1
                            track_dict_tmp.update(
                                {
                                    'unconfirmed_enter_frame_idxs': [],
                                    'unconfirmed_exit_frame_idxs': [],
                                })
                    else:
                        if cnt_enter:
                            track_dict_tmp['unconfirmed_enter_frame_idxs'] += [self.frame_idx]
                            # track_dict_tmp['confirm_frames'] = -self.ignore_frames#not counting & reset ignore_frame

                        elif cnt_exit:
                            track_dict_tmp['unconfirmed_exit_frame_idxs'] += [self.frame_idx]
                            # track_dict_tmp['confirm_frames'] = -self.ignore_frames#not counting & reset ignore_frame

                ############################new strategy or change###########################
                if tmp > 0:

                    if track_id in line_crossid_dict_anti['exit_ids']:
                        self.cnt[line_id]['exit'] -= 1
                        line_crossid_dict_anti['exit_ids'].remove(track_id)
                        self.opposite_direction_track_ids[track_id] = [self.track_start_time[track_id],
                                                                       int(self.frame_idx)]
                    elif int(self.frame_idx) - self.track_start_time[track_id] < self.pass_time_frames and self.track_start_time[track_id] != 1:
                        self.quick_pass_track_id[track_id] = [self.track_start_time[track_id], int(self.frame_idx)]
                    else:
                        self.cnt[line_id]['enter'] += 1
                        # track_dict_tmp['confirm_frames'] = -self.ignore_frames
                        track_dict_tmp['enter_frame_idxs'] += [self.frame_idx]
                        line_crossid_dict['enter_ids'] += [track_id]
                        line_crossid_dict_anti['enter_ids'] += [track_id]
                        self.cross_result.append([int(track_id), line_id, self.frame_idx, 1])
                        self.cross_result_frame.append([int(track_id), line_id, int(self.frame_idx), int(det_idx),1])
                        if self.crossgroup_result[line_id] == []:
                            self.crossgroup_result[line_id].append([self.frame_idx, track_id])
                        elif int(self.frame_idx) - int(self.crossgroup_result[line_id][-1][0]) < self.group_time_frames:
                            self.crossgroup_result[line_id][-1].append(track_id)
                            self.crossgroup_result[line_id][-1][0] = self.frame_idx
                        elif track_id in self.crossgroup_result[line_id][-1]:
                            self.crossgroup_result[line_id][-1][0] = self.frame_idx
                        else:
                            self.crossgroup_result[line_id].append([self.frame_idx, track_id])
                        self.cnt_group[line_id] = len(self.crossgroup_result[line_id])
                elif tmp < 0:
                    if track_id in line_crossid_dict_anti['enter_ids']:
                        self.cnt[line_id]['enter'] -= 1
                        line_crossid_dict_anti['enter_ids'].remove(track_id)
                        for i in range(len(self.crossgroup_result[line_id])):
                            if track_id in self.crossgroup_result[line_id][i]:
                                self.crossgroup_result[line_id][i].remove(track_id)
                                if len(self.crossgroup_result[line_id][i]) ==1:
                                    self.crossgroup_result[line_id].pop(i)
                                    break
                        self.cnt_group[line_id] = len(self.crossgroup_result[line_id])
                    else:
                        self.cnt[line_id]['exit'] += 1
                        # track_dict_tmp['confirm_frames'] = -self.ignore_frames
                        track_dict_tmp['exit_frame_idxs'] += [self.frame_idx]
                        line_crossid_dict['exit_ids'] += [track_id]
                        line_crossid_dict_anti['exit_ids'] += [track_id]
                        self.opposite_direction_track_ids[track_id] = [self.track_start_time[track_id],
                                                                       int(self.frame_idx)]
                        self.cross_result.append([int(track_id), line_id, self.frame_idx, -1])
                        self.cross_result_frame.append([int(track_id), line_id, int(self.frame_idx), int(det_idx),0])
                    ##############################################################################
            self.cross_ids.update({line_id: line_crossid_dict})
            self.cross_ids_anti.update({line_id: line_crossid_dict_anti})
        pass  # for line, line_id in zip(self.lines, self.line_ids):

    @staticmethod
    def line_count(line1, line2):
        # line1 = [x1,y1,x2,y2] is two points continues trajectory
        # line2 = [x1,y1,x2,y2] is two points of counting line
        line1_x1 = float(line1[0])
        line1_y1 = float(line1[1])
        line1_x2 = float(line1[2])
        line1_y2 = float(line1[3])
        line2_x1 = float(line2[0])
        line2_y1 = float(line2[1])
        line2_x2 = float(line2[2])
        line2_y2 = float(line2[3])
        cnt_enter = 0
        cnt_exit = 0

        delta = float(line1_x2 - line1_x1) * (line2_y1 - line2_y2) - (line2_x1 - line2_x2) * (line1_y2 - line1_y1)
        if (delta <= 1e-6) and (delta >= -1e-6):
            return cnt_enter, cnt_exit

        beta = float(line2_x1 - line1_x1) * (line2_y1 - line2_y2) - (line2_x1 - line2_x2) * (line2_y1 - line1_y1)
        beta_on_delta = beta / delta
        if (beta_on_delta > 1) or (beta_on_delta < 0):
            return cnt_enter, cnt_exit

        miu = float(line1_x2 - line1_x1) * (line2_y1 - line1_y1) - (line2_x1 - line1_x1) * (line1_y2 - line1_y1)
        miu_on_delat = miu / delta
        if (miu_on_delat > 1) or (miu_on_delat < 0):
            return cnt_enter, cnt_exit

        D2 = (line2_y2 - line2_y1) * line1_x2 + (line2_x1 - line2_x2) * line1_y2 + (
            line2_x2 * line2_y1 - line2_x1 * line2_y2)
        D1 = (line2_y2 - line2_y1) * line1_x1 + (line2_x1 - line2_x2) * line1_y1 + (
            line2_x2 * line2_y1 - line2_x1 * line2_y2)
        if D2 < 0 or D1 > 0:
            cnt_enter = 1
        elif D2 > 0 or D1 < 0:
            cnt_exit = 1
        pass
        return cnt_enter, cnt_exit


# Test unit
if __name__ == "__main__":
    # TODO
    track_output = \
        {
            "10":
            {"5":
             {"timestamp": "02:22.12",
              "det_box": [1, 2, 3, 4],
              "state": 2,
              "updatetimes": 2,
              "track_box": [1, 2, 3, 4],
              "det_idx": "0",
              "confident": 0.2
              }
             },
        }
    # how to use
    lines = [[1092, 12, 123, 123, 123], [1088, 12, 123, 123, 123]]
    counter = LineCounter(lines, trust_frames=3, ignore_frames=10)
    for i in range(10):
        counter.update(track_output, frame_idx='1')

    print counter.get_counter_number()
    print counter.get_current_crossed_ids()

    pass

