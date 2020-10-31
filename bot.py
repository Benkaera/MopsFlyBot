import discord
import time
import json
import requests

from discord.ext import commands


client = commands.Bot( command_prefix = '#' )


@client.event

async def on_ready():
	print('MopsBot connected')

@client.command( pass_context = True )

async def hello (ctx):
	author = ctx.message.author
	await ctx.send(f' {author.mention}  ПРИВЕТ hello i`m mops bot')

@client.command( pass_context = True )
async def bye (ctx):
	await ctx.send('  ну пока..')

@client.command( pass_context = True )
async def Strank (ctx):
	await ctx.send('  *поют турели* \n *звук входа в дискорд*')
	time.sleep(3)
	await ctx.send('что такое... что такое адепт? \n Love STRANK company?')
	time.sleep(2)
	await ctx.send('Что?')
	time.sleep(2)
	await ctx.send('You fucking love STRANK COMPANY??')
	time.sleep(3)
	await ctx.send('да..')
	time.sleep(3)
	await ctx.send('УУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУ \n УууууууууууууууОООооооооУУУ УУУУУУУУУУУУУУУУУУУУУУУУУУУУУ \n ВРУУУУУУУУУУУУУУУУУУУУМ ВООУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУ')
	await ctx.send('Fuck you u fuck strank love slau slav slou slous YYYYYYyoooooooo \n You fucking love STRANK \n You fucking love \n УУУУУУУУУУУУУУУУУУУУУУУУУУ ')
	await ctx.send('<:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> ')
	await ctx.send('УУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУ')
	await ctx.send('<:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> ')
	await ctx.send('<:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> ')
	await ctx.send('<:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> ')
	await ctx.send('<:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> ')
	time.sleep(2)
	await ctx.send('<:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> ')
	await ctx.send('УУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУ')
	await ctx.send('<:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> ')
	await ctx.send('<:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> ')
	await ctx.send('<:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> ')
	await ctx.send('<:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> ')
	await ctx.send('<:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> <:DoULIkeSTraNK:771968101448155176> ')
	await ctx.send('https://osu.ppy.sh/beatmapsets/1275242')
	
@client.command( pass_context = True )
async def Obiwan (ctx):
	await ctx.send('<:nozhkistola:771965730538258442> <:nozhkistola:771965730538258442> <:nozhkistola:771965730538258442> <:nozhkistola:771965730538258442>')
	await ctx.send('     \n какие мне купить ножки для стола на стену? регулироемые? диапазон высоты?.. эмм.. 1 см в плюс или в минус \n может и не хватить.. идеально было бы высоту норм подобрать \n стул обычный.. высота большая но без пружин, \n но у меня свой самосборный стул, высотаа, я выше сижу \n и стол выше, распорки хочу.. \n сложнее заменять пол без крепления к стене \n хреново.. \n ')
	await ctx.send('<:nozhkistola:771965730538258442> <:nozhkistola:771965730538258442> <:nozhkistola:771965730538258442> <:nozhkistola:771965730538258442>')
@client.command( pass_context = True )
async def Mops (ctx):
	await ctx.send(' Ты дурак зачем меня зовёшь? Хочешь повышение? Проси у биологического меня.. \n https://media.discordapp.net/attachments/686236808635482116/770660798464262194/image0-1.gif')
@client.command( pass_context = True )
async def Danta (ctx):
	await ctx.send('  тьмок..')
	
@client.command( pass_context = True )
async def MiloTlink (ctx):
	await ctx.send('  школьник.. ')
	await ctx.send('https://taganka.verbatoria.ru/wp-content/uploads/2020/01/%D0%B4%D0%B8%D0%B0%D0%B3%D0%BD%D0%BE%D1%81%D1%82%D0%B8%D0%BA%D0%B0-%D0%B4%D0%BB%D1%8F-%D1%88%D0%BA%D0%BE%D0%BB%D1%8C%D0%BD%D0%B8%D0%BA%D0%BE%D0%B2.jpg')
