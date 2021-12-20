from flask import Flask,render_template,url_for,request,redirect, make_response,cli,Response #, jsonify
#import random
import json
from time import time
#from ochistit import func_ochist
import requests as req
#from random import random
#import random
from datetime import datetime
#import re
#from flask import Flask,render_template,url_for,request,redirect, make_response
import random
import json
from time import time
import copy
from copy import deepcopy
import re
import sys
import os
import logging

cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: None

#export FLASK_APP=example
#export FLASK_ENV=development
#import time
#from flask import Flask, render_template, make_response
json_data=[]
jj=0
global_data=[]
spisok_scenariev=[]
start_flagss=0
data_flagss=0
izmen1_flagss=0
LIST_EPS_flagss=0
epdb=0
stopped_bufer_eps=False
regim_rabota_mode=0
alive_flagss=0
eps_network_buferss=0
add_eps_buferss=0
eb_ALL_delete=0
scenar_add=0
stopped_bufer_delete=False
#from flask_socketio import SocketIO, send, emit
global_number_eps=100
global_spis=''
global_pcath_size=0
global_velocity=0
pcap_cortg=[]
network_list=[]
eps_br=[]
lang_switch=0
GTP_FLAG=True
ipsrc=''
ipdst=''
minteid=''
maxteid=''
time_otvet=0
start_flag1=0
eb_pies_for_one=0
ind_sce_0_iter =0
ind_sce_0 =-1
net_sce_0 =-1
indef_scen =-1
indef_netw =-1
app = Flask(__name__)
#log = logging.getLogger('werkzeug')
#log.disabled = True
random.seed()  # Initialize the random number generator
number_EPS=0
conect=True
number_idd=0
udras= ''
data_grafik1=  [0 ]
data_grafik2=  [0 ]
bufer_network2=[ {'name' : 'Bitrate' , 'der' : 0} , {'name' : 'Video-ratio' , 'der' : 1 } ]
id_form23=-1
eeror_flag=False
data2_global=0
custom_bufer=[]
MAC_SRC=''
MAC_SRC_SORCE=[]
MAC_SRC_INDEX=-1
MAC_DST=''
mac_flag_error=False
labels = [
    'Video', 'Not Video'
]
indef_froma=0
stopped_msg_mac=''
stopped_bufer=False
bufer_menu_ALL_form_rus=[]
bufer_menu_ALL_form_eng=[]

rabota_status=[]

bufer_scenar_1=0
bufer_network_1=0

iterater_schetchik=0
secret_key=[str('test')]
user_key=[str('User')]
flag_regst=False
port_adres={'addr':'192.168.0.143','port':'5000'}
allert_flag=False
allert_msg=''
error_flag= False
paroll_flag= True
bufer_menu_change_MAC_SRC=0
error_flag_add_eps=False
error_flag_add_scenar=False
error_flag_add_scenar1=False


def isValidMACAddress(str):

    # Regex to check valid
    # MAC address
    regex = ("^([0-9A-Fa-f]{2}[:-])" +
             "{5}([0-9A-Fa-f]{2})|" +
             "([0-9a-fA-F]{4}\\." +
             "[0-9a-fA-F]{4}\\." +
             "[0-9a-fA-F]{4})$")

    # Compile the ReGex
    p = re.compile(regex)

    # If the string is empty
    # return false
    if (str == None):
        return False

    # Return if the string
    # matched the ReGex
    if(re.search(p, str)):
        return True
    else:
        return False

@app.route('/', methods = ['POST','GET','PUT'])
def nachal():
    global udras ,  secret_key , user_key ,  time_otvet ,eps_br
    global global_spis,global_pcath_size , global_velocity , GTP_FLAG,ipsrc , ipdst,minteid , maxteid , global_number_eps , network_list , spisok_scenariev , regim_rabota_mode , conect , MAC_SRC , MAC_DST ,MAC_SRC_SORCE,MAC_SRC_INDEX,error_flag_add_scenar , stopped_msg_mac
    #=-1
    if request.method == 'POST':
        """init  GTO """


        udras=str(request.form.get('uds'))
        udras=udras+':'+str(request.form.get('port'))
        bufer=udras
        #udras2=udras+':'+str(3000)
        login=str(request.form.get('login'))
        password=str(request.form.get('password'))
        #app.config['SERVER_NAME'] = udras

        try:
            global port_adres , error_flag , stopped_bufer ,start_flag1 , error_flag_add_eps , alive_flagss
            global  eps_network_buferss , add_eps_buferss , eb_ALL_delete , scenar_add , data_flagss , start_flagss , error_flag_add_eps ,  error_flag_add_scenar , mac_flag_error , LIST_EPS_flagss , scenar_add

            alive_flagss=0
            eps_network_buferss=0
            add_eps_buferss=0
            eb_ALL_delete=0
            scenar_add=0
            data_flagss=0
            start_flagss=0

            error_flag_add_eps=False
            error_flag_add_scenar=False
            mac_flag_error=False
            LIST_EPS_flagss=0
            scenar_add=0


            error_flag=False
            stopped_bufer=False
            error_flag_add_eps=False
            error_flag_add_scenar=False
            stopped_msg_mac=''
            start_flag1=0
            adr=str(request.host).split(':')
            #print('request.host=',request.host)
            bufer=bufer+':'+adr[0]
            port_adres = {'addr':adr[0] , 'port':adr[1] }


            start = time()*1000
            rr = req.get(f'http://{udras}/init',params=(port_adres))
            stop = int(time()*1000 -start)

            time_otvet = stop #rr.elapsed.total_seconds()
            conect = True


            buferr = rr.text

            js = json.loads(buferr)

            #print('\n js=',buferr)


            global pcap_cortg

            if js['response']['code'] == 0:
                #print('js=',js)
                spisok_scenariev=[]
                network_list=[]
                pcapp=js['params']['pcap']
                #print('\njs333=',js['params']['pcap'])
                for it in pcapp:
                    bufer=[]
                    bufer.append(it['video'])
                    bufer.append(it['br'])
                    bufer.append(it['path'])
                    pcap_cortg.append(bufer)
                #print('\npcap=',pcap_cortg)
    ##########################################################################################
                eps_br = []
                js2 = js['params']['eb']
                #print('\n js2=',js2)

                global_number_eps = len(js2)
                for it in js2 :
                    bufer = []
                    #print(,it)
                    bufer.append(it['br'])
                    bufer.append(it['user_scenario'])

                    bufer.append(it['network_scenario'])
                    bufer.append(it['id'])
                    lister=[]
                    lister2=[]

                    if it['user_scenario']['id']!=0 :

                        for it2 in range(len(spisok_scenariev)) :
                            #print('\nit2=',it2)
                            if int(spisok_scenariev[it2][0])   == it['user_scenario']['id']:


                                promeg= deepcopy(spisok_scenariev[it2])
                                lister.append((promeg))
                    else:
                        promeg={'id':it['user_scenario']['id'],'name':it['user_scenario']['name'] ,'pcap_id':it['user_scenario']['pcap_id'] ,'br':it['user_scenario']['br']}
                        bder=1

                        lister=deepcopy(it)

                    bufer.append(lister)

                    if it['network_scenario']['id']!=0 :

                        for it2 in network_list :
                            #print('\nit2=',it2)
                            if  int(it['network_scenario']['id']) == int(it2[3]):

                                promeg=deepcopy(it2)
                                lister2 =deepcopy(promeg)
                                #lister2=promeg
                    else:
                        promeg=deepcopy(it['network_scenario'])
                        lister2 = deepcopy(promeg)

                    bufer.append(lister2)

                    eps_br.append(bufer)



    ######################################################################################




                jss2=js['params']
                global_spis=jss2['file']['path']
                MAC_SRC=jss2['ipsrc']
                MAC_DST=jss2['ipdst']
                #print('jss2=',jss2)
                global_pcath_size=jss2['file']['size']
                global_velocity=jss2['br']
                regim_rabota_mode=jss2['mode']
                GTP_FLAG=jss2['gtp']['use']
                ipsrc=jss2['gtp']['ipsrc']
                ipdst=jss2['gtp']['ipdst']
                minteid=jss2['gtp']['minteid']
                maxteid=jss2['gtp']['maxteid']
                iter=0
                MAC_SRC_SORCE=[]
                for it in jss2['sources']:
                    bufer={'info':it['info'],'mac':it['mac'],'it':iter}
                    iter=iter+1

                    MAC_SRC_SORCE.append(bufer)
                    #print('it=',it)
                #MAC_SRC_SORCE=
                #print('MAC_SRC_SORCE =',MAC_SRC_SORCE[0])


                global_number_eps=len(jss2['eb']) #возможно ошибка

                ###############################custom
                bufer=[]
                bufer.append(0)
                bufer.append('Custom')

                ###############################
                bufe_pcap=[]
                if jss2['user_scenario'] :
                    for i in jss2['user_scenario'][0]['pcap_id']:

                        bufe_pcap.append(i)
                    bufer.append(bufe_pcap)
                else:
                    #for i in range(1,1):
                    bufe_pcap.append(1)
                    bufer.append(bufe_pcap)
                #print('\nperv=',bufer)
                spisok_scenariev.append(bufer)

                if jss2['user_scenario'] :
                    for it in jss2['user_scenario']:


                        bufer=[]
                        #bufer2=[]
                        bufer.append(it['id'])
                        bufer.append(it['name'])

                        bufe_pcap=[]
                        for i in it['pcap_id']:
                            bufe_pcap.append(i)
                        bufer.append(bufe_pcap)
                        #print(bufer)



                        spisok_scenariev.append(bufer)


                bufe_pcap=[] # не удалять


                bufe_pcap.append('Custom')
                if jss2['network_scenario']:
                    bufe_pcap.append(jss2['network_scenario'][0]['jitter'])
                else:
                    bufe_pcap.append({'timedown': 0, 'timeup': 0, 'value': 0})
                #bufe_pcap.append(jss2['network_scenario'][0]['jitter'])
                #bufe_pcap.append(jss2['network_scenario'][0]['burst'])
                if jss2['network_scenario']:
                    bufe_pcap.append(jss2['network_scenario'][0]['burst'])
                else:
                    bufe_pcap.append({'timedown': 0, 'timeup': 0})
                bufe_pcap.append(0)
                network_list.append(bufe_pcap) # custum scenari

                if jss2['network_scenario'] :

                    for it in jss2['network_scenario'] :
                        bufer=[]
                        bufer.append(it['name'])
                        bufer.append(it['jitter'])
                        bufer.append(it['burst'])
                        bufer.append(it['id'])
                        #print(it)
                        network_list.append(bufer) #name jitter , burst





                #global start_flag1
                #print('\n 23456network_list =',network_list)
                if js['state']['run'] == True :
                    start_flag1=start_flag1+1

                if js['state']['run'] == False :
                    start_flag1=0
                    #sesion_1=req.put(f'http://{udras}/state/graph')
                start_flag=True
                if start_flag1%2 == 0 :
                    start_flag=True
                else:
                    start_flag=False


                global   secret_key , user_key
                flag_1=False
                for it in secret_key:
                    if login == it :
                        flag_1=True
                flag_2=False
                for it in user_key :
                    if password == it:
                        flag_2=True



                if flag_1 and flag_2 :
                    #print('spisok_scenariev=',spisok_scenariev)

                    return  redirect(url_for("gra"))
                else:
                    conect = True
                    return  render_template('first.html' , flag_1=flag_1 ,conect = conect)


        except Exception as ex :
            conect = False
            flag_1=True
            flag_2=True
            print('\n \n 2345 flag_1=',flag_1,'flag_2=',flag_2 )
            return  render_template('first.html',flag_1=flag_1 ,conect = conect)

    flag_1=True
    conect = True

    return  render_template('first.html',flag_1=flag_1)

@app.route('/err', methods=[ 'POST'])
def ERR():
    if request.method == 'POST':
        if id_form23 == 0:
            pass

@app.route('/alive', methods=[ 'GET','POST'])
def alive():
    if request.method == 'POST' or request.method == 'GET' :
        global conect , start_flag1 , alive_flagss , data_flagss
        alive_flagss=alive_flagss+1
        textert_dlia_analiz=0
        if alive_flagss==1 and  data_flagss==0:
            try:
                conect=True

                rr=req.get(f'http://{udras}/alive')
                buferr=rr.text
                textert_dlia_analiz=buferr
                js = json.loads(buferr)
                alive_flagss=0
                print('\n js=',js)

                if js['response']['code']== 0:
                    json_data="God"
                    response = make_response(json_data)
                    data=["God",2]
                    json_data = json.dumps(data)

                    response = make_response(json_data)
                    #print('\n God=',json_data)
                    #print(json_data)

                    response.content_type = 'application/json'

                    return response

                else:
                    start_flag1=0
                    conect=False

            except req.ConnectionError as ex:
                    print('\n dert ConnectionError')

                    conect=False
                    start_flag1=0
                    fe=repr(ex)
                    alive_flagss=0

                    if 'Internal Server Error' in fe:
                        json_data="God"
                        conect=True
                        response = make_response(json_data)
                        data=["God",2]
                    else:
                        json_data="Not"
                        response = make_response(json_data)
                        data=["Not",2]

                    json_data = json.dumps(data)

                    response = make_response(json_data)
                    #print('\n Not=',json_data)
                    print('\n alive gs=',data)
                    print('\n alive textert_dlia_analiz=',ex)
                    print('\n fe=',ex)
                    #print('\n alive gs=',repr(ex))
                    #print('\n 23 js=',js)

                    response.content_type = 'application/json'

                    return response

            except Exception as ex:



                    conect=True
                    start_flag1=0
                    fe=repr(ex)
                    alive_flagss=0

                    #if 'Internal Server Error' in fe:
                        #json_data="God"
                        #conect=True
                        #response = make_response(json_data)
                        #data=["God",2]
                    #else:
                        #json_data="Not"
                        #response = make_response(json_data)
                        #data=["Not",2]
                    data=["God",2]

                    json_data = json.dumps(data)

                    response = make_response(json_data)
                    #print('\n Not=',json_data)
                    print('\n alive gs=',data)
                    print('\n alive textert_dlia_analiz=',ex)
                    print('\n fe=',ex)
                    #print('\n alive gs=',repr(ex))
                    #print('\n 23 js=',js)

                    response.content_type = 'application/json'

                    return response

                    #response = make_response(json_data)


@app.route('/lengrth_table_scer', methods=[ 'POST'])
def lengrth_table_scer():
    if request.method == 'POST':
        global lang_switch , stopped_bufer , stopped_msg_mac , error_flag_add_scenar1
        lang_switch = lang_switch+1
        stopped_bufer=False
        stopped_msg_mac=''
        error_flag_add_scenar1=False

        return redirect(url_for("scenar_spis"))
@app.route('/lengrth_table_network', methods=[ 'POST'])
def lengrth_table_network():
    if request.method == 'POST':
        global lang_switch  , stopped_bufer , stopped_msg_mac
        lang_switch = lang_switch+1
        stopped_bufer=False
        stopped_msg_mac=''
        return redirect(url_for("network_spis"))

@app.route('/lengrth_form_nastroika', methods=[ 'POST'])
def lengrth_form_nastroika():
    if request.method == 'POST' :
        global lang_switch ,number_idd  , mac_flag_error , stopped_bufer , stopped_msg_mac ,error_flag_add_scenar1
        lang_switch = lang_switch+1
        stopped_bufer=False
        stopped_msg_mac=''
        error_flag_add_scenar1=False

        return redirect(url_for("eps_scenar",number=number_idd))

@app.route('/lengrth_form_glubnastroika', methods=[ 'POST'])
def lengrth_form_glubnastroika():
    if request.method == 'POST' :
        global lang_switch ,number_idd , error_flag_add_scenar
        lang_switch = lang_switch+1
        error_flag_add_scenar=False

        return redirect(url_for("eb_nastroit",number=number_idd))

@app.route('/lengrth_epsbiar_network', methods=[ 'POST'])
def lengrth_epsbiar_network():
    if request.method == 'POST' :
        global lang_switch , number_idd
        lang_switch = lang_switch+1

        return redirect(url_for("eps_network",number=number_idd))
@app.route('/lengrth_epb_table', methods=[ 'POST'])
def lengrth_epb_table():
    if request.method == 'POST' :
        global lang_switch , error_flag_add_eps , error_flag_add_scenar1
        lang_switch = lang_switch+1
        error_flag_add_eps=False
        error_flag_add_scenar1=False

        return redirect(url_for("LIST_EPS"))

@app.route('/lengrth_epsbiar_scene', methods=[ 'POST'])
def lengrth_epsbiar_scene() :
    if request.method == 'POST' :
        global lang_switch , number_idd , error_flag_add_scenar ,error_flag_add_scenar1
        lang_switch = lang_switch+1
        error_flag_add_scenar=False
        error_flag_add_scenar1=False

        return redirect(url_for("eps_scenar",number=number_idd))
#
@app.route('/lengrth_2_gra', methods=[ 'POST'])
def lengrth_2_gra() :
    if request.method == 'POST':
        global lang_switch , stopped_msg_mac  , stopped_bufer
        stopped_msg_mac=''

        stopped_bufer=False
        lang_switch = lang_switch+1

        return redirect(url_for("gra"))
@app.route('/lengrth_form', methods=[ 'POST'])
def lengrth_form() :
    if request.method == 'POST' :
        global lang_switch , mac_flag_error
        lang_switch = lang_switch+1
        mac_flag_error=False

        return redirect(url_for("Menu"))

@app.route('/back', methods=[ 'POST'])
def back_menu() :

    if request.method == 'POST' :
        global stopped_msg_mac , stopped_bufer
        stopped_bufer=False
        stopped_msg_mac=''
        return redirect(url_for("gra"))
@app.route('/back_1', methods=[ 'POST'])
def back_menu_1():

    if request.method == 'POST' :
        global stopped_msg_mac , stopped_bufer ,add_eps_buferss , stopped_bufer_delete , stopped_bufer_eps
        stopped_bufer=False
        stopped_msg_mac=''
        stopped_bufer_delete=False
        stopped_bufer_eps=False
        if add_eps_buferss == 0 and eb_ALL_delete == 0:
            return redirect(url_for("gra"))
@app.route('/back_2', methods=[ 'POST'])
def back_list_1():
    if request.method == 'POST' :
        global stopped_msg_mac , stopped_bufer , error_flag_add_scenar1 ,error_flag_add_scenar , stopped_bufer_delete
        stopped_bufer=False
        stopped_msg_mac=''
        error_flag_add_scenar1=False
        error_flag_add_scenar=False
        stopped_bufer_delete=False

        return redirect("/scenar")
@app.route('/back_3', methods=[ 'POST'])
def back_list_2() :
    if request.method == 'POST' :
        global stopped_msg_mac , stopped_bufer , stopped_bufer_delete
        stopped_bufer=False
        stopped_msg_mac=''
        stopped_bufer_delete=False
        return redirect("/scenar_network")
@app.route('/back_4', methods=[ 'POST'])
def back_list_4() :
    if request.method == 'POST':
        global stopped_msg_mac , stopped_bufer , error_flag_add_eps ,  error_flag_add_scenar , error_flag_add_scenar1 , stopped_bufer_delete
        stopped_bufer=False
        error_flag_add_eps=False
        error_flag_add_scenar=False
        error_flag_add_scenar1=False
        stopped_bufer_delete=False
        stopped_msg_mac=''
        return redirect(url_for('LIST_EPS'))
