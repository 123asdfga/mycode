#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 09:57:31 2022

@author: ubuntu
"""
from sanic import Sanic
from sanic.response import json

app = Sanic("hello_example")

@app.route("/")
async def test(request):
  return json({"hello": "world"})

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000)
