import time

def getInstVeriCode(mailName, domain, browser):

    INST_CODE = 'https://email-fake.com/' + domain + '/' + mailName
    
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[1])
    browser.get(INST_CODE)
    
    # button = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/table/tbody/tr[3]/td[1]/a/button").click()
    # time.sleep(3)
    t = browser.title

    while True:
        if t[:4]=="Fake":
            browser.refresh()
            t = browser.title
            print(t)
            time.sleep(1)
        else:
            break

    # code = browser.find_element_by_xpath("//*[@id='email-table']/div[2]/div[1]/div/h1").text
    # code = code.replace("is your Instagram code", "")
    code = t[:6]
    browser.switch_to.window(browser.window_handles[0])
    return code
    

