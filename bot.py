import discord
from discord.ext import commands
from discord.ext.commands.core import command
import random
import json



with open('123.json','r',encoding='UTF8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(">> bot is online <<")



@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')

@bot.command()
async def 抱抱(ctx):
    user_name = ctx.message.author.mention
    await ctx.send(f'{user_name}  需要「愛」😭😭😭,請開始表演吧!')

# ayay
@bot.command()
async def ayay(ctx):
    #jdata['ayaya_pic'] 也有圖庫
    user_name = ctx.message.author.mention 
    await ctx.send(f'(ᗒᗨᗕ)／ あやや！あやや！＼(ᗒᗨᗕ)\n＼(ᗒᗨᗕ) AYAYA！AYAYA！(ᗒᗨᗕ)／\n' )


    
@bot.command()
async def 抽籤(ctx):
    random_pic = random.choice(jdata['url_pic']) #隨機取json字典裡的url
    user_name = ctx.message.author.mention #存放user name用
    await ctx.send(f'{user_name}  玩家抽籤！\n發出了光芒...\n\n\n恭喜...你的抽到是\n' + random_pic)


bot.run('OTI4ODI0NDc1MTM3NDc4NjY2.YdeZMw.2GPNq43ctUVbkyBWoiPksQ-M5N4')


