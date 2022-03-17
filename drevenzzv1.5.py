from BotAmino import *
from gtts import gTTS, lang
import amino
import os
import random
import sys
import amino
import datetime
from random import uniform, choice, randint
from amino import socket
from google_trans_new import google_translator
from pathlib import Path
from BotAmino import path_download, path_sound
from threading import Thread
from flask import Flask


print("wait...")
client = BotAmino()
client.prefix = "!" 
client.wait = 1  # wait 10 sec before doing a new command

app=Flask("")

@app.route("/")
def index():
    return "<h1>Bot is running</h1>"

Thread(target=app.run,args=("0.0.0.0",8080)).start()

def test(data):
    return data.authorId == ["b2ceed66-000a-4df9-afb8-b5795cabd8c4"]

@client.command("global")
def get_global(data):
  objectId = client.get_from_code(data.message).objectId
  data.subClient.send_message(data.chatId,message="ndc://g/user-profile/"+objectId)

@client.command("fondo")
image = subclient.get_chat_thread(chatId).backgroundImage
  if image is not None:
    print(image)
    filename = image.split("/")[-1]
    urllib.request.urlretrieve(image, filename)
    with open(filename, 'rb') as fp:
      with suppress(Exception):
        send_message(chatId, file=fp, fileType="image")
        print(os.remove(filename))

@client.answer("drev")
def hello(data):
    data.subClient.send_message(data.chatId, message="Estoy prendido.. >w<")

@client.command("help")
def help(data):
    data.subClient.send_message(chatId=data.chatId, message="""[c]== Comandos ==
!shipp = Compatibilidad contigo y con el mencionado.
!google = Busca lo que quieras.
!tra = Traduce lo que tu le digas en Ingles.
!askme = El bot responde lo que tu le preguntes.
!voz = El bot envia un audio con lo que tu le digas.
!pedido = Informaciòn para conseguir tu bot.
!audio = Da un audio random de los que tiene para que lo escuches.
!habla = El bot habla por ti de manera invisible.
!img = El bot muestra una imagen random de las que tiene.
!llora = El bot llora por ti.
!casarse = Te casas con la persona que mencionas.
!divorcio = Te divorcias con la persona con la cual te casaste.
!shipp = El bot calcula la compatibilidad que tienes con la persona que mencionas.
!matar = Matas a la persona que mencionas.
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
    """, replyTo = data.messageId)

@client.command("google")
def google(data):
    msg = data.message.split(" ")
    msg = '+'.join(msg)
    data.subClient.send_message(chatId=data.chatId, message=f"https://www.google.com/search?q={msg}")

@client.command("tra")
def tra(data):
    translator = google_translator()
    translate_text = translator.translate(data.message)
    data.subClient.send_message(data.chatId, f"{translate_text}")

@client.command("prueba")
def penis(data):
        data.subClient.send_message(messageType=109, chatId=data.chatId, message="⠄⠄⠄⢰⣧⣼⣯⠄⣸⣠⣶⣶⣦⣾⠄⠄⠄⠄⡀⠄⢀⣿⣿⠄⠄⠄⢸⡇⠄⠄ ⠄⠄⠄⣾⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⢀⣿⠄ ⠄⠄⢀⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿⣿⠄ ⠄⠄⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⠄ ⠄⢀⢸⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉⠋⣰ ⠄⣼⣖⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇⢀⣤ ⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴⣿⡗ ⢀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄ ⢸⣿⣦⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄ ⠘⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵⣾⠃⠄ ⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃⠄⠄ ⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁⠄⠄⠄ ⠄⠄⠄⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄⠄⠄⠄⠄ ⠄⠄⠄⠄⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄⠄⠄⠄⠄⢀⣠⣴ ⣿⣿⣿⣶⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⣠⣴⣿⣿⣿")

@client.command("askme")
def ball(data):
    ball = random.choice(["No.", "Sì.", "Tal vez.", "Claro.", "Nunca.", "Claro que sì.", "Porque si.", "Eres pelotudo.", "Tu mama", "Claro que no, no haria eso."])
    data.subClient.send_message(data.chatId, ball, replyTo = data.messageId)

@client.on_member_join_chat()
def say_hello(data):
    data.subClient.send_message(data.chatId, f"{data.author} eres bienvenido!")

@client.command("voz")
def say_something(data):
    audio_file = f"{path_download}/ttp.mp3"
    gTTS(text=data.message, lang='es', slow=False).save(audio_file)
    with open(audio_file, 'rb') as fp:
        data.subClient.send_message(data.chatId, file=fp, fileType="audio")
        os.remove(audio_file)

@client.on_member_leave_chat()
def say_goodbye(data):
    data.subClient.send_message(data.chatId, "¡Adios usuario! Esperamos verte pronto.")

@client.command("titulo")
def give_a_title(data):
    data.subClient.add_title(data.authorId, data.message)
    data.subClient.send_message(chatId=data.chatId, message="Listo, ya tienes tu título, no abuses.. >w<")

@client.callbacks.event("on_voice_message")
def on_audio(data):
    print("audio_file")

client.launch()
print("ready")
