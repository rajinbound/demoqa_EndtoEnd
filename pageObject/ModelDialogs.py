import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


#@pytest.fixture(scope="class")
class ModelDialog:


    small_model = (By.ID, "showSmallModal")
    large_model = (By.ID, "showLargeModal")


    def __init__(self, driver):
        self.driver = driver



    def user_small_model(self):
        return self.driver.find_element(*ModelDialog.small_model)


    def user_large_model(self):
        return self.driver.find_element(*ModelDialog.large_model)

