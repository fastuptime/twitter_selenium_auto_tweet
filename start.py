import time
import random
from selenium import webdriver

def log(log_text):
    log_text = str(time.strftime("%Y.%m.%d %H:%M:%S")) + " ➾ " + log_text
    print(log_text)
    log_file = open("log.txt", "a", encoding='utf-8')
    log_file.write(log_text + "\n")
    log_file.close()
email = 'FastUptime'
password = 'reset1reset1'

global_delay = 3
driver = webdriver.Chrome()
driver.get("https://twitter.com/login")
log('Bu program Can Tarafından Yapılmıştır.')
log('https://fastuptime.com ve https://speedsmm.com üzerinden bize ulaşabilirsiniz.')
log('Program başlatıldı')
log('Twitter açıldı')
def login(email, password):
    time.sleep(10)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys(email)
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div').click()
    time.sleep(1)
    log('Email girildi')
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(password)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div').click()
    log('Password girildi')
    log("Giriş yapıldı!\nGiriş yapılan mail adresi; " + email)
    time.sleep(3)
    tweet()

def tweet():
    log('Tweet Atma İşlemi Başlatılıyor')
    for i in range(1,140):
        try:
            driver.get("https://twitter.com/compose/tweet")
            main_tweet = '#takipcisatinal #ücretlitakip #takipçi #gt #insta #instagram #speedsmm #geritakip https://speedsmm.com'
            time.sleep(5)
            with open('tweets.json', 'r', encoding='utf-8') as f:
                data = f.read()
                tweet = random.choice(data.split('\n'))
                tweet = tweet.replace('"', '')
                tweet = tweet.replace('  ', ' ')
                tweet = tweet.replace(',', '')
                rasgele_plaform_adlari = ['discord', 'spotify', 'youtube', 'deezer', 'telegram', 'facebook', 'Messenger', 'wechat', 'Reddit', 'snapchat', 'Pinterest', 'Twitch']
                string_sayi = str(i) + ' #' + random.choice(rasgele_plaform_adlari)
                driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div').send_keys(string_sayi + " "+ main_tweet + tweet)
                time.sleep(global_delay)
                try:
                    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div').click()
                    log(str(i) + ". Tweet atıldı!")
                    time.sleep(global_delay)
                except:
                    log("Tweet atılamadı!")
                    time.sleep(2)
                    continue
        except:
            log("Tweet atılamadı!")
            time.sleep(2)
            continue
try:
    login(email, password)
except:
    log("Giriş yapılamadı!")
    login(email, password)