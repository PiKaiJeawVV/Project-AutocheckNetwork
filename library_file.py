from paramiko import SSHClient
from time import sleep, strptime
from paramiko.client import AutoAddPolicy
from re import match
#from hurry.filesize import size #<-- ทำไมต้องทำเองในเมื่อมีคนทำให้แล้ว
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

### Function Timestamp & สร้างไฟล์ตามด้วย วันที่และเวลา ###
timestr = datetime.datetime.now()
time_stamp = str(timestr.strftime("%d-%m-%Y %X"))
create_file = "output_" + time_stamp + ".txt"

#ip_mikrotik = ['172.22.2.18','172.22.2.19','172.22.2.20','172.22.2.21','172.22.2.22','172.22.2.23']
ip_mikrotik = ['172.22.2.210']