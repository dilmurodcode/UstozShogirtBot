import asyncio, re
from typing import Callable, Any, Awaitable, Dict

import aiogram
from aiogram import Dispatcher, Bot, F
from aiogram.filters import  CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from text import sherik_name, sherik_texnalogiya, sherik_aloqa, sherik_hudud, sherik_narx, sherik_vaqti, sherik_maqsad, sherik_kasb
from text import ish_name, ish_age, hodim_idora,ustoz_kerakk,shogirt_kerakk

bot = Bot(token='7723912045:AAEKwGAvHK62OP9heeGC53JW5_9sp77p-ig')
dp = Dispatcher()

class StateClearMiddleware(aiogram.BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message | CallbackQuery | FSMContext,
            data: Dict[str, Any]
    ) -> Any:
        state: FSMContext = data.get("state")
        if isinstance(event, Message) and state:
            if event.text in ["Sherik kerak", "Ish joyi kerak"]:
                await state.clear()
                await state.clear()
        return await handler(event, data)

@dp.message(CommandStart())
async def catch_command(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Sherik kerak'), KeyboardButton(text='Ish joyi kerak')],
            [KeyboardButton(text='Hodim kerak'), KeyboardButton(text='Ustoz kerak')],
            [KeyboardButton(text='Shogirt kerak')]
        ], resize_keyboard=True
    )
    await message.answer(
        text=f"Assalom alaykum {message.from_user.full_name} @{message.from_user.username} UstozShogird kanalining rasmiy botiga xush kelibsiz!\n\n/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!",
        reply_markup=keyboard)


def sherik_button():
    buttons = [
        [KeyboardButton(text="Ha"), KeyboardButton(text="Yo'q")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)


# ==============================================================================================
# Sherik kerak button

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
    validate_phone_number_pattern = "^\\+?998[0-9]{9}$"
    if re.match(validate_phone_number_pattern, message.text) != None:
        await state.update_data(aloqa=message.text)
        await message.answer(text=sherik_hudud)
        await state.set_state(RegistrationSherikKerak.hudud)
    else:
        await message.answer(text='Siz nomerni xato kiritdingiz\n\nQayta kiriting:')
        await state.set_state(RegistrationSherikKerak.aloqa)


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
    await state.update_data(maqsad=message.text, type='friend')
    data = await state.get_data()
    if data:
        global info
        info = data
        text = f"""
🏅 Sherik: {data['name']}
📚 Texnologiya: {data['texnalogiya']}
🇺🇿 Telegram: @{message.from_user.username}
📞 Aloqa: {data['aloqa']}
🌐 Hudud: {data['hudud']}
💰 Narxi: {data['narxi']}
👨🏻‍💻 Kasbi: {data['kasbi']}
🕰 Murojaat qilish vaqti: {data['vaqti']}
🔎 Maqsad: {data['maqsad']}
    """
        await message.answer(text=text, reply_markup=sherik_button())
    await state.clear()

# ===========================================================================================
# ish joyi kerak button

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
    if not message.text.isdigit():
        await message.answer(text='Iltimos son kiriting: ')
    else:
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
    validate_phone_number_pattern = "^\\+?998[0-9]{9}$"
    if re.match(validate_phone_number_pattern, message.text) != None:
        await state.update_data(aloqa=message.text)
        await message.answer(text=sherik_hudud)
        await state.set_state(RegistrationIshJoyKerak.hudud)
    else:
        await message.answer(text='Siz nomerni xato kiritdingiz\n\nQayta kiriting:')
        await state.set_state(RegistrationIshJoyKerak.aloqa)


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
    await state.set_state(RegistrationIshJoyKerak.maqsad)


@dp.message(RegistrationIshJoyKerak.maqsad)
async def get_maqsad(message: Message, state: FSMContext):
    await state.update_data(maqsad=message.text, type='work')
    data = await state.get_data()
    if data:
        global info
        info = data
        text = f"""
Ish joyi kerak\n\n
👨‍💼 Xodim: {data['name']}
🕑 Yosh: {data['age']}
📚 Texnologiya: {data['texnalogiya']}
🇺🇿 Telegram: @{message.from_user.username}
📞 Aloqa: {data['aloqa']}
🌐 Hudud: {data['hudud']}
💰 Narxi: {data['narxi']}
👨🏻‍💻 Kasbi: {data['kasbi']}
🕰 Murojaat qilish vaqti: {data['vaqti'] }
🔎 Maqsad: {data['maqsad']}
            """
        await message.answer(text=text, reply_markup=sherik_button())
    await state.clear()

@dp.message(F.text == "Yo'q")
async def yoq(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Sherik kerak'), KeyboardButton(text='Ish joyi kerak')],
            [KeyboardButton(text='Hodim kerak'), KeyboardButton(text='Ustoz kerak')],
            [KeyboardButton(text='Shogirt kerak')]
        ], resize_keyboard=True
    )
    await message.answer('Ariznagiz bekor qilindi', reply_markup=keyboard)