@app.route('/izmen1', methods=[ 'POST'])
def izmen1() :
    """change menu GTO """
    global GTP_FLAG , ipsrc , ipdst , minteid , maxteid , global_pcath_size , regim_rabota_mode , global_velocity , global_spis , MAC_SRC ,  MAC_DST ,mac_flag_error , stopped_bufer ,bufer_menu_change_MAC_SRC ,error_flag , stopped_bufer_delete
    #=''
    #=''


    #zagolovok=[global_velocity,znach,ipsrc,ipdst,minteid,maxteid,global_spis,global_pcath_size,global_number_eps]



    if request.method == 'POST':
        stopped_bufer_delete=False
        regim = request.form['user_regim']
        regim_rabota_mode = int(request.form['user_regim'])
        global stopped_msg_mac , izmen1_flagss
        stopped_bufer=False
        stopped_msg_mac=''
        izmen1_flagss=izmen1_flagss+1

        if  regim_rabota_mode ==1:
            stopped_bufer= False
            pass
        #regim_rabota_mode=regim
        #pass

        error_flag=False

        velocity = request.form['velocity']
        #global_velocity = velocity
        adres_ist = request.form['adres_ist']
        ipsrc = adres_ist
        adres_naz = request.form['adres_naz']
        ipdst = adres_naz
        MAC_FLAG= request.form.getlist('MAC_SRC_BOOl')

        MAC_FLAG2=True
        if len(MAC_FLAG) == 0:
            MAC_FLAG2=False


        if MAC_FLAG2:
            for lit in request.form.getlist('mac_select'):
                MAC_SRC =  lit

        MAC_DST_bufer =  str(request.form['MAC_adres_naz'])

        if len (MAC_DST_bufer) == 0:
            mac_flag_error= True
            stopped_bufer= False
            return redirect(url_for("Menu"))

        if  len(MAC_DST_bufer.split(':')) != 6 :
            mac_flag_error= True
            stopped_bufer= False
            #print('\n lenter=',len(MAC_DST_bufer.split(':')))
            #print('\n MAC_DST_bufer=',MAC_DST_bufer)
            #stopped_bufer= False
            return redirect(url_for("Menu"))

        if  isValidMACAddress(MAC_DST_bufer.upper()) :
            stopped_bufer= False
            pass

        else:
            #print('\n \n !!!!!!!!!!!!!!')
            mac_flag_error= True
            #stopped_bufer= False
            return redirect(url_for("Menu"))
        MAC_DST = MAC_DST_bufer

        size = request.form['razm_mb']
        global_pcath_size = size
        TEID = request.form['TEID']
        minteid = TEID
        TEID2 = request.form['TEID2']
        maxteid = TEID2

        #GTP2=request.form['GTP2']
        GTP2= request.form.getlist('GTP2')
        GTP_FLAG= GTP2
        pcap_adr= request.form['pcap_adr']
        global_spis=pcap_adr
        #GTP=request.form['GTP']
        out_gtp=True
        if len(GTP2) == 0:
            out_gtp=False
        #print(regim,velocity,adres_ist,out_gtp,adres_naz,TEID,pcap_adr,TEID2)
        stringer=''
        for it in pcap_adr:
            stringer=str(it)
        try:


            json_out={

            "params":{
            "mode":int(regim),
            "br":int(velocity),
            "ipdst":MAC_DST   ,
            "ipsrc": MAC_SRC ,
            "file":{
            "path": pcap_adr,
            "size": int(size)},
            "gtp":{
            "use": out_gtp,
            "ipsrc": str(adres_ist),
            "ipdst": str(adres_naz),
            "minteid": int(TEID),
            "maxteid": int(TEID2)}
            }
            }
            #print(json_out)
            #json_out2=json.dumps(json_out)
            #print('json_2=',json_out)
            #req.put
            #print('json_out=',json_out)
            if izmen1_flagss==1:

                rr=req.put(f'http://{udras}/params/common',json=(json_out))


                bufer_menu_change_MAC_SRC=0
                #print('rr=',rr.text)
                buferr=rr.text

                js = json.loads(buferr)
                izmen1_flagss=0
                #print('\n js=',js)
                global pcap_cortg
                mac_flag_error= False
                if js['response']['code'] == 0 :
                    global_velocity = int(js['params']['br'])

                    return redirect(url_for('gra'))
                else:
                    global_velocity = int(js['params']['br'])

                    return redirect(url_for("gra"))

        except Exception as ex:
            return  redirect(url_for("Menu"))



@app.route('/izmen_scenari/new', methods=[ 'POST','GET'])
def izmen_scenari():
    if request.method == 'POST' or request.method == 'GET':
        global custom_bufer , error_flag_add_scenar ,error_flag_add_eps , stopped_msg_mac , stopped_bufer ,error_flag_add_scenar1
        #global stopped_msg_mac
        stopped_bufer=False
        stopped_msg_mac=''
        #print('\n zachel_rabotaet')
        #print('\n zachel_rabotaet
        error_flag_add_eps=False
        scen=int(request.form['scenar_number234'])
        error_flag_add_scenar=False
        #regim=request.form['user_regim']
        scenar_pcap =request.form.getlist('scenar')
        print('\n scenar_pcap=',scenar_pcap)
        #print('\n pcap_cortg=',pcap_cortg)
        print('\n eps_br=',eps_br)

        vr_summ=0
        scenar_izmen=[]
        for i in scenar_pcap :
            scenar_izmen.append(int(i))
        vr_summ=0
        for i in scenar_izmen :
            #print(pcap_cortg[i-1])
            vr_summ = vr_summ+pcap_cortg[i-1][1]

        if vr_summ >50000000 :
            #number_idd
            error_flag_add_scenar=True

            return  redirect(url_for('eps_scenar',number=number_idd))
        vrr=0
        bool_flag_vlog=False
        col=0
        if(number_idd!=0) :

            for it in eps_br:
                if it[1]['id'] == int(number_idd) :
                    bool_flag_vlog=True
                    col=col+1
                    #pass
                else:
                    vrr=vrr+it[0]
            vrr=vrr+vr_summ*col
        else:

            for it in eps_br:
                #print('\n it[1]=',)
                if it[1]['id'] == int(number_idd) and it[0]== vr_summ:
                    #if (it[0]==)
                    bool_flag_vlog=True

                    col=col+1
                else:
                    vrr=vrr+it[0]
            vrr=vrr+vr_summ*col

        #print('\n bool_flag_vlog=',bool_flag_vlog)
        #print('\n global_velocity=',global_velocity)
        #print('\n vrr=',vrr)

        if(int(global_velocity)<int(vrr)) and bool_flag_vlog :
            error_flag_add_scenar1=True

            return  redirect(url_for('eps_scenar',number=number_idd))





                #if lang_switch%2== 0:
                    #stopped_msg_mac=bufer_menu_ALL_form_eng[0][2]

                #else:
                    #stopped_msg_mac=bufer_menu_ALL_form_rus[0][2]


            #error_flag_add_scenar1 =True

            #return  redirect(url_for('eps_scenar',number=number_idd))


        #if vr_summ >50000000 :
            #number_idd
            #error_flag_add_scenar1=True

            #return  redirect(url_for('eps_scenar',number=number_idd))

        bufer=0
        g=0

        for it in spisok_scenariev :
            if scen == int(it[0]) :
                bufer=g
            g=g+1

        #print('\nspisok_sceanarieb=',spisok_scenariev[bufer][1])
        name=spisok_scenariev[bufer][1]
        if scen == 0:
            spisok_scenariev[bufer][2]=scenar_izmen   # delete
            custom_bufer=scenar_izmen


        if scen != 0:

            json_out={
            "params":{
            "user_scenario":[{
            "id": scen,
            "name":name,
            "br": int(vr_summ),
            "pcap_id":scenar_izmen
            }]
            }
            }
            #print('do json=',json_out)
            try :
                print('\n \n do do put scenario out=',json_out)
                rr=req.put(f'http://{udras}/params/user_scenario',json=(json_out))
                js = json.loads(rr.text)
                print('\n \n  2out_put_scenar=',js)
                error_flag_add_scenar1=False
                error_flag_add_scenar=False

                if js['response']['code'] == 0 :
                    return redirect(url_for('scenar_spis'))
                else:
                    return redirect(url_for('scenar_spis'))



            except Exception as ex:
                return  render_template('first.html')
        else:

            return redirect(url_for('scenar_spis'))



        #pass




@app.route('/izmen2', methods=[ 'POST','GET']) # добавить условие при  нуле custom
def izmen2():
    if request.method == 'POST':
        global stopped_msg_mac ,  stopped_bufer , error_flag_add_scenar ,error_flag_add_scenar1
        stopped_bufer=False
        stopped_msg_mac=''

        print('eps=',eps_br)
        #print('rabotaetss\n')
        #eb=request.form.getlist('scenar')
        #print('\n eb=',eb)



        eb=int(request.form['eps_number'])
        num_scen=int(request.form['eps_scen'])
        eps_netw=int(request.form['eps_netw'])
        vr_buferr_all_eps_biar=0

        for iterr in eps_br:
            print('\n', iterr[3])

            if  (int(iterr[3])==int(eb)) :
                pass
            else:
                vr_buferr_all_eps_biar=vr_buferr_all_eps_biar+iterr[0]

        print('\n vr_buferr_all_eps_biar=',vr_buferr_all_eps_biar)
        #print('eps_netw=',eps_netw)
        #print('\n pcap_cortg=',pcap_cortg)
        scenar=request.form.getlist('scenar')
        scenar_izmen=[]
        vr_summ=0
        id=0
        id_netw=0
        #spisok_scenariev
        for i in scenar:
            scenar_izmen.append(int(i))
        #print('\n !!!!!!!!!!!!!!!!! scenar=',scenar_izmen)
        #print('\nnum_scen=',num_scen)
        #print('\nnum_scen=',num_scen)
        #print('\neps_netw=',eps_netw)
        #print('\n spisok_scenariev=',spisok_scenariev)
        num_scen1=0
        scenarier=0
        for itt in spisok_scenariev:
            if itt[0] == num_scen:
                scenarier=int(itt[0])
                break
            num_scen1=num_scen1+1

        num_scen=num_scen1


        #print('\nspis_scenar=',spisok_scenariev[num_scen])
        eps_netw1=0
        netwert=0
        for let in network_list:
            if let[3]== eps_netw:
                netwert=int(let[3])
                break
            eps_netw1=eps_netw1+1
        eps_netw=eps_netw1


        ############################newtork###################################################################
        jitter_timeup=int(request.form['jitter_timeup'])

        jitter_timedown=int(request.form['jitter_timedown'])
        jitter_value=int(request.form['jitter_value'])
        burst_timeup=int(request.form['burst_timeup'])
        burst_timedown=int(request.form['burst_timedown'])


        ###############################################################################################

        flag_scenar=False
        name_scenar=''

        if spisok_scenariev[num_scen][2] == scenar_izmen :
            #print('sovpadate')
            flag_scenar=True
            id = scenarier
            name_scenar=spisok_scenariev[num_scen][1]

        else:
            #print('nesovpadate')
            flag_scenar=False
            id = 0
            name_scenar='Custom'
        flag_netw=False
        #print(network_list[eps_netw])
        if jitter_timeup == int(network_list[eps_netw][1]['timeup']) and  jitter_timedown == int(network_list[eps_netw][1]['timedown']) and jitter_value == int(network_list[eps_netw][1]['value']) and  burst_timeup == int( network_list[eps_netw][2]['timeup']) and burst_timedown ==  int(network_list[eps_netw][2]['timedown']):
            #print('sovpadate')
            flag_netw=True
            id_netw = netwert
            #print(network_list[eps_netw])
            name_netw=network_list[eps_netw][0]

        else:
            #print('nesovpadate')
            flag_netw=False
            id_netw = 0
            name_netw='Custom'

        if spisok_scenariev[num_scen][0] == 0:
            #print('nesovpadate')
            flag_scenar=False
            id = 0
            name_scenar='Custom'

        if network_list[eps_netw][3] == 0:
            #print('nesovpadate')
            flag_netw=False
            id_netw = 0
            name_netw='Custom'

        #print('\n scenar=',flag_scenar,'netw=',flag_netw)

        jsno_out={}
        #if  flag_netw and flag_netw :
        vr_summ=0
        vr_eb=0
        for i in scenar_izmen:
            #print(pcap_cortg[i-1])
            vr_summ=vr_summ+pcap_cortg[i-1][1]
        vr_buferr_all_eps_biar=vr_buferr_all_eps_biar+vr_summ

        if vr_summ > 50000000 :
            error_flag_add_scenar =True

            return   redirect(url_for('eb_nastroit',number=number_idd))

            #error_flag_add_scenar1

        if global_velocity<vr_buferr_all_eps_biar:
            error_flag_add_scenar1 =True

            return   redirect(url_for('eb_nastroit',number=number_idd))

        vr_summ=int(request.form['znachenie'])
        #print('\n vr_summ=',vr_summ)
        vr_eb=int(request.form['znachenie'])

        if vr_eb > 50000000 :
            error_flag_add_scenar =True

            return   redirect(url_for('eb_nastroit',number=number_idd))
        #print('vr_summ=',vr_summ)
        json_out={}
        json_out2=0

        #for iitre in scenar_izmen:
        if  flag_scenar == False and  flag_netw == False  :
            json_out={
            "params":{
            "eb": [{
            "id":int(eb),
            "br":int(vr_summ),
            "user_scenario":{
            "id": 0,
            "name": name_scenar,
            "br": int(vr_summ),
            "pcap_id":scenar_izmen
            }, "network_scenario":{
            "id": 0,
            "name": "Custom",
            "jitter" :{
            "timeup":jitter_timeup,
            "timedown":jitter_timedown,
            "value":jitter_value
            },
            "burst": {
            "timeup":burst_timeup,
            "timedown":burst_timedown
            }
            }
            }]
            }
            }
            json_out2=json.dumps(json_out)
            #print('json_2=',json_out)
            try:
                print('\n \n do json_out=',json_out)
                rr=  req.put(f'http://{udras}/params/eb',json=(json_out))

                js = json.loads(rr.text)
                print('\n \n do js=',js)
                error_flag_add_scenar =False
                error_flag_add_scenar1 =False

                #print('\nFalse False=',js)

                if js['response']['code'] == 0 :
                    return redirect(url_for('LIST_EPS'))
                else:
                    return redirect(url_for('LIST_EPS'))
            except Exception as ex:
                return  render_template('first.html')

        if  flag_scenar == True and  flag_netw == True  :
            json_out={
            "params":{
            "eb": [{
            "id":int(eb),
            "br":int(vr_summ),
            "user_scenario":{
            "id": int(id)

            }, "network_scenario":{
            "id": int(id_netw)
            }
            }]
            }
            }
            json_out2=json.dumps(json_out)
            #print('json_2=',json_out)
            try:
                print('\n \n do json_out=',json_out)
                rr=  req.put(f'http://{udras}/params/eb',json=(json_out))

                js = json.loads(rr.text)
                print('\n \n do js=',js)
                #print('\nTrue True=',js)
                error_flag_add_scenar =False
                error_flag_add_scenar1 =False
                if js['response']['code'] == 0 :
                    return redirect(url_for('LIST_EPS'))
                else:
                    return redirect(url_for('LIST_EPS'))
            except Exception as ex:
                return  render_template('first.html')
        if  flag_scenar == True and  flag_netw == False  :
            json_out={
            "params":{
            "eb": [{
            "id":int(eb),
            "br":int(vr_summ),
            "user_scenario":{
            "id": int(id)
            }, "network_scenario":{
            "id": 0,
            "name": "Custom",
            "jitter" :{
            "timeup":jitter_timeup,
            "timedown":jitter_timedown,
            "value":jitter_value
            },
            "burst": {
            "timeup":burst_timeup,
            "timedown":burst_timedown
            }
            }
            }]
            }
            }
            json_out2=json.dumps(json_out)
            #print('json_2=',json_out)
            try:
                print('\n \n do json_out=',json_out)
                rr=  req.put(f'http://{udras}/params/eb',json=(json_out))

                js = json.loads(rr.text)
                print('\n \n do js=',js)
                #print('\nTrue False=',js)
                error_flag_add_scenar =False
                error_flag_add_scenar1 =False
                if js['response']['code'] == 0 :
                    return redirect(url_for('LIST_EPS'))
                else:
                    return redirect(url_for('LIST_EPS'))
            except Exception as ex:
                return  render_template('first.html')
        if  flag_scenar == False and  flag_netw == True  :
            json_out={
            "params":{
            "eb": [{
            "id":int(eb),
            "br":int(vr_summ),
            "user_scenario":{
            "id": 0,
            "name": name_scenar,
            "br": int(vr_summ),
            "pcap_id":scenar_izmen
            }, "network_scenario":{
            "id": int(id_netw)
            }
            }]
            }
            }
            json_out2=json.dumps(json_out)
            #print('json_2=',json_out)
            try:
                print('\n \n do json_out=',json_out)
                rr=  req.put(f'http://{udras}/params/eb',json=(json_out))

                js = json.loads(rr.text)
                print('\n \n do js=',js)
                #print('\nFalse True=',js)
                error_flag_add_scenar =False
                error_flag_add_scenar1 =False
                if js['response']['code'] == 0 :
                    return redirect(url_for('LIST_EPS'))
                else:
                    return redirect(url_for('LIST_EPS'))
            except Exception as ex:
                return  render_template('first.html')

        #network=request.form['network']
        #print('\neb=',eb)
        #print('\nnetwork=',network)



        # вставить изменения из общего конфигурации form
        return redirect(url_for("LIST_EPS"))

@app.route('/eb_ALL/delete', methods=[ 'POST'])
def eb_all_delete():
    """ delete all EPS-BIAR """
    global  eps_br , spisok_scenariev , network_list , stopped_msg_mac ,  stopped_bufer , eb_ALL_delete , stopped_bufer_delete



    if request.method == 'POST' :
        #global
        stopped_bufer_delete=False
        eb_ALL_delete=eb_ALL_delete+1

        start_flag=True
        if start_flag1%2 == 0:
            start_flag=True
        else:
            start_flag=False

        if start_flag== False:
            stopped_bufer=True

            if lang_switch%2== 0:
                stopped_msg_mac=bufer_menu_ALL_form_eng[0][4]

            else:
                stopped_msg_mac=bufer_menu_ALL_form_rus[0][4]


            return redirect(url_for('LIST_EPS'))

        spisok_eps=[]
        for i in eps_br:
            spisok_eps.append(int(i[3]))
        j=len(eps_br)
        js=[]
        #if eb_ALL_delete==1:
        tert=[]

        for ii in range(1,201) :
            #if j-1 != 0:
            if ii  in spisok_eps :
                #j=j-1
                #try:
                stopped_bufer=False
                stopped_msg_mac=''
                tert.append({"id":int(ii)})
                    #json_out={
                    #"params":{
                    #"eb":[{
                    #"id":int(ii)
                    #}]
                    #}
                    #}
                    #json_out2=json.dumps(json_out)
                    #print('do do rr=',json_out2)

                    #rr=  req.delete(f'http://{udras}/params/eb',json=(json_out))

                    #js = json.loads(rr.text)
                eb_ALL_delete=0
                    #print('delete outrr=',js)
                    #print('js=',js)
                    #if js['response']['code'] == 0 :
                        #return redirect(url_for('LIST_EPS'))
                    #else:
                        #return redirect(url_for('LIST_EPS'))

                #except Exception as ex:
                    #eb_ALL_delete=0

                    #return  render_template('first.html')

                    #return redirect(url_for('LIST_EPS'))

                    #return redirect(url_for("delete_eb",number=int(ii)))

            #else:
                #break
        eb_ALL_delete=0

        json_out={
        "params":{
        "eb":tert
        }
        }
        try:
            rr=  req.delete(f'http://{udras}/params/eb',json=(json_out))

            return redirect(url_for('LIST_EPS'))

        except Exception as ex:
            eb_ALL_delete=0
            return redirect(url_for('LIST_EPS'))




        return redirect(url_for('LIST_EPS'))


    # pass

