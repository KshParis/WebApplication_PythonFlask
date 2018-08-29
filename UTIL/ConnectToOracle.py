#Reusable library to connect to any Oracle database
#Usage: Modify the DB Host and SSID in the body.
#Author: KshParis  (GitHub)
import cx_Oracle

try:
    ora_user = "<<your ora username>>"
    ora_password = "<<user ora password>>" #Yes, i know... for the usage that i had, it was safe to have this exposed here.
    ora_server_ip = "xxx.xxx.xxx.xxx"
    ora_port = "1527"
    ora_SID = "<<ORA INSTANCE ID eg., 'ora' >>"
    connector = ora_user + '/' + ora_password + '@' + ora_server_ip + ':' + ora_port + '/' + ora_SID
    connect = cx_Oracle.connect(connector)
    cur = connect.cursor()

    print("connection sucessfull..")

except cx_Oracle.DatabaseError as e:
    error, = e.args
    if error.code == 1017:
        print('Please check your credentials.')
    else:
        print('Database connection error: %s'.format(e))