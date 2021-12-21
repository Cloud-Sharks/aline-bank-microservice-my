import requests
from faker import Faker

def populate_branch(auth):
    fake = Faker()
    register_url = 'http://localhost:8083/branches'

    branch_entries = 10
    for i in range(branch_entries):
        register_info = {
            "name" : fake.name(),
            "address" : fake.street_address(),
            "city" : fake.city(),
            "state" : fake.state(),
            "zipcode" : fake.numerify('#####'),
            "phone" : fake.numerify('(###)-###-####'),
            "bankID" : str(i+1)
        }
        reg_branch = requests.post(register_url, json=register_info, headers=auth)
        # print(reg_branch.text)

# login_info = {
#     'username' : 'adminUser',
#     'password' : 'Password*8'
# }
# login_response = requests.post('http://localhost:8070/login', json=login_info)
# bearer_token = login_response.headers['Authorization']
# auth = {'Authorization' : bearer_token}
# populate_branch(auth)
