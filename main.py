# writing a doggo bot for those who don't (or even those that do) have a doggo and want a doggo
# uploading this onto github to show others and do save work incase replit discards it lol

import discord
import os
import requests
import json
import random
from replit import db

#instance for discord
client = discord.Client()
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]
starter_encouragements = ["Cheer up hooman!", "You got this hooman!", "It will all be okay hooman!"]

# registers the event 
@client.event
# called when the bot ready
async def on_ready():
  print('Welcome back {0.user}'.format(client))

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)
  
def update_encouragement(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = [encouraging_message]
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragement(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
  db["encouragements"] = encouragements
  
@client.event
# when there is a message
async def on_message(message):
  msg = message.content
  if message.author == client.user:
    return
  
  if message.content.startswith('$hello'):
    await message.channel.send('Hello human!')

  if message.content.startswith('$help'):
    quote = get_quote()
    await message.channel.send(quote)

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))

# storing the token
client.run(os.getenv('TOKEN'))
