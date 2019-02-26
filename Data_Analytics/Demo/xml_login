# xml 위치정보
from selenium import webdriver
driver = webdriver.Chrome("chromedriver.exe")
driver.get("http://ksp.multicampus.com/ksp/servlet/controller.gate.common.GateConstServlet?p_grcode=000002&p_ssochk=N&p_gubun=&p_ifsubj=&p_ifyear=&p_ifsubjseq=&p_ifdistcode=")
driver.find_element_by_xpath('//*[@id="glovalWrap"]/div/div[1]/ul/li[1]/a/img').click()

userID = driver.find_element_by_xpath('//*[@id="id"]')
userID.send_keys('아이디 입력')

userPW = driver.find_element_by_xpath('//*[@id="pw"]')
userPW.send_keys('비밀번호 입력')

userID = driver.find_element_by_xpath('//*[@id="contents"]/div[2]/div/div/form/fieldset/div[2]/button').click()
