import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Токен бота из переменных окружения
TOKEN = os.environ.get('BOT_TOKEN')

def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("⭐️ Получить звёзды", callback_data='get_stars')],
        [InlineKeyboardButton("🎁 Магазин", callback_data='shop')],
        [InlineKeyboardButton("💎 Профиль", callback_data='profile')]
    ]
    
    update.message.reply_text(
        '🎮 Добро пожаловать в игровой бот!\n'
        'Здесь ты можешь получать звёзды и покупать улучшения!',
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    
    if query.data == 'get_stars':
        query.edit_message_text('🎉 Вам начислено 10 звёзд!')
    elif query.data == 'shop':
        query.edit_message_text('🛒 Магазин скоро откроется!')
    elif query.data == 'profile':
        query.edit_message_text('📊 Ваш профиль: 10 звёзд')

def main():
    if not TOKEN:
        logging.error("Токен бота не найден!")
        return
    
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    
    # Обработчики команд
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CallbackQueryHandler(button_handler))
    
    # Запуск бота
    updater.start_polling()
    logging.info("Бот запущен!")
    updater.idle()

if __name__ == '__main__':
    main()
