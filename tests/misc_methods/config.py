import os

base_url = os.getenv('BASE_URL', 'http://127.0.0.1:5000/')
register_url = os.getenv('REGISTER_URL', 'http://127.0.0.1:5000/auth/register')
home_page = os.getenv('HOME_PAGE', 'http://127.0.0.1:5000/index')