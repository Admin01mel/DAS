from ast import Name

import asyncio
#import grequests
from time import gmtime, strftime
import requests
from datetime import datetime
# Open database connection
#db = pymysql.connect(host='localhost',user='global',password='123456',database='alat',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
from pymysqlpool.pool import Pool
import pymysql.cursors
#pymysqlpool.logger.setLevel('DEBUG')
config={'host':'localhost', 'user':'global', 'password':'123456', 'database':'alat'}
#pool1 = pymysqlpool.ConnectionPool(size=32, pre_create_num=2,maxsize=32, name='pool1', **config)
pool = Pool(host='localhost', port=3306, user='global', password='123456', db='alat')

#pool = pymysqlpool.Pool(host='localhost',port=3306,user='global'password='123456', db='alat')
db=[0]*5
for i in range(3):
    db[i] = pool.get_conn()

url=[]
def queryData(x,query):
    cursor = db[x].cursor()
    cursor.execute(query)
    result = cursor.fetchall()     
    db[x].commit()
    cursor.close()
    pool.release(db[x])
    db[i] = pool.get_conn()
   # db.close()
    return result
# prepare a cursor object using cursor() method
class requestData:
    def __init__(self,index):
        self.index = index
    def sendNotif(kode_mesin,lokasi,nama_alat,nama_mesin,port,tanggal,status,kondisi,ipServer):
        try:
           
            #print(tanggal)
            url=f"http://{ipServer}/dasmon/apialat/insertnotifalat.php?kodemesin={kode_mesin}&lokasi={lokasi}&namaalat={nama_alat}&namamesin={nama_mesin}&port={str(port)}&tanggal={tanggal}&status={status}&kondisi={kondisi}"
            print(url)
            #rs = (grequests.get(u) for u in urls)
            #grequests.get(url)
            #async.get(r, hooks = {'response' : print("ok")})
            requests.get(url, timeout=4)
        except:
            print("request data Error")
class readDb:
    def readDataTabel(x,tb):
        query= f"select * from {tb}"
        try:
           results =queryData(x,query)
           return results
        except:
            print("eror query")

    def reaConfig(x):
        query ="select m_mesin.*,wifi.flag as wifi,network.flag as net,power.reboot as reboot  from m_mesin,wifi,network,power"
        try:
           results =queryData(x,query)
           return results
        except:
            print("eror query")

    def readM_mesin(x):
        query ="SELECT * from m_mesin"
        try:
           results =queryData(x,query)
           return results
        except:
            print("eror query")
    def readChannel(x):
        query ="SELECT m_mesin.nama as nama_mesin,m_mesin.lokasi,m_mesin.mute ,mesin.*,m_mesin.reset,m_mesin.cfg ,network.* from mesin  left join m_mesin on mesin.kode_mesin=m_mesin.kode_mesin LEFT JOIN network on network.kode_mesin=mesin.kode_mesin "
        try:
            results =queryData(x,query)
            return results
        except:
            print("eror query")
    def readChannelLCD(x):
        query = "SELECT a.*,b.kode_gi as nama_gi,b.system_delay,b.nama,b.reset,b.ack,b.cfg,b.mute FROM mesin a right JOIN m_mesin b ON a.kode_mesin = b.kode_mesin ORDER BY a.port ASC"
        try:
            results =queryData(x,query)
            return results
        except:
            print("eror query")
    def readChannelSynk(x):
        query = "SELECT\
                    a.flag_kondisi,\
                    a.kondisi,\
                    a.kode_mesin,\
                    c.ipserver\
                FROM\
                    mesin a\
                LEFT JOIN network c ON a.kode_mesin = c.kode_mesin\
                ORDER BY\
                    a. PORT ASC"
        try:
            results =queryData(x,query)
            return results
        except:
            print("eror query")

    def readcfg(x):
        query = "SELECT * from channel_cfg"
        try:
            results =queryData(x,query)
            return results
        except:
            print("eror query")
    def readNotifNew(x):
        query="Select notif_list.* ,network.ipserver,mesin.tel_low ,mesin.tel_high from notif_list LEFT JOIN network on notif_list.kode_mesin = network.kode_mesin LEFT JOIN mesin on notif_list.port = mesin.`port` where flag_notif =0"
        try:
            results =queryData(x,query)
            return results
        except:
            print("eror query")
    def readLog(x,jml):
        val = int(jml)*8
        query="select tanggal as dta ,notif_list.*,(select count(*) from notif_list) as jml from notif_list ORDER BY tanggal desc limit 8 offset "+str(val)
        try:
            results =queryData(x,query)
            return results
        except:
            print("eror query")
class updDb:
    def updData(x,tabel,row,val,where,val2):
        query =f"update {tabel} set {row} = {val} where {where} = {val2}"
       # print(query)
        try:
            results =queryData(x,query)
            return results
        except NameError:
            print("query Error"+NameError)
    def updMesin(x,kondisi,flag_kondisi,port):
        query=f"update mesin set kondisi = {kondisi},flag_kondisi={flag_kondisi} where port={port}"
        try:
            print(query)
            results =queryData(x,query)
            return results
        except NameError:
            print("query Error"+NameError)
    def rstMesin(x):
        query="update mesin,m_mesin set mesin.flag_kondisi = 0 ,mesin.kondisi=0, m_mesin.reset=1,m_mesin.cfg=1,m_mesin.mute=1"
        try:
           results =queryData(x,query)
           return results
            #print("db update")
        except NameError:
            print("query Error"+NameError)
    def updM_mesin(z,x,y):
        query="UPDATE m_mesin set "+str(x)+" = "+str(y) 
        try:
            results =queryData(z,query)
            return results
        except:
            print("query Erro")
    def rstMesinLCD(x):
        query="update mesin,m_mesin set mesin.flag_kondisi = 0 ,mesin.kondisi=0, m_mesin.reset=1,m_mesin.cfg=0,m_mesin.mute=1"
        try:
            results =queryData(x,query)
            return results
        except:
            print("query Erro")
class InsDb:
   def insNotif_list(x,port,kondisi,flag_kondisi,tanggal):
        status=""
        if (kondisi==1):
            status="HIGH"
        elif(kondisi==0):
            status="LOW"
        query=f"INSERT INTO notif_list (nama_gi,kode_mesin,nama_mesin,nama_alat,STATUS,PORT,tanggal,kondisi,flag_kondisi) SELECT m_mesin.nama_gi,mesin.kode_mesin,m_mesin.nama,mesin.nama_alat,mesin.{status},mesin.PORT,'{tanggal}',{kondisi},{flag_kondisi} FROM mesin LEFT JOIN m_mesin ON mesin.kode_mesin = m_mesin.kode_mesin WHERE mesin.`port` = {str(port)}"
        try:
            results =queryData(x,query)
            return results
        except NameError:
            print("Eror query"+NameError)

