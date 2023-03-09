import os
import shutil
import socketserver
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()

def get_browser():
    global options
    port = get_free_port()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--disable-site-isolation-trials')
    options.add_argument("--remote-debugging-port=" + str(port))
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome('D:\TAJobs\Winter 2023\Comp-4110\microblog\microblog-4110\testsuite\webdriver\chromedriver.exe',chrome_options=options)
    driver.maximize_window()
    return driver


def reset_options():
    global options
    options = Options()


def cleanup_directory():
    pass

def get_free_port():
    with socketserver.TCPServer(("localhost", 0), None) as s:
        return s.server_address[1]