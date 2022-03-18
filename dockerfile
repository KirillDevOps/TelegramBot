FROM pypi/pytelegrambotapi
COPY . /var/lib/telegram-bot-api
RUN python3 /var/lib/telegram-bot-api/bot.py
