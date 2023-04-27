import functions.fetchSteam as steam
import functions.tradeup as trade

data = {
    "wear": "fn",
    #"collection": "danger_zone",
    "quality": "normal",
    #"category": "mil-spec"
}

if __name__ == '__main__':
    #url = steam.make_url(data)
    #print(url)
    #res = steam.get_data(url)
    #print(res)

    #tmp = trade.ratio("mil-spec", "restricted", data)
    #print(tmp)

    res = trade.best_ratio("mil-spec", "restricted", data)
    print(res)