@app.route('/eb_ALL/add', methods=[ 'POST'])
def eb_all_add():
    global  eps_br , spisok_scenariev , network_list , error_flag_add_eps , add_eps_buferss # вставить

    if request.method == 'POST' :
        global stopped_msg_mac ,  stopped_bufer
        add_eps_buferss=add_eps_buferss+1
        stopped_bufer=False
        stopped_msg_mac=''
        col=int(request.form['colich'])
        #i = 0
        #for it in range(len())
        i=0
        #summer_velocity=0
        for it in eps_br:
            i=i+1
        #if 200 - i+1-col <0 or col == 0:
            #error_flag_add_eps=True
            #return redirect(url_for('LIST_EPS'))

        scenar=request.form.getlist('scenar')
        scenar_numb=0
        for it  in scenar:
            scenar_numb= int(it)

        network=request.form.getlist('network')
        pass

        network_numb=0
        for it  in network:
            network_numb= int(it)


        #out=len(eps_br)-1
        #print('\n out=',eps_br[out])

        spisok_eps=[]
        for i in eps_br:
            spisok_eps.append(int(i[3]))
        j=0
        js=[]
        global_velocity ,
        vrsumm_33=0
        print('\n len(eps_br)=',(i))

        if i == 200:
            return   redirect(url_for('LIST_EPS'))



        for ii in range(1,201) :

            if ii not in spisok_eps :
                #print('\n zachodit i=',ii)
                j=j+1
                if network_numb == 0 and scenar_numb == 0:


                    scenar_izmen=[]

                    #vr_summ=0 #pcap_cortg[i-1][1]
                    scenar_izmen=[]
                    for it in spisok_scenariev[scenar_numb][2] :
                        scenar_izmen.append(int(it))

                    vr_summ=0
                    for i in scenar_izmen:
                        #print(pcap_cortg[i-1])
                        vr_summ=vr_summ+pcap_cortg[i-1][1]
                    vrsumm_33=vrsumm_33+vr_summ



                if network_numb == 0 and scenar_numb != 0:

                    #new_id=int(eps_br[out][3])+i
                    vr_summ1=spisok_scenariev[scenar_numb][0]
                    scenar_izmen=[]


                    #vr_summ=0 #pcap_cortg[i-1][1]
                    scenar_izmen=[]
                    for it in spisok_scenariev[scenar_numb][2] :
                        scenar_izmen.append(int(it))

                    vr_summ=0
                    for i in scenar_izmen:
                        #print(pcap_cortg[i-1])
                        vr_summ=vr_summ+pcap_cortg[i-1][1]
                    vrsumm_33=vrsumm_33+vr_summ


                if network_numb != 0 and scenar_numb != 0:

                    #new_id=int(eps_br[out][3])+i
                    vr_summ1=spisok_scenariev[scenar_numb][0]
                    scenar_izmen=[]


                    #vr_summ=0 #pcap_cortg[i-1][1]
                    scenar_izmen=[]
                    for it in spisok_scenariev[scenar_numb][2] :
                        scenar_izmen.append(int(it))

                    vr_summ=0
                    for i in scenar_izmen:
                        #print(pcap_cortg[i-1])
                        vr_summ=vr_summ+pcap_cortg[i-1][1]
                    vrsumm_33=vrsumm_33+vr_summ


                if network_numb != 0 and scenar_numb == 0:

                    #new_id=int(eps_br[out][3])+i
                    vr_summ1=spisok_scenariev[scenar_numb][0]
                    scenar_izmen=[]


                    #vr_summ=0 #pcap_cortg[i-1][1]
                    scenar_izmen=[]
                    for it in spisok_scenariev[scenar_numb][2] :
                        scenar_izmen.append(int(it))

                    vr_summ=0
                    for i in scenar_izmen:
                        #print(pcap_cortg[i-1])
                        vr_summ=vr_summ+pcap_cortg[i-1][1]
                    vrsumm_33=vrsumm_33+vr_summ

            if j == col :
                break
        print('\n global_velocity=',global_velocity)
        print('\n vrsumm_33=',vrsumm_33)

        for it in eps_br :
            vrsumm_33=vrsumm_33+int(it[0])

        if int(global_velocity)<(vrsumm_33) :
            error_flag_add_eps=True
            add_eps_buferss=0


            return   redirect(url_for('LIST_EPS'))

        j=0

        #if add_eps_buferss==1:
        json_list=[]
        #json_list.append(tert)
        for ii in range(1,201) :

            if ii not in spisok_eps :
                #print('\n zachodit i=',ii)
                j=j+1
                if network_numb == 0 and scenar_numb == 0:


                    scenar_izmen=[]

                    #vr_summ=0 #pcap_cortg[i-1][1]
                    scenar_izmen=[]
                    for it in spisok_scenariev[scenar_numb][2] :
                        scenar_izmen.append(int(it))

                    vr_summ=0
                    for i in scenar_izmen:
                        #print(pcap_cortg[i-1])
                        vr_summ=vr_summ+pcap_cortg[i-1][1]
                    vrsumm_33=vrsumm_33+vr_summ

                    tert={
                    #"params":{
                    #"eb": [{
                    "id":ii,
                    "br":int(vr_summ),
                    "user_scenario":{
                    "id": 0,
                    "name": "Custom",
                    "br": int(vr_summ),
                    "pcap_id":spisok_scenariev[scenar_numb][2]
                    }, "network_scenario":{
                    "id": 0,
                    "name": "Custom",
                    "jitter" :{
                    "timeup":network_list[network_numb][1]['timeup'],
                    "timedown":network_list[network_numb][1]['timedown'],
                    "value":network_list[network_numb][1]['value']
                    },
                    "burst": {
                    "timeup":network_list[network_numb][2]['timeup'],
                    "timedown":network_list[network_numb][2]['timedown']
                    }
                    }
                    #}]
                    #}
                    }
                    json_list.append(tert)
                    #try :

                        #rr= req.post(f'http://{udras}/params/eb',json=(json_out))
                        #js = json.loads(rr.text)
                        #add_eps_buferss=0

                        #error_flag_add_eps=False


                    #except Exception as ex:
                        #return  render_template('first.html')


                if network_numb == 0 and scenar_numb != 0:

                    #new_id=int(eps_br[out][3])+i
                    vr_summ1=spisok_scenariev[scenar_numb][0]
                    scenar_izmen=[]


                    #vr_summ=0 #pcap_cortg[i-1][1]
                    scenar_izmen=[]
                    for it in spisok_scenariev[scenar_numb][2] :
                        scenar_izmen.append(int(it))

                    vr_summ=0
                    for i in scenar_izmen:
                        #print(pcap_cortg[i-1])
                        vr_summ=vr_summ+pcap_cortg[i-1][1]
                    vrsumm_33=vrsumm_33+vr_summ
                    tert={
                    #"params":{
                    #"eb": [{
                    "id":ii,
                    "br":int(vr_summ),
                    "user_scenario":{
                    "id": spisok_scenariev[scenar_numb][0]

                    }, "network_scenario":{
                    "id": 0,
                    "name": "Custom",
                    "jitter" :{
                    "timeup":network_list[network_numb][1]['timeup'],
                    "timedown":network_list[network_numb][1]['timedown'],
                    "value":network_list[network_numb][1]['value']
                    },
                    "burst": {
                    "timeup":network_list[network_numb][2]['timeup'],
                    "timedown":network_list[network_numb][2]['timedown']
                    }
                    }
                    #}]
                    #}
                    }
                    json_list.append(tert)

                    #try :
                        #rr=  req.post(f'http://{udras}/params/eb',json=(json_out))
                        #js = json.loads(rr.text)
                        #error_flag_add_eps=False
                        #add_eps_buferss=0



                    #except Exception as ex:
                        #return  render_template('first.html')

                if network_numb != 0 and scenar_numb != 0:

                    #new_id=int(eps_br[out][3])+i
                    vr_summ1=spisok_scenariev[scenar_numb][0]
                    scenar_izmen=[]


                    #vr_summ=0 #pcap_cortg[i-1][1]
                    scenar_izmen=[]
                    for it in spisok_scenariev[scenar_numb][2] :
                        scenar_izmen.append(int(it))

                    vr_summ=0
                    for i in scenar_izmen:
                        #print(pcap_cortg[i-1])
                        vr_summ=vr_summ+pcap_cortg[i-1][1]
                    vrsumm_33=vrsumm_33+vr_summ
                    tert={
                    #"params":{
                    #"eb": [{
                    "id":ii,
                    "br":int(vr_summ),
                    "user_scenario":{
                    "id": spisok_scenariev[scenar_numb][0]

                    }, "network_scenario":{
                    "id": network_list[network_numb][3]
                    }

                    #}]
                    #}
                    }
                    json_list.append(tert)
                    #try :
                        #rr=  req.post(f'http://{udras}/params/eb',json=(json_out))
                        #js = json.loads(rr.text)
                        #error_flag_add_eps=False
                        #add_eps_buferss=0


                    #except Exception as ex:
                        #return  render_template('first.html')

                if network_numb != 0 and scenar_numb == 0:

                    #new_id=int(eps_br[out][3])+i
                    vr_summ1=spisok_scenariev[scenar_numb][0]
                    scenar_izmen=[]


                    #vr_summ=0 #pcap_cortg[i-1][1]
                    scenar_izmen=[]
                    for it in spisok_scenariev[scenar_numb][2] :
                        scenar_izmen.append(int(it))

                    vr_summ=0
                    for i in scenar_izmen:
                        #print(pcap_cortg[i-1])
                        vr_summ=vr_summ+pcap_cortg[i-1][1]
                    vrsumm_33=vrsumm_33+vr_summ
                    tert={
                    #"params":{
                    #"eb": [{
                    "id":ii,
                    "br":int(vr_summ),
                    "user_scenario":{
                    "id": 0,
                    "name": "Custom",
                    "br": int(vr_summ),
                    "pcap_id":spisok_scenariev[scenar_numb][2]
                    }, "network_scenario":{
                    "id": network_list[network_numb][3]
                    }

                    #}]
                    #}
                    }
                    json_list.append(tert)




                    #try :


                        #rr=  req.post(f'http://{udras}/params/eb',json=(json_out))
                        #js = json.loads(rr.text)

                        #error_flag_add_eps=False
                        #add_eps_buferss=0

                    #except Exception as ex:
                        #return  render_template('first.html')
            if j == col :
                break

        json_out={
        "params":{
        "eb": json_list
        }
        }
        #print('\n json_out=',json_out)
        try :

            rr= req.post(f'http://{udras}/params/eb',json=(json_out))
            js = json.loads(rr.text)
            add_eps_buferss=0

            error_flag_add_eps=False

            if js['response']['code'] == 0 :
                add_eps_buferss=0

                return redirect(url_for('LIST_EPS'))
            else:
                add_eps_buferss=0
                return redirect(url_for('LIST_EPS'))

        except Exception as ex:
            return  render_template('first.html')

        #if js['response']['code'] == 0 :
            #add_eps_buferss=0

            #return redirect(url_for('LIST_EPS'))
        #else:
            #add_eps_buferss=0
            #return redirect(url_for('LIST_EPS'))

@app.route('/eb/add', methods=[ 'POST'])
def eb_add():
    """ add new EPS_BIAR"""
    if request.method == 'POST' :

        global  eps_br
        global stopped_msg_mac ,  stopped_bufer

        new_id=len(eps_br)+1
        #if new_id == 0:
            #new_id=new_id+1

        scenar_izmen=[]
        vr_summ=0

        if new_id <=200 :

            try:
                stopped_bufer=False
                stopped_msg_mac=''
                for i in scenar_izmen:
                    #print(pcap_cortg[i-1])
                    vr_summ=vr_summ+pcap_cortg[i-1][1]

                json_out={
                "params":{
                "eb": [{
                "id":new_id,
                "br":int(vr_summ),
                "user_scenario":{
                "id": 0,
                "name": "Custom",
                "br": int(vr_summ),
                "pcap_id":scenar_izmen
                }, "network_scenario":{
                "id": 0,
                "name": "Custom",
                "jitter" :{
                "timeup":0,
                "timedown":0,
                "value":0
                },
                "burst": {
                "timeup":0,
                "timedown":0
                }
                }
                }]
                }
                }
                rr=  req.post(f'http://{udras}/params/eb',json=(json_out))

                js = json.loads(rr.text)

                if js['response']['code'] == 0 :
                    return redirect(url_for('LIST_EPS'))
                else:
                    return redirect(url_for('LIST_EPS'))
            except Exception as ex:
                return  render_template('first.html')

        #pass
@app.route('/eps_epb/add', methods=[ 'POST','GET'])
def eps_epb_add():

    if request.method == 'POST' or request.method == 'GET':
        global   eps_br  #,spisok_scenariev
        global stopped_msg_mac ,  stopped_bufer , error_flag_add_scenar
        stopped_bufer=False
        error_flag_add_scenar=False
        stopped_msg_mac=''
        bufer_spisok_do=spisok_scenariev[:]
        number_eps= int(request.form['scenar_number'])
        eps_tek_uscher=[]
        g=0
        for itt in eps_br :
            if number_eps == int(itt[3]):
                eps_tek_uscher=deepcopy(itt)
                break
            g=g+1


        ber=[]
        print('\n \n do eps_tek_uscher=',eps_tek_uscher)
        print('do len=',len(eps_tek_uscher[4]))

        if len(eps_tek_uscher[4]) == 3:
            #ber=eps_br[g][4][2].copy()
            ber=deepcopy(eps_tek_uscher[4][2])
            new=[]
            for it in ber:
                new.append(it)
            new.append(1)
            ret=deepcopy(new)

            eps_tek_uscher[4][2] = deepcopy(ret)



            #eps_br[g][4][2]= lister2 #copy.deepcopy(ret)
        else:
            #varinatert=[]
            print('\n !1')
            if 'pcap_id' in eps_tek_uscher[1].keys():
                ber.extend(eps_tek_uscher[1]['pcap_id'])
            else:
                print('\n !2')
                ber.extend(eps_tek_uscher[4][2])
            #varinatert.extend(eps_tek_uscher[4][2])
            new=[]
            for it in ber:
                new.append(it)
            new.append(1)
            ret=deepcopy(new)
            #print('\n \n 2ret=',ret)
            if 'pcap_id' in eps_tek_uscher[1].keys():
                eps_tek_uscher[1]['pcap_id']=deepcopy(ret)


            eps_tek_uscher[4][2]=deepcopy(ret)

        eps_br[g]=deepcopy(eps_tek_uscher)
            #eps_br[g][4]['pcap_id']=  lister2 #copy.deepcopy(ret)

        #print('\n \n \n wert epss=',spisok_scenariev)

        return  redirect(url_for("eb_nastroit",number = number_eps))


@app.route('/eps_nastroika/eps_add_ALL', methods=[ 'POST','GET'])
def eps_epb_add_ALL():

    if request.method == 'POST' or request.method == 'GET':
        global   eps_br  #,spisok_scenariev
        global stopped_msg_mac ,  stopped_bufer , error_flag_add_scenar
        stopped_bufer=False
        error_flag_add_scenar=False
        stopped_msg_mac=''
        bufer_spisok_do=spisok_scenariev[:]
        number_eps= int(request.form['scenar_number2'])

        col=int(request.form['colich'])
        #i = 0
        #for it in range(len())
        i=0
        #summer_velocity=0
        #for it in eps_br:
            #i=i+1
        #if 200 - i+1-col <0 or col == 0:
            #error_flag_add_eps=True
            #return redirect(url_for('LIST_EPS'))

        #scen=request.form.getlist('scenar')
        scenar=request.form.getlist('scenar2') # pcap number
        #scen=int(request.form['scenar_number'])

        eps_tek_uscher=[]
        new=[]
        ret=[]
        g=0
        for itt in eps_br :
            if number_eps == int(itt[3]):
                eps_tek_uscher=deepcopy(itt)
                break
            g=g+1
        il=0
        #print('\n \n eps_tek_uscher=',eps_tek_uscher)
        #print('len=',len(eps_tek_uscher[4]))
        #out_pcap_spis=[]

        #for it in pcap_cortg:
            #bufer_str=''
            #il=il+1
            #out_pcap_spis.append({'key':il,'video':it[0],'br_v':it[1],'path':it[2]})

        for iter in range(col):

            ber=[]
            new=[]
            ret=[]

            if len(eps_tek_uscher[4]) == 3:
                #ber=eps_br[g][4][2].copy()
                ber=deepcopy(eps_tek_uscher[4][2])
                #new=[]
                for it in ber:
                    new.append(it)
                #for ill in out_pcap_spis:
                    #if   ill['']
                new.append(int(scenar[0]))
                ret=deepcopy(new)

                eps_tek_uscher[4][2] = deepcopy(ret)



                #eps_br[g][4][2]= lister2 #copy.deepcopy(ret)
            else:
                #varinatert=[]
                if 'pcap_id' in eps_tek_uscher[1].keys():
                    ber.extend(eps_tek_uscher[1]['pcap_id'])
                else:
                    ber.extend(eps_tek_uscher[4][2])
                #varinatert.extend(eps_tek_uscher[4][2])

                for it in ber:
                    new.append(it)
                new.append(int(scenar[0]))
                ret=deepcopy(new)
                #print('\n \n 2ret=',ret)

                if 'pcap_id' in eps_tek_uscher[1].keys():
                    eps_tek_uscher[1]['pcap_id']=deepcopy(ret)


        eps_tek_uscher[4][2]=deepcopy(ret)

        eps_br[g]=deepcopy(eps_tek_uscher)
            #eps_br[g][4]['pcap_id']=  lister2 #copy.deepcopy(ret)

        #print('\n \n \n wert epss=',spisok_scenariev)

        return  redirect(url_for("eb_nastroit",number = number_eps))



@app.route('/eps_epb/delete/<int:num>', methods=[ 'POST','GET'])
def eps_epb_delete(num):
    global   eps_br
    if request.method == 'POST' or request.method == 'GET':
        number_eps= int(request.form['scenar_number'])
        eps_tek_uscher=[]
        global stopped_msg_mac ,  stopped_bufer , error_flag_add_scenar , error_flag_add_scenar1 , stopped_bufer_delete
        error_flag_add_scenar=False
        error_flag_add_scenar1=False
        stopped_bufer_delete=False
        stopped_bufer=False
        stopped_msg_mac=''
        g=0
        for itt in eps_br :
            if number_eps == int(itt[3]):
                eps_tek_uscher=deepcopy(itt)
                break
            g=g+1

        ber=[]


        new=[]
        ol=0

        if len(eps_br[g][4]) == 3:
            ber=deepcopy(eps_tek_uscher[4][2])
            #new=[]
            #print('\n ber=',ber)
            ogranch=len(ber)

            for it in ber:
                if num == int(it) and ol ==0  and ogranch-ol-1!=0 :
                    ol=ol+1
                    #pass
                else:
                    new.append(it)
                    #break
            #new.append(1)
            eps_tek_uscher[4][2]=deepcopy(new)
        else:
            ber=deepcopy(eps_tek_uscher[4]['pcap_id'])

            for it in ber:
                if num != int(it)and ol ==0:
                    ol=ol+1
                else:
                    new.append(it)
                    #break

            eps_tek_uscher[4]['pcap_id']=deepcopy(new)
        eps_br[g]=deepcopy(eps_tek_uscher)

        return  redirect(url_for("eb_nastroit",number = number_eps))


