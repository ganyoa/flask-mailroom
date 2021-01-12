from model import db, TotalDonations

db.connect()
db.drop_tables([TotalDonations])
db.create_tables([TotalDonations])

TotalDonations(donor_name="Alice", donation_amount=1263).save()
TotalDonations(donor_name="Bob", donation_amount=742).save()
TotalDonations(donor_name="Charlie", donation_amount=1542).save()

