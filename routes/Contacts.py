from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.contact import Contact
from app import db

contacts = Blueprint('contacts', __name__)

@contacts.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)

@contacts.route('/about')
def about():
    return render_template('about.html')


@contacts.route('/add', methods=['POST'])
def add_contact():
    print(request.form['name'])
    print(request.form['email'])
    print(request.form['phone'])
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    new_contact = Contact(name, email, phone)
    print(new_contact)
    db.session.add(new_contact)
    db.session.commit()
    flash('Contact added')
    return redirect(url_for('contacts.index'))

@contacts.route('update/int<id>', methods=['GET', 'POST'])
def update_contact(id):
    if request.method == 'POST':
        contact = Contact.query.get(id)
        contact.name = request.form['name']
        contact.email = request.form['email']
        contact.phone = request.form['phone']
        flash('Contact updated')
        db.session.commit()
        return redirect(url_for('contacts.index'))
    else:
        contact = Contact.query.get(id)
        return render_template('update.html', contact=contact)

@contacts.route('delete/<id>')
def delete_contact(id):
    contact = Contact.query.get(id)
    print(contact)
    if contact:
        db.session.delete(contact)
        db.session.commit()
        flash('Contact deleted')
        print('Contact deleted')
        return redirect(url_for('contacts.index'))
    else:
        print('Contact not found')
        return redirect(url_for('contacts.index'))