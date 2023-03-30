from locust import HttpUser, task, between
import time
import json
import sys

class StressTester(HttpUser):
    wait_time = between(1, 5)
    response_branch = {}

    def on_start(self):
        time.sleep(2)

        # get all branches
        headers = {"Content-Type": "application/json"}
        response = self.client.get("/branches", headers=headers)
        if response.status_code == 200:
            response_branch_body = response.json()
            response_branch = response_branch_body["data"]
            print("Successfuly received all branches.")
        else:
            print("Failed to get branches.")
            sys.exit(1)

        if {"/auth/register": None} in response_branch:
            self.register_user()
            if {"/auth/login": None} in response_branch:
                self.login()
                time.sleep(5)
            else:
                print("Login page not found.")
                sys.exit(1)
        else:
            print("Registration page not found.")
            sys.exit(1)
    
    def register_user(self):
        payload = {
            "username": "LocustTester",
            "email": "tester@example.com",
            "password": "mypassword",
            "is_verified": True
        }
        headers = {"Content-Type": "application/json"}
        response = self.client.post("/auth/registerLocust", json=payload, headers=headers)
        if response.status_code == 200:
            print("New user registered successfully!")
        else:
            print("Failed to register user.")
            sys.exit(1)
    

    def login(self):
        payload = {
            "username": "LocustTester",
            "password": "mypassword45"
        }
        headers = {"Content-Type": "application/json"}
        response = self.client.post("/auth/loginLocust", json=payload, headers=headers)

        if response.status_code == 200:
            print("Login successful!")
        else:
            print("Failed to login.")
            sys.exit(1)
   
    @task(1)
    def my_task(self):
        pass
        response = self.client.get("/user/LocustTester")
        time.sleep(5)
        if response.status_code == 200:
            print("Navigation successful!")
        else:
            print("Failed to navigate to user page.")
            sys.exit(1)
        