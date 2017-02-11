from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
profile = webdriver.FirefoxProfile('/Users/tony/Library/Application Support/Firefox/Profiles/b4ph03l5.default')
browser = webdriver.Firefox(profile)
browser.maximize_window()
'''
browser.get('http://www.footaction.com')
browser.find_element_by_link_text('My Account').click()
WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, 'account_access_password')))
pwd = browser.find_element_by_id('account_access_password')
browser.execute_script('arguments[0].click()', pwd)
pwd.clear()
browser.execute_script("document.getElementById('account_access_password').value='tony1997';")
#pwd.send_keys('tony1997')
browser.find_element_by_id('btn_myacct_log_in').click()
#browser.find_element_by_link_text('My Account').click()
'''

browser.get('http://www.footaction.com/product/model:254106/sku:021117YZ/?SID=6526&cm_mmc=Linkshare-_-Deeplink-_-Text-_-Footaction')
size_dropdown = browser.find_element_by_id('size_4_021117YZ')
size_dropdown.click()

#if browser.find_element_by_id('miniAddToCartWrapper').is_displayed():
#    print('Not yet added to cart')

add_to_cart = browser.find_element_by_id('addToCartLink')
while (add_to_cart.is_displayed() == False):
    browser.refresh()
add_to_cart.click()

#WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, 'miniAddToCart_actions')))
view = browser.find_element_by_id('order_summary_link')
view.click()
#if browser.find_element_by_id('miniAddToCartWrapper').is_displayed():
print('Added to cart')
#    browser.get('http://www.footaction.com/shoppingcart/default.cfm?')
WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, 'cart_checkout_button')))
checkout = browser.find_element_by_id('cart_checkout_button')
checkout.click()
browser.execute_script("document.getElementById('billEmailAddress').value='antonytej@gmail.com';")
#browser.execute_script("document.getElementById('loginHeaderPassword').value='tony1997';")
#browser.execute_script("document.getElementById('loginHeaderButtonLogin').click();")
print('Logging in...')
WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, 'checkout_middle')))
login = browser.find_element_by_class_name('expandable-container')
browser.execute_script('arguments[0].click();', login)
#browser.find_element_by_id('loginHeaderEmailAddress').send_keys("antonytej@gmail.com")
browser.execute_script("document.getElementById('loginHeaderPassword').value='tony1997';")
loginbutton = browser.find_element_by_id('loginHeaderButtonLogin')
browser.execute_script('arguments[0].click();', loginbutton)
print('Logged in')
print('Submitting order')
submit = browser.find_element_by_id('orderSubmit')
browser.execute_script('arguments[0].click();', submit)
print('Order submitted')
'''
def shippingAddress(first_name, last_name, street, zip_code, phone, email):
    WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, 'billFirstName')))


    fname = browser.find_element_by_xpath('//*[@id="billFirstName"]')
    #browser.execute_script('arguments[0].checked = true;', fname)
    fname.send_keys(first_name)
    browser.find_element_by_id('billLastName').send_keys(last_name)
    browser.find_element_by_id('billAddress1').send_keys(street)
    browser.find_element_by_id('billPostalCode').send_keys(zip_code)
    #browser.find_element_by_id('billCity').send_keys(city)
    #browser.find_element_by_id('billState').send_keys(state, Keys.ENTER)
    browser.find_element_by_id('billHomePhone').send_keys(phone)
    browser.find_element_by_id('billEmailAddress').send_keys(email)
    browser.find_element_by_id('billPaneContinue').click();
    browser.find_element_by_id('shipMethodPaneContinue').click();

def payment(ccnmmyycsc):
    WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, 'CardNumber')))
    browser.find_element_by_id('CardNumber').send_keys(ccnmmyycsc)
'''

'''
browser.execute_script("document.getElementById('billFirstName').value='Antony';")
browser.execute_script("document.getElementById('billLastName').value='Tejakusuma';")
browser.execute_script("document.getElementById('billAddress1').value='6030 Countess Drive';")
browser.execute_script("document.getElementById('billPostalCode').value='95129';")
browser.execute_script("document.getElementById('billHomePhone').value='4087057483';")
browser.execute_script("document.getElementById('billEmailAddress').value='antonytej@gmail.com';")

WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, 'billPaneContinue')))
cont = browser.find_element_by_id('billPaneContinue')
browser.execute_script('document.getElementById("billPaneContinue").click();')
cont1 = browser.find_element_by_id('shipMethodPaneContinue')
browser.execute_script('arguments[0].click();', cont1)
#cont2 = browser.find_element_by_id('promoCodePaneContinue')
#browser.execute_script('arguments[0].click();', cont2)
'''
#shippingAddress('Antony',
 #               'Tejakusuma',
  #              '6030 Countess Drive',
   #             '95129',
    #            '4087057483',
     #           'antonytej@gmail.com')
#payment(48158200823173530819660)





#browser.implicitly_wait(5)
#login = browser.find_element_by_class_name('expandable-container')
#login = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'expandable-container')))
#browser.execute_script("arguments[0].click()", login)
#ActionChains(browser).move_to_element(login).click().perform()

#email = browser.find_element_by_id('login_email')
#email.send_keys('antonytej@gmail.com')
#passwd = browser.find_element_by_id('login_password')
#passwd.send_keys('tony1997')
#passwd.submit()

#browser.implicitly_wait(1)
#add_to_cart = browser.find_element_by_id('addToCart')
#add_to_cart.click()
#add_to_cart = browser.find_element_by_xpath('//*[@class="add_to_cart float_left"]')
#add_to_cart.click()
#cart_url = 'https://www.footlocker.com/catalog/shoppingCart'
#browser.get(cart_url)

#ActionChains(browser).move_to_element(size_dropdown).click(size_dropdown).perform()
#size = browser.find_element_by_link_text('09.0')
#size.click()
#cart = browser.find_element_by_id('pdp_addtocart_button')
#`cart.click()
#search_field.send_keys(Keys.TAB)
#search_field.send_keys('ultra boost')
#search_field.submit()

