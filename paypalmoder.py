import logging
import random

import requests
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

kassaEuro = ['1']
euroFinder = ['€']
euroNoSymbol = ['0']
euroN = [0]
profits = [0]
recordEuro = [2108]


ppmoderAdd = ['Палки в процессе добавления! Ожидайте админов.']
channelPost = ['1']

publish_post_markup = types.InlineKeyboardMarkup()
topublish = types.InlineKeyboardButton('Опубликовать пост✅', callback_data='topublish')
tonopublish = types.InlineKeyboardButton('Удалить🚫', callback_data='tonopublish')
publish_post_markup.add(topublish, tonopublish)

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
        recordEuro[0] = message.text
        print(recordEuro[0])
        await message.delete()

@dp.message_handler()
async def kassa(message: types.Message):
    if message.chat.type == types.ChatType.PRIVATE:
        if message.from_user.username == 'blackebayer':
            channelPost[0] = message.text

            words = message.text.split()
            for word in words:
                for x in euroFinder:
                    if word.count(x):
                        print('Yep. "%s" contains characters from "%s" item.' % (word, x))
                        kassaEuro[0] = word
                        print(kassaEuro[0])
                        euroNoSymbol[0] = int(kassaEuro[0].replace('€',''))
                        print(euroNoSymbol[0])
                        profits[0] += 1

    if message.chat.type == types.ChatType.PRIVATE:
        if message.from_user.id == 1892827220:
            channelPost[0] = message.text

            words = message.text.split()
            for word in words:
                for x in euroFinder:
                    if word.count(x):
                        print('Yep. "%s" contains characters from "%s" item.' % (word, x))
                        kassaEuro[0] = word
                        print(kassaEuro[0])
                        euroNoSymbol[0] = int(kassaEuro[0].replace('€',''))
                        print(euroNoSymbol[0])
                        profits[0] += 1

            await message.delete()

            if channelPost != '1':
                await message.answer(channelPost[0], reply_markup=publish_post_markup)

    if 'касса' in message.text:
        print(message.chat.id)
        euroN[0] += int(euroNoSymbol[0])
        if int(euroN[0]) > int(recordEuro[0]):
            recordEuro[0] = int(euroN[0])
        await message.answer('🍀Статистика за сегодня:🍀\n'
                             '🐘Профитов: '+str(profits[0])+'🐘\n'
                             '💸На сумму: '+str(euroN[0])+'€💸\n'
                             '❗️Рекорд: '+str(recordEuro[0])+'€❗️\n')
        euroN[0] = 0

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


@dp.callback_query_handler(lambda c: c.data == 'topublish')
async def self(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
                              text='🍀Пост успешно опубликован!🍀',reply_markup=None)

    requests.get('https://api.telegram.org/bot{}/sendMessage'.format(TOKEN), params=dict(
        chat_id=-1001443483878, text=channelPost[0]))

    requests.get('https://api.telegram.org/bot{}/sendMessage'.format(TOKEN), params=dict(
        chat_id=-1001375668801, text='⚡️NEW PROFIT⚡️\n'
                             '💸На сумму: '+str(euroNoSymbol[0])+'€💸\n'
                             'Дополнительная информация\n'
                             'в канале выплат!'))


@dp.callback_query_handler(lambda c: c.data == 'tonopublish')
async def self(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
                              text='🚫Пост успешно удален!🚫',reply_markup=None)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
