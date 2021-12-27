import requests
import logging
import os
from faker import Faker

def populate_bank(auth, bank_entries):
    logging.basicConfig(level=logging.INFO, filename="aline_files/core-my/docker-data/aline_log.log", filemode='a', format='%(process)d - [%(levelname)s ] - %(message)s')
    fake = Faker()
    # bank_url = 'http://localhost:8083/banks'
    bank_url = f"{os.environ.get('BANK_URL')}/banks"

    for i in range(bank_entries):
        bank_info = {
            "routingNumber" : fake.numerify('#########'),
            "address" : fake.street_address(),
            "city" : fake.city(),
            "state" : fake.state(),
            "zipcode" : fake.numerify('#####')
        }
        logging.info(f'Trying to post {bank_info}')
        try:
            reg_bank = requests.post(bank_url, json=bank_info, headers=auth)
            logging.info(f'Bank posted')
        except Exception as e:
            logging.error(f'Error entering bank: ', exc_info=True)

print('', end='')