@app.route('/eb/nastroit/<int:number>', methods=[ 'POST','GET'])
def eb_nastroit(number):
    """change alone EPS_BIAR """
    #print("!!!!!!!!!!!!!!!!!!! rabotaer")
    global  time_otvet , lang_switch , conect ,number_idd , eps_br
    global  spisok_scenariev ,  network_list ,eb_pies_for_one,time_otvet ,regim_rabota_mode ,error_flag_add_scenar , stopped_bufer , stopped_bufer_delete , stopped_msg_mac
    # error_flag_add_scenar

    number_idd=number
    buferr_scena=0
    buferr_network=0
    #print(bufer_menu_ALL_form_eng[6])
    #print(bufer_menu_ALL_form_rus[6])

    punkt_menu_nach=[[bufer_menu_ALL_form_eng[6][0],bufer_menu_ALL_form_eng[6][1] ,bufer_menu_ALL_form_eng[6][2],bufer_menu_ALL_form_eng[6][3],bufer_menu_ALL_form_eng[6][4],bufer_menu_ALL_form_eng[6][5],bufer_menu_ALL_form_eng[6][6],bufer_menu_ALL_form_eng[6][7]
    ,bufer_menu_ALL_form_eng[6][8]
    ,bufer_menu_ALL_form_eng[6][9],bufer_menu_ALL_form_eng[6][10],
    bufer_menu_ALL_form_eng[6][11],bufer_menu_ALL_form_eng[6][12],bufer_menu_ALL_form_eng[6][13]
    ,bufer_menu_ALL_form_eng[6][14],bufer_menu_ALL_form_eng[6][15],bufer_menu_ALL_form_eng[6][16]
    ,bufer_menu_ALL_form_eng[6][17],bufer_menu_ALL_form_eng[6][18],bufer_menu_ALL_form_eng[6][19],bufer_menu_ALL_form_eng[6][20],bufer_menu_ALL_form_eng[6][21],bufer_menu_ALL_form_eng[0][5],bufer_menu_ALL_form_eng[0][6],bufer_menu_ALL_form_eng[6][22]]
    ,[bufer_menu_ALL_form_rus[6][0],bufer_menu_ALL_form_rus[6][1] ,bufer_menu_ALL_form_rus[6][2]
    ,bufer_menu_ALL_form_rus[6][3],bufer_menu_ALL_form_rus[6][4],bufer_menu_ALL_form_rus[6][5]
    ,bufer_menu_ALL_form_rus[6][6],bufer_menu_ALL_form_rus[6][7]
    ,bufer_menu_ALL_form_rus[6][8],bufer_menu_ALL_form_rus[6][9],bufer_menu_ALL_form_rus[6][10]
    ,bufer_menu_ALL_form_rus[6][11],bufer_menu_ALL_form_rus[6][12],bufer_menu_ALL_form_rus[6][13]
    ,bufer_menu_ALL_form_rus[6][14],bufer_menu_ALL_form_rus[6][15],bufer_menu_ALL_form_rus[6][16]
    ,bufer_menu_ALL_form_rus[6][17],bufer_menu_ALL_form_rus[6][18],bufer_menu_ALL_form_rus[6][19],bufer_menu_ALL_form_rus[6][20],bufer_menu_ALL_form_rus[6][21],bufer_menu_ALL_form_rus[0][5],bufer_menu_ALL_form_rus[0][6],bufer_menu_ALL_form_rus[6][22]]]
    lang_bool=False
    punkt_menu=[]


    if lang_switch%2== 0:
        punkt_menu=punkt_menu_nach[0]
        lang_bool=True
    else:
        punkt_menu=punkt_menu_nach[1]
        lang_bool=False


    if lang_switch%2== 0:
        #punkt_menu=punkt_menu_nach[0]
        #lang_bool=True
        rabota_status=[{'key' : 0 , 'name' : bufer_menu_ALL_form_eng[0][0]},{'key' : 1 , 'name' : bufer_menu_ALL_form_eng[0][1]}]


    else:
        #punkt_menu=punkt_menu_nach[1]
        rabota_status=[{'key': 0 , 'name' : bufer_menu_ALL_form_rus[0][0]},{'key' : 1 , 'name' : bufer_menu_ALL_form_rus[0][1]} ]


    string=''

    for it in rabota_status:
        if it['key'] == regim_rabota_mode :
            string= it['name']
            break
    if lang_switch%2== 0:
        string=' '+string
    else:
        string=' '+string

    if request.method == 'POST' or request.method == 'GET':
        global conect  , ind_sce_0_iter , ind_sce_0,  net_sce_0 , indef_scen ,indef_netw
        eps_tek_uscher=[]
        local34=0
        local84=0

        g=0

        if ind_sce_0_iter==0 :
            ind_sce_0=int(request.form['scenar'])
            net_sce_0= int(request.form['network'])


        for itt in eps_br :
            if number == int(itt[3]):
                eps_tek_uscher=itt
                break
            g=g+1

        #print('\n \n eps_br=',eps_br[g])
        lerg2=[]


        for it in spisok_scenariev:
            if it[0] == ind_sce_0:
                break
            local34=local34+1


        if   spisok_scenariev[local34][0] == 0  :
            if ind_sce_0_iter==0 :
                if  'pcap_id' in eps_br[g][1].keys():
                    if (eps_br[g][1]['pcap_id']) == (spisok_scenariev[local34][2]) :

                        lerg2=spisok_scenariev[local34]

                        eps_br[g][1]['id']=lerg2[0]
                        eps_br[g][4]=lerg2
                    else:
                        lerg2=[eps_br[g][1]['id'],eps_br[g][1]['name'],eps_br[g][1]['pcap_id']]


                        eps_br[g][4]=deepcopy(lerg2)
                        pass
                else:

                        lerg2=spisok_scenariev[local34]

                        eps_br[g][1]['id']=lerg2[0]
                        eps_br[g][4]=lerg2

        else:
            if ind_sce_0_iter==0 :

                eps_br[g][1]=deepcopy(spisok_scenariev[local34])
                eps_br[g][4]=deepcopy(spisok_scenariev[local34])



        ind_sce_0_iter=ind_sce_0_iter+1



        eps_tek_uscher=deepcopy(eps_br[g])
        #print('eps_br=',eps_br)
        #print('g=',g)
        #print('eps_tek_uscher=',eps_tek_uscher)



        zagolovok =[]
        #zagolovok =[]

        eb_pies_for_one=eb_pies_for_one+1
        outp=[]
        for it in range(eb_pies_for_one) :
            outp.append('')

        scenar_podchodit=[]
        scenar_netw=[]

        g=0
        out_pcap_spis=[]
        string_pcap=[]
        out_pcap_id=[]
        size_min=0
        spisok_pcapof=[]
        for it in pcap_cortg:
            bufer_str=''
            g=g+1
            out_pcap_spis.append({'key':g,'video':it[0],'br_v':it[1],'path':it[2]})
            bufer_str=str(it[0])+', '+str(it[1])+', '+str(it[2])
            string_pcap.append({'key':g,'string':bufer_str,'br_v':it[1]})


        #print('\n eps_tek_uscher[1][]=',eps_tek_uscher)

        if local34 ==0 :


            if 'br' in eps_tek_uscher[1].keys() :
                for iler in eps_tek_uscher[4][2]:
                     spisok_pcapof.append(int(iler))

                #size_min=eps_tek_uscher[1]['br']
                #
            else:

                for iter in eps_tek_uscher[4][2]:
                    spisok_pcapof.append(int(iter))
                    for iler in out_pcap_spis:
                        if int(iter) ==int( iler['key']):
                            size_min=size_min+iler['br_v']

        else:

            for itr in eps_tek_uscher[4][2]:
                 spisok_pcapof.append(int(itr))

            size_min=0
            for iter in spisok_pcapof:
                for iler in out_pcap_spis:
                    if iter == iler['key']:
                        size_min=size_min+iler['br_v']

        size_min=0
        size_max=int(eps_tek_uscher[0])
        for iter in spisok_pcapof:
            for iler in out_pcap_spis:
                if iter == int(iler['key']):
                    size_min=size_min+iler['br_v']

        out_pcap_id=[]
        for iter in spisok_pcapof:

            out_pcap_id.append({'znach':int(iter)})


        for it in network_list:
            if it[3] == net_sce_0:
                break
            local84=local84+1
        if local84 ==0 :
            if eps_tek_uscher[2]['id']==0 :

                zagolovok.append((eps_tek_uscher[2]['jitter']['timeup']))
                zagolovok.append((eps_tek_uscher[2]['jitter']['timedown']))
                zagolovok.append((eps_tek_uscher[2]['jitter']['value']))
                zagolovok.append((eps_tek_uscher[2]['burst']['timeup']))
                zagolovok.append((eps_tek_uscher[2]['burst']['timedown']))
            else:
                zagolovok.append((network_list[0][1]['timeup']))
                zagolovok.append((network_list[0][1]['timedown']))
                zagolovok.append((network_list[0][1]['value']))
                zagolovok.append((network_list[0][2]['timeup']))
                zagolovok.append((network_list[0][2]['timedown']))




        else:

            zagolovok.append(int(network_list[local84][1]['timeup']))
            zagolovok.append(int(network_list[local84][1]['timedown']))
            zagolovok.append(int(network_list[local84][1]['value']))
            zagolovok.append(int(network_list[local84][2]['timeup']))
            zagolovok.append(int(network_list[local84][2]['timedown']))
            ############################################################
        start_flag=True

        start_flag=True
        if start_flag1%2 == 0:
            start_flag=True
        else:
            start_flag=False
        iter_nacha=[1]

        return render_template('form_nastroika.html',eps_number=number,size_min=size_min, size_max=size_max, punkt_menu=punkt_menu,conect=conect,lang_bool=lang_bool,

        int_scenar=ind_sce_0,int_netw=net_sce_0,pcap_spis=out_pcap_spis,pcap_id=out_pcap_id,string_pcap=string_pcap,zagolovok=zagolovok,eb_pies_for_one=outp,number=number,time_otvet=time_otvet,string=string
        , error_flag_add_scenar=error_flag_add_scenar,start_flag=start_flag , iter_nacha=iter_nacha,error_flag_add_scenar1=error_flag_add_scenar1,global_velocity=global_velocity,stopped_bufer=stopped_bufer,stopped_bufer_delete=stopped_bufer_delete,stopped_msg_mac=stopped_msg_mac)

@app.route('/eps_scenar/add_ALL', methods=[ 'POST'])
def add_al2_pcap_scen():
    global  time_otvet , lang_switch , conect , start_flag
    global stopped_msg_mac ,  stopped_bufer , error_flag_add_scenar
    stopped_bufer=False
    #error_flag_add_scenar= False
            #if vr_summ >50000000 :
                #number_idd
                #error_flag_add_scenar=True

                #return  redirect(url_for('eps_scenar',number=number_idd))
    stopped_msg_mac=''
    #punkt_menu_nach=[['Back','Change' ,'EPS number','number user scenario','number network scenario'],['Назад','Изменить' ,'Номер EPS','Номер 	пользовательского сценария','Номер Сетевого сценария']]
    lang_bool=False
    #punkt_menu=[]
    #if lang_switch%2== 0:
        #punkt_menu=punkt_menu_nach[0]
        #lang_bool=True
    #else:
        #punkt_menu=punkt_menu_nach[1]
        #lang_bool=False
    if request.method == 'POST':
            col=int(request.form['colich'])
            #i = 0
            #for it in range(len())
            i=0
            #summer_velocity=0
            #for it in eps_br:
                #i=i+1
            #if 200 - i+1-col <0 or col == 0:
                #error_flag_add_eps=True
                #return redirect(url_for('LIST_EPS'))

            #scen=request.form.getlist('scenar')
            scenar=request.form.getlist('scenar2') # pcap number
            scen=int(request.form['scenar_number'])

            global spisok_scenariev

            bufer=0
            g=0
            values=[]
            buferr=[]
            video=[]
            pcap_velocity=[]
            video=0
            dontvideo=0
            for it in spisok_scenariev :
                if scen == int(it[0]):
                    bufer=g
                g=g+1
            znach=spisok_scenariev[bufer]

            #print('\n pcap_cortg=',pcap_cortg)
            #print('\n scenar=',scenar)
            #print('\n col=',col)
            #print('\n scen=',scen)

            for iter in range(col):


                for it in znach[2]:
                    puth=[]
                    puth.append(pcap_cortg[int(scenar[0])-1][0])
                    puth.append(pcap_cortg[int(scenar[0])-1][1])
                    puth.append(pcap_cortg[int(scenar[0])-1][2])
                    buferr.append(puth)
                size=0
                ###############################################################################
                g=0
                out_pcap_spis=[]
                string_pcap=[]
                out_pcap_id=[]
                for it in pcap_cortg:
                    bufer_str=''
                    g=g+1
                    out_pcap_spis.append({'key':g,'video':it[0],'br_v':it[1],'path':it[2]})
                    bufer_str=str(it[0])+', '+str(it[1])+', '+str(it[2])
                    string_pcap.append({'key':g,'string':bufer_str})
                ###############################################################################


                ##print('spisok=',spisok_scenariev[number-1])
                promeg=spisok_scenariev[bufer][2]
                pr=[]
                #print('spisok_scenariev[bufer]=',spisok_scenariev[bufer])


                spisok_scenariev[bufer][2].append(int(scenar[0]))

                scenar_podchodit=spisok_scenariev[bufer][2]
                out_pcap_id=[]
                for i in scenar_podchodit:
                    out_pcap_id.append({'znach':i})

                for i in     out_pcap_id :
                    ##print('i=',i)
                    for j in out_pcap_spis:
                        ##print('j=',j)
                        if i['znach'] == j['key']:
                            size=size+j['br_v']
                            if j['video'] :
                                video=video+j['br_v']
                            else:
                                dontvideo=dontvideo+j['br_v']




            values.append(video/size*100)
            values.append(dontvideo/size*100)

            start_flag=True

            start_flag=True
            if start_flag1%2 == 0:
                start_flag=True
            else:
                start_flag=False


            return   redirect(url_for('eps_scenar',number=number_idd))#render_template('epsbiar_scene.html',punkt_menu=punkt_menu,conect=conect, scen_number =scen, set=zip(values,labels),berr=buferr ,size=size,string_pcap=string_pcap,pcap_id=out_pcap_id,time_otvet=time_otvet,start_flag1=start_flag)



@app.route('/eps_scenar/add', methods=[ 'POST'])
def add_pcap_scen():
    global  time_otvet , lang_switch , conect , start_flag
    global stopped_msg_mac ,  stopped_bufer , error_flag_add_scenar
    stopped_bufer=False
    #error_flag_add_scenar= False
            #if vr_summ >50000000 :
                #number_idd
                #error_flag_add_scenar=True

                #return  redirect(url_for('eps_scenar',number=number_idd))
    stopped_msg_mac=''
    punkt_menu_nach=[['Back','Change' ,'EPS number','number user scenario','number network scenario'],['Назад','Изменить' ,'Номер EPS','Номер 	пользовательского сценария','Номер Сетевого сценария']]
    lang_bool=False
    punkt_menu=[]
    if lang_switch%2== 0:
        punkt_menu=punkt_menu_nach[0]
        lang_bool=True
    else:
        punkt_menu=punkt_menu_nach[1]
        lang_bool=False
    if request.method == 'POST':

            scen=int(request.form['scenar_number'])

            global spisok_scenariev

            bufer=0
            g=0

            for it in spisok_scenariev :
                if scen == int(it[0]):
                    bufer=g
                g=g+1
            znach=spisok_scenariev[bufer]
            buferr=[]
            video=[]
            pcap_velocity=[]
            #print('2=',znach)
            values=[]

            for it in znach[2]:
                puth=[]
                puth.append(pcap_cortg[it-1][0])
                puth.append(pcap_cortg[it-1][1])
                puth.append(pcap_cortg[it-1][2])
                buferr.append(puth)
            size=0
            ###############################################################################
            g=0
            out_pcap_spis=[]
            string_pcap=[]
            out_pcap_id=[]
            for it in pcap_cortg:
                bufer_str=''
                g=g+1
                out_pcap_spis.append({'key':g,'video':it[0],'br_v':it[1],'path':it[2]})
                bufer_str=str(it[0])+', '+str(it[1])+', '+str(it[2])
                string_pcap.append({'key':g,'string':bufer_str})
            ###############################################################################

            video=0
            dontvideo=0
            #print('spisok=',spisok_scenariev[number-1])
            promeg=spisok_scenariev[bufer][2]
            pr=[]


            spisok_scenariev[bufer][2].append(1)

            scenar_podchodit=spisok_scenariev[bufer][2]
            out_pcap_id=[]
            for i in scenar_podchodit:
                out_pcap_id.append({'znach':i})

            for i in     out_pcap_id :
                #print('i=',i)
                for j in out_pcap_spis:
                    #print('j=',j)
                    if i['znach'] == j['key']:
                        size=size+j['br_v']
                        if j['video'] :
                            video=video+j['br_v']
                        else:
                            dontvideo=dontvideo+j['br_v']




            values.append(video/size*100)
            values.append(dontvideo/size*100)

            start_flag=True

            start_flag=True
            if start_flag1%2 == 0:
                start_flag=True
            else:
                start_flag=False


            return   redirect(url_for('eps_scenar',number=number_idd))#render_template('epsbiar_scene.html',punkt_menu=punkt_menu,conect=conect, scen_number =scen, set=zip(values,labels),berr=buferr ,size=size,string_pcap=string_pcap,pcap_id=out_pcap_id,time_otvet=time_otvet,start_flag1=start_flag)




@app.route('/eps_scenar/delete/<int:number>', methods=[ 'POST'])
def delete_pcap_scen(number):
    global  time_otvet , lang_switch , conect ,number_idd , spisok_scenariev , error_flag_add_scenar ,error_flag_add_scenar1 , stopped_bufer_delete
    error_flag_add_scenar= False
    error_flag_add_scenar1= False
    stopped_bufer_delete=False

    #number_idd=number

    punkt_menu_nach=[['Back','Change' ,'EPS number','number user scenario','number network scenario'],['Назад','Изменить' ,'Номер EPS','Номер 	пользовательского сценария','Номер Сетевого сценария']]
    lang_bool=False
    punkt_menu=[]
    if lang_switch%2== 0:
        punkt_menu=punkt_menu_nach[0]
        lang_bool=True
    else:
        punkt_menu=punkt_menu_nach[1]
        lang_bool=False
    if request.method == 'POST':
        scen=int(request.form['scenar_number'])
        bufer=0
        g=0

        for it in spisok_scenariev :
            if scen == int(it[0]):
                bufer=g
            g=g+1
        if len(spisok_scenariev[bufer][2]) >1 :
            scen=int(request.form['scenar_number'])

            pcap_id=int(number)


            znach=spisok_scenariev[bufer]
            buferr=[]
            video=[]
            pcap_velocity=[]
            #print('2=',znach)
            values=[]

            for it in znach[2]:
                puth=[]
                puth.append(pcap_cortg[it-1][0])
                puth.append(pcap_cortg[it-1][1])
                puth.append(pcap_cortg[it-1][2])
                buferr.append(puth)
            size=0
            ###############################################################################
            g=0
            out_pcap_spis=[]
            string_pcap=[]
            out_pcap_id=[]
            for it in pcap_cortg:
                bufer_str=''
                g=g+1
                out_pcap_spis.append({'key':g,'video':it[0],'br_v':it[1],'path':it[2]})
                bufer_str=str(it[0])+', '+str(it[1])+', '+str(it[2])
                string_pcap.append({'key':g,'string':bufer_str})
            ###############################################################################

            video=0
            dontvideo=0
            #print('spisok=',spisok_scenariev[number-1])
            promeg=spisok_scenariev[bufer][2]
            pr=[]
            g=0
            for it in promeg:
                if it == pcap_id:

                    break
                g=g+1

            spisok_scenariev[bufer][2].pop(g)

            scenar_podchodit=spisok_scenariev[bufer][2]
            out_pcap_id=[]
            for i in scenar_podchodit:
                out_pcap_id.append({'znach':i})

            for i in     out_pcap_id :
                #print('i=',i)
                for j in out_pcap_spis:
                    #print('j=',j)
                    if i['znach'] == j['key']:
                        size=size+j['br_v']
                        if j['video'] :
                            video=video+j['br_v']
                        else:
                            dontvideo=dontvideo+j['br_v']

            #if size >0 :
            values.append(video/size*100)
            values.append(dontvideo/size*100)

            start_flag=True
            if start_flag1%2 == 0:
                start_flag=True
            else:
                start_flag=False
            #if scenar_podchodit
            #scenar_podchodit=tuple(scenar_podchodit)


            return  redirect(url_for('eps_scenar',number=number_idd))#render_template('epsbiar_scene.html',punkt_menu=punkt_menu,conect=conect,
            # scen_number =scen, set=zip(values,labels)
             #,berr=buferr ,size=size,string_pcap=string_pcap
             #,pcap_id=out_pcap_id,time_otvet=time_otvet,start_flag1=start_flag)
        else:
            return redirect(url_for('eps_scenar',number=number_idd))



@app.route('/eps/scenar/delete/<int:number>', methods=[ 'POST'])
def delete_scenar(number):
    if request.method == 'POST':
        global stopped_bufer , stopped_msg_mac , spisok_scenariev , stopped_bufer_delete , stopped_bufer_delete

        for it in eps_br:
            if it[1]['id'] == int(number) :
                if lang_switch%2== 0:
                    stopped_msg_mac=bufer_menu_ALL_form_eng[0][2]

                else:
                    stopped_msg_mac=bufer_menu_ALL_form_rus[0][2]


                stopped_bufer =False
                stopped_bufer_delete=True

                return redirect(url_for('scenar_spis'))
        if number == 0:

            stopped_bufer=False
            stopped_bufer_delete=False
            stopped_msg_mac=''

        if number !=0  and number >0:
            try:
                stopped_bufer=False
                stopped_msg_mac=''
                stopped_bufer_delete=False

                json_out={
                "params":{
                "user_scenario":[{
                "id":int(number)
                }]
                }
                }
                json_out2=json.dumps(json_out)

                rr=req.delete(f'http://{udras}/params/user_scenario',json=(json_out))

                js = json.loads(rr.text)
                ber=spisok_scenariev
                spisok_scenariev=[]
                key=0

                print('key=',key)
                print('js=',js)

                for iler in ber:

                    if int(iler[0]) == int(number):
                        key=int(number)
                        continue
                    else:
                        #iler
                        bufer=[]
                        bufer.append(key)
                        bufer.append(iler[1])
                        bufer.append(iler[2])
                        print('bufer=',bufer)
                        #bufer[0]=key
                        spisok_scenariev.append(bufer)
                    key=key+1

                print('js=',spisok_scenariev)

                if js['response']['code'] == 0 :
                    return redirect(url_for('scenar_spis'))
                else:
                    return redirect(url_for('scenar_spis'))

            except Exception as ex:
                return  render_template('first.html')
        else:
            return redirect(url_for('scenar_spis'))



@app.route('/eps/network/delete/<int:number>', methods=[ 'POST'])
def delete_network(number):
    if request.method == 'POST':
        global stopped_bufer , stopped_msg_mac ,  network_list , stopped_bufer_delete
        if number == 0:
            #global stopped_bufer , stopped_msg_mac ,  network_list
            stopped_bufer=False
            stopped_msg_mac=''


        if number !=0  and number >0:


            for it in eps_br:
                if it[2]['id'] == int(number) :
                    if lang_switch%2== 0:
                        stopped_msg_mac=bufer_menu_ALL_form_eng[0][2]

                    else:
                        stopped_msg_mac=bufer_menu_ALL_form_rus[0][2]

                    #stopped_bufer =True # Подубать как чтобы можно зайти в форму .
                    stopped_bufer_delete=True

                    return redirect(url_for('network_spis'))


            try:
                stopped_bufer=False
                stopped_msg_mac=''
                stopped_bufer_delete=False

                json_out={
                "params":{
                "network_scenario":[{
                "id":int(number)
                }]
                }
                }
                json_out2=json.dumps(json_out)
                #print('delete=',json_out2)
                stopped_bufer=False
                stopped_msg_mac=''

                rr=req.delete(f'http://{udras}/params/network_scenario',json=(json_out))

                js = json.loads(rr.text)
                ber=network_list
                network_list=[]
                for iler in ber:
                    if int(iler[3]) == int(number):
                        continue
                    else:
                        network_list.append(iler)

                #print('js=',js)
                if js['response']['code'] == 0 :
                    return redirect(url_for('network_spis'))
                else:
                    return redirect(url_for('network_spis'))




            except Exception as ex:
                return  render_template('first.html')
        else:
            return redirect(url_for('network_spis'))



