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
####  output_raw = มาจากการรับค่าจาก stdout                                 ####
####  output_real = รับค่ามาจาก output_raw และนำมาตัดช่องว่างออก               ####
####  output_check = คือ string ที่เอาไว้เช็ค ค่าที่มาจาก output_real ว่าตรงกันไหม  ####
##############################################################################
### เช็ค ROS ออกเน็ตได้ไหม
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
    t1 = time.time()
    for data_send in ip_list:
        ### เช็คว่าติด Error ไหม หากติดทำการ pass แล้ว loop ip อื่นแทน <-- important
        try:
            check_wan_ros()
        except:
            #print(str(data_send) + " : Node Down !")
            insert_db_down()
            msg = data_send + ' Node Down !'
            requests.post(url, headers=headers, data = {'message':msg})
            pass
    db_python.close()
    t2 = time.time() - t1
<<<<<<< HEAD
    print(f'Time for run {t2:0.2f}')
=======
    print(f'Time for run {t2:0.2f}')
>>>>>>> 1ff650c131ffe602321509c15095cf7fbbcdd3b6
