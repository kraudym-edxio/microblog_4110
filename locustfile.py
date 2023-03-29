from locust import HttpUser, task
import requests

class MyUser(HttpUser):
    host = "http://127.0.0.1:5000"

    @task
    def my_task(self):
        self.client.get("/")
