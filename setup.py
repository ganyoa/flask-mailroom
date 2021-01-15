import random
from model import db, Donor, Donation

db.connect()
db.drop_tables([Donor, Donation])
db.create_tables([Donor, Donation])

alice = Donor(name="Alice")
alice.save()

bob = Donor(name="Bob")
bob.save()

charlie = Donor(name="Charlie")
charlie.save()

donors = [alice, bob, charlie]

for x in range(30):
    Donation(donor=random.choice(donors), value=random.randint(100, 10000)).save()


'''previous table fields
TotalDonations(donor_name="Alice", donation_amount=1263).save()
TotalDonations(donor_name="Bob", donation_amount=742).save()
TotalDonations(donor_name="Charlie", donation_amount=1542).save()
'''

