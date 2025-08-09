from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
from bs4 import BeautifulSoup


my_list=[]
Villes=["Illinois","Texas","New York","London","California","Florida","Ohio","Michigan"]
a=True
j=379
while a:
  try:
      driver = webdriver.Chrome(service=Service("/usr/local/bin/chromedriver"), options=chrome_options)
      if i==0:
        Site="https://www.houzz.com/professionals/electrical-contractors/probr0-bo~t_11818"
      else:
        Site="https://www.houzz.com/professionals/electrical-contractors/probr0-bo~t_11818?fi="+str(j*15)

      j+=1
      driver.get(Site)
      print(f"Title for page {j}:", driver.title)
      page_source = driver.page_source
      soup = BeautifulSoup(page_source, "html.parser")
      url0 = soup.find('ul', class_='hz-pro-search-results mb0')
      if url0:
        subtags = url0.find_all('li')
        for tag in subtags:
          try:

            url_tag = tag.find('a',class_='sc-62xgu6-0 cYgEZl sc-mwxddt-0 iIGnLB hui-link sc-cqJhZP dAzltj hz-pro-ctl')
            if url_tag and "href" in url_tag.attrs:
                s = url_tag["href"]
                my_list.append(s)

          except:
            continue

      driver.quit()
      time.sleep(2)
  except:
    driver.quit()
    a=False
    break
