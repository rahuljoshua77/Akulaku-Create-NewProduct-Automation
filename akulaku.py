import undetected_chromedriver as uc
import autoit
uc.install()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os,re
import random
import time
#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from multiprocessing import Pool
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
 
cwd = os.getcwd()

def upload_file(path):
    try:
        path = path.replace(';', ':')
    except:
        pass
    try:
        path = path.replace('|', ':')
    except:
        pass
    autoit.win_active("File Upload")
    sleep(0.5)
    autoit.control_send("File Upload","Edit1",path)
    sleep(0.5)
    autoit.control_send("File Upload","Edit1","{ENTER}")

def xpath_type(el,mount):
    sleep(0.5)
    return wait(browser,10).until(EC.presence_of_element_located((By.XPATH, el))).send_keys(mount)

def xpath_el(el):
    element_all = wait(browser,20).until(EC.presence_of_element_located((By.XPATH, el)))
    sleep(0.5)
    return element_all.click()

def product():
    sleep(2)
    try:
        xpath_el('/html/body/div[2]/div[2]/div[1]/i')
    except:
        pass
    sleep(2)
    browser.get('https://vendor.akulaku.com/#/index/newProducts')
    print(f"[{time.strftime('%d-%m-%y %X')}] Add New Product, Please wait!")
    sleep(1)
    try:
        xpath_el('//*[@id="ngdialog1"]/div[2]/div[1]/i')
    except:
        pass
  
    xpath_el(f"//option[contains(text(),'{kategori}')]")
    print(f"[{time.strftime('%d-%m-%y %X')}] Input Kategori: {kategori}") 
         
    xpath_el(f"//option[contains(text(),'{sub_kategori}')]")
    print(f"[{time.strftime('%d-%m-%y %X')}] Input Sub Kategori: {sub_kategori}")
    xpath_type('//input[@ng-model="itemName"]',nama_produk)
    print(f"[{time.strftime('%d-%m-%y %X')}] Input Nama Produk")
    xpath_type('//input[@ng-model="brand"]',merk_produk)
    print(f"[{time.strftime('%d-%m-%y %X')}] Input Merk Produk")
    xpath_type('//input[@ng-blur="priceInputBlur(item)"]', harga_produk)
    print(f"[{time.strftime('%d-%m-%y %X')}] Input Harga Produk")
  
   
    element =  wait(browser,30).until(EC.presence_of_element_located((By.XPATH,'(//div[@class="img-upload"])[1]')))
    
    xpath_el('(//div[@class="img-upload"])[1]')
    sleep(1)
    upload_file(f'{cwd}\\{gambar_utama}')
    sleep(2)
    try:
        element =  wait(browser,30).until(EC.presence_of_element_located((By.XPATH,'(//div[@class="img-upload"])[2]')))
        browser.execute_script("arguments[0].scrollIntoView();", element)
    except:
        pass
    print(f"[{time.strftime('%d-%m-%y %X')}] Input Gambar Utama: {gambar_utama}")
    for i in gambar_banner:
        xpath_el('(//div[@class="img-upload"])[1]')
        sleep(2)
        upload_file(f'{cwd}\\{i}')
        print(f"[{time.strftime('%d-%m-%y %X')}] Input Gambar Banner: {i}")
        sleep(2)

    for i in gambar_rincian:
        element =  wait(browser,30).until(EC.presence_of_element_located((By.XPATH,'(//div[@class="img-upload"])[2]')))
        browser.execute_script("arguments[0].scrollIntoView();", element)
        xpath_el('(//div[@class="img-upload"])[2]')
        sleep(2)
        upload_file(f'{cwd}\\{i}')
        print(f"[{time.strftime('%d-%m-%y %X')}] Input Gambar Rincian: {i}")
        sleep(1)
    xpath_type('//textarea[@ng-model="description"]',deskripsi)
    print(f"[{time.strftime('%d-%m-%y %X')}] Input Deskripsi")

    # xpath_el('//button[@class="al-button al-button--primary al-button--medium"]')
    # xpath_type('//input[@ng-model="item.attrKey.name"]',spesifikasi_item_name)
    # xpath_el('//button[@class="al-button al-button--success al-button--mini is-plain"]')
    
    # xpath_type('//input[@ng-show="item.isValEdit"]',spesifikasi_item_value)
    # xpath_el('//button[@class="al-button al-button--warning"]')
    
    xpath_el('//div[@class="attr-btn-add ng-binding"]')
    xpath_type('//input[@ng-model="item.attrKey.name"]',variasi)
    print(f"[{time.strftime('%d-%m-%y %X')}] Input Variasi")
    xpath_el('//button[@class="al-button al-button--success al-button--mini is-plain"]')
    xpath_type('//input[@ng-show="item.isValEdit"]',variasi_value)
    xpath_type('//input[@ng-model="weight"]',berat_produk)
    print(f"[{time.strftime('%d-%m-%y %X')}] Input Berat Produk")
    xpath_type('//input[@ng-model="length"]',panjang_produk)
    print(f"[{time.strftime('%d-%m-%y %X')}] Input Panjang Produk")
    xpath_type('//input[@ng-model="width"]',lebar_produk)
    print(f"[{time.strftime('%d-%m-%y %X')}] Input Lebar Produk")
    xpath_type('//input[@ng-model="height"]',tinggi_produk)
    print(f"[{time.strftime('%d-%m-%y %X')}] Input Tinggi Produk")
    try:
        xpath_el('//input[@ng-value="1"]')
    except:
        pass
    element = wait(browser,10).until(EC.presence_of_element_located((By.XPATH, '//button[@class="al-button al-button--danger al-button--medium"]')))
    browser.execute_script("arguments[0].scrollIntoView();", element)
    xpath_el('//button[@class="al-button al-button--danger al-button--medium"]')
    sleep(1)
    xpath_type('//input[@ng-model="item.vendorSkuId"]',shopsku)
    print(f"[{time.strftime('%d-%m-%y %X')}] Input Shop SKU")
    xpath_type('//input[@ng-model="item.stock"]',jumlah_sku)
    print(f"[{time.strftime('%d-%m-%y %X')}] Input Jumlah SKU")
    xpath_el('//button[@class="al-button al-button--success"]')
    notice = wait(browser,10).until(EC.presence_of_element_located((By.XPATH, '//h3[@class="notice"]'))).text
    print(f"[{time.strftime('%d-%m-%y %X')}] {notice}")

