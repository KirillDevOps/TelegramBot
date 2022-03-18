FROM pyTelegramBotAPI
COPY . /var/lib/telegram-bot-api
RUN python3 /var/lib/telegram-bot-api/bot.py
