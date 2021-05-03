import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


#@pytest.fixture(scope="class")
class AutoPractice:


    def __init__(self, driver):
        self.driver = driver


    first_name = (By.ID, "firstName")
    last_name = (By.ID, "lastName")
    user_email = (By.ID, "userEmail")
    gender = (By.XPATH, "//label[contains(text(),'Male')]")
    mobile = (By.ID, "userNumber")
    DoB_calender = (By.ID, "dateOfBirthInput")
    Dob_Month= (By.XPATH, "//option[contains(text(), 'January')]")
    Dob_year = (By.XPATH, "//option[contains(text(), '1988')]")
    Dob_day = (By.XPATH, "//div[1]/div[1]/div[2]/div[2]/div[1]/div[6]")
    #subject = (By.XPATH, "//form[1]/div[6]/div[2]/div[1]/div[1]/div[1]")
    subject = (By.XPATH, "//input[@id='subjectsInput']")
    hobbies = (By.XPATH, "//label[contains(text(),'Sports')]")
    user_image = (By.ID, "uploadPicture")
    Current_Address = (By.XPATH, "//textarea[@id='currentAddress']")
    select_State= (By.XPATH, "//div[contains(text(),'Select State')]")
    state = (By.XPATH, "//div[contains(text(),'NCR')]")
    select_city = (By.XPATH, "//div[10]/div[3]")
    city = (By.XPATH, "//div[contains(text(),'Delhi')]")
    submit_button= (By.XPATH, "//button[@id='submit']")


    def user_first_name(self):
        return self.driver.find_element(*AutoPractice.first_name)


    def user_last_name(self):
        return self.driver.find_element(*AutoPractice.last_name)


    def users_email(self):
        return self.driver.find_element(*AutoPractice.user_email)


    def user_gender(self):
        return self.driver.find_element(*AutoPractice.gender)



    def user_mobile(self):
        return self.driver.find_element(*AutoPractice.mobile)


    def user_calender(self):
        return self.driver.find_element(*AutoPractice.DoB_calender)


    def user_dob_month(self):
        return self.driver.find_element(*AutoPractice.Dob_Month)


    def user_dob_year(self):
        return self.driver.find_element(*AutoPractice.Dob_year)


    def user_dob_day(self):
        return self.driver.find_element(*AutoPractice.Dob_day)


    def user_subject(self):
        return self.driver.find_element(*AutoPractice.subject)


    def user_hobbies(self):
        return self.driver.find_element(*AutoPractice.hobbies)


    def user_picture(self):
        return self.driver.find_element(*AutoPractice.user_image)


    def user_current_address(self):
        return self.driver.find_element(*AutoPractice.Current_Address)


    def user_select_State(self):
        return self.driver.find_element(*AutoPractice.select_State)


    def user_state(self):
        return self.driver.find_element(*AutoPractice.state)


    def user_select_city(self):
        return self.driver.find_element(*AutoPractice.select_city)


    def user_city(self):
        return self.driver.find_element(*AutoPractice.city)


    def user_submit_button(self):
        return self.driver.find_element(*AutoPractice.submit_button)


