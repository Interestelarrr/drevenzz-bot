import config
import amino
import random
import urllib.request
import urllib.parse
import json
import requests
import re
import time
import os
import subprocess
from io import BytesIO
from threading import Thread
from getpass import getpass
from pprint import pprint
client = amino.Client()

#Vol. Login & Credits

print("on by keldrysh")

client.login(email='drevenzzbot@gmail.com',password='andromedala')

os.system ("clear")

print("""
      ¡Bienvenido a Drevenzz! 
      Este bot esta creado
      por keldrysh/drevenzz
      """
)

#Vol. Help

HELP = """ 
[CUS]🏁  ゛ㅤ  𔒌̤ㅤ㍖꯭㍈꯭㌲  ⏎ 

!everyone =  llama a todos.
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
[C]!help (en proceso de actualizar) en el chat para tener ayuda.

[CUS]🏁  ゛ㅤ  𔒌̤ㅤ㍖꯭㍈꯭㌲  ⏎ 

"""

leave = """[BC]Lamentamos que te vayas.

[C]Pero recuerda que siempre
[C]serás nuevamente bienvenido
[C]y esperamos a que vuelvas <3

"""

name_pr = lambda l: ' '.join(l)

#Vol. Configs Welcome/Bienvenida.


#Bienvenida


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


#despedida

@client.callbacks.event('on_group_member_leave')
def on_group_member_leave(data):
        msg = {
        'message': f"{leave}",
        'chatId': data.message.chatId,
        'mentionUserIds': [data.message.author.userId]
        }
        send_message(data.comId, msg)

def send_message(cid, msg):
   acced = amino.SubClient(comId=cid, profile=client.profile)
   try:
       acced.send_message(**msg)
   except Exception:
       print("Error: 404")

#Vol. Setting help

@client.callbacks.event("on_text_message")
def on_text_message(data):

    #parametros
    command = data.message.content.split(' ')
    print(command)
    pr_t = command[1:]
    command = command[0] 

    #help:
    if command == "!help":
       acced = amino.SubClient(comId=data.comId, profile=client.profile)
       acced.send_message(chatId=data.message.chatId, message = HELP) 

# Comandos-Everyone

users = []
@client.callbacks.event("on_text_message")
def on_text_message(data):
   subclient = amino.SubClient(data.comId, profile=client.profile)
   
   chatId = data.message.chatId
   print(f"{data.message.author.nickname}: {data.message.content}")

   if data.message.content == "!everyone":
     I = 0
     while I < 1:
       users = []
       people = subclient.get_chat_users(chatId,start=0,size=871).userId
       for usersin in people: 
         users.append(usersin)
         print(users)
       subclient.send_message(chatId, message="<$@Esto es Importante$>!", mentionUserIds=users)
       print("send")
       del users
       I += 1

