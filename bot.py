import asyncio
import random
from telegram import Bot

TOKEN = "8368341315:AAFG4-C3E6gnMWWmZ_SBZEZKsMSW6ibx9jY"
CHAT_ID = "-1003881530143"

bot = Bot(token=TOKEN)

def generate_prediction():

    rounds = []

    for i in range(4):
        value = round(random.uniform(1.2,3.0),2)
        rounds.append(value)

    text = "🚀 Aviator Prediction\n\n"

    for i,v in enumerate(rounds):
        text += f"Round {i+1} → {v}x\n"

    return text


async def run_bot():

    while True:

        message = generate_prediction()

        await bot.send_message(
            chat_id=CHAT_ID,
            text=message
        )

        print("Signal Sent")

        await asyncio.sleep(180)


asyncio.run(run_bot())
