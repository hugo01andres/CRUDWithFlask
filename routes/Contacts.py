from flask import Blueprint, render_template, request, redirect, url_for, flash


contacts = Blueprint('contacts', __name__)

@contacts.route('/')
def home():
    return render_template('index.html')

@contacts.route('/about')
def about():
    return render_template('about.html')


@contacts.route('/add')
def add_contact():
    return 'Add new contact'

@contacts.route('update')
def update_contact():
    return 'Update contact'

@contacts.route('delete')
def delete_contact():
    return 'Delete contact'