import telebot
import logging
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

TOKEN = '1857297167:AAE7TDJ7l7dCw48Y_jbXtkB_19qtzvsiwEw'
bot = Bot(TOKEN)
dp = Dispatcher(bot)

text = '[💸Канал выплат💸](https://t.me/joinchat/ZJWZj5mCEog4NmQy)'
toolID = [
    '1',
    '2',
    '3'
]

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


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
