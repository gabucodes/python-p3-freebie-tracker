from models import Dev, Company, Freebie
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()


print("Oldest company:", Company.oldest_company(session))


c1 = session.query(Company).first()
d1 = session.query(Dev).first()
f1 = c1.give_freebie(d1, "Water Bottle", 20)
session.add(f1)
session.commit()


f1.print_details()


receiver = session.query(Dev).filter(Dev.id != d1.id).first()
d1.give_away(receiver, f1)
session.commit()


f1.print_details()
