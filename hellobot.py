import discord
import random
import os
import math

intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))


greetings = [
	'No one would have believed in the last years of the nineteenth century that this world was being watched keenly and closely by intelligences greater than man’s and yet as mortal as his own; that as men busied themselves about their various concerns they were scrutinised and studied, perhaps almost as narrowly as a man with a microscope might scrutinise the transient creatures that swarm and multiply in a drop of water. Know this, new member: We\'re watching you.',
	'In a distant and secondhand set of dimensions, in an astral plane that was never meant to fly, the curling star mists waver and part... see... this latest member of our community',
	'Welcome to The Salty Spittoon. How tough are you?',
	'Furthermore, I believe Carthage should be destroyed',
	'Looks like meat is back on the menu, boys!',
	'This is getting out of hand. Now there are two of them?',
	'Abandon hope, all ye who enter here',
	'Hey! Look at this nerd',
	'@Aeiou Say hello to this person',
	'Kon\'nichiwa',
	'You! Person who just joined! Very important question: What do you think of the Dewey Decimal System?',
	'I think the account that just joined is a bot',
	'Hallo',
	'*Aggressive honking noises*',
	'*Welcoming honking noises*',
	'Aloha',
	'Hola',
	'Speak of the devil...',
	'Bonjour',
	'Hello there',
	'Welcome',
	'Hi!',
	'Guten Tag',
	'Hiya',
	'Hello'
]

def getMessage():
	# Weighted random; entries have a weight equal to their position in the list (not their index; position starts at 1)
	count = len(greetings)
	weightIndex = random.randint(0, (count ** 2 + count) / 2 - 1)
	index = math.floor((math.sqrt(1 + 8 * weightIndex) - 1) / 2)
	return greetings[index]

@client.event
async def on_member_join(member: discord.member):
	print('Someone joined as ' + str(member))
	greeting = getMessage()
	await member.guild.text_channels[0].send(greeting)


@client.event
async def on_message(message: discord.message):
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

def getKey():
	return os.getenv('BOT_TOKEN')


print('Starting')
print('Key: ' + getKey())
client.run(getKey())
print('Started')
