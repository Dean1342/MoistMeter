
import discord
import csv

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user} is now running!')

@client.event
async def on_message(message):
    words = message.content.split()
    
    if words:
        if words[0] == "!moisture":
            if len(words) > 1:
                if words[1] == "total":
                    count = 0
                    
                    with open("C:/Users/deann/Code/Discord/MoistMeterBot/moisture.csv", "r") as csv_file:
                        reader = csv.reader(csv_file)
                        next(reader)
                        for row in reader:
                            count += 1
                    
                    await message.channel.send(f"Total number of Moist Meters: {count}")
                    return
                else:
                    search_term = " ".join(words[1:])
                    
                    search_term = search_term.lower()
                    
                    matches = []
                    
                    with open("C:/Users/deann/Code/Discord/MoistMeterBot/moisture.csv", "r") as csv_file:
                        reader = csv.reader(csv_file)
                        for row in reader:
                            if search_term in row[0].lower():
                                matches.append((row[0], row[1]))
                    
                    if matches:
                        if len(matches) == 1:
                            await message.channel.send(f"{matches[0][0]} | Moisture: {matches[0][1]}%")
                        else:
                            await message.channel.send(f"Multiple matches found for '{search_term}':")
                            for match in matches:
                                await message.channel.send(f"- {match[0]} | Moisture: {match[1]}%")
                    else:
                        await message.channel.send(f"Could not find a moisture rating for {search_term}")

client.run('token')





