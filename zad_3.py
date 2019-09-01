import service

class Main():
    def __init__(self):
        #wywolanie modulu selenium, otwarcie przegladarki Chrome w trybie automatycznym, przejscie do podanej strony(allegro.pl)
        self.service = service.Service('http://allegro.pl')
        #definicja zmiennej tytul w celu porownania z tytulem strony
        self.title = 'Allegro.pl – najlepsze ceny, największy wybór i zawsze bezpieczne zakupy online'
        #zdefiniowanie szukanego elementu
        self.serch_item = 'rower'

    def start(self):
        # sprawdza czy zaladowala sie poprawna strona
        if self.service.getTitle() != self.title:
            return False
        # jezeli na stronie pojawia sie okno z reklama, test znajduje odpowiedni przycisk zamykajacy ja i go klika
        if self.service.getFindElementbySelector("div._4f735_Ag0om._ur8qq > div > div._3kk7b._vnd3k._1h8s6._13prn._12isx._kiiea._oeb1x > button").click():
            pass
        #wywolanie funkcji serch
        self.getSearch()
        #wywolanie funkcji zamykajacej sesje
        self.service.sesionClose()
        return True

    def search(self):
        # znalezienie pola tekstowego "szukaj"
        self.look_for = self.service.getFindElementbyName("string")
        # przeslanie wartosci do sekcji "szukaj"
        self.look_for.send_keys(self.serch_item)
        # nacisniecie przycisku Enter w celu zatwierdzenia podanej wartosci
        self.service.getAkcept(self.look_for)
        #wywolanie funkcji sort()
        self.sort()

    def sort(self):
        #znalezienie pola odpowiedzialnego za sortowanie a nastepnie wybranie odpowiedniej opcji i zatwierdzenie jej metoda click()
        self.service.getFindElementbySelector("div._e219d_jjqRf > div._e219d_1LGAZ > div > div > div > div > div > select > option:nth-child(3)").click()