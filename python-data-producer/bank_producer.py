import requests
from faker import Faker

def populate_bank(auth):
    fake = Faker()
    register_url = 'http://localhost:8083/banks'

    bank_entries = 10
    for i in range(bank_entries):
        register_info = {
            "routingNumber" : fake.numerify('#########'),
            "address" : fake.street_address(),
            "city" : fake.city(),
            "state" : fake.state(),
            "zipcode" : fake.numerify('#####')
        }
        reg_bank = requests.post(register_url, json=register_info, headers=auth)
        # print(reg_bank.text)

# login_info = {
#     'username' : 'adminUser',
#     'password' : 'Password*8'
# }
# login_response = requests.post('http://localhost:8070/login', json=login_info)
# bearer_token = login_response.headers['Authorization']
# auth = {'Authorization' : bearer_token}
# populate_bank(auth)