from flask import (Blueprint, render_template)
from . import admin



@admin.route('/')
def dashboard():
    return 'dashboard'


@admin.route('/login')
def login():
    return render_template('login.html')


@admin.route('/register')
def register():
    return render_template('register.html')