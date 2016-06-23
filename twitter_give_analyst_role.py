from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time



def logg_to_twitter(user,password):
    try:
        driver = webdriver.PhantomJS()
        driver.get("https://twitter.com/login/error?redirect_after_login=%2F")
        driver.find_element_by_css_selector('form.signin .field .email-input').send_keys(user)
        time.sleep(3)
        driver.find_element_by_css_selector('form.signin .field .js-password-field').send_keys(password)            
        time.sleep(3)
        driver.find_element_by_css_selector('form.signin button.submit.primary-btn ').click()
        return driver
    except Exception as e:
        print ('Log to twitter error', e)
        return None




def give_a_role(driver,analyst):
    driver.get("https://analytics.twitter.com")
    driver.set_window_size(1366,1500)
    time.sleep(5)
    driver.find_elements_by_css_selector("li.SharedNavBar-navItem.dropdown.apex-navbar-dropdown")[1].click()
    time.sleep(5)
    driver.find_element_by_partial_link_text("Edit access").click()
    driver.find_element_by_css_selector('button.add-users.btn').click()
    time.sleep(3)
    analyst_field=driver.find_element_by_css_selector("input#user-search-field.user-search-field")
    analyst_field.send_keys(analyst)
    analyst_field.click()
    analyst_field.send_keys(Keys.ENTER)
    time.sleep(5)
    driver.find_element_by_css_selector("div.search-field.twitter-form").send_keys(Keys.ENTER)
    analyst_field.send_keys(Keys.ENTER)
    time.sleep(6)
    driver.find_element_by_css_selector("input#account-user-role-analyst").click()
    driver.find_element_by_css_selector("button.account-users-save.btn.btn-primary").click()
    driver.quit()



def give_analyst_role(user, password, analyst):
    '''analyst is twitter username of person, we want to give access to our account'''
    driver = logg_to_twitter(user,password)
    give_a_role(driver, analyst)


if __name__ == "__main__":
    give_analyst_role()
