@dp.message(F.text == "Ha")
async def xa(message: Message, state: FSMContext):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Sherik kerak'), KeyboardButton(text='Ish joyi kerak')],
            [KeyboardButton(text='Hodim kerak'), KeyboardButton(text='Ustoz kerak')],
            [KeyboardButton(text='Shogirt kerak')]
        ], resize_keyboard=True
    )
    data = info
    if data and data['type'] == 'work':
        text = f"""
Ish joyi kerak\n\n
👨‍💼 Xodim: {data['name'] }
🕑 Yosh: {data['age']}
📚 Texnologiya: {data['texnalogiya']}
🇺🇿 Telegram: @{message.from_user.username}
📞 Aloqa: {data['aloqa']}
🌐 Hudud: {data['hudud']}
💰 Narxi: {data['narxi']}
👨🏻‍💻 Kasbi: {data['kasbi']}
🕰 Murojaat qilish vaqti: {data['vaqti']}
🔎 Maqsad: {data['maqsad']}
        """
        await bot.send_message(chat_id=8016755758, text=text)
        await bot.send_message(chat_id='@aiogramstart', text=text)

    if data and data['type'] == 'friend':
        text = f"""
Sherik kerak\n\n
👨‍💼 Xodim: {data['name']}
📚 Texnologiya: {data['texnalogiya']}
🇺🇿 Telegram: @{message.from_user.username}
📞 Aloqa: {data['aloqa']}
🌐 Hudud: {data['hudud']}
💰 Narxi: {data['narxi']}
👨🏻‍💻 Kasbi: {data['kasbi']}
🕰 Murojaat qilish vaqti: {data['vaqti']}
🔎 Maqsad: {data['maqsad']}
            """
        await bot.send_message(chat_id=8016755758, text=text)
        await bot.send_message(chat_id='@aiogramstart', text=text)

    data = info
    if data and data['type'] == 'hodim':
        text = f"""
Hodim kerak:\n
🏢 Idora: {data['idora']}
📚 Texnologiya: {data['texnalogiya']}
🇺🇿 Telegram: @{message.from_user.username}
📞 Aloqa: {data['aloqa']}
🌐 Hudud: {data['hudud']}
✍️ Mas'ul: {data['masul']}
🕰 Murojaat vaqti: {data['murojat_vaqti']}
🕰 Ish vaqti: {data['ish_vaqti']}
💰 Maosh: {data['moash']}
‼️ Qo`shimcha: {data['qoshimcha']}

        #ishJoyi
                """
        await bot.send_message(chat_id=8016755758, text=text)
        await bot.send_message(chat_id='@aiogramstart', text=text)

    data = info
    if data and data['type'] == 'ustoz':
        text = f"""
Ustoz kerak:\n\n
🎓 Ustoz: {data['shogirt']}
🕑 Yosh: {data['yosh']}
📚 Texnologiya: {data['texnalogiya']}
🇺🇿 Telegram: @{message.from_user.username}
📞 Aloqa: {data['aloqa']}
🌐 Hudud: {data['hudud']}
💰 Narxi: {data['narx']}
🏻‍💻 Kasbi: {data['kasbi']}
🕰 Murojaat qilish vaqti: {data['murojat_vaqti']}
🔎 Maqsad: {data['maqsad']}
                    """
        await bot.send_message(chat_id=8016755758, text=text)
        await bot.send_message(chat_id='@aiogramstart', text=text)

    data = info
    if data and data['type'] == 'Dost':
        text = f"""
Shogirt kerak:\n\n
🎓 Shogird: {data['shogirt']}
🕑 Yosh: {data['yosh']}
📚 Texnologiya: {data['texnalogiya']}
🇺🇿 Telegram: @{message.from_user.username}
📞 Aloqa: {data['aloqa']}
🌐 Hudud: {data['hudud']}
💰 Narxi: {data['narx']}
🏻‍💻 Kasbi: {data['kasbi']}
🕰 Murojaat qilish vaqti: {data['murojat_vaqti']}
🔎 Maqsad: {data['maqsad']}
                            """
        await bot.send_message(chat_id=8016755758, text=text)
        await bot.send_message(chat_id='@aiogramstart', text=text)


    await message.answer('Arizangiz adminga yuborildi', reply_markup=keyboard)
    await state.clear()