@app.route('/eb/delete/<int:number>', methods=[ 'POST','GET'])
def delete_eb(number):
    if request.method == 'POST' or request.method == 'GET' :
        global stopped_bufer , stopped_msg_mac , eps_br , error_flag_add_scenar , error_flag_add_scenar1 ,error_flag_add_eps , stopped_bufer_delete


        #if len(eps_br)>1 :
        """delete one EPS_BIAR """
        start_flag=True
        if start_flag1%2 == 0:
            start_flag=True
        else:
            start_flag=False
        #print('\n start_flag=',start_flag)
        #print('\n len(eps_br)=',len(eps_br))

        if start_flag== False and len(eps_br)-1==0 :
            stopped_bufer=True

            if lang_switch%2== 0:
                stopped_msg_mac=bufer_menu_ALL_form_eng[0][4]

            else:
                stopped_msg_mac=bufer_menu_ALL_form_rus[0][4]


            return redirect(url_for('LIST_EPS'))


        try:
            stopped_bufer=False
            stopped_msg_mac=''
            error_flag_add_scenar=False
            error_flag_add_scenar1=False
            error_flag_add_eps=False
            stopped_bufer_delete=False

            json_out={
            "params":{
            "eb":[{
            "id":int(number)
            }]
            }
            }
            json_out2=json.dumps(json_out)
            #print('do do rr=',json_out2)

            rr=  req.delete(f'http://{udras}/params/eb',json=(json_out))

            js = json.loads(rr.text)
            #print('delete outrr=',js)
            #print('js=',js)
            if js['response']['code'] == 0 :
                return redirect(url_for('LIST_EPS'))
            else:
                return redirect(url_for('LIST_EPS'))

        except Exception as ex:
            return  redirect(url_for('LIST_EPS'))
        #else:
            #return redirect(url_for('LIST_EPS'))

                #pass

        #rr=req.get(f'http://{udras}/params/eb')


    #pass
@app.route('/eps/scenar/<int:number>', methods=[ 'POST','GET'])
def eps_scenar(number):
    """  customization of an individual scenario """
    global lang_switch , conect , number_idd , regim_rabota_mode , indef_froma , stopped_msg_mac ,  stopped_bufer , stopped_bufer_delete
    number_idd=number
    indef_froma=6
    #if stopped_bufer ==True:
        #return redirect(url_for('gra'))
    punkt_menu=[]

    punkt_menu_nach=[[bufer_menu_ALL_form_eng[4][0],bufer_menu_ALL_form_eng[4][1] ,bufer_menu_ALL_form_eng[4][2],bufer_menu_ALL_form_eng[4][3],bufer_menu_ALL_form_eng[4][4]
    ,bufer_menu_ALL_form_eng[4][5],bufer_menu_ALL_form_eng[4][6],bufer_menu_ALL_form_eng[4][7],bufer_menu_ALL_form_eng[4][8],bufer_menu_ALL_form_eng[4][9]
    ,bufer_menu_ALL_form_eng[4][10],bufer_menu_ALL_form_eng[4][11],bufer_menu_ALL_form_eng[4][12],bufer_menu_ALL_form_eng[4][13],bufer_menu_ALL_form_eng[4][14],bufer_menu_ALL_form_eng[0][5],bufer_menu_ALL_form_eng[0][6],bufer_menu_ALL_form_eng[4][15]]
    ,[bufer_menu_ALL_form_rus[4][0],bufer_menu_ALL_form_rus[4][1] ,bufer_menu_ALL_form_rus[4][2],bufer_menu_ALL_form_rus[4][3],bufer_menu_ALL_form_rus[4][4]
    ,bufer_menu_ALL_form_rus[4][5],bufer_menu_ALL_form_rus[4][6],bufer_menu_ALL_form_rus[4][7],bufer_menu_ALL_form_rus[4][8],bufer_menu_ALL_form_rus[4][9]
    ,bufer_menu_ALL_form_rus[4][10],bufer_menu_ALL_form_rus[4][11],bufer_menu_ALL_form_rus[4][12],bufer_menu_ALL_form_rus[4][13],bufer_menu_ALL_form_rus[4][14],bufer_menu_ALL_form_rus[0][5],bufer_menu_ALL_form_rus[0][6],bufer_menu_ALL_form_rus[4][15]]]

    lang_bool=False
    stopped_bufer_delete=False
    punkt_menu=[]
    if lang_switch%2== 0:
        punkt_menu=punkt_menu_nach[0]
        lang_bool=True
    else:
        punkt_menu=punkt_menu_nach[1]
        lang_bool=False
    #global conect
    if lang_switch%2== 0:
        #punkt_menu=punkt_menu_nach[0]
        #lang_bool=True
        rabota_status=[{'key' : 0 , 'name' : bufer_menu_ALL_form_eng[0][0]},{'key' : 1 , 'name' : bufer_menu_ALL_form_eng[0][1]}]


    else:
        #punkt_menu=punkt_menu_nach[1]
        rabota_status=[{'key': 0 , 'name' : bufer_menu_ALL_form_rus[0][0]},{'key' : 1 , 'name' : bufer_menu_ALL_form_rus[0][1]} ]


    string=''

    for it in rabota_status:
        if it['key'] == regim_rabota_mode :
            string= it['name']
            break
    if lang_switch%2== 0:
        string=' '+string
    else:
        string=' '+string
    print('\n punkt_menu_nach=',punkt_menu_nach)

    if request.method == 'POST' or request.method == 'GET':

        bufer=0
        g=0



        for it in spisok_scenariev :
            if number == int(it[0]):
                bufer=g
            g=g+1

        znach=spisok_scenariev[bufer]
        buferr=[]
        video=[]
        pcap_velocity=[]
        #print('2=',znach)
        values=[]

        for it in znach[2]:
            puth=[]
            puth.append(pcap_cortg[it-1][0])
            puth.append(pcap_cortg[it-1][1])
            puth.append(pcap_cortg[it-1][2])
            buferr.append(puth)
        size=0
        ###############################################################################
        g=0
        out_pcap_spis=[]
        string_pcap=[]
        out_pcap_id=[]
        for it in pcap_cortg:
            bufer_str=''
            g=g+1
            out_pcap_spis.append({'key':g,'video':it[0],'br_v':it[1],'path':it[2]})
            bufer_str=str(it[0])+', '+str(it[1])+', '+str(it[2])
            string_pcap.append({'key':g,'string':bufer_str})
        ###############################################################################

        video=0
        dontvideo=0
        #
        scenar_podchodit=spisok_scenariev[bufer][2]
        out_pcap_id=[]
        g=1
        for i in scenar_podchodit:
            out_pcap_id.append({'znach':i,'numb':g})
            g=g+1

        for i in     out_pcap_id :
            #print('i=',i)
            for j in out_pcap_spis:
                #print('j=',j)
                if i['znach'] == j['key']:
                    size=size+j['br_v']
                    if j['video'] :
                        video=video+j['br_v']
                    else:
                        dontvideo=dontvideo+j['br_v']




        values.append(video/size*100)
        values.append(dontvideo/size*100)

        start_flag=True
        if start_flag1%2 == 0:
            start_flag=True
        else:
            start_flag=False
        iter_nacha=[1]

        print('\n stopped_bufer=',stopped_bufer)
        print('\n stopped_bufer_delete=',stopped_bufer_delete)
        print('\n stopped_msg_mac=',stopped_msg_mac)
        print('\n error_flag_add_scenar=',error_flag_add_scenar)
        print('\n error_flag_add_scenar=',error_flag_add_scenar)



        return render_template('epsbiar_scene.html',punkt_menu=punkt_menu,conect=conect,
        lang_switch=lang_bool, scen_number=number,
        set=zip(values,labels),berr=buferr ,size=size,string_pcap=string_pcap,pcap_id=out_pcap_id,
        time_otvet=time_otvet,start_flag1=start_flag,string=string , error_flag_add_scenar=error_flag_add_scenar,iter_nacha=iter_nacha,error_flag_add_scenar1=error_flag_add_scenar1,global_velocity=global_velocity,stopped_msg_mac=stopped_msg_mac,stopped_bufer=stopped_bufer,stopped_bufer_delete=stopped_bufer_delete)


@app.route('/network/add', methods=[ 'POST'])
def network_add():
    if request.method == 'POST':
        global network_list  , stopped_bufer , stopped_msg_mac , stopped_bufer_delete
        new_id=len(network_list)+1
        name =request.form['name']
        znach=[]

        max=0
        for it in network_list :
            if it[3]> max:
                max=int(it[3])
        max=max+1

        #name =request.form.getlist['name']
        scenar= request.form.getlist('scenar')
        int_sceanar=[]
        for i in  scenar:
            int_sceanar.append(int(i))
        #print('\n network_list=',network_list)
        #print('\n scenar=',scenar)
        #print('\n max=',max)
        #print('\n int_sceanar[0]=',int_sceanar[0])
        #if network_list
        for iler in network_list:
            #print('iler=',iler[3])
            if int(iler[3])== int(int_sceanar[0]):
                znach=iler
                break
        #print('\n znach=',znach)
        #znach=network_list[int_sceanar[0]-1]
        js_jitter=znach[1]
        zagolovok =[]
        jitter_timeup=int(js_jitter['timeup'])
        jitter_timedown=int(js_jitter['timedown'])
        jitter_value=int(js_jitter['value'])
        zagolovok.append(int(js_jitter['timeup']))
        zagolovok.append(int(js_jitter['timedown']))
        zagolovok.append(int(js_jitter['value']))
        js_jitter=znach[2]
        #zagolovok =[]
        burst_timeup=int(js_jitter['timeup'])
        burst_timedown=int(js_jitter['timedown'])
        zagolovok.append(int(js_jitter['timeup']))
        zagolovok.append(int(js_jitter['timedown']))


        json_out={
        "params":{
        "network_scenario":[{
        "id":max,
        "name": name,
        "jitter" :{
        "timeup":jitter_timeup,
        "timedown":jitter_timedown,
        "value":jitter_value
        },
        "burst": {
        "timeup":burst_timeup,
        "timedown":burst_timedown
        }
        }]
        }
        }
        print('\n json_out=',json_out)
        print('\n network_list=',network_list)
        try :
            #['Custom', {'timedown': 0, 'timeup': 34, 'value': 0}, {'timedown': 0, 'timeup': 0}, 0]
            bufer=[]
            bufer.append(name)
            bufer.append({'timedown': jitter_timeup, 'timeup': jitter_timedown, 'value': jitter_value})
            bufer.append({'timedown': burst_timeup, 'timeup': burst_timedown  })
            bufer.append(max)

            network_list.append(bufer)
            stopped_bufer=False
            stopped_bufer_delete=False
            stopped_msg_mac=''
            rr=req.post(f'http://{udras}/params/network_scenario',json=(json_out))
            js = json.loads(rr.text)

            if js['response']['code'] == 0 :
                return redirect(url_for('network_spis'))
            else:
                return redirect(url_for('network_spis'))
        except Exception as ex:
            return  render_template('first.html')

        #print('scenar',spisok_scenariev[int_sceanar[0]-1])
        pass
    #pass
        #pass
@app.route('/izmen_network/new', methods=[ 'POST'])
def network_change():
    global  network_list , eps_network_buferss
    if request.method == 'POST':
        eps_network_buferss=eps_network_buferss+1

        id_change=int(request.form['scenar_number234'])
        timeup_jitter=int(request.form['timeup_jitter'])
        timedown_jitter=int(request.form['timedown_jitter'])
        value_jitter=int(request.form['value_jitter'])
        timeup_burst=int(request.form['timeup_burst'])
        timedown_burst=int(request.form['timedown_burst'])
        bufer_network=0
        for it in network_list:

            if it[3] == id_change:
                break
            bufer_network=bufer_network+1
        #g=0
        #for it in range(len(bufer_network)) :
            #g=g+1
        #bufer_network=g

        #if bufer_network!=0:
        #print(network_list[bufer_network])


        name=network_list[bufer_network][0]
        #if eps_network_buferss==1:
        if id_change != 0 :
            json_out={
            "params":{
            "network_scenario":[{
            "id": id_change,
            "name": name,
            "jitter" :{
            "timeup":timeup_jitter,
            "timedown":timedown_jitter,
            "value":value_jitter
            },
            "burst": {
            "timeup":timeup_burst,
            "timedown":timedown_burst
            }
            }]
            }
            }
            rr=req.put(f'http://{udras}/params/network_scenario',json=(json_out))


            js = json.loads(rr.text)
            eps_network_buferss=0

            if js['response']['code'] == 0 :
                return redirect(url_for('network_spis'))
            else:
                return redirect(url_for('network_spis'))
        else:
            network_list[id_change]=['Custom',{'timedown': timedown_jitter, 'timeup': timeup_jitter, 'value': value_jitter},{'timedown': timedown_burst, 'timeup': timeup_burst},network_list[bufer_network][3]]
            return redirect(url_for('network_spis'))

    #pass
@app.route('/eps/network/<int:number>', methods=[ 'POST','GET'])
def eps_network(number):
    global lang_switch , conect , number_idd ,regim_rabota_mode  , eps_network_buferss , stopped_bufer ,stopped_bufer , stopped_bufer_delete
    number_idd=number
    stopped_bufer_delete=False

    punkt_menu=[]
    punkt_menu_nach=[[bufer_menu_ALL_form_eng[8][0],bufer_menu_ALL_form_eng[8][1],bufer_menu_ALL_form_eng[8][2],bufer_menu_ALL_form_eng[8][3]
    ,bufer_menu_ALL_form_eng[8][4],bufer_menu_ALL_form_eng[8][5],bufer_menu_ALL_form_eng[8][6],bufer_menu_ALL_form_eng[8][7],bufer_menu_ALL_form_eng[0][5],bufer_menu_ALL_form_eng[0][6]  ],
    [bufer_menu_ALL_form_rus[8][0],bufer_menu_ALL_form_rus[8][1],bufer_menu_ALL_form_rus[8][2],bufer_menu_ALL_form_rus[8][3],bufer_menu_ALL_form_rus[8][4],bufer_menu_ALL_form_rus[8][5]
    ,bufer_menu_ALL_form_rus[8][6],bufer_menu_ALL_form_rus[8][7],bufer_menu_ALL_form_rus[0][5] ,bufer_menu_ALL_form_rus[0][6]  ]]

    lang_bool=False
    punkt_menu=[]
    if lang_switch%2== 0:
        punkt_menu=punkt_menu_nach[0]
        lang_bool=True
    else:
        punkt_menu=punkt_menu_nach[1]
        lang_bool=False
    #global conect
    if lang_switch%2== 0:
        #punkt_menu=punkt_menu_nach[0]
        #lang_bool=True
        rabota_status=[{'key' : 0 , 'name' : bufer_menu_ALL_form_eng[0][0]},{'key' : 1 , 'name' : bufer_menu_ALL_form_eng[0][1]}]


    else:
        #punkt_menu=punkt_menu_nach[1]
        rabota_status=[{'key': 0 , 'name' : bufer_menu_ALL_form_rus[0][0]},{'key' : 1 , 'name' : bufer_menu_ALL_form_rus[0][1]} ]


    string=''

    for it in rabota_status:
        if it['key'] == regim_rabota_mode :
            string= it['name']
            break

    if lang_switch%2== 0:
        string=' '+string
    else:
        string=' '+string

    if request.method == 'POST' or request.method == 'GET':
        number_idd=number
        #znach=network_list[number-1]
        bufer_network=0
        #if stopped_bufer ==True:
            #return redirect(url_for('gra'))
        #print('network_list=',network_list)
        for it in network_list:
            if it[3] == number:
                break
            bufer_network=bufer_network+1



        znach=network_list[bufer_network]
        buferr=[]
        video=[]
        pcap_velocity=[]
        js_jitter=znach[1]
        zagolovok =[]
        zagolovok.append(int(js_jitter['timeup']))
        zagolovok.append(int(js_jitter['timedown']))
        zagolovok.append(int(js_jitter['value']))
        js_jitter=znach[2]
        #zagolovok =[]
        zagolovok.append(int(js_jitter['timeup']))
        zagolovok.append(int(js_jitter['timedown']))
        global start_flag1
        start_flag=False
        if start_flag1%2 == 0:
            start_flag=True
        else:
            start_flag=False
        network_number=number
        eps_network_buferss=0



        return render_template('epsbiar_network.html',
        punkt_menu=punkt_menu,lang_bool=lang_bool,conect=conect,
        network_number=network_number,zagolovok=zagolovok,time_otvet=time_otvet,start_flag1=start_flag,string=string , stopped_bufer=stopped_bufer , stopped_msg_mac=stopped_msg_mac )



@app.route('/LIST_EPS', methods=[ 'POST','GET'])
def LIST_EPS():
    """ display all EPS_BIAR"""
    global  time_otvet , lang_switch , conect , global_number_eps , ind_sce_0_iter ,regim_rabota_mode ,indef_froma ,  stopped_msg_mac,stopped_bufer
    global eps_br , bufer_scenar_1  , bufer_network_1 ,error_flag , error_flag_add_eps ,error_flag_add_scenar ,error_flag_add_scenar1 ,LIST_EPS_flagss ,add_eps_buferss , eb_ALL_delete ,stopped_bufer_eps
    indef_froma=3
    error_flag=False
    eb_ALL_delete=0
    #error_flag_add_eps= False
    error_flag_add_scenar=False
    error_flag_add_scenar1=False
    stopped_bufer_eps=False


    #if stopped_msg_mac in 'DPDK: Received a null packet' or  stopped_msg_mac in 'DPDK: Allocation problem' :
        #stopped_bufer= False ## вставить
        #stopped_msg_mac=''

        #pass
