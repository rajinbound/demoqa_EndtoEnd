import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from Utilities.BaseClass import BaseClass
from pageObject.AutoPractice import AutoPractice
from pageObject.Alert_page import AlertPage
from pageObject.ToolTip import ToolTip
from pageObject.Dropable import Dropable

from pageObject.ModelDialogs import ModelDialog
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestDemoQA(BaseClass):



    def test_Student_Registration_Form(self, setup, getData):
        log = self.getLogger()
        self.driver.get("https://demoqa.com/automation-practice-form")
        Autopractice = AutoPractice(self.driver)
        log.info("Entering the first name")
        Autopractice.user_first_name().send_keys(getData[0])
        log.info("Entering the last name")
        Autopractice.user_last_name().send_keys(getData[1])
        log.info("Entering the email")
        Autopractice.users_email().send_keys(getData[2])
        Autopractice.user_gender().click()
        log.info("Entering the mobile")
        Autopractice.user_mobile().send_keys(getData[3])
        Autopractice.user_calender().click()
        Autopractice.user_dob_month().click()
        Autopractice.user_dob_year().click()
        Autopractice.user_dob_day().click()
        log.info("Entering the subject")
        Autopractice.user_subject().send_keys(getData[4])
        Autopractice.user_subject().send_keys(Keys.ENTER)
        Autopractice.user_hobbies().click()
        Autopractice.user_picture().send_keys(getData[5])
        log.info("Entering the address")
        Autopractice.user_current_address().send_keys(getData[6])
        Autopractice.user_select_State().click()
        Autopractice.user_state().click()
        Autopractice.user_select_city().click()
        Autopractice.user_city().click()
        Autopractice.user_submit_button().click()

        Student_name = self.driver.find_element_by_xpath("//td[contains(text(),'Raj Mishra')]").text
        log.info(Student_name)
        Student_email = self.driver.find_element_by_xpath("//td[contains(text(),'random@random.com')]").text
        log.info(Student_email)
        Gender = self.driver.find_element_by_xpath("//td[contains(text(),'Male')]").text
        log.info(Gender)
        Mobile = self.driver.find_element_by_xpath("//td[contains(text(),'7734000000')]").text
        log.info(Mobile)
        Date_of_birth = self.driver.find_element_by_xpath("//td[contains(text(),'01 January,1988')]").text
        log.info(Date_of_birth)
        Subjects = self.driver.find_element_by_xpath("//td[contains(text(),'Arts')]").text
        log.info(Subjects)
        Hobbies = self.driver.find_element_by_xpath("//td[contains(text(),'Sports')]").text
        log.info(Hobbies)
        picture = self.driver.find_element_by_xpath("//td[contains(text(),'img.png')]").text
        log.info(picture)
        address = self.driver.find_element_by_xpath("//td[contains(text(),'Southampton')]").text
        log.info(address)
        State_City = self.driver.find_element_by_xpath("//td[contains(text(),'NCR Delhi')]").text
        log.info(State_City)
        # print(Student_name,Student_email,Gender,Mobile,Date_of_birth,Subjects,Hobbies,picture,address,State_City)

        assert "Raj Mishra" == Student_name
        assert getData[2] == Student_email
        assert "Male" == Gender
        assert getData[3] == Mobile
        assert "01 January,1988" == Date_of_birth
        assert getData[4] == Subjects
        assert "Sports" == Hobbies
        assert "img.png" == picture
        assert getData[6] == address
        assert "NCR Delhi" == State_City


    def test_accept_the_alert(self):
        log = self.getLogger()
        self.driver.get("https://demoqa.com/alerts")
        alertpage = AlertPage(self.driver)
        alertpage.alert_click().click()
        time.sleep(5)
        log.info("Alert is being accepted")
        alert = self.driver.switch_to.alert
        alert.accept()


    def test_hoover_me_to_see(self):
        log = self.getLogger()
        self.driver.get("https://demoqa.com/tool-tips")
        tooltip = ToolTip(self.driver)
        hoover = tooltip.user_tool_tip()
        action = ActionChains(self.driver)
        log.info("Hoover is being performed")
        action.move_to_element(hoover).perform()


    def test_drag_drop(self):
        log = self.getLogger()
        self.driver.get("https://demoqa.com/droppable")
        drag = Dropable(self.driver)
        drag_item = drag.user_drag()
        target_item = drag.user_drop()
        action_chains = ActionChains(self.driver)
        log.info("Alert is being draged")
        action_chains.drag_and_drop(drag_item, target_item).perform()



    def test_model_dialog(self):
        log = self.getLogger()
        self.driver.get("https://demoqa.com/modal-dialogs")
        model = ModelDialog(self.driver)
        model.user_small_model().click()
        time.sleep(5)
        log.info("Modal is being closed")
        model.user_close_model().click()



    @pytest.fixture(params=[("Raj", "Mishra", "random@random.com", "7734000000", "Arts", "C:\\Users\\rmishra\\Downloads\\DemoQA\\uploads\\img.png", "Southampton")])
    def getData(self, request):
        return request.param