#==============================================================================================

class RegistrationHodimKerak(StatesGroup):
    idora = State()
    texnalogiya = State()
    aloqa = State()
    hudud = State()
    masul = State()
    murojat_vaqti = State()
    ish_vaqti = State()
    moash = State()
    qoshimcha = State()


@dp.message(F.text == 'Hodim kerak')
async def hodim_kerak(message: Message, state: FSMContext):
    await message.answer(text=hodim_idora)
    await state.set_state(RegistrationHodimKerak.idora)
    await message.answer(text='🎓 Idora nomi?')


@dp.message(RegistrationHodimKerak.idora)
async def name_idora(message: Message, state: FSMContext):
    await state.update_data(idora=message.text)
    await message.answer(text=sherik_texnalogiya)
    await state.set_state(RegistrationHodimKerak.texnalogiya)


@dp.message(RegistrationHodimKerak.texnalogiya)
async def get_texnalogiya(message: Message, state: FSMContext):
    await state.update_data(texnalogiya=message.text)
    await message.answer(text=sherik_aloqa)
    await state.set_state(RegistrationHodimKerak.aloqa)


@dp.message(RegistrationHodimKerak.aloqa)
async def get_aloqa(message: Message, state: FSMContext):
    validate_phone_number_pattern = "^\\+?998[0-9]{9}$"
    if re.match(validate_phone_number_pattern, message.text) != None:
        await state.update_data(aloqa=message.text)
        await message.answer(text=sherik_hudud)
        await state.set_state(RegistrationHodimKerak.hudud)
    else:
        await message.answer(text='Siz nomerni xato kiritdingiz\n\nQayta kiriting:')
        await state.set_state(RegistrationIshJoyKerak.aloqa)


@dp.message(RegistrationHodimKerak.hudud)
async def get_hudud(message: Message, state: FSMContext):
    await state.update_data(hudud=message.text)
    await message.answer(text="✍️Mas'ul ism sharifi?")
    await state.set_state(RegistrationHodimKerak.masul)


@dp.message(RegistrationHodimKerak.masul)
async def get_masul(message: Message, state: FSMContext):
    await state.update_data(masul=message.text)
    await message.answer(text=sherik_vaqti)
    await state.set_state(RegistrationHodimKerak.murojat_vaqti)

@dp.message(RegistrationHodimKerak.murojat_vaqti)
async def get_murojat_vaqti(message: Message, state: FSMContext):
    await state.update_data(murojat_vaqti=message.text)
    await message.answer(text="🕰 Ish vaqtini kiriting?")
    await state.set_state(RegistrationHodimKerak.ish_vaqti)

@dp.message(RegistrationHodimKerak.ish_vaqti)
async def get_ish_vaqti(message: Message, state: FSMContext):
    await state.update_data(ish_vaqti=message.text)
    await message.answer(text="💰 Maoshni kiriting?")
    await state.set_state(RegistrationHodimKerak.moash)

@dp.message(RegistrationHodimKerak.moash)
async def get_moash(message: Message, state: FSMContext):
    await state.update_data(moash=message.text)
    await message.answer(text="‼️ Qo`shimcha ma`lumotlar?")
    await state.set_state(RegistrationHodimKerak.qoshimcha)


@dp.message(RegistrationHodimKerak.qoshimcha)
async def get_qoshimcha(message: Message, state: FSMContext):
    await state.update_data(qoshimcha=message.text, type='hodim')
    data = await state.get_data()
    if data:
        global info
        info = data
        text = f"""
Hodim kerak:\n
🏢 Idora: {data['idora']}
📚 Texnologiya: {data['texnalogiya']}
🇺🇿 Telegram: @{message.from_user.username}
📞 Aloqa: {data['aloqa']}
🌐 Hudud: {data['hudud']}
✍️ Mas'ul: {data['masul']}
🕰 Murojaat vaqti: {data['murojat_vaqti']}
🕰 Ish vaqti: {data['ish_vaqti']}
💰 Maosh: {data['moash']}
‼️ Qo`shimcha: {data['qoshimcha']}

#ishJoyi
        """
        await message.answer(text=text, reply_markup=sherik_button())
        await message.answer(text="Barcha ma'lumotlar to'g'rimi?")

    await state.clear()