@client.command( pass_context = True )
async def Hey (ctx):
	await ctx.send('  Hey Hey Heeeey..')
	await ctx.send('  https://www.youtube.com/watch?v=rLy-AwdCOmI')
@client.command( pass_context = True )
async def helpp (ctx):
	await ctx.send('hello, bye, Mops, MiloTlink, Vega1, Danta, Hey, Bobi, Черви, random, Obiwan, Strank')
@client.command( pass_context = True )
async def Vega1 (ctx):
	await ctx.send('  читер.. никогда не сможет паснуть sidetracked day ..')
	await ctx.send('https://osu.ppy.sh/users/14165370')
	
@client.command( pass_context = True )
async def Черви (ctx):
	await ctx.send('Это песня про червей \n Они в сердце моём \n Это песня про червей \n Зачем что-то ещё?')
	time.sleep(2)
	await ctx.send('Если есть черви, то зачем что-то ещё?')
	time.sleep(5)
	await ctx.send('Когда у тебя в сердце черви копошатся, \n Что же сделает нормальный человек?.. (а что?) \n А нормальный человек \n Просто съест своих червей \n Просто съест своих червей  \n Он просто съест \n Он просто съест своих червей... \n И скажет спасибо Путину! \n\n\n')
	time.sleep(5)
	await ctx.send('Спасибо...  \n За... \n Червей... \n Тебе...... \n Просто так я не дам тебе червей! \n Не дам! \n Не да-а-а-ам! \n\n\n')
	time.sleep(6)
	await ctx.send('Но тебе можно просто взять червей на огороде, \n Но это не то, \n Когда в сердце черви... \n Они вкуснее... \n И полезнее... \n И теплее... \n\n\n')
	time.sleep(5)
	await ctx.send('https://osu.ppy.sh/beatmapsets/1266730#osu/2632644')
	
@client.command( pass_context = True )
async def Bobi (ctx):
	await ctx.send(' <:Bobby:734330985671426169> <:Bobby:734330985671426169> <:Bobby:734330985671426169>  <:Bobby:734330985671426169> <:Bobby:734330985671426169> <:Bobby:734330985671426169>  <:Bobby:734330985671426169> <:Bobby:734330985671426169> <:Bobby:734330985671426169> <:Bobby:734330985671426169>   ')
	time.sleep(0.1)
	await ctx.send(' <:Bobby:734330985671426169> <:Bobby:734330985671426169> <:Bobby:734330985671426169>  <:Bobby:734330985671426169> <:Bobby:734330985671426169> <:Bobby:734330985671426169>  <:Bobby:734330985671426169> <:Bobby:734330985671426169> <:Bobby:734330985671426169> <:Bobby:734330985671426169>   ')
	time.sleep(0.1)
	await ctx.send(' <:Bobby:734330985671426169> <:Bobby:734330985671426169> <:Bobby:734330985671426169>  <:Bobby:734330985671426169> <:Bobby:734330985671426169> <:Bobby:734330985671426169>  <:Bobby:734330985671426169> <:Bobby:734330985671426169> <:Bobby:734330985671426169> <:Bobby:734330985671426169>   ')
	time.sleep(0.1)
	await ctx.send(' <:Bobby:734330985671426169> <:Bobby:734330985671426169> <:Bobby:734330985671426169>  <:Bobby:734330985671426169> <:Bobby:734330985671426169> <:Bobby:734330985671426169>  <:Bobby:734330985671426169> <:Bobby:734330985671426169> <:Bobby:734330985671426169> <:Bobby:734330985671426169>   ')
	
	
@client.command()
async def random(ctx):
    response = requests.get('https://some-random-api.ml/img/racoon') # ссылка на API
    json_data = json.loads(response.text)

    embed = discord.Embed(color = 0xff9900, title = 'рандомная собака') 
    embed.set_image(url = json_data['link']) 
    await ctx.send(embed = embed)
	

	
	
	
	
token = open( 'token.txt', 'r' ).readline()
client.run(token)