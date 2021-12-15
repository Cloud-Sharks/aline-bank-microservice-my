import sqlalchemy as db
from sqlalchemy import text
from faker import Faker

# specify db config
config = {
    'host' : 'localhost',
    'port' : 3307,
    'user' : 'user',
    'password' : 'pwd',
    'database' : 'alinedb'
}

db_user = config.get('user')
db_pwd = config.get('password')
db_host = config.get('host')
db_port = config.get('port')
db_name = config.get('database')

# specify connection string
connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'
# connect to database
engine = db.create_engine(connection_str)
connection = engine.connect()

def populate_bank(conn):
    fake = Faker()
    # optional clear table entries
    clear = True
    if clear:
        conn.execute(text('DELETE FROM bank'))
        conn.execute(text('ALTER TABLE bank AUTO_INCREMENT = 1'))

    # create and insert X entries
    num_entries = 10
    for i in range(num_entries):
        # define values to be inserted into user table
        # id is bigInt auto-inc
        address = fake.street_address() # varchar(255)
        city = fake.city() # varchar(255)
        routing_number = fake.numerify('#########') # varchar(9)
        state = fake.state() # varchar(255)
        zipcode = fake.zipcode() # varchar(255) nullable

        # create and execute insert string
        bank_ins = text("INSERT INTO bank (address, city, routing_number, state, zipcode) VALUES (:address, :city, :routing_number, :state, :zipcode)")
        conn.execute(bank_ins, address=address, city=city, routing_number=routing_number, state=state, zipcode=zipcode)

populate_bank(connection)