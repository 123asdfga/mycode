1.opencv4.5 (ubuntu安装命令配置cuda)


cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local/opencv-4.5.0 -D BUILD_SHARED_LIBS=ON  -D OPENCV_EXTRA_MODULES_PATH=/home/ubuntu/opencv-4.5.0/opencv_contrib-4.5.0/modules -D CUDA_CUDA_LIBRARY=/usr/local/cuda/lib64/stubs/libcuda.so -D CUDNN_INCLUDE_DIR=/usr/local/cuda/include -D CUDNN_LIBRARY=/usr/local/cuda/lib64/libcudnn.so -D WITH_CUDA=ON -D CUDA_ARCH_BIN="6.1" -D WITH_TBB=ON -D WITH_V4L=ON -D INSTALL_C_EXAMPLES=ON -D BUILD_EXAMPLES=OFF -D WITH_OPENGL=ON -D ENABLA_FAST_MATH=1 -D CUDA_FAST_MATH=1 -D WITH_CUBLAS=1 -D WITH_NVCUVID=ON -D BUILD_opencv_cudacodec=OFF -D BUILD_PNG=ON -D WITH_PNG=ON -D BUILD_JPEG=ON -D WITH_JPEG=ON -D BUILD_JASPER=ON -D WITH_JASPER=ON -D BUILD_TIFF=ON -D WITH_TIFF=ON -D BUILD_ZLIB=ON -D WITH_GSTREAMER=OFF -D WITH_1394=OFF -D OPENCV_ENABLE-NONFREE=ON -D OPENCV_GENERATE_PKGCONFIG=ON -D CUDA_nppicom_LIBRARY=stdc++ ..


2. 要求ffmpeg正确安装和环境配置（ffmpeg安装不完全cmake报错）

3.行人目标检测视频demo制作过程

（1）用目标检测算法（yolox >yolov5>目前使用检测算法）生成trajectory文件（trajectory:行人轨迹文件包含检测框）

（2）利用reid标注文档相关代码进行视频数据的切分
（3）利用track_img_1.py代码把检测框抠出来保存为一个一个id的形式，相同id在一个文件夹中
（4）把错分的id进行清洗操作，保证一个id下面是同一个人

（5）verification生成清洗后的trajectory文件
 
 (6)根据2生成的图片（待检测框）查找算法未检测的行人，对trajectory文件进行添加（5帧之内行人的检测框大致相等差距不大）

