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

def populate_branch(conn):
    fake = Faker()
    # optional clear table entries
    clear = True
    if clear:
        conn.execute(text('DELETE FROM branch'))
        conn.execute(text('ALTER TABLE branch AUTO_INCREMENT = 1'))

    # create and insert X entries
    num_entries = 10
    for i in range(num_entries):
        # define values to be inserted into user table
        # id is bigInt auto-inc
        address = fake.street_address() # varchar(255)
        city = fake.city() # varchar(255)
        name = fake.name() # varchar(255)
        phone = fake.phone_number() # varchar(255) nullable
        state = fake.state() # varchar(255) nullable
        zipcode = fake.zipcode() # varchar(255) nullable
        # bank_id is restricted foreign key from table 'bank'

        # create and execute insert string
        branch_ins = text("INSERT INTO branch (address, city, name, phone, state, zipcode) VALUES (:address, :city, :name, :phone, :state, :zipcode)")
        conn.execute(branch_ins, address=address, city=city, name=name, phone=phone, state=state, zipcode=zipcode)

populate_branch(connection)

