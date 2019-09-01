import service
import time


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
        return self.condition()

    def search(self):
        self.look_for = self.service.getFindElementbyName("string")
        self.look_for.send_keys(self.serch_item)
        self.service.getAkcept(self.look_for)
        self.first_bicycle = self.service.getFindElementbySelector("div.bf8839e").text
        self.auction_on_page = self.service.getFindElementsbySelector("div.bf8839e")
        print("price first bicycle: ", self.first_bicycle)

    def condition(self):
        self.first_bicycle_prince = self.first_bicycle.split(',')[0].replace(' ', '')
        self.price_in_zl = []
        self.price_in_gr = []
        if int(self.first_bicycle_prince) < 500:
            self.first_condition()
            self.service.sesionClose()
            return True
        elif int(self.first_bicycle_prince) > 721:
            self.second_condition()
            self.service.sesionClose()
            return True
        else:
            self.service.sesionClose()
            return False
    def first_condition(self):
        if len(self.auction_on_page) >= 5:
            for i in self.auction_on_page[0:5]:
                self.price_in_zl.append(i.text.split(',')[0].replace(" ", ''))
                self.price_in_gr.append(i.text.split(',')[1].split()[0])
            self.price_in_zl = list(map(int, self.price_in_zl))
            self.price_in_gr = list(map(int, self.price_in_gr))
            self.price_in_zl = sum(self.price_in_zl)
            self.price_in_gr = sum(self.price_in_gr) / 100
            print("value of the first 5 items : ", self.price_in_zl + self.price_in_gr, "zl")

    def second_condition(self):
        self.service.getFindElementbySelector("div._e219d_jjqRf > div._e219d_1LGAZ > div > div > div > div > div > select > option:nth-child(2)").click()
        self.min_price_all = []
        time.sleep(2)
        self.min_price = self.service.getFindElementsbySelector("span.fee8042")
        for price in self.min_price:
            self.min_price_all.append(price.text.split('zł')[0].replace(" ", '').replace(",", '.'))
        self.min_price_all = min(list(map(float, self.min_price_all)))
        self.service.getFindElementbySelector("div._e219d_jjqRf > div._e219d_1LGAZ > div > div > div > div > div > select > option:nth-child(3)").click()
        self.max_price_all = []
        time.sleep(2)
        self.max_price = self.service.getFindElementsbySelector("span.fee8042")
        for price in self.max_price:
            self.max_price_all.append(price.text.split('zł')[0].replace(" ", '').replace(",", '.'))
        self.max_price_all = max(list(map(float, self.max_price_all)))
        print("delta price : ", self.max_price_all - self.min_price_all)