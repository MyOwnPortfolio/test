from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://dmytrokovalenkodk.wix.com/qa-task-1")
driver.find_element_by_id("DrpDwnMn05label").click()
driver.find_element_by_id("iinjpnrhnameField").send_keys("Pedro")
driver.find_element_by_id("iinjpnrhemailField").send_keys("yuko@ukr.net")
driver.find_element_by_id("iinjpnrhsubjectField").send_keys("test")
driver.find_element_by_id("iinjpnrhmessageField").send_keys("test")
driver.find_element_by_id("iinjpnrhsubmit").click()
assert "Your details were sent successfully!"
print("test Done")
driver.close()
