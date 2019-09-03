import service

class functions():

    def __init__(self):
        self.set_url = service.Service()

    def url(self, adress_url, title, advertisment):
        self.set_url.website(adress_url)
        if self.set_url.getFindElementbySelector(advertisment).click():
            pass
        assert title in self.set_url.getTitle()

    def search(self, item, search_name, title):
        look_for = self.set_url.getFindElementbyName(search_name)
        look_for.clear()
        look_for.send_keys(item)
        self.set_url.getAkcept(look_for)
        assert title.lower() in self.set_url.getTitle().lower()

    def getFirst_price(self, selector):
        return self.set_url.getFindElementbySelector(selector)

    def getAll_auctions(self, selector):
        return self.set_url.getFindElementbySelector(selector)

    def getAuctions_per_page(self, selector):
        return self.set_url.getFindElementsbySelector(selector)

    def close(self):
        self.set_url.sesionClose()
