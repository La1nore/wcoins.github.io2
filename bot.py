from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import logging
import pymongo
from datetime import datetime
import asyncio

API_TOKEN = '7049802781:AAFV7YnJW3doV1gzN062ChzMsCgXSlA291s'
WEB_APP_URL = 'https://your-web-app-url.com'
MONGO_URI = 'mongodb+srv://la1nor:noscope2374@cluster0.575re.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
DB_NAME = 'tickdb'
COLLECTION_NAME = 'users'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

client = pymongo.MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    user = collection.find_one({"_id": user_id})
    
    if not user:
        collection.insert_one({
            "_id": user_id,
            "tokens": 0,
            "start_time": datetime.utcnow()
        })
    
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text='Open Web App', web_app=types.WebAppInfo(url=WEB_APP_URL))
    keyboard.add(button)
    await message.answer("Welcome! Click below to open the web app.", reply_markup=keyboard)

@dp.message_handler(commands=['balance'])
async def show_balance(message: types.Message):
    user_id = message.from_user.id
    user = collection.find_one({"_id": user_id})
    
    if user:
        tokens = user['tokens']
        await message.answer(f"Your balance: {tokens} tokens.")
    else:
        await message.answer("User not found.")

async def main():
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())
