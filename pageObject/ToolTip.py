import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


#@pytest.fixture(scope="class")
class ToolTip:


    tool_tip = (By.ID, "toolTipButton")


    def __init__(self, driver):
        self.driver = driver



    def user_tool_tip(self):
        return self.driver.find_element(*ToolTip.tool_tip)