# create an engine
from sqlalchemy import create_engine
engine = create_engine('sqlite:///C:\\Python27\\mystuff\\phonebook.db', echo=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# define table
from sqlalchemy import Column, Integer, String
class Phonebook(Base):
    __tablename__ = "friends"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)

    def __repr__(self):
	    return "<Phonebook(name='%s', email='%s', phone='%s')>"\
	        %(self.name, self.email, self.phone)


# create a list with our friend's numbers
friends_numbers = [
    {'name': 'James Rodriguez',
     'email': 'james@email.com',
     'phone': '123-456-7890'},
    {'name': 'Pibe Valderrama',
     'email': 'pibe@email.com',
     'phone': '111-222-3333'},
    {'name': 'Farid Mondragon',
     'email': 'farid@email.com',
     'phone': '222-333-4444'}     
     ]

# create tables
Base.metadata.create_all(engine)

# establish a session
from sqlalchemy.orm import sessionmaker

session = sessionmaker(bind=engine)
session = session()

# create instances
# use ** to unpack the key-value pairs
james = Phonebook(**friends_numbers[0])

# add james to the Phonebook database
session.add(james)
session.new

# delete james from the Phonebook database
session.expunge(james)
session.new

# add all records from the friends_numbers list into the db
phonebook_rows = [Phonebook(**p) for p in friends_numbers]
sesql.pysion.add_all(phonebook_rows)
session.commit()

# query the database
# count how many records we have
print session.query(Phonebook).count()

# find James Rodriguez record using filter_by
friend = session.query(Phonebook).filter_by(name='James Rodriguez')
result = list(friend)
print result