import discord 
import asyncio
from discord.ext import commands
from discord.ext.commands import check
from discord import voice_client
from discord import Role
from discord import Guild
import datetime
import pyautogui
import time
from PIL import Image

client = commands.Bot(command_prefix= '!', help_command=None)

@client.command()
async def help(ctx):
    out = """```
    Para definir quem sera o host(para deixar de ser o host, bastar executar o comando novamente):
    !host          ->   É a pessoa responsável de poder dar todos os outros comandos. O bot irá capturar a tela do host, então ele sempre 
                          precisa ficar telando o jogo.
    
    Para começar a capturar:
    !start         ->   O bot começa a capturar a tela do host.
    
    Quando a partida finalizar:
    !quit          ->  O bot para de capturar a tela do host, e também desmuta todos do canal de voz.


    #Outros comandos:
    !user         ->   Verificar os usuários|hosts que estão no canal de voz.
    !mute         ->   Muta todo mundo.
    !unmute       ->   Desmuta todo mundo.
    ```"""
    await ctx.send(out)

global discussion
discussion = False

global leader
leader = None

global flag
flag = False

def compare_file():
    foto = pyautogui.screenshot()
    foto.save("imagem.png")
    
    time.sleep(0.3)
   
    image1 = Image.open("imagem.png")
    image2 = Image.open("votos.png")

    assert image1.mode == image2.mode, "Verifica se as imagens sao do mesmo tipo."
    assert image1.size == image2.size, "Verifica o tamanho das imagens."

    pairs = zip(image1.getdata(), image2.getdata())
    if len(image1.getbands()) == 1:
        dif = sum(abs(p1-p2) for p1,p2 in pairs)
    else:
        dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))


    ncomponents = image1.size[0] * image1.size[1] * 3
    porcentagem = (dif / 255.0 * 100) / ncomponents
   
    discussion = False
    if porcentagem < 25:
        discussion = True
    return discussion


@client.command()
async def host(ctx):
    global leader

    if leader == None:
        leader = ctx.author
        await ctx.send(f"Host conectado: {ctx.author.name}")
    elif leader != None and leader != ctx.author:
        await ctx.send(f"O @{leader} É o atual host. Caso seja o host e deseje sair do modo host digite !host ")
    else:
        await ctx.send(f"Host desconectado: {ctx.author.name}")
        leader = None


@client.command()
async def users(ctx):
    global leader
    
    if leader == None:
        await ctx.send("Primeiro precisa-se de um host. DIGITE: !host")
    else:
        out = "Usuarios conectados: "

        for member in list(client.get_channel(leader.voice.channel.id).members):
            out += f"- {member}\n"
        
        await ctx.send(f"```{out}```")

@client.command()
async def mute(ctx):
    global leader
    global discussion
    discussion = False

    try:
        if ctx.author != leader and leader == None:
            await ctx.send(f"O host precisa ser inicializado. Digite: !host")
        elif ctx.author != leader and leader != None:
            await ctx.send(f"Apenas o {leader} pode utilizar esse comando.")
    except:
        pass

    try:
        for member in list(client.get_channel(leader.voice.channel.id).members):
            await member.edit(mute= True)

    except AttributeError:
        print("Não existe ninguém como host.")

@client.command()
async def unmute(ctx):
    global leader
    try:
        if ctx.author != leader and leader == None:
            await ctx.send(f"O host precisa ser inicializado. Digite: !host")
        elif ctx.author != leader and leader != None:
            await ctx.send(f"Apenas o {leader} pode utilizar esse comando.")
    except:
        pass

    try:
        for member in list(client.get_channel(leader.voice.channel.id).members):
                await member.edit(deafen= False, mute= False)

    except AttributeError:
        print("Não existe ninguém como host.")

@client.command()
async def start(ctx):
    global leader 
    global discussion
    
    global flag
    flag = True

    try:
        if ctx.author != leader and leader == None:
            await ctx.send(f"O host precisa ser inicializado. Digite: !host")
        elif ctx.author != leader and leader != None:
            await ctx.send(f"Apenas o {leader} pode utilizar esse comando.")
    except:
        pass
    

    while flag:
        file = compare_file()
        if file == True:
            for member in list(client.get_channel(leader.voice.channel.id).members):
                    await member.edit(mute= False)
        else:
            for member in list(client.get_channel(leader.voice.channel.id).members):
                    await member.edit(mute= True)

@client.command()
async def quit(ctx):
    global leader 
    global flag
    
    flag = False
    
    try:
        if ctx.author != leader and leader == None:
            await ctx.send(f"O host precisa ser inicializado. Digite: !host")
        elif ctx.author != leader and leader != None:
            await ctx.send(f"Apenas o {leader} pode utilizar esse comando.")
    except:
        pass
    
    for member in list(client.get_channel(leader.voice.channel.id).members):
        await member.edit(mute= False)


# INSIRA O TOKEN DO SEU BOT - O token é gerado no próprio site do discord.
client.run("")