import functions.fetchSteam as steam


data = {
    "wear": "fn",
    "collection": "danger_zone",
    "quality": "normal",
    "category": "mil-spec"
}

if __name__ == '__main__':
    url = steam.make_url(data)
    print(url)
    res = steam.get_data(url)
    print(res)

