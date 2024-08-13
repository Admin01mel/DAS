from ast import Name

import asyncio
import json
#import grequests
from time import gmtime, strftime
import requests
import os
from datetime import datetime
# Open database connection
#db = pymysql.connect(host='localhost',user='global',password='123456',database='alat',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
from pymysqlpool.pool import Pool
import pymysql.cursors
#pymysqlpool.logger.setLevel('DEBUG')
#pool1 = pymysqlpool.ConnectionPool(size=32, pre_create_num=2,maxsize=32, name='pool1', **config)
pool = Pool(host='localhost', port=3306, user='global', password='123456', db='alat')
#pool = Pool(host='localhost', port=3306, user='localhost', password='', db='alat')

#pool = pymysqlpool.Pool(host='localhost',port=3306,user='global'password='123456', db='alat')
db=[0]*5
for i in range(3):
    db[i] = pool.get_conn()

url=[]
def queryData(x,query):
    global db
    global pool
    try:
        db[x].ping(reconnect=True)
        cursor = db[x].cursor()
        cursor.execute(query)
        result = cursor.fetchall()     
        db[x].commit()
        cursor.close()
        pool.release(db[x])
        db[i] = pool.get_conn()
        #print(result)
        return result 
    
    except :
                
        os.popen("pm2 restart all")
# prepare a cursor object using cursor() method
class requestData:
    def __init__(self,index):
        self.index = index
    def sendNotif(kode_mesin,lokasi,nama_alat,nama_mesin,port,tanggal,status,kondisi,ipServer,api,chatid,idm,ipgipat):
               
        
        try:
            url=f"http://{ipServer}/dasmon/apialat/insertnotifalat.php?kodemesin={kode_mesin}&lokasi={lokasi}&namaalat={nama_alat}&namamesin={nama_mesin}&port={str(port)}&tanggal={tanggal}&status={status}&kondisi={kondisi}"
            url2=f"https://api.telegram.org/bot{api}/SendMessage?chat_id={chatid}&text=Lokasi:{lokasi}%0ANama:{nama_alat}%0AStatus:{status}%0Atanggal:{tanggal}%0AChannel:{port}%0A{nama_mesin}"
            r=requests.get(url, timeout=2)
            print(r.status_code)
            if(r.status_code!=200):
                try:
                    r=requests.get(url2, timeout=2)
                    print(url2)
                    print(r.status_code)
                except:
                    print("No internet connection or Telegram error")
        except:
            try:
                r=requests.get(url2, timeout=2)
                #print(url2)
                #print(r.status_code)
            except:                 
                    print("No internet connection or Telegram error")
        url3=f"http://{ipgipat}/addLog/DAS"
        waktu =tanggal.strftime('%B %d, %Y:%H:%M:%S')
        param ={"machine_code":kode_mesin,"modbus":idm,"alias":f"{kode_mesin}{idm}CHN{port}","waktu":waktu}
        #print(url3)
        #print(param)
        try:
            
            r=requests.post(url3,json=param, timeout=2)
            print(r.text)
        except:
            print("gagal kirim server GIPAT")
        
            

class readDb:
    def readDataTabel(x,tb):
        query= f"select * from {tb}"
        try:
           results =queryData(x,query)
           return results
        except:
            print("eror query")

    def reaConfig(x):
        query ="select m_mesin.*,wifi.flag as wifi,network.flag as net,power.reboot as reboot, daspower_config.flag as power_config from m_mesin,wifi,network,power,daspower_config"
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
        query ="SELECT \
                    b.nama AS nama_mesin,\
                    b.lokasi,\
                    b.mute,\
                    a.*, b.RESET,\
                    b.reset_lcd,\
                    b.cfg,\
                    b.cfg_lcd,\
                    c.*,\
                    d.flag as power_cfg\
                FROM\
                    mesin a\
                LEFT JOIN m_mesin b ON a.kode_mesin = b.kode_mesin\
                LEFT JOIN network c ON c.kode_mesin = a.kode_mesin\
                LEFT JOIN daspower_config d on a.kode_mesin =d.kode_mesin"   
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
    def readPowerCfg(x):
        query = "SELECT\
                    a.*,b.cfg as lcd_cfg\
                FROM\
                    daspower_config a\
                LEFT JOIN m_mesin b ON a.kode_mesin = b.kode_mesin"
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
    def readChannelPower(x):
        query = "SELECT a.*,b.id_modbus,c.mute from mesin a left join daspower_config b on a.kode_mesin = b.kode_mesin left join m_mesin c on a.kode_mesin=c.kode_mesin"
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
        query="Select daspower_config.id_modbus as idm , notif_list.* ,network.ipserver,network.ipgipat,mesin.tel_low ,mesin.tel_high,user_notif.api,user_notif.chatid from notif_list LEFT JOIN network on notif_list.kode_mesin = network.kode_mesin LEFT JOIN mesin on notif_list.port = mesin.`port` LEFT JOIN user_notif on notif_list.kode_mesin = user_notif.kode_mesin LEFT JOIN daspower_config on daspower_config.kode_mesin = user_notif.kode_mesin where flag_notif =0"
        try:
            results =queryData(x,query)
            return results
        except:
            print("eror query")
    def readNotifLCD(x):
        query="Select distinct notif_list.* ,network.ipserver,mesin.tel_low ,mesin.tel_high from notif_list LEFT JOIN network on notif_list.kode_mesin = network.kode_mesin LEFT JOIN mesin on notif_list.port = mesin.`port` where flag_notif_lcd =0"
        try:
            results =queryData(x,query)
            return results
        except:
            print("eror query")
    def readKondisiLCD(x):
        query="select DISTINCT port from notif_list where flag_notif_lcd = 0"
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
            
            results =queryData(x,query)
            return results
        except NameError:
            print("query Error"+NameError)
    def rstMesin(x):
        query="update mesin,m_mesin set mesin.flag_kondisi = 0 ,mesin.kondisi=0, m_mesin.reset=1,m_mesin.mute=1"
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
    def updDaspwrMon(x,data,idM):
        query =f'\
            Update das_power_mon \
                set f={data["F"]},\
                v_rn ={data["VRN"]},\
                v_sn ={data["VSN"]}, \
                v_tn ={data["VTN"]}, \
                v_avgn ={data["VAVGN"]}, \
                v_rs ={data["VRS"]}, \
                v_st ={data["VST"]}, \
                v_rt ={data["VRT"]}, \
                v_avg ={data["VAVG"]}, \
                i_r ={data["IR"]}, \
                i_s ={data["IS"]}, \
                i_t ={data["IT"]}, \
                i_n ={data["IN"]}, \
                p_fr ={data["PFR"]}, \
                p_fs={data["PFS"]}, \
                p_ft={data["PFS"]}, \
                p_favg ={data["PFAVG"]} \
            where kode_mesin ={data["kode"]} '
        try:
            results =queryData(x,query)
            return results
        except NameError:
            print("Eror query"+NameError)



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

