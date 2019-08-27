from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

try:
    driver = webdriver.Chrome(executable_path='C:\TestFiles\chromedriver.exe')
    driver.get('http://allegro.pl')
    assert "Allegro.pl – najlepsze ceny, największy wybór i zawsze bezpieczne zakupy online" in driver.title
    advertisement = driver.find_elements_by_css_selector("div._3kk7b._vnd3k._1h8s6._13prn._12isx._kiiea._oeb1x")
    if advertisement:
        driver.find_element_by_css_selector("div._3kk7b._vnd3k._1h8s6._13prn._12isx._kiiea._oeb1x").click()
    search = driver.find_element_by_name("string")
    search.send_keys("rower")
    search.send_keys(Keys.RETURN)
    print("price first bicycle: ", driver.find_element_by_css_selector("div.bf8839e").text)
    print( "number of auctions per page: ", len(driver.find_elements_by_css_selector("div.bf8839e")))
    print("number of all auctions: ", driver.find_element_by_css_selector("div._lsy4e._1hs1x._1ue2y._1t9p2._1h7wt._15mod._1vryf._1yfhn._3db39_1ZtAT._7ccvy").text.split()[-2])
    driver.close()
    print("Test PASS")

except NoSuchElementException:
    print("Brak elementu")
    print("Test FAILL")
    raise

except:
    print("Test FAILL")
    raise
