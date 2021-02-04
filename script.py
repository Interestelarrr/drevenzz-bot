import config
import amino
import random
import threading
import urllib.request
import urllib.parse
import json
import requests
import re
import time
import os
import subprocess
from gtts import gTTS
from io import BytesIO
from flask import Flask
from amino import socket
from threading import Thread
from getpass import getpass
from pprint import pprint
client = amino.Client()


app=Flask("")

@app.route("/")
def index():
    return "<h1>Bot is running</h1>"

Thread(target=app.run,args=("0.0.0.0",8080)).start()


print("""
     ("`-/")_.-'"``-._
      . . `; -._    )-;-,_`)
     (v_,)'  _  )`-.\  ``-'
    _.- _..-_/ / ((.'
  ((,.-'   ((,/   
""")


def mensajeLogin():
   client.login("drevenzzea@gmail.com","andromedala")
   socketloop = threading.Thread(target = reconsocketloop)
   socketloop.daemon = True
   socketloop.start()
   

#Puedes cambiar el getpass por input, pero getpass es mas seguro! 


os.system ("clear")


print("""
      ,/|         _.--''^``-...___.._.,;
     /, \'.     _!'          ,--,,,--'''
    { \    `_!''       '    /})
     `;;'            ;   ; ;
 ._.--''     ._,,, _..'  .;.'
  (,_....----'''     (,..--''
       
""")



#Vol. Help

HELP = """    🏁  ゛ㅤ  𔒌̤ㅤ㍖꯭㍈꯭㌲  ⏎ 

!abrazar = Abraza a una persona mencionandola.
!besar = Besa a una persona mencionandola.
!selfie = Tomate una selfie.
!youtube = Manda un video que tu le pidas
!sonrojarse = Estas sonrojado por la persona que mencionas
!pegar = Golpeas a la persona mencionandola.
!patada = Le das una patada a una persona mencionandola.
!comment = El bot comenta tu muro con lo que tu pongas
!morder = Muerde a la persona que tu mencionas
!cosquilla = Haces cosquillas a la persona que mencionas
!pat = Acaricias la cabeza de quien mencionas

"""
#Vol. Bienvenida/Welcome

join = """ [CUS]𖦆̸ㅤ  𝒲ㅤ〕𝖾𝗅𝖼𝗈𝗆𝖾ㅤㅤ㋖ㅤㅤ⅚̤ㅤ  ⏎ 

[C]Drevenzz bot, te da la Bienvenida
[C]a este chat y te deseamos junto a
[C]tod@s una buena estadía en el chat
[C]y esperamos que te diviertas aquí.

[CuS]/ㅤ/ㅤㅤㅤ◜♡◝ㅤ  〔 ❆ 〕  ㅤ \ㅤ\


[C]No olvides que ante cualquier duda
[C]o reporte, no dudes hablar con el
[C]staff del chat y ante la duda de
[C]algún comando no olvides escribir
[C]!help en el chat para tener ayuda.

[CUS]🏁  ゛ㅤ  𔒌̤ㅤ㍖꯭㍈꯭㌲  ⏎ 

"""

leave = """[BC]Lamentamos que te vayas.

[C]Pero recuerda que siempre
[C]serás nuevamente bienvenido
[C]y esperamos a que vuelvas <3

"""

name_pr = lambda l: ' '.join(l)

# Globally
def esMala(frase):
   malasPalabras=["puta","puto","mierda","zorra","zorrita","pelotuda de mierda","pelotudo de mierda","sorete","forro","chupame el pito","chupame la pija","chupame la concha","pija","poronga","pene","trolo","trola","trolo de mierda","trola de mierda","orto","hija de puta","hijo de puta","gilipollas","polla","cogeme","garchar","garchame","tula","sexo","cagada","maricon", "culeado", "culiado", "culiada", "qla", "la concha de tu hermana", "la concha", "la concha de tu tía", "orgia", "sexo anal", "hijo de re mil puta", "deficiente", "cretina", "lela", "ramera", "fulana", "calientaguevos", "ridícula", "petarda", "pasmarote", "fistro", "desidiosa", "reputa", "soputa", "recontraputa", "hija de puta", "hija de un millón de putas", "escupepitos", "caradepedo", "alientoamojón","revuelcaleche", "coñoesumadre y de su abuela", "conchuda", "culoroto", "nalgas reventadas", "tragasable", "ojete desilachado", "capulla", "zoquete", "masturbadora", "chupa!tampones", "turra", "ojete", "atorrante", "mamaguevos", "cara de concha", "mugrosa", "maldita", "inmunda", "apestosa", "cabrona", "maricona", "huevona", "tarada", "culeada", "gilipollas", "pelotuda", "malnacida", "retardada", "atrasada", "inútil", "móngola", "estúpida", "chupapollas", "cochambrosa", "puta", "panocha", "panochon"]
   for palabra in malasPalabras:
    if palabra.lower() in frase.lower():
      return True
   return False

