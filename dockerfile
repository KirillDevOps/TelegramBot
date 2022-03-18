FROM pypi/pytelegrambotapi
COPY . /var/lib/telegram-bot-api
RUN pip install python-telegram-bot --upgrade
RUN python3 /var/lib/telegram-bot-api/bot.py
