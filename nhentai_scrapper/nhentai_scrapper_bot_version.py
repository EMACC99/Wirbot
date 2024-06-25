import requests
import bs4 as bs


URL = "https://nhentai.net/"
SEARCH_URL = "https://nhentai.net/search/?q="


class bot_scrapper:
    @staticmethod
    def get_codes(doujins):
        codes = []
        for doujin in doujins:
            soup2 = bs.BeautifulSoup(str(doujin), "lxml")
            code = soup2.find("a", href=True)
            code = code["href"]
            if code is None:
                continue
            codes.append(code)
        return codes

    @staticmethod
    def get_front_page():
        req = requests.get(URL)
        if not req.ok:
            return req.status_code
        soup = bs.BeautifulSoup(req.content, "lxml")
        doujins = soup("a")[17:-8]
        return bot_scrapper.get_codes(doujins)

    @staticmethod
    def search(keywords):
        # search_url = "https://nhentai.net/search/?q="
        search_str = keywords.replace(" ", "+")
        req = requests.get(SEARCH_URL + search_str)
        if not req.ok:
            return req.status_code
        soup = bs.BeautifulSoup(req.content, "lxml")
        doujins = soup("a")[21:-8]
        if len(doujins) == 0:
            doujins = soup("a")[21:]

        return bot_scrapper.get_codes(doujins)
