from locust import HttpUser, task, between
import time

USER_CREDENTIALS = [
    ("user1", "password", "user1@email.com"),
    ("user2", "password", "user2@email.com"),
    ("user3", "password", "user3@email.com"),
]

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

        if len(USER_CREDENTIALS) > 0:
            user, passw, email = USER_CREDENTIALS.pop()
        if {"/auth/registerLocust": None} in response_branch:
            self.register_user(user, passw, email)
            if {"/auth/loginLocust": None} in response_branch:
                self.login(user, passw)
                time.sleep(5)
            else:
                print("Login page not found.")
        else:
            print("Registration page not found.")
    
    def register_user(self, user, passw, email):
        payload = {
            "username": user,
            "email": email,
            "password": passw,
            "is_verified": True
        }
        headers = {"Content-Type": "application/json"}
        response = self.client.post("/auth/registerLocust", json=payload, headers=headers)
        if response.status_code == 200:
            print("New user registered successfully!")
        else:
            print("Failed to register user.")
    

    def login(self, user, passw):
        payload = {
            "username": user,
            "password": passw
        }
        headers = {"Content-Type": "application/json"}
        response = self.client.post("/auth/loginLocust", json=payload, headers=headers)

        if response.status_code == 200:
            print("Login successful!")
        else:
            print("Failed to login.")
   
    @task(1)
    def my_task(self):
        pass
        response = self.client.get("/user")
        time.sleep(5)
        if response.status_code == 200:
            print("Navigation successful!")
        else:
            print("Failed to navigate to user page.")
        