from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app.models import *

def config_views(app):
  
  @app.get('/')
  def index():
    return render_template('index.html')

  @app.post('/login')
  def login_view():
    login_data = request.form
    email = login_data['email']
    password = login_data['password']
    next_page = login_data['next']

    user_query = User.quey.filter(User.email == email).first()

    if user_query is None or not user_query.check_hash(password):
      flash('Usuário ou senha incorretos')
      return redirect(url_for('login', next=next_page))
    
    login_user(user_query, remember=True)