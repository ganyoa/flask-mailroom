import os

from flask import Flask, render_template, request, redirect, url_for
from model import Donor, Donation
import peewee

app = Flask(__name__)


@app.route('/')
def home():
    return redirect(url_for('donations'))


@app.route('/donations')
def donations():
 return render_template('donations.jinja2', all_donations=Donation.select())


@app.route('/add', methods=['GET', 'POST'])
def add():
    registered_donors=Donor.select()
    if request.method == 'POST':
        try:
            name_check = Donor.get(Donor.name == (request.form['name'])).id
            Donation(donor=name_check, value=request.form['number']).save()
            return redirect(url_for('donations'))
        except peewee.DoesNotExist:
            return render_template('add.jinja2', error="Donor name is not registered.")
    else:
        return render_template('add.jinja2')


if __name__ == "__main__":
 port = int(os.environ.get("PORT", 6738))
 app.run(host='0.0.0.0', port=port)

