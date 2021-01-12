import os

from peewee import Model, CharField, IntegerField
from playhouse.db_url import connect


db = connect(os.environ.get('DATABASE_URL', 'sqlite:///my_mailroom_db.db'))

class TotalDonations(Model): # my_database.db table name
    donor_name = CharField(max_length=255, unique=True)
    donation_amount = IntegerField()

    class Meta:
        database = db