from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import imdb
import webbrowser

ia = imdb.IMDb()
imdbID = ''
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

input_ = input("Enter movie title: ")
movies = ia.search_movie(input_)
imdbID = 'tt' + movies[0].movieID
print(imdbID)
driver = webdriver.Chrome(options=options, executable_path="C:\\Users\\lvoye\\chromedriver\\chromedriver.exe")
driver.get("https://vsrequest.video/request.php?key=wYpnEU9LgFR7SKFt&secret_key=ymw0z9g7swyvtullenzpqo4yrivist&video_id=" + str(imdbID) + "&ip=50.96.35.250") 
source = driver.find_elements_by_tag_name('body')
driver.get(source[0].text)
link = driver.find_elements_by_tag_name('form')[0].get_attribute("action")
webbrowser.open(link)
driver.quit()