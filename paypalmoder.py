import logging
import random
from aiogram import Bot, Dispatcher, executor, types

from filters import IsAdminFilter
import telebot
from aiogram.utils import deep_linking

logging.basicConfig(level=logging.INFO)

TOKEN = '1857297167:AAE7TDJ7l7dCw48Y_jbXtkB_19qtzvsiwEw'
bot = Bot(TOKEN)
dp = Dispatcher(bot)
GROUP_ID = 564021126

dp.filters_factory.bind(IsAdminFilter)

text = '[💸Канал выплат💸](https://t.me/joinchat/ZJWZj5mCEog4NmQy)'
toolID = [
    'None',
    'None',
    '3'
]
kasima = [
    'Чепуха',
    'Лучше бы молчал...',
    'Ну и бред',
    'Лучше бы воркал...',
    'Ничего умнее от тебя не ожидал услышать...',
    'Из нас двоих ботом кажешься ты',
    'Не пиши сюда больше пж'
]
victimID = [
    '1'
]
ppmoderAdd = ['1']


markup_inline_choice = types.InlineKeyboardMarkup()
addPP = types.InlineKeyboardButton('Добавить PP', callback_data='add')
markup_inline_choice.add(addPP)

markup_pp = types.InlineKeyboardMarkup()
added = types.InlineKeyboardButton('PP добавлены', callback_data='added')
markup_pp.add(added)


@dp.message_handler(content_types=['new_chat_members'])
async def users_joined(message: types.Message):
    await message.answer('🍀К чату присоединился воркер!🍀'
                         '\nПрофиль: @{0}\n'
                         '\n'
                         '❗️Вся информация в закрепленных \nсообщениях.\n'
                         '\n'
                         '🔫Хорошего дня и удачного скама!'.format(message.from_user.username))
    await message.delete()
    await message.answer(text, parse_mode='Markdown')


@dp.message_handler(is_admin=True, commands=["adminPanel"])
async def cmd_start(message: types.Message):
    await message.delete()
    await message.answer('♣️Админ: @{0}♣️\n'
                         '      Выберите действие:'.format(message.from_user.username),
                         reply_markup=markup_inline_choice)

@dp.message_handler(commands=["available_pp"])
async def avaliable(message: types.Message):
    await message.answer('🍀Доступные палки:🍀\n'
                         +ppmoderAdd[0])


@dp.callback_query_handler(lambda c: c.data == 'add')
async def self(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
                              text='🍀Введите доступные🍀\n'
                                   '      палки!\n', reply_markup=markup_pp)


@dp.message_handler(regexp='🐘')
async def personal(message: types.Message):
    if message.from_user.id == 1892827220:
        toolID[0] = message.text
        print(toolID[0])
        await message.delete()


@dp.message_handler(regexp='💸')
async def personal(message: types.Message):
    if message.from_user.id == 1892827220:
        toolID[1] = message.text
        print(toolID[1])
        await message.delete()


@dp.message_handler(regexp='❗️')
async def personal(message: types.Message):
    if message.from_user.id == 1892827220:
        toolID[2] = message.text
        print(toolID[2])
        await message.delete()


@dp.message_handler()
async def kassa(message: types.Message):
    if 'касса' in message.text:
        await message.answer('🍀Статистика за сегодня:🍀\n'
                             '🐘Профитов: '+toolID[0]+'\n'
                             '💸На сумму: '+toolID[1]+'\n'
                             '❗️Рекорд: '+toolID[2]+'\n')

    if 'заряду' in message.text:
        await message.answer_sticker('CAACAgIAAxkBAAECaFBgwSqxwBgXUxDQwb6P0GcO3sTkygACRQADZtYKO1dsr_MdF_EUHwQ')

    if message.from_user.id == 1892827220:
        if message.from_user.last_name == 'Українаа':
            victimID[0] = message.text
            print(victimID[0])
            await message.delete()

    if message.from_user.username == victimID[0]:
        await message.reply(random.choice(kasima))

    if message.from_user.username == '09370007390':
        if '‼️' in message.text:
            ppmoderAdd[0] = message.text
            await message.delete()

    if message.from_user.username == 'ucyberpolice':
        if '‼️' in message.text:
            ppmoderAdd[0] = message.text
            await message.delete()

    if message.from_user.username == 'blackebayer':
        if '‼️' in message.text:
            ppmoderAdd[0] = message.text
            await message.delete()


@dp.callback_query_handler(lambda c: c.data == 'added')
async def self(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
                              text='🍀Палки сохранены!🍀\n'
                                   '       /available_pp',reply_markup=None)

#if message.chat.type != types.ChatType.PRIVATE:


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
