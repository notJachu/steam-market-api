import fetchSteam as steam
import functions.params as par


def make_tradeup(options, allow_filler=False):
    options["category"] = "mil-spec"
    url = steam.make_url(options)
    blue = steam.get_data(url)
    options["category"] = "restricted"
    url = steam.make_url(options)
    purple = steam.get_data(url)
