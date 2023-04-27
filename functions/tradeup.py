import functions.fetchSteam as steam
import functions.params as par


def make_tradeup(options, allow_filler=False):
    options["category"] = "mil-spec"
    url = steam.make_url(options)
    blue = steam.get_data(url)
    options["category"] = "restricted"
    url = steam.make_url(options)
    purple = steam.get_data(url)


def ratio(c1, c2, opt):
    opt["category"] = c1
    url = steam.make_url(opt)
    r1 = steam.get_data(url)
    opt["category"] = c2
    url = steam.make_url(opt)
    r2 = steam.get_data(url)
    if not r2 or not r1:
        return False
    #print(f"{c1}: {r1}")
    #print(f"{c2}: {r2}")
    a1 = 0
    a2 = 0
    for i in r1:
        a1 += i[1]
    a1 /= len(r1)

    for i in r2:
        a2 += i[1]
    a2 /= len(r2)

    return [opt["collection"], a2/a1]


def best_ratio(c1, c2, opt):
    res = []

    for a in par.collections:
        opt["collection"] = a
        k = ratio(c1, c2, opt)
        if k:
            res.append(k)
        else:
            print(f"failed for {a}")

    return res
