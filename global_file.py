#!/usr/bin/env python
# -*- coding: utf-8 -*-

from paramiko import SSHClient
from time import sleep, strptime
from paramiko.client import AutoAddPolicy
from re import match
from hurry.filesize import size #<-- ทำไมต้องทำเองในเมื่อมีคนทำให้แล้ว
import re
import paramiko.transport
import datetime
import subprocess
import mysql.connector
import multiprocessing as mp
import requests
import asyncio
import time
import base64

### ดึง username และ password มาแปลงค่า
with open(r"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",'r') as user:
    user_convert = user.read().splitlines()
    file_user = '\n'.join(user_convert)
    decode_file_user = base64.b64decode(file_user).decode('utf-8')

with open(r"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",'r') as password:
    pass_convert = password.read().splitlines()
    file_pass = '\n'.join(pass_convert)
    decode_file_pass = base64.b64decode(file_pass).decode('utf-8')

### Function Timestamp & สร้างไฟล์ตามด้วย วันที่และเวลา ###
timestr = datetime.datetime.now()
time_stamp = str(timestr.strftime("%d-%m-%Y %X"))
create_file = "output_" + time_stamp + ".txt"

### Input ip file ###
### linux
with open(">Path for linux<",) as ip_ros:
    ip_list = ip_ros.read().splitlines()
    file_convert = '\n'.join(ip_list)
####################################################################################
### windows
#with open(">Path for windows<",) as ip_ros:
#    ip_list = ip_ros.read().splitlines()
#    file_convert = '\n'.join(ip_list)
####################################################################################

### For DB connector ###
db_detail = mysql.connector.connect(
    host="xxxxxxx",
    user="xxxxxxx",
    password="xxxxxxxx",
    database="xxxxxxxxx")
db_python = db_detail.cursor()

### Function Line Notify ###
url = 'https://notify-api.line.me/api/notify'
token = 'xxxxxxxxxxxx' #<-- Token line
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}


if __name__ == '__main__':
    pass
