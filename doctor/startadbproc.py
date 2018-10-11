# coding:utf-8
import psutil
import os
import subprocess

ads = 'adb shell tail -f /tmp/dingdong.log'
subprocess.Popen(ads, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