#bufer_scenar_1=0
#bufer_network_1=0
    punkt_menu_nach=[[bufer_menu_ALL_form_eng[5][0],bufer_menu_ALL_form_eng[5][1] ,bufer_menu_ALL_form_eng[5][2],bufer_menu_ALL_form_eng[5][3],bufer_menu_ALL_form_eng[5][4]
    ,bufer_menu_ALL_form_eng[5][5],bufer_menu_ALL_form_eng[5][6],bufer_menu_ALL_form_eng[5][7]
    ,bufer_menu_ALL_form_eng[5][8],bufer_menu_ALL_form_eng[5][9],bufer_menu_ALL_form_eng[5][10]
    ,bufer_menu_ALL_form_eng[5][11],bufer_menu_ALL_form_eng[5][12],bufer_menu_ALL_form_eng[5][13]
    ,bufer_menu_ALL_form_eng[5][14],bufer_menu_ALL_form_eng[5][15],bufer_menu_ALL_form_eng[5][16],bufer_menu_ALL_form_eng[0][5],bufer_menu_ALL_form_eng[0][6]]
    ,[bufer_menu_ALL_form_rus[5][0],bufer_menu_ALL_form_rus[5][1] ,bufer_menu_ALL_form_rus[5][2]
    ,bufer_menu_ALL_form_rus[5][3],bufer_menu_ALL_form_rus[5][4]
    ,bufer_menu_ALL_form_rus[5][5],bufer_menu_ALL_form_rus[5][6],bufer_menu_ALL_form_rus[5][7]
    ,bufer_menu_ALL_form_rus[5][8],bufer_menu_ALL_form_rus[5][9],bufer_menu_ALL_form_rus[5][10]
    ,bufer_menu_ALL_form_rus[5][11],bufer_menu_ALL_form_rus[5][12],bufer_menu_ALL_form_rus[5][13],bufer_menu_ALL_form_rus[5][14]
    ,bufer_menu_ALL_form_rus[5][15],bufer_menu_ALL_form_rus[5][16],bufer_menu_ALL_form_rus[0][5],bufer_menu_ALL_form_rus[0][6]]]
    lang_bool=False
    if lang_switch%2== 0:
        punkt_menu=punkt_menu_nach[0]
        lang_bool=True
    else:
        punkt_menu=punkt_menu_nach[1]
        lang_bool=False
    global conect

    if lang_switch%2== 0:
        #punkt_menu=punkt_menu_nach[0]
        #lang_bool=True
        rabota_status=[{'key' : 0 , 'name' : bufer_menu_ALL_form_eng[0][0]},{'key' : 1 , 'name' : bufer_menu_ALL_form_eng[0][1]}]


    else:
        #punkt_menu=punkt_menu_nach[1]
        rabota_status=[{'key': 0 , 'name' : bufer_menu_ALL_form_rus[0][0]},{'key' : 1 , 'name' : bufer_menu_ALL_form_rus[0][1]} ]


    string=''

    for it in rabota_status:
        if it['key'] == regim_rabota_mode :
            string= it['name']
            break
    if lang_switch%2== 0:
        string=' '+string
    else:
        string=' '+string


    if request.method == 'POST' or request.method == 'GET' :
        add_eps_buferss=0
        LIST_EPS_flagss=LIST_EPS_flagss+1
        if conect ==False:
            return redirect(url_for('gra'))
        #if LIST_EPS_flagss==1:
        try:
            ind_sce_0_iter=0
            conect=True
            start=time()*1000
            rr=  req.get(f'http://{udras}/params/eb')
            LIST_EPS_flagss=0
            stop=int(time()*1000-start)
            time_otvet=stop*1
            #GET(/params/eb/1?id=)
            buferr=rr.text
            js = json.loads(buferr)

            print('\n 23js=',js)

            if js['response']['code'] == 0 :
                eps_br=[]
                js2=js['params']['eb']
                global_number_eps=len(js2)
                #print('\n js2=',js2)
                for it in js2:
                    bufer=[]
                    #print(it)
                    bufer.append(it['br'])
                    bufer.append(it['user_scenario'])
                    bufer.append(it['network_scenario'])
                    bufer.append(it['id'])
                    lister=[]
                    lister2=[]

                    if it['user_scenario']['id']!=0 :

                        for it2 in range(len(spisok_scenariev)) :
                            #print('\nit2=',it2)
                            if int(spisok_scenariev[it2][0])   == it['user_scenario']['id']:
                                #print('\n raborasd')
                                #print('\n 23it=',it2)

                                #promeg={'id':int(spisok_scenariev[it2][0])}
                                promeg= deepcopy(spisok_scenariev[it2])
                                #print('\n \n promeg=',id(promeg))
                                lister.append((promeg))
                                #lister= (promeg).copy()
                    else:
                        promeg={'id':it['user_scenario']['id'],'name':it['user_scenario']['name'] ,'pcap_id':it['user_scenario']['pcap_id'] ,'br':it['user_scenario']['br']}
                        bder=1

                        lister=deepcopy(it)

                    bufer.append(lister)

                    if it['network_scenario']['id']!=0 :

                        for it2 in network_list :
                            if  int(it['network_scenario']['id']) == int(it2[3]):
                                promeg=deepcopy(it2)
                                lister2 =deepcopy(promeg)
                                #lister2=promeg
                    else:
                        promeg=deepcopy(it['network_scenario'])
                        lister2 = deepcopy(promeg)
                        #lister2= promeg
                        #pass
                    bufer.append(lister2)

                    eps_br.append(bufer)
            print('eps_br=',eps_br)
            print('spisok_scenariev=',spisok_scenariev)
            min=len(eps_br)
            g=0
            out_pcap_spis=[]
            for it in pcap_cortg:
                #bufer_str=''
                g=g+1
                out_pcap_spis.append({'key':g,'video':it[0],'br_v':it[1],'path':it[2]})

            buferr=[]
            i=0
            summer_velocity2=0

            for it in eps_br:
                summer_velocity2=summer_velocity2+int(it[0])


            summer_velocity=0
            for it in eps_br:
                i=i+1
                print('\n it=',it)
                if int(it[1]['id']) == 0 :
                    buferr_summ=0


                    for iter in spisok_scenariev :
                        if int(iter[0]) == int(it[1]['id']) :

                            for ler in iter[2] :
                                for it34 in out_pcap_spis:
                                    if int(it34['key']) == int(ler) :
                                        buferr_summ=buferr_summ+it34['br_v']
                    if  buferr_summ == it[0] :

                        summer_velocity=summer_velocity+buferr_summ
                        print('\n \n buferr_summ=',buferr_summ)
                        buferr.append({'key':i,'veloc':int(it[0]),'status':it[1]['id'],'status_nt':it[2]['id'],'global_numb':it[3]})

                    else:
                        summer_velocity=summer_velocity+it[0]
                        buferr.append({'key':i,'veloc':int(it[0]),'status':it[1]['id'],'status_nt':it[2]['id'],'global_numb':it[3]})
                else:
                    buferr_summ=0

                    for iter in spisok_scenariev :
                        if int(iter[0]) == int(it[1]['id']) :

                            for ler in iter[2] :
                                for it34 in out_pcap_spis:
                                    if int(it34['key']) == int(ler) :
                                        buferr_summ=buferr_summ+it34['br_v']

                    summer_velocity=summer_velocity+buferr_summ
                    buferr.append({'key':i,'veloc':int(it[0]),'status':it[1]['id'],'status_nt':it[2]['id'],'global_numb':it[3]})



                    #pass

                #buferr.append({'key':i,'veloc':it[0],'status':it[1]['id'],'status_nt':it[2]['id'],'global_numb':it[3]})
            max=200-i
            #print('SCENAR=',spisok_scenariev)
            scenar_lister=[]
            #scenar_lister.append({'name':'Custom','indef':0})
            bufer_network=[]
            #bufer_network.append({'name':'Custom','indef':0})

            g=0
            #print('spisok_scenariev=',spisok_scenariev)
            for i in spisok_scenariev:
                scenar_lister.append({'name':i[1],'indef':g,'indef_ir':i[0]})
                g=g+1

            g=0
            #print('network_list=',network_list)

            for i in network_list:
                bufer_network.append({'name':i[0],'indef':g,'der':i[3]})
                g=g+1

            start_flag=False

            if start_flag1%2 == 0:
                start_flag=True    #bool(5)#"true" #True возможно наборот
            else:
                start_flag=  False #bool(0)#"false" #False
            #print('summer_velocity=',summer_velocity)

            iter_nacha=[1]
            #print('\n do do eps_br=',eps_br)
            #print('\n do do leneps_br=',len(eps_br))
            # for it in eps_br: scenar
            # it[1]['id']

            # for it in eps_br: network
            # it[2]['id']
            print('\n stopped_bufer=',stopped_bufer)


            return  render_template('epb_table.html',iter_nacha=iter_nacha,lang_bool=lang_bool,conect=conect,punkt_menu=punkt_menu,summer_velocity=summer_velocity,
            start_flag=start_flag,buferr=buferr,
            scenar_lister=scenar_lister,bufer_network=bufer_network,time_otvet=time_otvet,string=string , bufer_scenar_1=bufer_scenar_1,bufer_network_1=bufer_network_1,stopped_msg_mac=stopped_msg_mac,stopped_bufer=stopped_bufer,max_dop=max,error_flag_add_eps=error_flag_add_eps,min_eps=min,summer_velocity2=global_velocity)
            pass

        except Exception as ex:
            time_otvet=0
            bufer_network=[]
            summer_velocity=[]
            buferr=[]
            scenar_lister=[]
            conect = False
            start_flag=False
            max=200
            min=0
            summer_velocity2=0

            if start_flag1%2 == 0:
                start_flag=True    #bool(5)#"true" #True возможно наборот
            else:
                start_flag=  False #bool(0)#"false" #False
            return  render_template('epb_table.html',lang_bool=lang_bool
            ,conect=conect,punkt_menu=punkt_menu,summer_velocity=summer_velocity,
            start_flag=start_flag,buferr=buferr,
            scenar_lister=scenar_lister,bufer_network=bufer_network,time_otvet=time_otvet,string=string, bufer_scenar_1=bufer_scenar_1,bufer_network_1=bufer_network_1,stopped_msg_mac=stopped_msg_mac,stopped_bufer=stopped_bufer,max_dop=max,error_flag_add_eps=error_flag_add_eps,min_eps=min,summer_velocity2=global_velocity)

@app.route('/start', methods=[ 'POST'])
def start():
    global conect , allert_msg  , start_flag1 , error_flag , stopped_msg_mac , stopped_bufer ,start_flagss , stopped_bufer_eps
    if request.method == 'POST':
        print('\n start!!!!!!')
        start_flagss=start_flagss+1
        print('\n start_flagss=',start_flagss)

        if len(eps_br) ==0 :
            #error_flag=True
            if lang_switch%2== 0:
                stopped_msg_mac=bufer_menu_ALL_form_eng[0][3]

            else:
                stopped_msg_mac=bufer_menu_ALL_form_rus[0][3]


            stopped_bufer =True
            #stopped_bufer_eps=True

            return redirect(url_for('gra'))


        #if len(stopped_msg_mac) >1:
                #start_flag1=0
                #return  redirect(url_for("gra")) #render_template('2_gra.html')
        #error_flag

        #if start_flagss ==1:

        try:
            """run start/stop  """
            print('\n start23!!!!!!')
            #global
            #global conect
            conect=True
            start_flag=False
            json_out={}
            if start_flag1%2 == 0:
                start_flag=True    #False  #bool(5)#"true" #True возможно наборот
            else:
                start_flag= False# False #bool(0)#"false" #False

            start=time()*1000
            json_out={"state":{"run":start_flag}}






            sesion_1=req.put(f'http://{udras}/state/run',json=json_out)
            #time.sleep(10)
            stopped_bufer=False
            stopped_bufer_eps=False

            stop=int(time()*1000-start)
            time_otvet =stop*1


            js=json.loads(sesion_1.text)
            print('\n !!!js=',js)
            if js['response']['code'] == 0:
                start_flagss=0
                ###stopped_msg_mac=''
                error_flag=False
                allert_msg=''

                start_flag1=start_flag1+1
                if js['state']['run'] == False :
                    start_flag1=0
                if js['state']['run'] == True :
                    start_flag1=1
                #if stopped_msg_mac in 'DPDK: Invalid MAC address of the destination' or stopped_msg_mac in 'DPDK: MAC address of the source is out of the list' or stopped_msg_mac in 'DPDK: Invalid MAC address of the source':
                    #start_flag1=0
                    #print('\n !!!!rab2')

                #error_flag=False

            else:
                stopped_bufer=False



                allert_msg= js['response']['msg']
                print('allert_msg=',allert_msg)

                if str("Request PUT(/state/run) Generator is already ") in str(allert_msg):
                    #start_flag1=1
                    error_flag=False
                else:
                    start_flagss=0
                    start_flag1=0
                    error_flag=True

                #if str("Request PUT(/state/run) Generator is already running") in str(allert_msg):
                    #start_flag1=start_flag1+1
                if js['state']['run'] == False :
                    start_flag1=0
                    error_flag=False
                if js['state']['run'] == True :
                    start_flag1=1
                    error_flag=False



            start_flag=True
            if start_flag1%2 == 0:
                start_flag=True
            else:
                start_flag=False

            print('\n start start_flag=',start_flag)
            print('\n start start_flag1=',start_flag1)


            return  redirect(url_for("gra")) #render_template('2_gra.html')

        except Exception as ex:

            conect=False
            start_flagss=0

            start_flag1=0
            error_flag=True
            allert_msg= js['response']['msg']

            print('\n start=',allert_msg)
            return  redirect(url_for("gra"))
    else:

        return  redirect(url_for("gra"))

@app.route('/stopped2', methods = ['GET','POST'])
def stopped2():

    #conect=False
    #start_flag1=0
    #data2=[("Not"),0]
    #stopped_msg_mac
    #stopped_bufer
    if request.method == 'POST' or request.method == 'GET' :
        print('\n rabbb')
        global stopped_bufer ,  stopped_msg_mac , stopped_bufer_delete , jj , indef_froma
        print('\n stopped_bufer',stopped_bufer)
        print('\n stopped_msg_mac',stopped_msg_mac)

        ######### Убрать
        #stopped_bufer=True
        #stopped_msg_mac='Request PUT(/state/run) Generator is already running'

        ######### Убрать

        if stopped_bufer :
            data2=["God",2]

        #json_data=data
            json_data = json.dumps(data2)
            response = make_response(json_data)
            #jj=jj+1

            #if jj>1 :
            stopped_bufer_delete=False
            #stopped_bufer=True

        #data=["God",2]

        #json_data = json.dumps(global_data)

            response = make_response(json_data)
            print('\n resp=',json_data)
            return response , 400

        else:
            data2=["Not",2]
            stopped_bufer_delete=False



        #json_data=data
            json_data = json.dumps(data2)
            response = make_response(json_data)
        #data=["God",2]

        #json_data = json.dumps(global_data)
            stopped_bufer=False
            stopped_msg_mac=''

            response = make_response(json_data)
            print('\n resp=',json_data)
            return response

    #pass

@app.route('/stopped', methods = ['GET','POST'])
def stopped():
    global conect , allert_msg  , start_flag1 , error_flag , indef_froma ,stopped_msg_mac , stopped_bufer , regim_rabota_mode

    if request.method == 'POST' or request.method == 'GET':
        #if regim_rabota_mode == 0:
        print('eps_biar_graph =', request)
        eps_biar_graph = (request.get_data()).decode('utf-8')
        print('eps_biar_graph =', eps_biar_graph)
        eps_biar_graph=json.loads(eps_biar_graph)
        stopped_msg_mac=eps_biar_graph['stopped']['msg']
        print('stopped_msg_mac =', stopped_msg_mac)




        #start_flag1=1
        start_flag1=0
        #if stopped_msg_mac in 'DPDK: Invalid MAC address of the destination' or stopped_msg_mac in 'DPDK: MAC address of the source is out of the list' or stopped_msg_mac in 'DPDK: Invalid MAC address of the source':
            #start_flag1=1
        #else:
            #start_flag1=0
        #error_flag=True
        #stopped_msg_mac= stopped_msg_mac
        stopped_bufer=True
        #start_flag=False
        #json_out={}
        #if start_flag1%2 == 0:
            #start_flag=True    #False  #bool(5)#"true" #True возможно наборот
        #else:
            #start_flag= False# False #bool(0)#"false" #False
        if indef_froma == 1 :
            print('1')
            return redirect(url_for("gra"))
        if indef_froma == 2 :
            print('2')

            return redirect(url_for("Menu"))
        if indef_froma == 3 :
            print('3')

            return redirect(url_for("LIST_EPS"))
        if indef_froma == 4 :
            print('4')

            return redirect(url_for("scenar_spis"))
        if indef_froma == 5 :
            print('5')

            return redirect(url_for("network_spis"))

        if indef_froma == 6:

            return redirect(url_for("network_spis"))




    #pass

@app.route('/Menu', methods = ['GET','POST'])
def Menu():
    global lang_switch , conect ,rabota_status ,regim_rabota_mode , MAC_SRC ,  MAC_DST ,mac_flag_error  , indef_froma , stopped_msg_mac,stopped_bufer ,MAC_SRC_SORCE ,bufer_menu_change_MAC_SRC,error_flag
    error_flag=False
    #stopped_msg_mac=''
    tert=[]
    if lang_switch%2== 0:
        tert=bufer_menu_ALL_form_eng[0][3]

    else:
        tert=bufer_menu_ALL_form_rus[0][3]
    if stopped_bufer and (tert  in stopped_msg_mac  ):
        stopped_bufer=False






    #stopped_bufer=False

    #bufer_menu_change_MAC_SRC=0

    #MAC_SRC_SORCE.append( {'info': 'wlp5s0', 'mac': 'D0:37:45:76:DD:19'})
    spisk=[]
    #if stopped_msg_mac in 'DPDK: Received a null packet' or  stopped_msg_mac in 'DPDK: Allocation problem' :
        #stopped_bufer= False
        #stopped_msg_mac=''

        #pass


    for iter2 in range(len(MAC_SRC_SORCE)):
        #print('iter2=',iter2)
        spisk.append({'status':int(iter2)})




    #start_flag1=start_flag1+1
    #sesion_1=req.put(f'http://{udras}/state/graph')
    #if conect == False:
        #return redirect(url_for("gra"))


    indef_froma=2

    min=0
    if len(eps_br) == 0:
        min=0
    else:
        for it in eps_br:
            min=min+int(it[0])

    punkt_menu_nach=[[bufer_menu_ALL_form_eng[2][0],bufer_menu_ALL_form_eng[2][1] ,bufer_menu_ALL_form_eng[2][2],bufer_menu_ALL_form_eng[2][3],bufer_menu_ALL_form_eng[2][4],bufer_menu_ALL_form_eng[2][5],bufer_menu_ALL_form_eng[2][6],bufer_menu_ALL_form_eng[2][7],bufer_menu_ALL_form_eng[2][8],bufer_menu_ALL_form_eng[2][9]
    ,bufer_menu_ALL_form_eng[2][10],bufer_menu_ALL_form_eng[2][11],bufer_menu_ALL_form_eng[2][12],bufer_menu_ALL_form_eng[2][13],bufer_menu_ALL_form_eng[2][14]
    ,bufer_menu_ALL_form_eng[2][15],bufer_menu_ALL_form_eng[2][16],bufer_menu_ALL_form_eng[2][17],bufer_menu_ALL_form_eng[0][5],bufer_menu_ALL_form_eng[0][6]]
    ,[bufer_menu_ALL_form_rus[2][0],bufer_menu_ALL_form_rus[2][1] ,bufer_menu_ALL_form_rus[2][2],bufer_menu_ALL_form_rus[2][3],bufer_menu_ALL_form_rus[2][4],bufer_menu_ALL_form_rus[2][5],bufer_menu_ALL_form_rus[2][6],bufer_menu_ALL_form_rus[2][7],bufer_menu_ALL_form_rus[2][8],bufer_menu_ALL_form_rus[2][9],bufer_menu_ALL_form_rus[2][10],bufer_menu_ALL_form_rus[2][11],bufer_menu_ALL_form_rus[2][12],bufer_menu_ALL_form_rus[2][13]
    ,bufer_menu_ALL_form_rus[2][14],bufer_menu_ALL_form_rus[2][15],bufer_menu_ALL_form_rus[2][16],bufer_menu_ALL_form_rus[2][17],bufer_menu_ALL_form_rus[0][5],bufer_menu_ALL_form_rus[0][6]]]

    values=[967.67, 1190.89]
    menu=[]
    znach=0
    if GTP_FLAG:
        znach=1

    zagolovok=[global_velocity,znach,ipsrc,ipdst,minteid,maxteid,global_spis,global_pcath_size,global_number_eps]


    param=False
    lang_bool=False
    #bufer_menu_ALL_form_rus
    #bufer_menu_ALL_form_eng
    if lang_switch%2== 0:
        punkt_menu=punkt_menu_nach[0]
        lang_bool=True
        stringg=(bufer_menu_ALL_form_eng[0][0])
        stringg=stringg.split()
        znach2=''
        g=0
        for it in stringg:
            if g>=2:
                znach2= znach2+ ' '+it
            g=g+1
        stringg=(bufer_menu_ALL_form_eng[0][1])
        stringg=stringg.split()
        znach3=''
        g=0
        for it in stringg:
            if g>=2:
                znach3= znach3+ ' '+it
            g=g+1

        #znach=stringg[]
        rabota_status=[{'key' : 0 , 'name' :znach2},{'key' : 1 , 'name' : znach3}]


    else:
        punkt_menu=punkt_menu_nach[1]

        stringg=bufer_menu_ALL_form_rus[0][0]
        stringg=stringg.split()

        znach2=''
        g=0
        for it in stringg:
            if g>=2:
                znach2= znach2+ ' '+it
            g=g+1
        stringg=bufer_menu_ALL_form_rus[0][1]
        stringg=stringg.split()

        znach3=''
        g=0
        for it in stringg:
            if g>=2:
                znach3= znach3+ ' '+it
            g=g+1

        rabota_status=[{'key': 0 , 'name' : znach2},{'key' : 1 , 'name' :znach3} ]

        lang_bool=False
    #print('\n rabota_status=',punkt_menu)

    start_flag=True
    if start_flag1%2 == 0:
        start_flag=True
    else:
        start_flag=False
    print('spisk=',spisk)
    print('MAC_SRC_SORCE=',MAC_SRC_SORCE)
    print('\n stopped_bufer=',stopped_bufer)

    print('\n stopped_bufer=',stopped_bufer)
    return render_template('form.html',punkt_menu=punkt_menu,conect=conect,
    lang_switch=lang_bool, menu=menu,  set=zip(values, labels), rabota_status=rabota_status, param = param,
    zagolovok=zagolovok, start_flag1=start_flag, regim_rabota_mode=regim_rabota_mode, time_otvet=time_otvet
    , MAC_SRC=MAC_SRC, MAC_DST=MAC_DST
    ,mac_flag_error=mac_flag_error
    , stopped_msg_mac=stopped_msg_mac
    ,stopped_bufer=stopped_bufer
    ,MAC_SRC_SORCE=MAC_SRC_SORCE
    ,spisk=spisk,bufer_menu_change_MAC_SRC=bufer_menu_change_MAC_SRC,min=min)

