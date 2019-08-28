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
    first_bicycle = driver.find_element_by_css_selector("div.bf8839e").text
    number_all_auctions = driver.find_element_by_css_selector("div._lsy4e._1hs1x._1ue2y._1t9p2._1h7wt._15mod._1vryf._1yfhn._3db39_1ZtAT._7ccvy").text.split()[-2]
    print("price first bicycle: ", first_bicycle)
    print( "number of auctions per page: ", len(driver.find_elements_by_css_selector("div.bf8839e")))
    print("number of all auctions: ", number_all_auctions)
    prince_in_gr = first_bicycle.split()[0].split(',')
    print((int(prince_in_gr[0]) * 100) + int(prince_in_gr[1]))
    driver.close()
    if ((int(prince_in_gr[0]) * 100) + int(prince_in_gr[1])) > int(number_all_auctions):
        print("Test PASS")
    else:
        print("Test FAILL")

except NoSuchElementException:
    print("Brak elementu")
    print("Test FAILL")
    raise

except:
    print("Test FAILL")
    raise