def reconsocketloop():
    shandle = client.socket
    while (1):
        shandle.close()
        shandle.start()
        time.sleep(120)

def esBuenaFrase(frase):
   esBuenaFrase = True

   listaDePalabras = frase.split() # separa por espacios en palabras
   for unaPalabra in listaDePalabras:
     if esMala(unaPalabra):
       esBuenaFrase = False
       break

   return esBuenaFrase


def send_message(cid, msg):
    acced = amino.SubClient(comId=cid, profile=client.profile)
    try:
        acced.send_message(**msg)
    except Exception:
        print("Error: 404")

def url_like(url):
    link = requests.get(url)
    result = BytesIO(link.content)
    return result      
        
def comment(cid, msg):
    acced = amino.SubClient(comId=cid, profile=client.profile)
    try:
        acced.comment(**msg)
    except Exception:
        print("Error: 404")

#Funcion join desactualizada

def join_chats(cid, msg):
    acced = amino.SubClient(comId=cid, profile=client.profile)
    
    x = re.search("http://aminoapps.com/p/", str(msg['message']))
    p = re.search("http://aminoapps.com/c/", str(msg))

    if x:
      msg = re.sub("http://aminoapps.com/p/","", str(msg['message']))
      ide = client.get_from_code(msg).objectId
      print(ide)
    elif p:
      ide = client.get_from_code(msg).objectId
      print(ide)
    else:
      ide = msg['message']
    try:
        acced.join_chat(ide)
    except Exception:
        print("Error: 404")

#Funcion join no funciona ! Fin.

def search_users(cid, nickname):
    print(nickname)
    acced = amino.SubClient(comId=cid, profile=client.profile)
    result = None
    try:
        result = acced.search_users(nickname)
    except Exception:
        print("Error: 404")
    return result

def youtube(cid,chatId,msg):
    acced = amino.SubClient(comId=cid, profile=client.profile)
    msg = msg['message']
    query_string = urllib.parse.urlencode({"search_query" : str(msg)})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'watch\?v=(\S{11})', html_content.read().decode())
    result='https://youtu.be/' + search_results[0]
    message = {
     'message': "[CB][Video]: "+result+"\n\n\n[C]𒀭 ࣪𝗗.𝗋̶ִɘ࣪𝗏̶◖ִ𝖾︭࣪𝗇ִ︦𝗓𝗓ִ̫𖦹 ۫ ּ🍓",
     'chatId': chatId, 
     'embedLink': result, 
     'embedContent': '𒀭 ࣪𝗗.𝗋̶ִɘ࣪𝗏̶◖ִ𝖾︭࣪𝗇ִ︦𝗓𝗓ִ̫𖦹 ۫ ּ🍓',
     'embedTitle': '𒀭 ࣪𝗗.𝗋̶ִɘ࣪𝗏̶◖ִ𝖾︭࣪𝗇ִ︦𝗓𝗓ִ̫𖦹 ۫ ּ🍓',
     'embedImage': url_like(f'https://img.youtube.com/vi/{search_results[0]}/1.jpg')}

    try:
        send_message(cid,message)
    except Exception:
        print("Error: 404")


#bienvenida


@client.callbacks.event('on_group_member_join')
def on_group_member_join(data):
        nick = data.message.author.nickname
        msg = {
        'message': f"""{join}\n\n[C]{nick} eres finalmente bienvenido/a!
       
[CUS]㍖꯭꯭꯭㍏꯭꯭꯭㌺ㅤ ㅤ⎘ㅤ ㅤ♘ㅤ ㅤ𝅗𝅥ㅤ ㅤ˟⊿
          """,
        'chatId': data.message.chatId,
        'mentionUserIds': [data.message.author.userId]
        }
        send_message(data.comId, msg)

#mensaje

