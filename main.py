from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'hi everyone'


@main.route('/profile')
def index():
    return "Profile here"