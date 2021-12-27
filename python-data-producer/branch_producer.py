import requests
import logging
import os
from faker import Faker

def populate_branch(auth, branch_entries):
    logging.basicConfig(level=logging.INFO, filename="aline_files/core-my/docker-data/aline_log.log", filemode='a', format='%(process)d - [%(levelname)s ] - %(message)s')
    fake = Faker()
    # branch_url = 'http://localhost:8083/branches'
    branch_url = f"{os.environ.get('BANK_URL')}/branches"

    for i in range(branch_entries):
        branch_info = {
            "name" : fake.name(),
            "address" : fake.street_address(),
            "city" : fake.city(),
            "state" : fake.state(),
            "zipcode" : fake.numerify('#####'),
            "phone" : fake.numerify('(###)-###-####'),
            "bankID" : str(i+1)
        }
        logging.info(f'Trying to post {branch_info}')
        try:
            reg_branch = requests.post(branch_url, json=branch_info, headers=auth)
            logging.info('Branch posted')
        except Exception as e:
            logging.error(f'Error entering branch: ', exc_info=True)

print('', end='')
