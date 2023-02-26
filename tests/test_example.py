import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager

def test_edge_session():
    service = EdgeService(executable_path=EdgeChromiumDriverManager().install())

    driver = webdriver.Edge(service=service)
    driver.get("https://www.google.com/")
    title = driver.title
    assert title == "Google"
    
    driver.close()
    driver.quit()