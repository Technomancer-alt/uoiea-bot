import discord
import random
import os
import math
import time

intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))


greetings = [
	('No one would have believed in the last years of the nineteenth century that this world was being watched keenly and closely by intelligences greater than man’s and yet as mortal as his own; that as men busied themselves about their various concerns they were scrutinised and studied, perhaps almost as narrowly as a man with a microscope might scrutinise the transient creatures that swarm and multiply in a drop of water. Know this, new member: We\'re watching you.', 1),
	('In a distant and secondhand set of dimensions, in an astral plane that was never meant to fly, the curling star mists waver and part... see... this latest member of our community', 1),
	('Welcome to The Salty Spittoon. How tough are you?', 3),
	('Freddie Mercury did nothing wrong', 3),
	('Furthermore, I believe Carthage should be destroyed', 3),
	('Looks like meat is back on the menu, boys!', 5),
	('This is getting out of hand. Now there are two of them?', 5),
	('Abandon hope, all ye who enter here', 5),
	('technodancer does it have "What are you doing in my swamp!?"', 2),
	('Hey! Look at this nerd', 5),
	('You\'re finally awake', 3),
	('@Aeiou Say hello to this person', 5),
	('Kon\'nichiwa', 10),
	('You! Person who just joined! Very important question: What do you think of the Dewey Decimal System?', 5),
	('I think the account that just joined is a bot', 5),
	('Hallo', 10),
	('*Aggressive honking noises*', 8),
	('*Welcoming honking noises*', 8),
	('Aloha', 10),
	('Hola', 10),
	('Speak of the devil...', 8),
	('Bonjour', 10),
	('Hello there', 10),
	('Welcome', 10),
	('Hi!', 10),
	('Guten Tag', 10),
	('Hiya', 10),
	('Hello', 10)
]

def getMessage():
	sumWeight = 0
	for entry in greetings:
		sumWeight += entry[1]
	selection = random.randint(0, sumWeight)
	for entry in greetings:
		selection -= entry[1]
		if selection <= 0:
			return entry[0]
	return 'YOU CAUSED A GLITCH, YOU BUGGER!'


@client.event
async def on_member_join(member: discord.member):
	print('Someone joined as ' + str(member))
	time.sleep(1) # If we don't sleep, sometimes we send the message before the normal Discord join message
	greeting = getMessage()
	await member.guild.text_channels[0].send(greeting)


@client.event
async def on_message(message: discord.message):
	if message.author == client.user:
		return # Don't reply to ourself
	
	if '>>BOT_STATUS' in message.content:
		print('Status was requested')
		key = getKey()
		if len(key) > 8:
			key = key[0:8] + (len(key) - 8) * '-'  # Redact the rest of this for security
		await message.channel.send('Currently online; Key is: ' + key)
	elif '>>BOT_WELCOME' in message.content:
		print('Message was requested')
		await message.channel.send(getMessage())
	elif '>>BOT_MUSIC' in message.content:
		print('Music was requested')
		await message.channel.send('https://www.youtube.com/watch?v=c5daGZ96QGU&ab_channel=Misaki')
	elif '>>BOT_HELP' in message.content:
		print('Help requested')
		await message.channel.send('`>>BOT_STATUS`: Tells you if the bot is online')
		await message.channel.send('`>>BOT_MUSIC`: Links a song')
		await message.channel.send('`>>BOT_WELCOME`: Says a welcome message')
		await message.channel.send('`>>BOT_HELP`: Displays the list of bot commands')
		await message.channel.send('`>>BOT_DEWEY for`: Makes you `@pro dewey decimal system`')
		await message.channel.send('`>>BOT_DEWEY against`: Makes you `@anti dewey decimal system`')
		await message.channel.send('`>>BOT_DEWEY out`: Makes you neutral on the dewey decimal system')
		await message.channel.send('`>>BOT_PING`: Ping pong')
		await message.channel.send('`>>BOT_SERVER join`: Gives you the `@Server player` role')
		await message.channel.send('`>>BOT_SERVER leave`: Removes your `@Server player` role')
		await message.channel.send('1 secret command :thinking:')
	elif '>>BOT_DEWEY' in message.content:
		proRole = discord.utils.find(lambda r: r.name == 'pro dewey decimal system', message.guild.roles)
		antiRole = discord.utils.find(lambda r: r.name == 'anti dewey decimal system', message.guild.roles)
		if 'for' in message.content:
			await message.author.remove_roles(antiRole)
			await message.author.add_roles(proRole)
			await message.channel.send('Welcome to the fight')
		elif 'against' in message.content:
			await message.author.add_roles(antiRole)
			await message.author.remove_roles(proRole)
			await message.channel.send('You joined a thing')
		elif 'out' in message.content:
			await message.author.remove_roles(antiRole)
			await message.author.remove_roles(proRole)
			await message.channel.send('Take a side you coward')
	elif '>>BOT_PING' in message.content:
		print('Ping pong')
		await message.channel.send('Pong!')
	elif '>>BOT_PONG' in message.content:
		print('pong ping')
		await message.channel.send('Ping!')
	elif '>>BOT_SERVER' in message.content:
		serverRole = discord.utils.find(lambda r: r.name == 'Server player', message.guild.roles)
		if 'join' in message.content:
			await message.author.add_roles(serverRole)
			await message.channel.send('Welcome to the public server')
		elif 'leave' in message.content:
			await message.author.remove_roles(serverRole)
			await message.channel.send('We\'ll miss you')

			
def getKey():
	return os.getenv('BOT_TOKEN')


print('Starting')
print('Key: ' + getKey())
client.run(getKey())
print('Started')
