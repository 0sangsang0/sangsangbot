# -*- coding:utf-8 -*- #

import discord
import os

access_token = os.environ['BOT_TOKEN']
token = access_token
client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("쌍쌍봇 ver 1.0.0"))
    print("봇 실행됨!")
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content == "쌍쌍봇 안녕":
        await message.channel.send("안녕하세요!")

client.run(token)

