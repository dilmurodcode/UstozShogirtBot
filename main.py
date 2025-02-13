import asyncio

from aiogram import Dispatcher, Bot, F, Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from text import sherik_name,sherik_texnalogiya,sherik_aloqa, sherik_hudud,sherik_narx,sherik_vaqti,sherik_maqsad, sherik_kasb
from text import ish_name, ish_age

bot = Bot(token='7723912045:AAEKwGAvHK62OP9heeGC53JW5_9sp77p-ig')
dp = Dispatcher()
form_router = Router()

@dp.message(Command('start'))
async def catch_command(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Sherik kerak'), KeyboardButton(text='Ish joyi kerak')],
            [KeyboardButton(text='Hodim kerak'), KeyboardButton(text='Ustoz kerak')],
            [KeyboardButton(text='Shogirt kerak')]
        ], resize_keyboard=True
    )
    await message.answer(text=f"Assalom alaykum {message.from_user.full_name} @{message.from_user.username} UstozShogird kanalining rasmiy botiga xush kelibsiz!\n\n/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!", reply_markup=keyboard)


def sherik_button():
    buttons = [
        [KeyboardButton(text="Ha"), KeyboardButton(text="Yo'q")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

#==============================================================================================
                #Sherik kerak button

class RegistrationSherikKerak(StatesGroup):
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
    await state.set_state(RegistrationSherikKerak.name)


@dp.message(RegistrationSherikKerak.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text=sherik_texnalogiya)
    await state.set_state(RegistrationSherikKerak.texnalogiya)


@dp.message(RegistrationSherikKerak.texnalogiya)
async def get_texnalogiya(message: Message, state: FSMContext):
    await state.update_data(texnalogiya=message.text)
    await message.answer(text=sherik_aloqa)
    await state.set_state(RegistrationSherikKerak.aloqa)


@dp.message(RegistrationSherikKerak.aloqa)
async def get_aloqa(message: Message, state: FSMContext):
    await state.update_data(aloqa=message.text)
    await message.answer(text=sherik_hudud)
    await state.set_state(RegistrationSherikKerak.hudud)


@dp.message(RegistrationSherikKerak.hudud)
async def get_hudud(message: Message, state: FSMContext):
    await state.update_data(hudud=message.text)
    await message.answer(text=sherik_narx)
    await state.set_state(RegistrationSherikKerak.narxi)


@dp.message(RegistrationSherikKerak.narxi)
async def get_narxi(message: Message, state: FSMContext):
    await state.update_data(narxi=message.text)
    await message.answer(text=sherik_kasb)
    await state.set_state(RegistrationSherikKerak.kasbi)


@dp.message(RegistrationSherikKerak.kasbi)
async def get_kasbi(message: Message, state: FSMContext):
    await state.update_data(kasbi=message.text)
    await message.answer(text=sherik_vaqti)
    await state.set_state(RegistrationSherikKerak.vaqti)


@dp.message(RegistrationSherikKerak.vaqti)
async def get_vaqti(message: Message, state: FSMContext):
    await state.update_data(vaqti=message.text)
    await message.answer(text=sherik_maqsad)
    await state.set_state(RegistrationSherikKerak.maqsad)


@dp.message(RegistrationSherikKerak.maqsad)
async def get_maqsad(message: Message, state: FSMContext):
    await state.update_data(maqsad=message.text)
    data = await state.get_data()
    text = f"""
🏅 Sherik: {data['name']}
📚 Texnologiya: {data['texnalogiya']}
🇺🇿 Telegram: @{message.from_user.username} ,{message.from_user.id}
📞 Aloqa: {data['aloqa']}
🌐 Hudud: {data['hudud']}
💰 Narxi: {data['narxi']}
👨🏻‍💻 Kasbi: {data['kasbi']}
🕰 Murojaat qilish vaqti: {data['vaqti']}
🔎 Maqsad: {data['maqsad']}
    """
    await message.answer(text=text, reply_markup=sherik_button())
    await state.clear()

#===========================================================================================
                #ish joyi kerak button

class RegistrationIshJoyKerak(StatesGroup):
    name = State()
    age = State()
    texnalogiya = State()
    aloqa = State()
    hudud = State()
    narxi = State()
    kasbi = State()
    vaqti = State()
    maqsad = State()

@dp.message(F.text == 'Ish joyi kerak')
async def ish_kerak(message: Message, state: FSMContext):
    await message.answer(text=ish_name)
    await state.set_state(RegistrationIshJoyKerak.name)

@dp.message(RegistrationIshJoyKerak.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text=ish_age)
    await state.set_state(RegistrationIshJoyKerak.age)


@dp.message(RegistrationIshJoyKerak.age)
async def get_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer(text=sherik_texnalogiya)
    await state.set_state(RegistrationIshJoyKerak.texnalogiya)


@dp.message(RegistrationIshJoyKerak.texnalogiya)
async def get_texnalogiy(message: Message, state: FSMContext):
    await state.update_data(texnalogiya=message.text)
    await message.answer(text=sherik_aloqa)
    await state.set_state(RegistrationIshJoyKerak.aloqa)


@dp.message(RegistrationIshJoyKerak.aloqa)
async def get_aloqa(message: Message, state: FSMContext):
    await state.update_data(aloqa=message.text)
    await message.answer(text=sherik_hudud)
    await state.set_state(RegistrationIshJoyKerak.hudud)


@dp.message(RegistrationIshJoyKerak.hudud)
async def get_hudud(message: Message, state: FSMContext):
    await state.update_data(hudud=message.text)
    await message.answer(text=sherik_narx)
    await state.set_state(RegistrationIshJoyKerak.narxi)


@dp.message(RegistrationIshJoyKerak.narxi)
async def get_narxi(message: Message, state: FSMContext):
    await state.update_data(narxi=message.text)
    await message.answer(text=sherik_kasb)
    await state.set_state(RegistrationIshJoyKerak.kasbi)


@dp.message(RegistrationIshJoyKerak.kasbi)
async def get_kasbi(message: Message, state: FSMContext):
    await state.update_data(kasbi=message.text)
    await message.answer(text=sherik_vaqti)
    await state.set_state(RegistrationIshJoyKerak.vaqti)


@dp.message(RegistrationIshJoyKerak.vaqti)
async def get_vaqti(message: Message, state: FSMContext):
    await state.update_data(vaqti=message.text)
    await message.answer(text=sherik_maqsad)
    await state.set_state(RegistrationSherikKerak.maqsad)


@dp.message(RegistrationIshJoyKerak.maqsad)
async def get_maqsad(message: Message, state: FSMContext):
    data = await state.get_data()
    text = f"""
Ish joyi kerak\n\n
👨‍💼 Xodim: {data['name']}
🕑 Yosh: {data['age']}
📚 Texnologiya: {data['texnalogiya']}
🇺🇿 Telegram: @{message.from_user.username} ,{ message.from_user.id}
📞 Aloqa: {data['aloqa']}
🌐 Hudud: {data['hudud']}
💰 Narxi: {data['narxi']}
👨🏻‍💻 Kasbi: {data['kasbi']}
🕰 Murojaat qilish vaqti: {data['vaqti']}
🔎 Maqsad: {data['maqsad']}
    """
    await message.answer(text=text, reply_markup=sherik_button())
    await state.clear()







async def main():
    print('working')
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())



