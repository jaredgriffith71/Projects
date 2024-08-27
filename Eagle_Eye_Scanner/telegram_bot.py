from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

# Replace with your bot's token
API_TOKEN = '7546943927:AAFOqfThcLXFblo7gAL9v25yqQEi_Q-H208'

# Replace with your chat ID
CHAT_ID = -1002230829243

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Handler for the /start command
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply("We will begin scanning!")

# Handler for the /help command
@dp.message(Command("help"))
async def send_help(message: types.Message):
    await message.reply("There is no help here.")

# Function to send a message to the specified chat ID
async def send_message_to_chat(message_text: str):
    try:
        await bot.send_message(chat_id=CHAT_ID, text=message_text)
        print(f"Message sent to chat {CHAT_ID}: {message_text}")
    except Exception as e:
        print(f"Failed to send message: {e}")

# Main function to start the bot
async def main():
    print('Bot is online!')
    # Start polling
    await dp.start_polling(bot)

# Entry point
if __name__ == '__main__':
    asyncio.run(main())
