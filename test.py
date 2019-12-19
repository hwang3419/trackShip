from selenium import webdriver
print('123')
opt=webdriver.ChromeOptions()
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')
opt.add_argument("window-size=1024,768")
opt.add_argument("--no-sandbox")
opt.binary_location = '/usr/bin/google-chrome-stable'
d=webdriver.Chrome(executable_path='/usr/lib/chromedriver',chrome_options=opt)
print(d)