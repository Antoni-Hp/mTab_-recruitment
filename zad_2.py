import functions

adres_url = 'http://allegro.pl'
title_1 = 'Allegro.pl – najlepsze ceny, największy wybór i zawsze bezpieczne zakupy online'
advertisment_selector = "div._4f735_Ag0om._ur8qq > div > div._3kk7b._vnd3k._1h8s6._13prn._12isx._kiiea._oeb1x > button"
search_item = "rower"
search_name = "string"
search_title = "%s - Allegro.pl - Więcej niż aukcje. Najlepsze oferty na największej platformie handlowej" %search_item
price_item_selector = "div.bf8839e"
all_auctions_selector = "div._lsy4e._1hs1x._1ue2y._1t9p2._1h7wt._15mod._1vryf._1yfhn._3db39_1ZtAT._7ccvy"

zad2 = functions.functions()
zad2.url(adres_url, title_1, advertisment_selector)
zad2.search(search_item, search_name, search_title)
first_price = zad2.getFirst_price(price_item_selector).text
all_auctions = zad2.getAll_auctions(all_auctions_selector).text.split()[-2]
number_auctions_per_page = len(zad2.getAuctions_per_page(price_item_selector))
zad2.close()


prince_in_gr = first_price.split()[0].split(',')
if ((int(prince_in_gr[0]) * 100) + int(prince_in_gr[1])) > int(all_auctions):
    print("test pass")
else:
    print("test fail")

print("price first bicycle: ", first_price)
print("number of all auctions: ", all_auctions)
print("number of auctions per page: ", number_auctions_per_page)