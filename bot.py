import random
from aiogram import Bot, Dispatcher, executor, types

TOKEN = "ТУТ_ТВОЙ_ТОКЕН"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

anime_list = [
    {
        "title": "Attack on Titan",
        "genres": "Action, Drama, Fantasy",
        "episodes": "89",
        "rating": "9.1"
    },
    {
        "title": "Naruto",
        "genres": "Action, Adventure",
        "episodes": "220",
        "rating": "8.3"
    },
    {
        "title": "Death Note",
        "genres": "Mystery, Thriller",
        "episodes": "37",
        "rating": "9.0"
    },
    {
        "title": "Demon Slayer",
        "genres": "Action, Fantasy",
        "episodes": "55",
        "rating": "8.7"
    }
]

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("🎲 Рандомне аніме")
    keyboard.add(button)

    await message.answer("Натисни кнопку щоб отримати рандомне аніме", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "🎲 Рандомне аніме")
async def random_anime(message: types.Message):
    anime = random.choice(anime_list)

    text = f"""
🎬 Назва: {anime['title']}
📺 Серії: {anime['episodes']}
🎭 Жанри: {anime['genres']}
⭐ Рейтинг: {anime['rating']}
"""

    await message.answer(text)

if name == "main":
    executor.start_polling(dp)