@client.callbacks.event("on_text_message")
def on_text_message(data):

    #nyet

    msg = data.message.content
    nick = data.message.author.nickname
    message = {
        'chatId': data.message.chatId
    }
    #parametros
  
    command = msg.split(' ')
    print(f'{nick}: {msg}')
    pr_t = command[1:]
    command = command[0] 
    
    #help:
    if command == "!help":
        name = name_pr(pr_t)
        if name == "!id":
            message.update({
                'message': """id:
  Esto es para tener el ID de dicho chat.
  Uso: !id"""
            })
            
        elif name == "!kiss":
            message.update({
                'message': """kiss:
  Es un comando para besar apasionadamente aun usuario. :3 
  Uso: !kiss user"""
            })

        elif name == "!kill":
            message.update({
                'message': """kill:
  ¡Este comando le da K'O a su oponente enseguida! D': 
  Uso: !kill user"""
            })

        elif name == "!hug":
            message.update({
                'message': """hug:
  Este comando le dara un gran abrazo. >w< 
  Uso: !hug user"""
            })

        elif name == "!help":
            message.update({
                'message': """help:
  ¿Qué? ¿Estas viendo para que sirve el help mientras usas el help? OMG. """
            })

        elif name == "!comment":
            message.update({
                'message': """comment:
  Te dare el comentario que quieras, ¡Pero ten cuidado! Un gran poder lleva una gran responsabilidad 
  Uso: !comment cualquier mensaje"""
            }) 

        elif name == "~kiss":
            message.update({
                'message': """kiss:
  Beso fantasma >w<
  Uso: ~kiss user"""
            })

        elif name == "~ban":
            message.update({
                'message': """ban:
  ban fantasma :3
  Uso: ~ban user"""

            })

        elif name == "!join":
            message.update({
                'message': """join:
  Este comando es para unirme a tu chat >w<
  Uso: !join linkdelchat """
            })

        elif name == "~hit":
            message.update({
                'message': """puñetazo:
  ¡Te dara una golpiza! >:3
  Uso: ~puñetazo user """
            })
        elif name == "!speak":
            message.update({
                'message': """speak:
  Quieres qué diga lo que me dices? >.<
  Uso: !speak cualquier mensaje """
            })
        elif name == "!id":
            message.update({
                'message': """id:
  ¿Quieres sacar un id? uwu
  Uso: !id? http://amino.com/EXAMPLE. """
            })
        else:
            message.update({'message': HELP}, messageType=100)

    #comandos exclusivo

    elif command == "!comment":
        message = {
            'message': name_pr(pr_t),
            'userId': data.message.author.userId
        }
        comment(data.comId, message)
        return
    
    elif command == "!join":
        message = {
            'message': name_pr(pr_t)
        }
        join_chats(data.comId, message)
        return

    if command == "!selfie": 
        message.update({
        'message': """{Nick}
        se hizo una selfie""",
        'file': url_like(data.message.author.icon),
        'fileType': "image" })
        send_message(data.comId, message)
        message_2 = {
        'chatId': data.message.chatId,
        'message': f"{nick} se ha tomado una selfie {name_pr(pr_t)}",
         'messageType': 100
        }
        send_message(data.comId, message_2)
        return 

    elif command == "-chat":
        params = name_pr(pr_t)
        link = "https://cb.totallyusefulapi.ml/"+params
        response = requests.get(link)
        json_data = json.loads(response.text)
        chatbot = json_data["reply"]
        message.update({
            'message': chatbot,
            'replyTo': data.message.messageId
          })
        send_message(data.comId, message)
        return

    elif command == "!youtube":
        message = {
            'message': name_pr(pr_t)
        }
        youtube(data.comId, data.message.chatId, message)
        return

    #comandos de guion: 

    elif msg.lower() == "!id": 
        message.update({
            'message': f"! comunidad = {data.comId} \n! chat = {data.message.chatId}"
        }, messageType=100)

    if command == "!besar": 
        os.chdir("besos")
        besos = os.listdir()
        with open(str(random.choice(besos)), "rb")   as file: 
            message.update({
                'message': 'I am alive.', 
                'file': file, 
                'fileType': "gif"
            })
            send_message(data.comId, message)
        message_2 = {
        'chatId': data.message.chatId,
        'message': f"{nick} ha besado apasionadamente a: {name_pr(pr_t)}.",
         'messageType': 100
        }
        send_message(data.comId, message_2)
        os.chdir("..")  
        return

    if command == "!morder": 
        os.chdir("mordidas")
        mordidas = os.listdir()
        with open(str(random.choice(mordidas)), "rb")   as file: 
            message.update({
                'message': 'I am alive.', 
                'file': file, 
                'fileType': "gif"
            })
            send_message(data.comId, message)
        message_2 = {
        'chatId': data.message.chatId,
        'message': f"{nick} ha mordido a: {name_pr(pr_t)}.",
         'messageType': 100
        }
        send_message(data.comId, message_2)
        os.chdir("..")
        return   

    if command == "!abrazar": 
        os.chdir("abrazos")
        abrazos = os.listdir()
        with open(str(random.choice(abrazos)), "rb")   as file: 
            message.update({
                'message': 'I am alive.', 
                'file': file, 
                'fileType': "gif"
            })
            send_message(data.comId, message)
        message_2 = {
        'chatId': data.message.chatId,
        'message': f"{nick} ha apachuchado a: {name_pr(pr_t)}.",
         'messageType': 100
        }
        send_message(data.comId, message_2)
        os.chdir("..")
        return               

    if command == "!pegar": 
        os.chdir("golpes")
        golpes = os.listdir()
        with open(str(random.choice(golpes)), "rb")   as file: 
            message.update({
                'message': 'I am alive.', 
                'file': file, 
                'fileType': "gif"
            })
            send_message(data.comId, message)
        message_2 = {
        'chatId': data.message.chatId,
        'message': f"{nick} le ha golpeado fuertemente a: {name_pr(pr_t)}.",
         'messageType': 100
        }
        send_message(data.comId, message_2)
        os.chdir("..")  
        return 

    if command == "!cosquilla": 
        os.chdir("cosquillas")
        cosquillas = os.listdir()
        with open(str(random.choice(cosquillas)), "rb")   as file: 
            message.update({
                'message': 'I am alive.', 
                'file': file, 
                'fileType': "gif"
            })
            send_message(data.comId, message)
        message_2 = {
        'chatId': data.message.chatId,
        'message': f"{nick} le està haciendo cosquillas a: {name_pr(pr_t)}.",
         'messageType': 100
        }
        send_message(data.comId, message_2)
        os.chdir("..")  
        return 

    if command == "!patada": 
        os.chdir("patadas")
        patadas = os.listdir()
        with open(str(random.choice(patadas)), "rb")   as file: 
            message.update({
                'message': 'I am alive.', 
                'file': file, 
                'fileType': "gif"
            })
            send_message(data.comId, message)
        message_2 = {
        'chatId': data.message.chatId,
        'message': f"{nick} le ha dado una patada K.O a: {name_pr(pr_t)}.",
         'messageType': 100
        }
        send_message(data.comId, message_2)
        os.chdir("..")  
        return 

    if command == "!pat": 
        os.chdir("patpat")
        patpat = os.listdir()
        with open(str(random.choice(patpat)), "rb")   as file: 
            message.update({
                'message': 'I am alive.', 
                'file': file, 
                'fileType': "gif"
            })
            send_message(data.comId, message)
        message_2 = {
        'chatId': data.message.chatId,
        'message': f"{nick} le ha dado un pat en la cabeza a: {name_pr(pr_t)}.",
         'messageType': 100
        }
        send_message(data.comId, message_2)
        os.chdir("..")  
        return 

    if command == "!sonrojarse": 
        os.chdir("sonrojado")
        sonrojado = os.listdir()
        with open(str(random.choice(sonrojado)), "rb")   as file: 
            message.update({
                'message': 'I am alive.', 
                'file': file, 
                'fileType': "gif"
            })
            send_message(data.comId, message)
        message_2 = {
        'chatId': data.message.chatId,
        'message': f"{nick} ha sido sonrojado por: {name_pr(pr_t)}.",
         'messageType': 100
        }
        send_message(data.comId, message_2)
        os.chdir("..")  
        return 

    elif command == "!p":
        params = name_pr(pr_t)
        if (esBuenaFrase(params)):
          message.update({
            'message': f"{nick} {name_pr(pr_t)}", 'messageType': 100})

    elif command == "!on":
        message.update({
            'message': f"Mi creador {nick} me ha encendido {name_pr(pr_t)} recuerden que el comando solo funciona con mi creador.",
            'messageType': 100
        })      

    elif command == "!limpiar":
        message.update({
            'message': f"\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎\n‎      ‏‏‎ \n‎      ‏‏‎  \n‎      ‏‏‎  \n‎      ‏‏‎  \n‎      ‏‏‎  \n‎      ‏‏‎  \n‎      ‏‏‎  \n‎      ‏‏‎  \n‎      ‏‏‎  \n‎      ‏‏‎  \n‎      ‏‏‎  \n‎      ‏‏‎  \n‎      ‏‏‎  \n‎ {nick}   \n:::::CHAT LIMPIADO:::::",
            'messageType': 100})   
    
    if command[0] in '!~':
        send_message(data.comId, message)

mensajeLogin()
