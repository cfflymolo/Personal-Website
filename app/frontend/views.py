from flask import render_template
from . import frontend


@frontend.route('/')
def home():
    return render_template('index.html')
