import telebot
import logging
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

TOKEN = '1857297167:AAE7TDJ7l7dCw48Y_jbXtkB_19qtzvsiwEw'
bot = Bot(TOKEN)
dp = Dispatcher(bot)

text = '[💸Канал выплат💸](https://t.me/joinchat/ZJWZj5mCEog4NmQy)'

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

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)