#=====================================================================================

class RegistrationUstozKerak(StatesGroup):
    shogirt = State()
    yosh = State()
    texnalogiya = State()
    aloqa = State()
    hudud = State()
    narx = State()
    kasbi = State()
    murojat_vaqti = State()
    maqsad = State()

@dp.message(F.text == 'Ustoz kerak')
async def ustoz_kerak(message: Message, state: FSMContext):
    await state.update_data(shogirt=message.text)
    await message.answer(text=ustoz_kerakk)
    await state.set_state(RegistrationUstozKerak.shogirt)
    await message.answer(text='Ism, familiyangizni kiriting?')

@dp.message(RegistrationUstozKerak.shogirt)
async def get_shogirt(message: Message, state: FSMContext):
    await state.update_data(texnalogiya=message.text)
    await message.answer(text=ish_age)
    await state.set_state(RegistrationUstozKerak.yosh)


@dp.message(RegistrationUstozKerak.yosh)
async def get_yosh(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer(text='Iltimos son kiriting: ')
    else:
        await state.update_data(yosh=message.text)
        await message.answer(text=sherik_texnalogiya)
        await state.set_state(RegistrationUstozKerak.texnalogiya)


@dp.message(RegistrationUstozKerak.texnalogiya)
async def get_texnalogiya(message: Message, state: FSMContext):
    await state.update_data(texnalogiya=message.text)
    await message.answer(text=sherik_aloqa)
    await state.set_state(RegistrationUstozKerak.aloqa)


@dp.message(RegistrationUstozKerak.aloqa)
async def get_aloqa(message: Message, state: FSMContext):
    validate_phone_number_pattern = "^\\+?998[0-9]{9}$"
    if re.match(validate_phone_number_pattern, message.text) != None:
        await state.update_data(aloqa=message.text)
        await message.answer(text=sherik_hudud)
        await state.set_state(RegistrationUstozKerak.hudud)
    else:
        await message.answer(text='Siz nomerni xato kiritdingiz\n\nQayta kiriting:')
        await state.set_state(RegistrationUstozKerak.aloqa)


@dp.message(RegistrationUstozKerak.hudud)
async def get_hudud(message: Message, state: FSMContext):
    await state.update_data(hudud=message.text)
    await message.answer(text=sherik_narx)
    await state.set_state(RegistrationUstozKerak.narx)

@dp.message(RegistrationUstozKerak.narx)
async def get_narx(message: Message, state: FSMContext):
    await state.update_data(narx=message.text)
    await message.answer(text=sherik_kasb)
    await state.set_state(RegistrationUstozKerak.kasbi)


@dp.message(RegistrationUstozKerak.kasbi)
async def get_kasbi(message: Message, state: FSMContext):
    await state.update_data(kasbi=message.text)
    await message.answer(text=sherik_vaqti)
    await state.set_state(RegistrationUstozKerak.murojat_vaqti)


@dp.message(RegistrationUstozKerak.murojat_vaqti)
async def get_murojat_vaqti(message: Message, state: FSMContext):
    await state.update_data(murojat_vaqti=message.text)
    await message.answer(text=sherik_maqsad)
    await state.set_state(RegistrationUstozKerak.maqsad)


@dp.message(RegistrationUstozKerak.maqsad)
async def get_maqsad(message: Message, state: FSMContext):
    await state.update_data(maqsad=message.text, type='ustoz')
    data = await state.get_data()
    if data:
        global info
        info = data
        text = f"""
Ustoz kerak:\n\n
🎓 Ustoz: {data['shogirt']}
🕑 Yosh: {data['yosh']}
📚 Texnologiya: {data['texnalogiya']}
🇺🇿 Telegram: @{message.from_user.username}
📞 Aloqa: {data['aloqa']}
🌐 Hudud: {data['hudud']}
💰 Narxi: {data['narx']}
🏻‍💻 Kasbi: {data['kasbi']}
🕰 Murojaat qilish vaqti: {data['murojat_vaqti'] }
🔎 Maqsad: {data['maqsad']}
            """
        await message.answer(text=text, reply_markup=sherik_button())
        await  message.answer(text="Barcha ma'lumotlar to'g'rimi?")
    await state.clear()

#==================================================================================================


class RegistrationShogirtKerak(StatesGroup):
    shogirt = State()
    yosh = State()
    texnalogiya = State()
    aloqa = State()
    hudud = State()
    narx = State()
    kasbi = State()
    murojat_vaqti = State()
    maqsad = State()

@dp.message(F.text == 'Shogirt kerak')
async def ustoz_kerak(message: Message, state: FSMContext):
    await state.update_data(shogirt=message.text)
    await message.answer(text=shogirt_kerakk)
    await state.set_state(RegistrationShogirtKerak.shogirt)
    await message.answer(text='Ism, familiyangizni kiriting?')

@dp.message(RegistrationShogirtKerak.shogirt)
async def get_shogirt(message: Message, state: FSMContext):
    await state.update_data(texnalogiya=message.text)
    await message.answer(text=ish_age)
    await state.set_state(RegistrationShogirtKerak.yosh)


@dp.message(RegistrationShogirtKerak.yosh)
async def get_yosh(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer(text='Iltimos son kiriting: ')
    else:
        await state.update_data(yosh=message.text)
        await message.answer(text=sherik_texnalogiya)
        await state.set_state(RegistrationShogirtKerak.texnalogiya)


@dp.message(RegistrationShogirtKerak.texnalogiya)
async def get_texnalogiya(message: Message, state: FSMContext):
    await state.update_data(texnalogiya=message.text)
    await message.answer(text=sherik_aloqa)
    await state.set_state(RegistrationShogirtKerak.aloqa)


@dp.message(RegistrationShogirtKerak.aloqa)
async def get_aloqa(message: Message, state: FSMContext):
    validate_phone_number_pattern = "^\\+?998[0-9]{9}$"
    if re.match(validate_phone_number_pattern, message.text) != None:
        await state.update_data(aloqa=message.text)
        await message.answer(text=sherik_hudud)
        await state.set_state(RegistrationShogirtKerak.hudud)
    else:
        await message.answer(text='Siz nomerni xato kiritdingiz\n\nQayta kiriting:')
        await state.set_state(RegistrationShogirtKerak.aloqa)


@dp.message(RegistrationShogirtKerak.hudud)
async def get_hudud(message: Message, state: FSMContext):
    await state.update_data(hudud=message.text)
    await message.answer(text=sherik_narx)
    await state.set_state(RegistrationShogirtKerak.narx)

@dp.message(RegistrationShogirtKerak.narx)
async def get_narx(message: Message, state: FSMContext):
    await state.update_data(narx=message.text)
    await message.answer(text=sherik_kasb)
    await state.set_state(RegistrationShogirtKerak.kasbi)


@dp.message(RegistrationShogirtKerak.kasbi)
async def get_kasbi(message: Message, state: FSMContext):
    await state.update_data(kasbi=message.text)
    await message.answer(text=sherik_vaqti)
    await state.set_state(RegistrationShogirtKerak.murojat_vaqti)


@dp.message(RegistrationShogirtKerak.murojat_vaqti)
async def get_murojat_vaqti(message: Message, state: FSMContext):
    await state.update_data(murojat_vaqti=message.text)
    await message.answer(text=sherik_maqsad)
    await state.set_state(RegistrationShogirtKerak.maqsad)


@dp.message(RegistrationShogirtKerak.maqsad)
async def get_maqsad(message: Message, state: FSMContext):
    await state.update_data(maqsad=message.text, type='Dost')
    data = await state.get_data()
    if data:
        global info
        info = data
        text = f"""
Shogirt kerak:\n\n
🎓 Shogird: {data['shogirt']}
🕑 Yosh: {data['yosh']}
📚 Texnologiya: {data['texnalogiya']}
🇺🇿 Telegram: @{message.from_user.username}
📞 Aloqa: {data['aloqa']}
🌐 Hudud: {data['hudud']}
💰 Narxi: {data['narx']}
🏻‍💻 Kasbi: {data['kasbi']}
🕰 Murojaat qilish vaqti: {data['murojat_vaqti'] }
🔎 Maqsad: {data['maqsad']}
            """
        await message.answer(text=text, reply_markup=sherik_button())
        await  message.answer(text="Barcha ma'lumotlar to'g'rimi?")
    await state.clear()


async def main():
    dp.message.middleware(StateClearMiddleware())
    dp.callback_query.middleware(StateClearMiddleware())
    print('working')
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
