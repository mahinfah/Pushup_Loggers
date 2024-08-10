from flask import Blueprint, render_template
 
 
auth = Blueprint('auth',__name__)


@auth.route('signup')
def signup():
    return "this is my"


@auth.route('Login')
def login():
    return "this is my login page"



@auth.route('logout')
def logout():
    return "this is my logout page"