@app.route('/change_eps', methods=['GET', 'POST'])
def change_eps():
    global eps_br  ,    spisok_scenariev ,  network_list , stopped_msg_mac ,  stopped_bufer , conect , error_flag_add_eps
    if request.method == 'POST' or request.method == 'GET':
        eps_biar_graph = (request.get_data()).decode('utf-8')
        #network = request.form['network']
        #network = bufer_network_1  #request.form['scenar']
        #scenar = bufer_scenar_1  #request.form['scenar']


        #eps_biar_graph=eps_biar_graph.decode('utf-8')
        json_poputka=json.loads(eps_biar_graph)
        js=json_poputka['ip_global'].split(',')
        g=0
        print('\n json=',js)
        scenar_nastraiv=[]
        nastraiv_nastraiv=[]
        for it in js:
            if g%2 ==0 :
                scenar_nastraiv.append(int(it))
            else:
                nastraiv_nastraiv.append(int(it))
            g=g+1
        json_list=[]
        eb=0
        vr_summ=0
        vr_summ2=0
        id_scenar=0
        id_netw=0
        print('\n scenar_nastraiv=',scenar_nastraiv)
        #print('\n nastraiv_nastraiv=',nastraiv_nastraiv)
        #print('\n eps_br=',eps_br)
        print('\n spisok_scenariev=',spisok_scenariev)
        #print('\n network_list=',network_list)
        #print('\n scenar=',scenar)
        kel=0
        g=0
        out_pcap_spis=[]
        for it in pcap_cortg:
            #bufer_str=''
            g=g+1
            out_pcap_spis.append({'key':g,'br_v':it[1]})
            #bufer_str=str(it[0])+', '+str(it[1])+', '+str(it[2])
            #string_pcap.append({'key':g,'string':bufer_str})
        for shag in eps_br :
            #print('\n 23 shag=',shag)
            index_ider=0
            eb=shag[3]




            #vr_summ=shag[0]
            vr_summ=shag[0]
            for iler in spisok_scenariev:
                if int(iler[0]) == scenar_nastraiv[kel] :
                    vr_summ=0
                    for ger in iler[2] :
                        for itt in out_pcap_spis :
                            if int(itt['key']) == int(ger) :
                                vr_summ=vr_summ+itt['br_v']

                        #pass
            print('br_summ=',vr_summ)

            #vr_summ=shag[0]
            index_ider=shag[1]['id']

            flag_1=False
            flag_2=False
            pcap_id=[]
            scenar_izmen=[]
            vr_eb=0


            if scenar_nastraiv[kel] != 0 :
                id_scenar= int(scenar_nastraiv[kel])
            else:
                if 'pcap_id' in shag[1].keys():
                    #print('shag=',shag)

                    pcap_id=shag[1]['pcap_id']
                    for iler in pcap_id:
                        scenar_izmen.append(int(iler))


                    vr_eb=shag[1]['br'] # вставить проверку на минимальную сумму
                    pass
                else:
                    pcap_id=spisok_scenariev[0][2] #shag[1]['id']
                    vr_eb=vr_summ # вставить проверку на минимальную сумму
                    for iler in pcap_id:
                        scenar_izmen.append(int(iler))
                    pass


                flag_1=True

            if nastraiv_nastraiv[kel] != 0 :
                id_netw= int(nastraiv_nastraiv[kel])
            else:
                if 'burst' in shag[2].keys():
                    #print('\n shag=',shag)
                    jitter_timeup= shag[2]['jitter']['timeup']
                    jitter_timedown=shag[2]['jitter']['timedown']
                    jitter_value=shag[2]['jitter']['value']
                    burst_timeup=shag[2]['burst']['timeup']
                    burst_timedown=shag[2]['burst']['timedown']

                    pass
                else:
                    jitter_timeup=network_list[0][1]['timeup']
                    jitter_timedown=network_list[0][1]['timedown']
                    jitter_value=network_list[0][1]['value']
                    burst_timeup=network_list[0][2]['timeup']
                    burst_timedown=network_list[0][2]['timedown']
                    pass
                flag_2=True
            #print('\n \n !!!!!!!!!!!vr_eb=',vr_eb)



            if    flag_1!=   True and   flag_2!=   True:
                vrsem=0

                #for il in out_pcap_spis:
                #    if  int(id_scenar) == int(il['key']) :
                        #vrsem=vrsem+il['br_v']
                #if vr_summ< vrsem and index_ider !=scenar_nastraiv[kel]:
                    #vr_summ=vrsem
                #if index_ider !=scenar_nastraiv[kel] :
                    #vrsem=0
                    #for il in out_pcap_spis:
                        #if  int(id_scenar) == int(il['key']) :
                            #vrsem=vrsem+il['br_v']
                    #vr_summ=vrsem
                #if index_ider !=scenar_nastraiv[kel]:
                    #print('\n \n !!!!!!!!!!!! rab\n')
                vr_summ2=vr_summ2+vr_summ
                tert={
                "id":int(eb),
                "br":int(vr_summ),
                "user_scenario":{
                "id": int(id_scenar)
                }, "network_scenario":{
                "id": int(id_netw)
                }
                }
                json_list.append(tert)
            if    flag_1!=   True and   flag_2==   True:
                vrsem=0

                #for il in out_pcap_spis:
                    #if  int(id_scenar) == int(il['key']) :
                        #vrsem=vrsem+il['br_v']
                #if vr_summ< vrsem :
                    #vr_summ=vrsem

                #if index_ider !=scenar_nastraiv[kel] :
                    #vrsem=0
                    #for il in out_pcap_spis:
                        #if  int(id_scenar) == int(il['key']) :
                            #vrsem=vrsem+il['br_v']
                    #vr_summ=vrsem
                vr_summ2=vr_summ2+vr_summ
                tert={
                "id":int(eb),
                "br":int(vr_summ),
                "user_scenario":{
                "id": int(id_scenar)
                }, "network_scenario":{
                "id": 0,
                "name": "Custom",
                "jitter" :{
                "timeup":jitter_timeup,
                "timedown":jitter_timedown,
                "value":jitter_value
                },
                "burst": {
                "timeup":burst_timeup,
                "timedown":burst_timedown
                }
                }
                }
                json_list.append(tert)

            if    flag_1==   True and   flag_2!=   True:
                vrsem=0

                for il in out_pcap_spis:
                    for it in scenar_izmen:
                        if  it == il['key'] :
                            vrsem=vrsem+il['br_v']
                if vr_summ!= vrsem :
                    vr_summ=vrsem

                #if index_ider !=scenar_nastraiv[kel] :
                    #vrsem=0
                    #for il in out_pcap_spis:
                        #for it in scenar_izmen:
                            #if  it == il['key'] :
                                #vrsem=vrsem+il['br_v']
                    #vr_summ=vrsem

                vr_summ2=vr_summ2+vr_summ
                tert={
                "id":int(eb),
                "br":int(vr_summ),
            "user_scenario":{
            "id": 0,
            "name": 'Custom',
            "br": int(vr_eb),
            "pcap_id":scenar_izmen
             }, "network_scenario":{
                "id": int(id_netw)
                }
                }
                json_list.append(tert)


            if    flag_1==   True and   flag_2==   True:
                vrsem=0

                for il in out_pcap_spis:
                    for it in scenar_izmen:
                        if  it == il['key'] :
                            vrsem=vrsem+il['br_v']
                if vr_summ!= vrsem  :
                    vr_summ=vrsem
                #if index_ider !=scenar_nastraiv[kel] :
                    #vrsem=0
                    #for il in out_pcap_spis:
                        #for it in scenar_izmen:
                            #if  it == il['key'] :
                                #vrsem=vrsem+il['br_v']
                    #vr_summ=vrsem


                vr_summ2=vr_summ2+vr_summ
                tert={
                "id":int(eb),
                "br":int(vr_summ),
                "user_scenario":{
                "id": 0,
                "name": 'Custom',
                "br": int(vr_summ),
                "pcap_id":scenar_izmen
                 }, "network_scenario":{
                "id": 0,
                "name": "Custom",
                "jitter" :{
                "timeup":jitter_timeup,
                "timedown":jitter_timedown,
                "value":jitter_value
                },
                "burst": {
                "timeup":burst_timeup,
                "timedown":burst_timedown
                }
                }
                }
                json_list.append(tert)

            kel=kel+1
                #pass
        #print('\n json_list=',json_list)

        json_out={
        "params":{
        "eb": json_list
        }
        }
        json_out2=json.dumps(json_out)
        print('\n \n \n !!!!!!!!!!!!json_out=',json_out)

        print('\n vr_summ2=',vr_summ2)
        print('\n global_velocity=',global_velocity)

        if  int(global_velocity)<vr_summ2 :
            error_flag_add_eps=True

            return redirect(url_for('LIST_EPS'))


        try:
            #
            stopped_msg_mac=''
            stopped_bufer=False
            conect=True
            error_flag_add_eps=False
            rr=  req.put(f'http://{udras}/params/eb',json=(json_out))

            js = json.loads(rr.text)
            #print('\n \n \n !!!!!!!!!!!!True True=',js)

            if js['response']['code'] == 0 :
                return redirect(url_for('LIST_EPS'))
            else:
                return redirect(url_for('LIST_EPS'))
        except Exception as ex:
            conect=False

            return redirect(url_for('LIST_EPS'))


        #print('\n number=',number)
        #pass



        #print('\n number=',number)
        #pass


@app.route('/scenar/add', methods=['GET', 'POST'])
def scenar_add():
    """ add new scenario  """
    if request.method == 'POST' or request.method == 'GET':
        global spisok_scenariev , stopped_bufer , stopped_msg_mac ,scenar_add , stopped_bufer_delete
        scenar_add=scenar_add+1
        #print('\n spisok_scenariev=',spisok_scenariev)
        max=0
        for it in spisok_scenariev :
            if it[0]> max:
                max=it[0]
        max=max+1

        #new_id=len(spisok_scenariev)+1
        name =request.form['name']
        #name =request.form.getlist['name']
        scenar= request.form.getlist('scenar')

        print('\n scenar=',scenar)
        print('\n name=',name)
        print('\n spisok_scenariev=',spisok_scenariev)
        int_sceanar=[]
        for i in  scenar:
            int_sceanar.append(int(i))

        vr_summ=0
        scenar_izmen=[]
        g=0
        print('spisok_scenariev=',pcap_cortg)

        #for iter in spisok_scenariev :
        for iter in spisok_scenariev :
            if int(iter[0]) == int(int_sceanar[0]):
                for lit in iter[2]:

                    scenar_izmen.append((lit))




        #for i in spisok_scenariev[int_sceanar[0]-1][2]:
            #scenar_izmen.append(int(i))

        print(scenar_izmen)


        for i in scenar_izmen:

            vr_summ=vr_summ+int(pcap_cortg[i-1][1])

        json_out={
        "params":{
        "user_scenario":[{
        "id": max,
        "name":name,
        "br": int(vr_summ),
        "pcap_id":scenar_izmen
        }]
        }
        }
        #if scenar_add==1:
        try :
            stopped_bufer=False
            stopped_msg_mac=''
            stopped_bufer_delete=False
            print('do do \n json_out=',json_out)
            rr=req.post(f'http://{udras}/params/user_scenario',json=(json_out))
            js = json.loads(rr.text)
            scenar_add=0

            if js['response']['code'] == 0 :
                return redirect(url_for('scenar_spis'))
            else:
                return redirect(url_for('scenar_spis'))
        except Exception as ex:
            scenar_add=0
            return  render_template('first.html')

        #print('scenar',spisok_scenariev[int_sceanar[0]-1])
        #pass
    #pass
@app.route('/scenar', methods=['GET', 'POST'])
def scenar_spis():
    """ value scripting"""
    global lang_switch , conect ,custom_bufer ,regim_rabota_mode , indef_froma ,stopped_msg_mac , stopped_bufer ,error_flag ,  error_flag_add_scenar , stopped_bufer_delete
    indef_froma=4
    error_flag=False
    error_flag_add_scenar=False
    #stopped_bufer_delete=False


    punkt_menu=[]
    #print(',\n bufer_menu_ALL_form_rus[3][9]=',bufer_menu_ALL_form_eng[3] )
    #print('\n bufer_menu_ALL_form_eng[3][9]=', bufer_menu_ALL_form_eng[3][9])

    punkt_menu_nach=[[bufer_menu_ALL_form_eng[3][0],bufer_menu_ALL_form_eng[3][1] ,bufer_menu_ALL_form_eng[3][2],bufer_menu_ALL_form_eng[3][3],bufer_menu_ALL_form_eng[3][4]
    ,bufer_menu_ALL_form_eng[3][5],bufer_menu_ALL_form_eng[3][6],bufer_menu_ALL_form_eng[3][7],bufer_menu_ALL_form_eng[3][8],bufer_menu_ALL_form_eng[3][9],bufer_menu_ALL_form_eng[0][5],bufer_menu_ALL_form_eng[0][6]]
    ,[bufer_menu_ALL_form_rus[3][0],bufer_menu_ALL_form_rus[3][1] ,bufer_menu_ALL_form_rus[3][2],bufer_menu_ALL_form_rus[3][3],bufer_menu_ALL_form_rus[3][4],bufer_menu_ALL_form_rus[3][5],bufer_menu_ALL_form_rus[3][6]
    ,bufer_menu_ALL_form_rus[3][7],bufer_menu_ALL_form_rus[3][8],bufer_menu_ALL_form_rus[3][9],bufer_menu_ALL_form_rus[0][5],bufer_menu_ALL_form_rus[0][6]]]

    lang_bool=False
    if lang_switch%2== 0:
        punkt_menu=punkt_menu_nach[0]
        lang_bool=True
    else:
        punkt_menu=punkt_menu_nach[1]
        lang_bool=False
    global conect


    if lang_switch%2== 0:
        #punkt_menu=punkt_menu_nach[0]
        #lang_bool=True
        rabota_status=[{'key' : 0 , 'name' : bufer_menu_ALL_form_eng[0][0]},{'key' : 1 , 'name' : bufer_menu_ALL_form_eng[0][1]}]


    else:
        #punkt_menu=punkt_menu_nach[1]
        rabota_status=[{'key': 0 , 'name' : bufer_menu_ALL_form_rus[0][0]},{'key' : 1 , 'name' : bufer_menu_ALL_form_rus[0][1]} ]


    string=''

    for it in rabota_status:
        if it['key'] == regim_rabota_mode :
            string= it['name']
            break

    if lang_switch%2== 0:
        string=' '+string
    else:
        string=' '+string

    if request.method == 'POST' or request.method == 'GET':
        if conect ==False:
            return redirect(url_for('gra'))
        tert=[]
        if lang_switch%2== 0:
            tert=bufer_menu_ALL_form_eng[0][3]

        else:
            tert=bufer_menu_ALL_form_rus[0][3]
        if stopped_bufer and (tert  in stopped_msg_mac  ):
            stopped_bufer=False

        #if stopped_bufer ==True:
            #return redirect(url_for('gra'))

        try:
            global spisok_scenariev , time_otvet ,custom

            spisok_outt=[]
            #spisok_scenariev=[]

            #spisok_outt.append([0,'Custom'])
            start= time()*1000

            rr=req.get(f'http://{udras}/params/user_scenario')

            stop=int(time()*1000-start)

            time_otvet =stop
            bufer=rr.text
            json_poputka=json.loads(bufer)
            nachalo=[]
            bufer=[]
            bufer2=[]
            print('json=',json_poputka)
            #print('spisok_scenariev=',spisok_scenariev)


            if json_poputka['response']['code'] == 0 :
                g=0
                if json_poputka['params']['user_scenario'] !=[]:
                    spisok_scenariev=[]
                    if  len(spisok_scenariev)>1:
                        nachalo=spisok_scenariev[0]
                        bufer2.append(nachalo[0])
                        bufer2.append(nachalo[1])


                    else:
                        #bufer=[]
                        bufer.append(0)
                        bufer.append('Custom')
                        bufer2.append(0)
                        bufer2.append('Custom')
                        if len(custom_bufer) == 0:

                            bufe_pcap=[]
                            for i in json_poputka['params']['user_scenario'][0]['pcap_id']:
                                bufe_pcap.append(i)
                            bufer.append(bufe_pcap)
                        else:
                            bufe_pcap=[]

                            bufer.append(custom_bufer)

                        nachalo=bufer
                        spisok_scenariev=[]
                        #print('\n \n 2nachalo=',nachalo)
                        spisok_scenariev.append(nachalo)
                else:
                    nachalo=spisok_scenariev[0]

                    #print('rabotaet=',nachalo)
                    bufer2.append(nachalo[0])
                    bufer2.append(nachalo[1])

                #print('\n \n spisok_outt=',spisok_outt)
                #print('\n \n spisok_scenariev=',spisok_scenariev)

                spisok_outt.append(bufer2)
                if json_poputka['params']['user_scenario'] !=[]:
                    for it in json_poputka['params']['user_scenario']:


                        bufer=[]

                        bufer2=[]
                        bufer2.append(it['id'])
                        bufer2.append(it['name'])
                        spisok_outt.append(bufer2)

                        bufer.append(it['id'])
                        bufer.append(it['name'])
                        #spisok_outt.append(bufer)
                        bufe_pcap=[]
                        for i in it['pcap_id']:
                            bufe_pcap.append(i)
                        bufer.append(bufe_pcap)

                        spisok_scenariev.append(bufer)
                global start_flag1
                print('spos=',spisok_scenariev)
                start_flag=False
                if start_flag1%2 == 0:
                    start_flag=True
                else:
                    start_flag=False
                iter_nacha=[1]
                print('\n  \n stopd=',stopped_msg_mac)
                print('\n \n stopped_bufer=',stopped_bufer)
                print('\n \n stopped_bufer_delete=',stopped_bufer_delete)


                return  render_template('table_scenari.html',punkt_menu=punkt_menu,conect=conect,lang_switch=lang_bool,
                iter_nacha=iter_nacha,spisok_outt=spisok_outt,time_otvet=time_otvet,start_flag1=start_flag,string=string ,stopped_msg_mac= stopped_msg_mac, stopped_bufer=stopped_bufer,stopped_bufer_delete=stopped_bufer_delete) #redirect(f"/eps/{global_number_eps}")

            else:
                return redirect(url_for('gra'))


        except Exception as ex:
            iter_nacha=[]
            spisok_outt=[]
            time_otvet=0
            start_flag=False
            conect=False
            if start_flag1%2 == 0:
                start_flag=True
            else:
                start_flag=False
            return render_template('table_scenari.html',punkt_menu = punkt_menu , conect = conect , lang_switch = lang_bool ,
            iter_nacha = iter_nacha , spisok_outt = spisok_outt , time_otvet = time_otvet , start_flag1 = start_flag,string=string,stopped_msg_mac= stopped_msg_mac, stopped_bufer=stopped_bufer,stopped_bufer_delete=stopped_bufer_delete) #redirect(f"/eps/{global_number_eps}")



