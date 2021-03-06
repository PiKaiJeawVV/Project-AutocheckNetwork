#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from global_file import *

### Function insert node down to database ###
def insert_db_down():
    add_query = ("insert into log_status (ip, status, datetime) values (%s, %s, %s)")
    add_data = (data_send, "NodeDown", time_stamp)
    db_python.execute(add_query, add_data)
    db_detail.commit()

def insert_db_fixed():
    add_query = ("insert into log_fixed (ip, status, status2, datetime) values (%s, %s, %s, %s)")
    add_data = (data_send, "1", "fixed", time_stamp)
    db_python.execute(add_query, add_data)
    db_detail.commit()

### Funtion Reset DHCP ###
def reset_dhcp():
    ip = data_send
    port = 22
    username = decode_file_user
    password = decode_file_pass
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(ip,port,username,password)
    stdin,stdout,stderr = client.exec_command("/ip dhcp-client")
    stdin,stdout,stderr = client.exec_command("renew 0")
    sleep(2)
    stdin,stdout,stderr = client.exec_command("..")
    stdin,stdout,stderr = client.exec_command("..")
    stdin,stdout,stderr = client.exec_command("ping count=10 www.google.com")
    sleep(3)
    client.close()
    for output_raw in stdout:
        output_raw.strip()
    output_real = output_raw
    output_real.replace(' ', '')
    output_check = r"(ms)"
    recheck_txt = re.search(output_check, output_real)
    if recheck_txt:
        status_reset_dhcp = 1
        insert_db_fixed()
        msg = data_send + " Reset Already Can Online"
        requests.post(url, headers=headers, data = {'message':msg})
    else:
        status_reset_dhcp = 2
        add_query = ("insert into log_status (ip, status, datetime) values (%s, %s, %s)")
        add_data = (data_send, status_reset_dhcp, time_stamp)
        db_python.execute(add_query, add_data)
        db_detail.commit()
        msg = data_send + " Have No Internet"
        requests.post(url, headers=headers, data = {'message':msg})

### Funtion Reset PPPoE ###
def reset_pppoe():
    ip = data_send
    port = 22
    username = decode_file_user
    password = decode_file_pass
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(ip,port,username,password)
    stdin,stdout,stderr = client.exec_command("/interface pppoe-client disable 0")
    sleep(5)
    stdin,stdout,stderr = client.exec_command("/interface pppoe-client enable 0")
    sleep(3)
    stdin,stdout,stderr = client.exec_command("..")
    stdin,stdout,stderr = client.exec_command("..")
    stdin,stdout,stderr = client.exec_command("ping count=10 www.google.com")
    sleep(3)
    client.close()
    for output_raw in stdout:
        output_raw.strip()
    output_real = output_raw
    output_real.replace(' ', '')
    output_check = r"(ms)"
    recheck_txt = re.search(output_check, output_real)
    if recheck_txt:
        status_reset_pppoe = 1
        insert_db_fixed()
        msg = data_send + " Reset Already Can Online"
        requests.post(url, headers=headers, data = {'message':msg})
    else:
        status_reset_pppoe = 2
        add_query = ("insert into log_status (ip, status, datetime) values (%s, %s, %s)")
        add_data = (data_send, status_reset_pppoe, time_stamp)
        db_python.execute(add_query, add_data)
        db_detail.commit()
        msg = data_send + " Have No Internet"
        requests.post(url, headers=headers, data = {'message':msg})


##############################################################################
####  output_raw = ??????????????????????????????????????????????????? stdout                                 ####
####  output_real = ????????????????????????????????? output_raw ???????????????????????????????????????????????????????????????               ####
####  output_check = ????????? string ??????????????????????????????????????? ????????????????????????????????? output_real ????????????????????????????????????  ####
##############################################################################
### ???????????? ROS ???????????????????????????????????????
#def check_wan_ros(send):
def check_wan_ros():
    ip =  data_send
    port = 22
    username = decode_file_user
    password = decode_file_pass
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(ip,port,username,password)
    stdin,stdout,stderr = client.exec_command("ping count=10 www.google.com")
    sleep(3)
    client.close()
    for output_raw in stdout:
        output_raw.strip()
    output_real = output_raw
    output_real.replace(' ', '')
    output_check = r"(ms)"
    recheck_txt = re.search(output_check, output_real)
    if recheck_txt:
        status_check_wan = 1
    else:
        status_check_wan = 2
        if ip == '172.22.x.x': reset_dhcp()
        elif ip == '172.22.x.x': reset_dhcp()
        elif ip == '172.22.x.x': reset_dhcp()
        elif ip == '172.22.x.x': reset_dhcp()
        elif ip == '172.22.x.x': reset_dhcp()
        elif ip == '172.22.x.x': reset_dhcp()
        elif ip == '172.22.x.x': reset_dhcp()
        else:
            reset_pppoe()


### main function run ###
if __name__ == '__main__':
    for data_send in ip_list:
        ### ?????????????????????????????? Error ????????? ????????????????????????????????? pass ???????????? loop ip ????????????????????? <-- important
        try:
            check_wan_ros()
        except:
            insert_db_down()
            msg = data_send + ' Node Down !'
            requests.post(url, headers=headers, data = {'message':msg})
            pass
    db_python.close()
