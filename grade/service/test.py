from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import requests

def login(id,pw):
    session = requests.session()

    params = dict()
    params['id'] = id
    params['pw'] = pw
    params['browser'] = 'chrome'
    params['direct_div']=None
    params['pw_pass']=None

    login_url = 'https://portal.korea.ac.kr/common/Login.kpd'

    res = session.post(login_url, data = params) 

    res.raise_for_status() 
    params2 = dict()
    params2['token']=session.cookies.get_dict()['ssotoken']
    params2['path']='/grade/SearchGradeAll.jsp'
    params2['url']='http://infodepot.korea.ac.kr/grade/SearchGradeAll.jsp'
    params2['compId']=84
    params2['menuCd']=280
    params2['return_url']='/grade/SearchGradeAll.jsp'
    params2['query']=None
    params2['language']='ko'
    params2['compDiv']=None
    params2['locale']='ZW4='
    params2['lang']='KOR'

    res = session.post('http://infodepot.korea.ac.kr/grade/SearchGradeAll.jsp', data = params2) 

    
    soup = BeautifulSoup(res.text,'lxml')
    
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
                gradeArr[tempArr[0]] = [tempArr]
            
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






"""
def login(id,pw):
    driver = webdriver.Chrome("C:\\Users\\winny\\OneDrive\\바탕 화면\\MS\\installed\\chromedriver.exe")

    driver.get("https://portal.korea.ac.kr/front/Intro.kpd")
    sleep(0.3)
    driver.find_element_by_name('id').send_keys(id)
    sleep(0.3)
    driver.find_element_by_name('pw').send_keys(pw)
    sleep(0.3)
    driver.find_element_by_xpath('//*[@id="loginform"]/input').click()
    sleep(0.3)
    #driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/ul/li[4]/a').click()

    

    driver.get("http://infodepot.korea.ac.kr/grade/SearchGradeAll.jsp")
    sleep(0.3)
    
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
                gradeArr[tempArr[0]] = [tempArr]
            
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
    
"""
    