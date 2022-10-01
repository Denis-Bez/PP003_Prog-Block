# Flask libraries
from flask import Flask, render_template, redirect, flash, url_for, session, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

import time

# Configuratins and castom libraries
from config import CONFIG
from site_elements import menu

# CONFIGURATION BLOCK
SECRET_KEY = CONFIG['FLASK_SECRET_KEY']

application = Flask (__name__)

application.config["MAIL_DEFAULT_SENDER"] = CONFIG["MAIL_DEFAULT_SENDER"]
application.config["MAIL_PASSWORD"] = CONFIG["MAIL_PASSWORD"]
application.config["MAIL_PORT"] = 465
application.config["MAIL_SERVER"] = "mail.worldcadabra.com"
application.config["MAIL_USE_TLS"] = False
application.config["MAIL_USE_SSL"] = True
application.config["MAIL_USERNAME"] = CONFIG["MAIL_USERNAME"]
mail = Mail(application)

# HEANDLERS BLOCK
@application.route('/', methods=["POST", "GET"])
async def index():
    if request.method == "POST":
        await test()
    return render_template('index.html', title="Проект Worldcadabra - для эмигрантов и путешественников", menu=menu)


async def test():
    try:
        print('Script was started!')
        i = 0
        msg = Message("Срабатывание скрипта на сайте", recipients=["v417459@yandex.ru"])
        while True:
            i += 1
            msg.body = (f"Сработал скрипт {i}-ая итерация. Следующее сообщение через 10 минут")
            mail.send(msg)
            time.sleep(600)
    except Exception as e:
        msg = Message("Ошибка скрипта на сайте", recipients=["v417459@yandex.ru"])
        msg.body = (f"Ошибка {e}")
        mail.send(msg)
    

if __name__ == "__main__":
    application.run(debug=True)