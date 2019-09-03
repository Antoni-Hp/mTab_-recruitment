import functions


# test podaje wszystkie potrzebne dane do wykonania testu - adres strony,  tytuł przed i po wyszukiwaniu, szukany obiekt,
# oraz potrzebne nazwy klas, selektorów i name
adres_url = 'http://allegro.pl'
title_1 = 'Allegro.pl – najlepsze ceny, największy wybór i zawsze bezpieczne zakupy online'
advertisment_selector = "div._4f735_Ag0om._ur8qq > div > div._3kk7b._vnd3k._1h8s6._13prn._12isx._kiiea._oeb1x > button"
search_item = "rower"
search_name = "string"
search_title = "%s - Allegro.pl - Więcej niż aukcje. Najlepsze oferty na największej platformie handlowej" %search_item

# test uruchamia klase functions() uruchamiajac tym samym przegladarkę
zad1 = functions.functions()
# test wywoluje funkcje odpowiedzialną za przejscie do podanej strony oraz sprawdza czy akcja się powiodła
zad1.url(adres_url, title_1, advertisment_selector)
# test wywołuje funkcje odpowiedzialną za wyszukiwanie podanego obiektu, przechodzi do strony z wynikami wyszukiwania,
# a nastepnie sprawdza czy akcja się powiodła
zad1.search(search_item, search_name, search_title)
# test zamyka przegladarkę jezeli nie napotkał żadych błędów
zad1.close()

print("test pass")