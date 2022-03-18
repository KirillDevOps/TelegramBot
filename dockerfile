FROM python3
COPY . /var/lib/telegram-bot-api
RUN apt-get install python3-pip
RUN pip install pytelegrambotapi
RUN python3 /var/lib/telegram-bot-api/bot.py