def login():
    print(f"[{time.strftime('%d-%m-%y %X')}] Login")
    xpath_type('(//input[@type="email"])[1]',email)
    sleep(0.5)
    xpath_type('(//input[@type="password"])',password)
    sleep(0.5)
    xpath_type('(//input[@type="password"])',Keys.ENTER)
   
def open_browser(k,y):
    
    global browser
    global element
    global email
    global password
    global kategori
    global sub_kategori
    global nama_produk 
    global merk_produk 
    global harga_produk
    global gambar_utama
    global gambar_banner
    global gambar_rincian
    global deskripsi 
    global shopsku
    global jumlah_sku
    global variasi_value
    global variasi
    global berat_produk
    global lebar_produk
    global tinggi_produk
    global panjang_produk

    k = k.split("|")
    email = k[0]
    password = k[1]
    y = y.split("|")
    kategori = y[0]
    sub_kategori = y[1]
    nama_produk = y[2]
    merk_produk = y[3]
    harga_produk = y[4]
    gambar_utama = y[5]
    gambar_banner = y[6]
    gambar_banner = gambar_banner.split(",")
    
    gambar_rincian = y[7]
    gambar_rincian = gambar_rincian.split(",")
    deskripsi = y[8]
    
    variasi = y[9]
    variasi_value = y[10]
    berat_produk = y[11]
    panjang_produk = y[12]
    lebar_produk = y[13]
    tinggi_produk = y[14]
    shopsku = y[15]
    jumlah_sku = y[16]
  
    random_angka = random.randint(100,999)
    random_angka_dua = random.randint(10,99)
    #opts.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.{random_angka}.{random_angka_dua} Safari/537.36")
    browser = webdriver.Firefox()
    browser.get('https://vendor.akulaku.com/#/index/newProducts')
    try:
        login() 
        product()
        browser.quit()
    except Exception as e:
        print(f"[{time.strftime('%d-%m-%y %X')}] Failed, Error: {e}")
        with open('failed.txt','a') as f:
            f.write('{0}|{1}\n'.format(email,password))
        browser.quit()

if __name__ == '__main__':
    global list_accountsplit
    print(f"[{time.strftime('%d-%m-%y %X')}] Automation Input Product Web")
    print(f"[{time.strftime('%d-%m-%y %X')}] Coder: RJD")
    file_list = "rincian.txt"
    myfiles = open(f"{cwd}/{file_list}","r")
    data_list = myfiles.read()
    data = data_list.split("\n")

    file_list_akun = "akun_akulaku.txt"
    myfile_akun = open(f"{cwd}/{file_list_akun}","r")
    akun = myfile_akun.read()
    list_accountsplit = akun.split("\n")

    for i in range(0,len(list_accountsplit)):
        open_browser(list_accountsplit[i],data[i])