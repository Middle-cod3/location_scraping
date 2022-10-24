

from flask import Flask,jsonify,request,session,render_template
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys








#defining flask app
app = Flask(__name__, static_url_path='/static')  
#Step – 2 (configuring your application)
app.secret_key = 'ItShouldBeAnythingButSecret'








# ================================>>
capabilities = DesiredCapabilities().CHROME
  
# instance of Options class allows
# us to configure Headless Chrome
options = Options()
options.add_argument("--disable-infobars")
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")
options.add_argument("--disable-popup-blocking")
options.add_argument("--incognito")
  
# this parameter tells Chrome that
# it should be run without UI (Headless)



prefs = {
    'profile.default_content_setting_values':
    {
        'notifications': 1,
        'geolocation': 1
    },



   'profile.managed_default_content_settings':
    {
        'geolocation': 1
    },
}



options.add_experimental_option(
    "prefs", prefs
)



options.headless = True
capabilities.update(options.to_capabilities())
  
# initializing webdriver for Chrome with our options
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome(options=options)

# getting GeekForGeeks webpage
url = "https://www.google.com"




text_search="latitude and longitude of my location"
print(text_search)
# Fetching the Url
driver.get(url)
print("url fetched")
text_search
element=driver.find_element("name","q")
element.send_keys(text_search )
element.send_keys(Keys.ENTER)
page_content = driver.page_source
lat_long=driver.find_element("xpath",'//div[@class="Z0LcW t2b5Cf"]').text
print(lat_long)  
# We can also get some information
# about page in browser.
# So let's output webpage title into
# terminal to be sure that the browser
# is actually running.
#print(driver.title)
  
# close browser after our manipulations
driver.close()




#app run

if __name__ == '__main__':
    app.run(debug=True,port=9001)    
