# Work with Python 3.6
import discord
from os import system
import random
import datetime
import os

system("title "+"재미봇")

TOKEN = os.environ["BOT_TOKEN"]

client = discord.Client()


@client.event
async def on_member_join(member):
    role = ''
    for i in member.server.roles:
        if i.name == "유저":
            role = i
            break
    await client.add_roles(member, role)


@client.event
async def on_message(message):
    member = message.author
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    
    if message.content.startswith('!확률 '):
        text = message.content
        text = text.replace("!확률 ", "", 1)
        nsu = random.randrange(0,101)
        asu = str(nsu)
        mtl = "``" + text + "`` 은 (는)"
        msg = "``" + asu + "%``입니다."
        mtl = mtl.format(message)
        msg = msg.format(message)
        await client.send_message(message.channel, embed=discord.Embed(title = mtl, description = msg, colour = 0x2EFEF7))
        return

    if message.content.startswith('!따라해 '):
        text = message.content
        text = text.replace("!따라해 ", "",1)
        msg = text.format(message)
        await client.send_message(message.channel, msg)

    if(message.content == "!역할 행복이"):
        for i in member.server.roles:
            if i.name == "행복이":
                role = i
                break
        await client.add_roles(member, role)

    if(message.content == "!역할 재미끄투"):
        for i in member.server.roles:
            if i.name == "재미끄투":
                role = i
                break
        await client.add_roles(member, role)

    if message.content.startswith('!재미봇'):
        msg = '안녕하세요, {0.author.mention} 님'.format(message)
        await client.send_message(message.channel, msg)
    
    if(message.content == '!버전'):
        version = os.environ["VERSION"]
        msg = '재미봇 버전: ' + version
        msg = msg.format(message)
        await client.send_message(message.channel, embed=discord.Embed(title = msg,colour = 0x2EFEF7))
        
    if message.content.startswith('!명령어'):
        mtl = "재미봇 명령어"
        msg = '**!버전**: 재미봇의 버전을 확인합니다.\n**!상태 <내용>**: 재미봇의 상태를 변경합니다.\n**!가위, !바위, !보**: 재미봇과 가위바위보를 합니다.\n**!확률 <내용>**: 백분율로 확률을 구합니다.\n**!따라해 <내용>** 말을 따라합니다.'
        await client.send_message(message.channel, embed=discord.Embed(title = mtl, description = msg, colour = 0x2EFEF7))

    if message.content.startswith('!상태 '):
        text = message.content
        rpl = text.replace("!상태", "")
        await client.change_presence(game=discord.Game(name=rpl))
        mtl = ':white_check_mark: 설정되었습니다.'.format(message)
        await client.send_message(message.channel, embed=discord.Embed(title = mtl, colour = 0x2EFEF7))


    if(message.content == '!바위'):
        nsu = random.randrange(1,4)
        mtl = "가위바위보 결과"
        if(nsu == 1):
            msg = '당신은 바위를 내셨고, 재미봇은 보를 냈습니다!\n야호! 제가 이겼습니다!'


        if(nsu == 2):
            msg = '당신은 바위를 내셨고, 재미봇도 바위를 냈습니다!\n무승부입니다! 한 판 더 하실래요...?'


        if(nsu == 3):
            msg = '당신은 바위를 내셨고, 재미봇은 가위를 냈습니다!\n제가 졌습니다! ㅠㅠ'            
        

        msg = msg.format(message)
        await client.send_message(message.channel, embed=discord.Embed(title = mtl, description = msg, colour = 0x2EFEF7))


    if(message.content == '!가위'):
        nsu = random.randrange(1,4)
        mtl = "가위바위보 결과"
        if(nsu == 1):
            msg = '당신은 가위를 내셨고, 재미봇은 바위를 냈습니다!\n야호! 제가 이겼습니다!'


        if(nsu == 2):
            msg = '당신은 가위를 내셨고, 재미봇도 가위를 냈습니다!\n무승부입니다! 한 판 더 하실래요...?'


        if(nsu == 3):
            msg = '당신은 가위를 내셨고, 재미봇은 보자기를 냈습니다!\n제가 졌습니다! ㅠㅠ'            
        

        msg = msg.format(message)
        await client.send_message(message.channel, embed=discord.Embed(title = mtl, description = msg, colour = 0x2EFEF7))

    if(message.content == "!보" or message.content == "!보자기"):
        nsu = random.randrange(1,4)
        mtl = "가위바위보 결과"
        if(nsu == 1):
            msg = '당신은 보를 내셨고, 재미봇은 가위를 냈습니다!\n야호! 제가 이겼습니다!'


        if(nsu == 2):
            msg = '당신은 보를 내셨고, 재미봇도 보를 냈습니다!\n무승부입니다! 한 판 더 하실래요...?'


        if(nsu == 3):
            msg = '당신은 보를 내셨고, 재미봇은 바위를 냈습니다!\n제가 졌습니다! ㅠㅠ'            
        

        msg = msg.format(message)
        await client.send_message(message.channel, embed=discord.Embed(title = mtl, description = msg, colour = 0x2EFEF7))

    if message.content.startswith('!시간'):
        if(message.content == "!시간 1"):
            now = datetime.now()
            hr = "``" + str(now.hour) + "`` : "
            mi = "``" + str(now.minute) + "`` : "
            sc = "``" + str(now.second) + "``"
            if(now.hour > 12):
                thr = now.hour - 12
                hr = "``" + str(thr) + "`` : "
                oj = "``오후``  "
            else:
                oj = "``오전``  "
            await client.send_message(message.channel, oj + hr + mi+ sc)


        if(message.content == "!시간 2"):
            now = datetime.now()
            hr = str(now.hour) + "시 "
            mi = str(now.minute) + "분 "
            sc = str(now.second) + "초"
            if(now.hour > 12):
                thr = now.hour - 12
                hr = str(thr) + "시 "
                oj = "오후 "
            else:
                oj = "오전 "
            mtl = "현재 시간은 " + oj + hr + mi + sc + " 입니다."
            await client.send_message(message.channel, embed=discord.Embed(title = mtl, colour = 0x2EFEF7))


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="명령어는 \"!명령어\" 로 확인!ㅤㅤㅤㅤㅤㅤㅤ"))
    print('다음 계정으로 로그인됨:')
    print(client.user.name)
    print(client.user.id)
    print('--- 동작 중 ---')

client.run(TOKEN)
