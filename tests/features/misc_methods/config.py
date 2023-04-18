import os

base_url = os.getenv('BASE_URL', 'http://localhost:5000/')
register_url = os.getenv('REGISTER_URL', 'http://localhost:5000/auth/register')
home_page = os.getenv('HOME_PAGE', 'http://localhost:5000/index')

user_name = 'sophie'
user_email = 'sophie.arianne.pereira@gmail.com'
user_password = 'sophie'