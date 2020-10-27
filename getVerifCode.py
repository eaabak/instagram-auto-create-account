import time

def getInstVeriCode(mailName, domain, browser):

    INST_CODE = 'https://email-fake.com/' + domain + '/' + mailName
    
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[1])
    browser.get(INST_CODE)
    time.sleep(20)
    code = browser.find_element_by_xpath("//*[@id='email-table']/div[2]/div[1]/div/h1").text
    code = code.replace("is your Instagram code", "")
    print(code)
    browser.switch_to.window(browser.window_handles[0])
    return code
