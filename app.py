# Flask libraries
from flask import Flask, render_template, redirect, flash, url_for, session, request, abort
from flask_sqlalchemy import SQLAlchemy

# Configuratins and castom libraries
from config import CONFIG

# CONFIGURATION BLOCK
SECRET_KEY = CONFIG['FLASK_SECRET_KEY']

app = Flask (__name__)


# HEANDLERS BLOCK
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)