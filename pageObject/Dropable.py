import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


#@pytest.fixture(scope="class")
class Dropable:


    drag_element = (By.ID, "draggable")
    drop_element = (By.ID, "droppable")


    def __init__(self, driver):
        self.driver = driver



    def user_drag(self):
        return self.driver.find_element(*Dropable.drag_element)


    def user_drop(self):
        return self.driver.find_element(*Dropable.drop_element)