from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep


def login(id,pw):
    driver = webdriver.Chrome("C:\\Users\\winny\\OneDrive\\바탕 화면\\MS\\installed\\chromedriver.exe")

    driver.get("https://portal.korea.ac.kr/front/Intro.kpd  ")
    sleep(0.3)
    driver.find_element_by_name('id').send_keys(id)
    sleep(0.3)
    driver.find_element_by_name('pw').send_keys(pw)
    sleep(0.3)
    driver.find_element_by_xpath('//*[@id="loginform"]/input').click()
    sleep(0.3)
    driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/ul/li[4]/a').click()

    sleep(0.3)

    driver.get("http://infodepot.korea.ac.kr/grade/SearchGradeAll.jsp")
    
    
    html = driver.page_source
    driver.close()
    soup = BeautifulSoup(html,'lxml')
    
    detailInfo = soup.findAll('table')[0].findAll('td')
    totalInfo = soup.findAll('table')[1].findAll('td')

    gradeArr = {}

    totalGradeArr = {}

    tempArr = []
    for i in range(len(detailInfo)):
        if (i+1)%15==0:
            try:
                gradeArr[tempArr[0]].append(tempArr)
            except KeyError:
                gradeArr[tempArr[0]] = tempArr           
            
            tempArr=[]
        else:
            tempArr.append(str(detailInfo[i])[4:-5]) 

    tempArr = []
    for i in range(len(totalInfo)):
        if (i+1)%9==0:
            try:
                totalGradeArr[tempArr[0]].append(tempArr)
            except KeyError:
                totalGradeArr[tempArr[0]]=[tempArr]
            
            tempArr=[]
        else:
            tempArr.append(str(totalInfo[i])[4:-5])  

    
    return gradeArr,totalGradeArr
    
    
    