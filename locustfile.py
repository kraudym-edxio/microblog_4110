from locust import HttpUser, task, between
import time

class StressTester(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        time.sleep(2)
        self.register_user()
        self.login()
    
    def register_user(self):
        payload = {
            "username": "LocustTester",
            "email": "tester@example.com",
            "password": "mypassword"
        }
        headers = {"Content-Type": "application/json"}
        response = self.client.post("/auth/register", json=payload, headers=headers)

        if response.status_code == 200:
            print("New user registered successfully!")
        else:
            print("Failed to register user.")
    

    def login(self):
        payload = {
            "username": "LocustTester",
            "password": "mypassword45"
        }
        headers = {"Content-Type": "application/json"}
        response = self.client.post("/auth/login", json=payload, headers=headers)

        if response.status_code == 200:
            print("Login successful!")
        else:
            print("Failed to login.")
   
    @task
    def my_task(self):
        pass
        time.sleep(1)
        response = self.client.get("/user/LocustTester")
        if response.status_code == 200:
            print("Navigation successful!")
        else:
            print("Failed to navigate to user page.")
        