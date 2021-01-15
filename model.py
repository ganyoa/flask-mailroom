import os

from peewee import Model, CharField, IntegerField, ForeignKeyField
from playhouse.db_url import connect


db = connect(os.environ.get('DATABASE_URL', 'sqlite:///my_mailroom_db.db'))

class Donor(Model):
    name = CharField(max_length=255, unique=True)

    class Meta:
        database = db

class Donation(Model):
    value = IntegerField()
    donor = ForeignKeyField(Donor, backref='donations')

    class Meta:
        database = db

'''previous table
class TotalDonations(Model): # my_database.db table name
    donor_name = CharField(max_length=255)
    donation_amount = IntegerField()

    class Meta:
        database = db
'''