@app.route('/scenar_network', methods=['GET', 'POST'])
def network_spis():
    """ scenar network """
    global network_list , time_otvet , lang_switch , conect ,regim_rabota_mode,indef_froma ,stopped_msg_mac , stopped_bufer ,error_flag , stopped_bufer_delete
    indef_froma=5
    error_flag=False
    #if stopped_msg_mac in 'DPDK: Received a null packet' or  stopped_msg_mac in 'DPDK: Allocation problem' :
        #stopped_bufer= False
        #stopped_msg_mac=''

        #pass

    punkt_menu = []

    punkt_menu_nach=[[bufer_menu_ALL_form_eng[7][0],bufer_menu_ALL_form_eng[7][1] ,bufer_menu_ALL_form_eng[7][2],bufer_menu_ALL_form_eng[7][3],bufer_menu_ALL_form_eng[7][4]
    ,bufer_menu_ALL_form_eng[7][5],bufer_menu_ALL_form_eng[7][6],bufer_menu_ALL_form_eng[7][7],bufer_menu_ALL_form_eng[7][8],bufer_menu_ALL_form_eng[7][9],bufer_menu_ALL_form_eng[0][5],bufer_menu_ALL_form_eng[0][6]],
    [bufer_menu_ALL_form_rus[7][0],bufer_menu_ALL_form_rus[7][1] ,bufer_menu_ALL_form_rus[7][2],bufer_menu_ALL_form_rus[7][3],bufer_menu_ALL_form_rus[7][4],bufer_menu_ALL_form_rus[7][5],bufer_menu_ALL_form_rus[7][6]
    ,bufer_menu_ALL_form_rus[7][7],bufer_menu_ALL_form_rus[7][8],bufer_menu_ALL_form_rus[7][9],bufer_menu_ALL_form_rus[0][5],bufer_menu_ALL_form_rus[0][6]]]

    lang_bool=False
    if lang_switch%2== 0:
        punkt_menu = punkt_menu_nach[0]
        lang_bool = True
    else:
        punkt_menu = punkt_menu_nach[1]
        lang_bool = False
    global conect

    if lang_switch%2== 0:
        #punkt_menu=punkt_menu_nach[0]
        #lang_bool=True
        rabota_status=[{'key' : 0 , 'name' : bufer_menu_ALL_form_eng[0][0]},{'key' : 1 , 'name' : bufer_menu_ALL_form_eng[0][1]}]


    else:
        #punkt_menu=punkt_menu_nach[1]
        rabota_status=[{'key': 0 , 'name' : bufer_menu_ALL_form_rus[0][0]},{'key' : 1 , 'name' : bufer_menu_ALL_form_rus[0][1]} ]


    string=''

    for it in rabota_status:
        if it['key'] == regim_rabota_mode :
            string= it['name']
            break

    if lang_switch%2== 0:
        string=' '+string
    else:
        string=' '+string

    if request.method == 'POST' or request.method == 'GET':
        #if conect ==False:
            #return redirect(url_for('gra'))

        tert=[]
        if lang_switch%2== 0:
            tert=bufer_menu_ALL_form_eng[0][3]

        else:
            tert=bufer_menu_ALL_form_rus[0][3]
        if stopped_bufer and (tert  in stopped_msg_mac  ):
            stopped_bufer=False

        #if stopped_bufer ==True:
            #return redirect(url_for('gra'))

        global start_flag1
        spisok_outt=[]
        eps_spis=[]
        time_otvet=0


        #global spisok_scenariev



        #spisok_outt.append([0,'Настраиваемый'])
        try:

            start= time()

            rr=req.get(f'http://{udras}/params/network_scenario')
            stop=int(time()*1000-start*1000)
            time_otvet =stop
            bufer=rr.text
            json_poputka=json.loads(bufer)
            print('\n network_scenario json_poputka=',json_poputka)
            #bufer.append(it['name'])
            #bufer.append(it['jitter'])
            #bufer.append(it['burst'])
            nachalo=[]
            bufer=[]
            bufer2=[]
            #print('jsony=',json_poputka['params']['network_scenario'])


            if json_poputka['response']['code'] == 0 :
                g=0
                nachalo=[]
                bufe_pcap=[]
                if json_poputka['params']['network_scenario'] !=  []:
                    #print('\n \n !!!!!!!!!!!')
                    if len(network_list)>1  :
                        #print('\n \n posle')
                        nachalo=network_list[0]
                    else:
                        bufe_pcap.append('Custom')
                        bufe_pcap.append(json_poputka['params']['network_scenario'][0]['jitter'])
                        bufe_pcap.append(json_poputka['params']['network_scenario'][0]['burst'])
                        bufe_pcap.append(json_poputka['params']['network_scenario'][0]['id'])
                        nachalo=bufe_pcap
                    network_list=[]
                    network_list.append(nachalo)

                #else:
                    #for itel in network_list:
                        #if
                        #if isinstance(itelбб )
                    #if len(network_list)>1:
                        #ber=network_list[0]
                        #network_list=[]
                        #network_list=ber
                    #pass
                    #pass
                #print('do network_list=',network_list)
                #print('do json_poputka=',json_poputka['params']['network_scenario'])

                #print('posle network_list=',network_list)
                spisok_outt.append([0,'Custom'])
                #network_list.append(bufe_pcap)
                if json_poputka['params']['network_scenario']!=[]:
                    for it in json_poputka['params']['network_scenario']:
                        bufer=[]
                        bufer2=[]
                        bufer3=[]
                        bufer2.append(it['id'])
                        bufer2.append(it['name'])
                        bufer3.append(it['name'])
                        bufer3.append(it['jitter'])
                        bufer3.append(it['burst'])
                        bufer3.append(it['id'])
                        spisok_outt.append(bufer2)
                        network_list.append(bufer3)



            eps_spis=[]

            #global start_flag1
            start_flag=False
            if start_flag1%2 == 0:
                start_flag = True
            else:
                start_flag = False
            iter_nacha = [1]

            return  render_template('table_network.html',punkt_menu = punkt_menu , conect = conect , lang_bool = lang_bool ,
            iter_nacha = iter_nacha , spisok_outt = spisok_outt , eps_spis = eps_spis ,
            time_otvet = time_otvet , start_flag1 = start_flag,string=string,stopped_msg_mac= stopped_msg_mac, stopped_bufer=stopped_bufer,stopped_bufer_delete=stopped_bufer_delete) #redirect(f"/eps/{global_number_eps}")

        except Exception as ex:
            conect=False
            iter_nacha=[1]
            start_flag=False

            return  render_template('table_network.html',punkt_menu = punkt_menu , conect = conect , lang_bool = lang_bool ,
            iter_nacha = iter_nacha , spisok_outt = spisok_outt , eps_spis = eps_spis ,
            time_otvet = time_otvet , start_flag1 = start_flag ,string=string,stopped_msg_mac= stopped_msg_mac, stopped_bufer=stopped_bufer,stopped_bufer_delete=stopped_bufer_delete) #redirect(f"/eps/{global_number_eps}")

@app.route('/grafik', methods=[ 'POST'])
def grafik():
    if request.method == 'POST' :
        global data2_global , data_grafik1 , data_grafik2 , data_flagss #=0
        data_flagss=0

        bufer1=[]
        bufer2=[]

        data_grafik1=request.form.getlist('comp_select')

        for it in  data_grafik1:
            bufer1.append(int(it))
        data_grafik1=bufer1

        data_grafik2=request.form.getlist('data2')
        #print('\n \n !!!!!!!!!!!!!!=',data_grafik2)
        for it in  data_grafik2:
            bufer2.append(int(it))
        data_grafik2=bufer2
        return  redirect(url_for("gra"))


@app.route('/registr', methods=[ 'POST'])
def registr():
    return redirect(url_for("nachal"))

@app.route('/gra', methods=[ 'GET'])
def gra():
    """Main form  """

    global  global_number_eps , lang_switch ,conect , port_adres , data2_global , allert_flag , allert_msg , error_flag , bufer_network2 ,regim_rabota_mode ,indef_froma , stopped_msg_mac,stopped_bufer, start_flag1 , error_flag_add_eps ,error_flag_add_scenar,mac_flag_error,LIST_EPS_flagss , scenar_add , stopped_bufer_delete , stopped_bufer_eps#=True
    #print('\n 23stopped_msg_mac=',stopped_msg_mac)
    error_flag_add_eps=False
    error_flag_add_scenar=False
    stopped_bufer_delete=False
    mac_flag_error=False
    LIST_EPS_flagss=0
    scenar_add=0


    #if len(stopped_msg_mac)>1 and stopped_bufer== True:
        #start_flag1=0


    indef_froma=1

    bufer = 0
    select_eps = 0
    select_value = 0
    obozn=[]
    if lang_switch%2== 0:
        obozn=bufer_menu_ALL_form_eng[0][3]

    else:
        obozn=bufer_menu_ALL_form_rus[0][3]

    if stopped_bufer and (tert  in stopped_msg_mac  ):
        stopped_bufer=False

    punkt_menu_nach=[[bufer_menu_ALL_form_eng[1][0],bufer_menu_ALL_form_eng[1][1] ,bufer_menu_ALL_form_eng[1][2],bufer_menu_ALL_form_eng[1][3],bufer_menu_ALL_form_eng[1][4],bufer_menu_ALL_form_eng[1][5],bufer_menu_ALL_form_eng[1][6],bufer_menu_ALL_form_eng[1][7],str(bufer_menu_ALL_form_eng[1][8]),bufer_menu_ALL_form_eng[1][9],bufer_menu_ALL_form_eng[1][10],bufer_menu_ALL_form_eng[1][11],bufer_menu_ALL_form_eng[1][12]
    ,bufer_menu_ALL_form_eng[1][13],bufer_menu_ALL_form_eng[0][5],bufer_menu_ALL_form_eng[0][6],bufer_menu_ALL_form_eng[0][7]],
    [bufer_menu_ALL_form_rus[1][0],bufer_menu_ALL_form_rus[1][1], bufer_menu_ALL_form_rus[1][2],bufer_menu_ALL_form_rus[1][3],bufer_menu_ALL_form_rus[1][4],bufer_menu_ALL_form_rus[1][5],bufer_menu_ALL_form_rus[1][6],bufer_menu_ALL_form_rus[1][7],str(bufer_menu_ALL_form_rus[1][8]),bufer_menu_ALL_form_rus[1][9],bufer_menu_ALL_form_rus[1][10],bufer_menu_ALL_form_rus[1][11],bufer_menu_ALL_form_rus[1][12]
    ,bufer_menu_ALL_form_rus[1][13],bufer_menu_ALL_form_rus[0][5],bufer_menu_ALL_form_rus[0][6],bufer_menu_ALL_form_rus[0][7]]]
    data=[]
    global_number_eps_1=global_number_eps+1
    rabota_status=0


    perv=True
    if data_grafik2[0] %2 == 0:
        perv=True
    else:
        perv=False




    #data=[{'name':0}, {'name':1}, {'name':2}]
    start_flag=True
    if start_flag1%2 == 0:
        start_flag=True
    else:
        start_flag=False

    lang_bool=False
    if lang_switch%2== 0:
        punkt_menu=punkt_menu_nach[0]
        lang_bool=True

    else:
        punkt_menu=punkt_menu_nach[1]
        lang_bool=False

    data.append({ 'name' : 0 , 'name2' : punkt_menu[10] })

    g=0
    for it in ((eps_br)) :
        #if it == 0:
            #data.append({'name':it,'name2':'ALL'})
        #else:
        g=g+1
        data.append({ 'name': it[3] , 'name2' : g })

    bufer_network2=[ {'name' : punkt_menu[8] , 'der' : 0 } , { 'name' : punkt_menu[9] , 'der' : 1 }]
    #port_adres={'addr':'192.168.0.163','port':'5000'}
    adr=port_adres['addr']
    adr_port=port_adres['port']
    url_output=f'http://{adr}:{adr_port}'

    #param=False
    #lang_bool=False
    #bufer_menu_ALL_form_rus
    #bufer_menu_ALL_form_eng
    if lang_switch%2== 0:
        #punkt_menu=punkt_menu_nach[0]
        #lang_bool=True
        rabota_status=[{'key' : 0 , 'name' : bufer_menu_ALL_form_eng[0][0]},{'key' : 1 , 'name' : bufer_menu_ALL_form_eng[0][1]}]


    else:
        #punkt_menu=punkt_menu_nach[1]
        rabota_status=[{'key': 0 , 'name' : bufer_menu_ALL_form_rus[0][0]},{'key' : 1 , 'name' : bufer_menu_ALL_form_rus[0][1]} ]


    string=''
    i_regim=0


    for it in rabota_status:
        #print('key=',it['key'])
        if it['key'] == regim_rabota_mode :
            i_regim=it['key']
            if i_regim == 1:
                bufer_network2=[ {'name' : punkt_menu[13] , 'der' : 0 } , { 'name' : punkt_menu[9] , 'der' : 1 }]

            string= it['name']
            break

    if lang_switch%2== 0:
        string=' '+string
    else:
        string=' '+string


    if conect :
        global GTP_FLAG , global_spis , ipsrc , ipdst , minteid , maxteid , global_pcath_size  , global_velocity
        try:

            #data={'addr':'192.168.0.163','port':'5000'}
            #start=time.clock()
            buferr=[]
            start = (time()*1000)


            #rr=req.get(f'http://{udras}/init',params=(port_adres))
            stop=int(time()*1000 -start)
            rr=req.get(f'http://{udras}/alive')
            conect=True
            buferr=rr.text
            #print('start_flag1=',start_flag1)
            #print('error_flag=',error_flag)
            #print('\n \n \n !!!! stopped_msg_mac=',stopped_msg_mac)
            #print('\n \n \n !!!! stopped_bufer=',stopped_bufer)
            if stopped_bufer  and len(stopped_msg_mac)>1 :
                error_flag=False
                start_flag1=0
                start_flag=True
                if start_flag1%2 == 0:
                    start_flag=True
                else:
                    start_flag=False
            #if stopped_msg_mac in 'DPDK: Invalid MAC address of the destination' or stopped_msg_mac in 'DPDK: MAC address of the source is out of the list' or stopped_msg_mac in 'DPDK: Invalid MAC address of the source':
                #start_flag1=1
                #start_flag1=0
            if stopped_bufer and (stopped_msg_mac in 'DPDK: Invalid MAC address of the destination' or stopped_msg_mac in 'DPDK: MAC address of the source is out of the list' or stopped_msg_mac in 'DPDK: Invalid MAC address of the source'):
                start_flag1=0
                error_flag=False
                #print('\n !!!!rab1')
                start_flag=True
                if start_flag1%2 == 0:
                    start_flag=True
                else:
                    start_flag=False
            #if error_flag == True:
                #stopped_bufer=False
            #print('\n stopped_bufer=',stopped_bufer)

            #start_flag1=0
            #error_flag=True
            start_flag=True
            if start_flag1%2 == 0:
                start_flag=True
            else:
                start_flag=False
            print('\n \n start_flag=', start_flag)
            print('\n \n start_flag1=', start_flag1)
            print('\n \n stopped_bufer_eps=', stopped_bufer_eps)
            print('\n \n stopped_msg_mac=', stopped_msg_mac)
            print('\n \n error_flag=', error_flag)


        #stopped_msg_mac= stopped_msg_mac
        #stopped_bufer=True
            return render_template('2_gra.html',bufer_network2=bufer_network2,
            data_grafik1 = data_grafik1 , data_grafik2 = data_grafik2 , perv=perv,
            url_output = url_output,conect = conect , lang_bool= lang_bool , punkt_menu = punkt_menu ,
            start_flag = start_flag , data = data , epdb=epdb,time_otvet= time_otvet ,
            lang_switch = lang_switch , allert_flag=error_flag , allert_msg=allert_msg , string=string ,stopped_msg_mac=stopped_msg_mac,stopped_bufer=stopped_bufer,i_regim=i_regim,stopped_bufer_eps=stopped_bufer_eps,obozn=obozn)

        except Exception as ex:
            conect=False

            return render_template('2_gra.html', bufer_network2 = bufer_network2 , data_grafik1 = data_grafik1 , data_grafik2 = data_grafik2 ,
            perv = perv , url_output = url_output , conect = conect ,lang_bool = lang_bool,
            punkt_menu = punkt_menu , start_flag = start_flag , data = data , epdb = epdb , time_otvet= time_otvet , lang_switch= lang_switch , allert_flag = error_flag ,
            allert_msg = allert_msg ,  string=string ,stopped_msg_mac=stopped_msg_mac,stopped_bufer=stopped_bufer,i_regim=i_regim,stopped_bufer_eps=stopped_bufer_eps,obozn=obozn)
    else  :
        conect=False
        return render_template('2_gra.html',bufer_network2 = bufer_network2 , data_grafik1 = data_grafik1 , data_grafik2 = data_grafik2 ,
        perv = perv , url_output = url_output , conect = conect , lang_bool = lang_bool , punkt_menu = punkt_menu , start_flag = start_flag , data = data ,
        epdb = epdb ,time_otvet = time_otvet , lang_switch = lang_switch , allert_flag = error_flag , allert_msg = allert_msg , string=string,stopped_msg_mac=stopped_msg_mac,stopped_bufer=stopped_bufer,i_regim=i_regim,stopped_bufer_eps=stopped_bufer_eps,obozn=obozn)


@app.route('/data/<int:number>', methods=["GET", "POST"])

def data(number):
    if request.method == 'POST' or request.method == 'GET':
        global time_otvet , conect,start_flag1 , global_data ,data_flagss ,conect
        start_flag=False
        #json_out={}
        data_flagss=data_flagss+1
        if start_flag1%2 == 0:
            start_flag=True    #False  #bool(5)#"true" #True возможно наборот
        else:
            start_flag= False# False #bool(0)#"false" #False
        #if data_flagss==1:
        #print('data_flagss=',data_flagss)

        try:


            rr=  req.get(f'http://{udras}/alive')
            conect=True
            if conect or start_flag :
                #if data_flagss==1:

                if number == 0 :
                        print('\n rabb')
                        print('\n \n  /data/0')



                        try:
                            #rr=req.put(f'http://{udras}/params/eb',json=(json_out))

                            start = time()*1000

                            rr =  req.get(f'http://{udras}/stats/eb')
                            js = json.loads(rr.text)
                            data_flagss=0
                            #print('\n \n!!!234 js=',js)
                            stop = int(time()*1000-start)
                            time_otvet = stop

                            eps_biar_graph = rr.text #.decode('utf-8')
                            data_flagss=0



                            json_poputka = json.loads(eps_biar_graph)

                            if js['response']['code'] == 0 :
                                print('\n 4js=',js)



                                timer = str(datetime.fromisoformat(json_poputka['stats']['time'])) #random.randint(100,200000)
                                data=[timer,int(json_poputka['stats']['size']),int(json_poputka['stats']['vpercent']),(time_otvet)]
                                global_data=data
                                #data={'time':timer,'value':int(json_poputka['stats']['size'])}
                                json_data = json.dumps(data)

                                response = make_response(json_data)

                                response.content_type = 'application/json'

                                return response
                        except Exception as ex:
                            print('\n /data/0=',repr(ex))
                            fe=repr(ex)
                            data_flagss=0



                            if 'Internal Server Error' in fe:
                                #json_data="God"
                                response = make_response(json_data)
                                #data=["God",2]

                                json_data = json.dumps(global_data)

                                response = make_response(json_data)

                                response.content_type = 'application/json'
                                return response




                            #conect = False
                            return  render_template('first.html')
                                #else:


                else:

                    try:
                        print('\n \n  /data/23')

                        start = time()*1000
                        rr = req.get(f'http://{udras}/stats/eb/{number}')

                        js = json.loads(rr.text)
                        data_flagss=0
                        stop = int(time()*1000-start)
                        time_otvet = stop*1

                        eps_biar_graph = rr.text #.decode('utf-8')
                        data_flagss=0



                        json_poputka=json.loads(eps_biar_graph)

                        if js['response']['code'] == 0 :
                            #data_flagss=0


                            timer= str(datetime.fromisoformat(json_poputka['stats']['time'])) #random.randint(100,200000)
                            data=[timer,int(json_poputka['stats']['size']),int(json_poputka['stats']['vpercent']),(time_otvet)]
                            global_data=data
                            json_data = json.dumps(data)

                            response = make_response(json_data)

                            response.content_type = 'application/json'

                            return response
                    except Exception as ex:
                        #conect = False

                        print('\n /data/number=',str(ex))
                        fe=str(ex)
                        data_flagss=0


                        if 'Internal Server Error' in fe:
                            #json_data="God"
                            response = make_response(json_data)
                            #data=["God",2]

                            json_data = json.dumps(global_data)

                            response = make_response(json_data)

                            response.content_type = 'application/json'
                            return response

                        return  render_template('first.html')
        except Exception as ex:
                print('\n dert ConnectionError')

                conect=False
                start_flag1=0
                data2=[("Not"),0]
                #json_data=data
                json_data = json.dumps(data2)
                response = make_response(json_data)
                #data=["God",2]

                #json_data = json.dumps(global_data)

                response = make_response(json_data)
                print('\n resp=',json_data)
                return response , 400


        #print('\n rr=',rr.text)







@app.route('/verify', methods = ['POST', 'GET'])
def verify():
    """ processing incoming values"""
    if request.method == 'POST' or request.method == 'GET':

        return redirect(f"/gra")


if __name__ == "__main__":

    bufer=[]
    bufer_menu_ALL_form_rus , bufer_menu_ALL_form_eng

    with open('menu_eng_v2.txt', encoding='utf-8') as itr :
        for line in itr:
            tert=line.split('#')
            tert=tert[0]
            bufer_menu_ALL_form_eng.append(tert.split(','))
    bufer=[]
    with open('menu_rus_v2.txt', encoding='utf-8') as itr :
        for line in itr:
            tert=line.split('#')
            tert=tert[0]
            shert=[]
            bufer_menu_ALL_form_rus.append(tert.split(','))
    #export FLASK_ENV=development
    #from waitress import serve
    #from waitress import serve
    #serve(app, host="0.0.0.0", port=3050)
    #os.environ["WERKZEUG_RUN_MAIN"] = "true"

    app.run('0.0.0.0',debug=False,threaded=False, processes=1)
        #adr=port_adres['addr']
        #adr_port=port_adres['port']
    #app.run(port_adres['addr'],port=port_adres['port'])
