import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


#@pytest.fixture(scope="class")
class AlertPage:


    alert_element = (By.ID, "timerAlertButton")


    def __init__(self, driver):
        self.driver = driver



    def alert_click(self):
        return self.driver.find_element(*AlertPage.alert_element)