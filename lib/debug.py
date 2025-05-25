from models import Dev, Company, Freebie
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# Test class method
print("Oldest company:", Company.oldest_company(session))

# Test instance method (give_freebie)
c1 = session.query(Company).first()
d1 = session.query(Dev).first()
f1 = c1.give_freebie(d1, "Water Bottle", 20)
session.add(f1)
session.commit()

# Test freebie method (print_details)
f1.print_details()

# Test give_away method
receiver = session.query(Dev).filter(Dev.id != d1.id).first()
d1.give_away(receiver, f1)
session.commit()

# Confirm it worked
f1.print_details()
