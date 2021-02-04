import requests
import bs4 as bs

url = "https://nhentai.net/"
search_url = "https://nhentai.net/search/?q="

def get_codes(doujins):
    codes = []
    for doujin in doujins:
        soup2 = bs.BeautifulSoup(str(doujin), 'lxml')
        code = soup2.find('a', href=True)
        code = code['href']
        if code is None:
            continue
        # print(f"{title}, {code}")
        codes.append(code)
    return codes

def get_front_page():
    req = requests.get(url)
    if not req.ok:
        return req.status_code
    soup = bs.BeautifulSoup(req.content, 'lxml')
    doujins = soup("a")[17:-8]
    return get_codes(doujins)


def search(keywords):
    # print(keywords)
    search_url = "https://nhentai.net/search/?q="
    # search_str = ' '
    # search_str = search_str.join(keywords)
    search_str = keywords.replace(' ', '+')
    # print("search_str:", search_str)
    # print(search_url+search_str)
    req = requests.get(search_url+search_str)
    if not req.ok:
        return req.status_code
    soup = bs.BeautifulSoup(req.content, 'lxml')
    doujins = soup('a')[21:-8]
    if len(doujins) == 0:
        doujins = soup('a')[21:]

    return get_codes(doujins)