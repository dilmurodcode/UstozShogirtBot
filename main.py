import asyncio
from aiogram import Dispatcher, Bot, F, Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from text import sherik_name,sherik_texnalogiya,sherik_aloqa, sherik_hudud


bot = Bot(token='7723912045:AAEKwGAvHK62OP9heeGC53JW5_9sp77p-ig')
dp = Dispatcher()
form_router = Router()

@dp.message(Command('start'))
async def catch_command(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Sherik kerak'), KeyboardButton(text='Ish joyi kerak', callback_data="ish joy kerak")],
            [KeyboardButton(text='Hodim kerak'), KeyboardButton(text='Ustoz kerak')],
            [KeyboardButton(text='Ustoz kerak')]
        ], resize_keyboard=True
    )
    await message.answer(text=f"Assalom alaykum {message.from_user.full_name} UstozShogird kanalining rasmiy botiga xush kelibsiz!\n\n/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!", reply_markup=keyboard)

class Registration_sherik_kerak(StatesGroup):
    name = State()
    texnalogiya = State()
    aloqa = State()
    hudud = State()
    narxi = State()
    kasbi = State()
    vaqti = State()
    maqsad = State()


@dp.message(F.text == 'Sherik kerak')
async def sherik_kerak(message: Message, state: FSMContext):
    await message.answer(text=sherik_name)
    await state.set_state(Registration_sherik_kerak.name)


@dp.message(Registration_sherik_kerak.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text=sherik_texnalogiya)
    await state.set_state(Registration_sherik_kerak.texnalogiya)


@dp.message(Registration_sherik_kerak.texnalogiya)
async def get_texnalogiya(message: Message, state: FSMContext):
    await state.update_data(texnalogiya=message.text)
    await message.answer(text=sherik_aloqa)
    await state.set_state(Registration_sherik_kerak.aloqa)


@dp.message(Registration_sherik_kerak.aloqa)
async def get_aloqa(message: Message, state: FSMContext):
    await state.update_data(aloqa=message.text)
    await message.answer(text=sherik_hudud)
    await state.set_state(Registration_sherik_kerak.hudud)

dp.message(Registration_sherik_kerak.hudud)
async def get_hudud(message: Message, state: FSMContext):

#
# @dp.message(Registration.city)
# async def get_city(message: Message, state: FSMContext):
#     user_data = await state.get_data()
#     await message.answer(f"✅ Ro'yxatdan o'tdingiz!\n\n"
#                          f"👤 Ism: {user_data['name']}\n"
#                          f"🎂 Yosh: {user_data.get('age')}\n"
#                          f"🌆 Shahar: {message.text}")
#     await state.clear()


async def main():
    print('working')
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())



