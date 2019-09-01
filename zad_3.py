import service

class Main():
    def __init__(self):
        self.service = service.Service('http://allegro.pl')
        self.title = 'Allegro.pl – najlepsze ceny, największy wybór i zawsze bezpieczne zakupy online'
        self.serch_item = 'rower'

    def start(self):
        if self.service.getTitle() != self.title:
            return False
        if self.service.getFindElementbySelector("div._4f735_Ag0om._ur8qq > div > div._3kk7b._vnd3k._1h8s6._13prn._12isx._kiiea._oeb1x > button").click():
            pass
        self.search()
        self.service.sesionClose()
        return True

    def search(self):
        self.search = self.service.getFindElementbyName("string")
        self.search.send_keys(self.serch_item)
        self.service.getAkcept(self.search)
        self.sort()

    def sort(self):
        self.service.getFindElementbySelector("div._e219d_jjqRf > div._e219d_1LGAZ > div > div > div > div > div > select > option:nth-child(3)").click()