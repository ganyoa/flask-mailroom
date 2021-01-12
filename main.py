import os

from flask import Flask, render_template, request, redirect, url_for
from model import TotalDonations

app = Flask(__name__)


@app.route('/')
def home():
    return redirect(url_for('donations'))


@app.route('/donations')
def donations():
 return render_template('donations.jinja2', tasks=TotalDonations.select())


@app.route('/add', methods=['GET', 'POST'])
def add():

    if request.method == 'POST':
        task = TotalDonations(donor_name=request.form['name'], donation_amount=request.form['number'])
        task.save()

        return redirect(url_for('donations'))
    else:
        return render_template('add.jinja2')


if __name__ == "__main__":
 port = int(os.environ.get("PORT", 5000))
 app.run(host='0.0.0.0', port=port)

'''
add.jinja2


'''