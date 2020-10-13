import discord
import random
import os

intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))


greetings = [
	'Hello',
	'Hi!',
	'Guten Tag',
	'Hiya',
	'Hello there',
	'Hey! Look at this nerd',
	'Kon\'nichiwa',
	'I think the account that just joined is a bot',
	'Hallo',
	'Aloha',
	'Bonjour',
	'Furthermore, I believe Carthage should be destroyed',
	'Abandon hope, all ye who enter here'
]


@client.event
async def on_member_join(member: discord.member):
	print('Someone joined as ' + str(member))
	await member.guild.text_channels[0].send(greetings[random.randint(0, len(greetings) - 1)])


@client.event
async def on_message(message: discord.message):
	if '@Uioea' in message.content or 'BOT_STATUS' in message.content:
		print('Status was requested')
		key = getKey()
		if len(key) > 8:
			key = key[0:8] + (len(key) - 8) * '*'  # Redact the rest of this for security
		await message.channel.send('Currently online; Key is: ' + key)


def getKey():
	return os.getenv('BOT_TOKEN')


client.run(getKey())
