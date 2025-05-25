from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Company, Dev, Freebie

# Create the engine and bind it to the database
engine = create_engine('sqlite:///freebies.db')
Base.metadata.bind = engine

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Clear old data (optional: helpful for reseeding)
session.query(Freebie).delete()
session.query(Dev).delete()
session.query(Company).delete()

# Create some companies
company1 = Company(name="Google", founding_year=1998)
company2 = Company(name="Amazon", founding_year=1994)
company3 = Company(name="OpenAI", founding_year=2015)

# Create some developers
dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")
dev3 = Dev(name="Charlie")

# Create some freebies
freebie1 = Freebie(item_name="T-shirt", value=20, company=company1, dev=dev1)
freebie2 = Freebie(item_name="Sticker", value=5, company=company2, dev=dev2)
freebie3 = Freebie(item_name="Mug", value=15, company=company3, dev=dev1)
freebie4 = Freebie(item_name="Notebook", value=10, company=company1, dev=dev3)

# Add and commit everything
session.add_all([company1, company2, company3, dev1, dev2, dev3, freebie1, freebie2, freebie3, freebie4])
session.commit()

print("✅ Database seeded successfully!")
