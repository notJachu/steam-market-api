import requests as rq
import json
import functions.params as par
import time

base_url = "https://steamcommunity.com/market/search/render/?q="


def make_url(options):
    url = ""
    url += base_url
    if "wear" in options:
        url += "&category_730_Exterior%5B%5D=" + par.wear[options["wear"]]

    if "quality" in options:
        url += "&category_730_Quality%5B%5D=" + par.quality[options["quality"]]

    if "category" in options:
        url += "&category_730_Rarity%5B%5D=" + par.category[options["category"]]

    if "collection" in options:
        url += "&category_730_ItemSet%5B%5D=" + par.collections[options["collection"]]


    url += "&sort_dir=desc" \
           "&appid=730" \
           "&norender=1" \
           "&count=500"
    return url


def test():
    res = rq.get('https://steamcommunity.com/market/search/render/?search_descriptions='
                 '&category_730_ItemSet%5B%5D=tag_set_community_21'
                 '&sort_column=default'
                 '&category_730_Exterior%5B0%5D=tag_WearCategory0'
                 '&category_730_Quality%5B%5D=tag_normal'
                 '&sort_dir=desc'
                 '&appid=730'
                 '&norender=1'
                 '&count=500')

    response = json.loads(res.text)
    print(response['results'])
    for a in response['results']:
        print(a['name'], a['sell_price_text'])


def get_data(url):
    result = []
    res = rq.get(url)
    print(res)
    if res.status_code == 429:
        print("steam gave up lol")
        time.sleep(10)
        print("hope")
    response = json.loads(res.text)
    if response["total_count"] == 0:
        return False
    for a in response['results']:
        result.append([a["name"], int(a["sell_price"]) / 100])

    return result

# print(make_url(data))
