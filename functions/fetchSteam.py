import requests as rq
import json

collections = {
    "broken_fang_agents": "tag_set_op10_characters",
    "riptide_agents": "tag_set_op11_characters",
    "shattered_web_agents": "tag_set_op9_characters",
    "inferno_2": "tag_set_inferno_2",
    "nuke_2": "tag_set_nuke_2",
    "dd2_2": "tag_set_dust_2_2021",
    "mirage_2": "tag_set_mirage_2021",
    "train_2": "tag_set_train_2021",
    "vertigo_2": "tag_set_vertigo_2021",
    "alpha": "tag_set_bravo_ii",
    "ancient": "tag_set_op10_ancient",
    "arms_deal_2": "tag_set_weapons_ii",
    "arms_deal_3": "tag_set_weapons_iii",
    "arms_deal_1": "tag_set_weapons_i",
    "assault": "tag_set_assault",
    "aztec": "tag_set_aztec",
    "baggage": "tag_set_baggage",
    "bank": "tag_set_bank",
    "blacksite": "tag_set_blacksite",
    "bravo": "tag_set_bravo_i",
    "brakout": "tag_set_community_4",
    "cache": "tag_set_cache",
    "canals": "tag_set_canals",
    "chop_shop": "tag_set_chopshop",
    "chroma_2": "tag_set_community_7",
    "chroma_3": "tag_set_community_12",
    "chroma": "tag_set_community_6",
    "clutch": "tag_set_community_19",
    "cbbl": "tag_set_cobblestone",
    "control": "tag_set_op10_ct",
    "cs20": "tag_set_community_24",
    "danger_zone": "tag_set_community_21",
    "dreams_and_nightmares": "tag_set_community_30",
    "dd2": "tag_set_dust_2",
    "dust": "tag_set_dust",
    "es_2013": "tag_set_esports",
    "es_winter_2013": "tag_set_esports_ii",
    "es_2014": "tag_set_esports_iii",
    "falchion": "tag_set_community_8",
    "fracture": "tag_set_community_26",
    "gamma_2": "tag_set_gamma_2",
    "gamma": "tag_set_community_13",
    "glove": "tag_set_community_15",
    "gods_and_monsters": "tag_set_gods_and_monsters",
    "havoc": "tag_set_op10_t",
    "horizon": "tag_set_community_20",
    "huntsman": "tag_set_community_3",
    "inferno": "tag_set_inferno",
    "italy": "tag_set_italy",
    "lake": "tag_set_lake",
    "militia": "tag_set_militia",
    "mirage": "tag_set_mirage",
    "norse": "tag_set_norse",
    "nuke": "tag_set_nuke",
    "office": "tag_set_office",
    "broken_fang": "tag_set_community_27",
    "hydra": "tag_set_community_17",
    "riptide": "tag_set_community_29",
    "overpass": "tag_set_overpass",
    "phoenix": "tag_set_community_2",
    "prisma_2": "tag_set_community_25",
    "prisma": "tag_set_community_22",
    "recoil": "tag_set_community_31",
    "revolution": "tag_set_community_32",
    "revolver": "tag_set_community_10",
    "rising_sun": "tag_set_kimono",
    "safehouse": "tag_set_safehouse",
    "shadow": "tag_set_community_9",
    "shattered_web": "tag_set_community_23",
    "snakebite": "tag_set_community_28",
    "spectrum_2": "tag_set_community_18",
    "spectrum": "tag_set_community_16",
    "st_marc": "tag_set_stmarc",
    "train": "tag_set_train",
    "vanguard": "tag_set_community_5",
    "vertigo": "tag_set_vertigo",
    "wildfire": "tag_set_community_11",
    "winter_offensive": "tag_set_community_1",
    "x-ray": "tag_set_xraymachine"

}

wear = {
    "fn": "tag_730_Exterior_WearCategory0",
    "mw": "tag_730_Exterior_WearCategory1",
    "ft": "tag_730_Exterior_WearCategory2",
    "ww": "tag_730_Exterior_WearCategory3",
    "bs": "tag_730_Exterior_WearCategory4"
}

category = {
    "normal": "tag_730_Quality_normal",
    "souvenir": "tag_730_Quality_tournament",
    "stattrak": "tag_730_Quality_strange",
    "unusual": "tag_730_Quality_unusual",
    "unusual_st": "tag_730_Quality_unusual_strange"
}

quality = {
    "consumer": "tag_730_Rarity_Rarity_Common_Weapon",
    "mil-spec": "tag_730_Rarity_Rarity_Rare_Weapon",
    "restricted": "tag_730_Rarity_Rarity_Mythical_Weapon",
    "industrial": "tag_730_Rarity_Rarity_Uncommon_Weapon",
    "classified": "tag_730_Rarity_Rarity_Legendary_Weapon",
    "covert": "tag_730_Rarity_Rarity_Ancient_Weapon",
    "base": "tag_730_Rarity_Rarity_Common",
    "distinguished": "tag_730_Rarity_Rarity_Rare_Character",
    "extraordinary": "tag_730_Rarity_Rarity_Ancient",
    "superior": "tag_730_Rarity_Rarity_Legendary_Character",
    "exceptional": "tag_730_Rarity_Rarity_Mythical_Character",
    "master": "tag_730_Rarity_Rarity_Ancient_Character",
    "high_grade": "tag_730_Rarity_Rarity_Rare",
    "remarkable": "tag_730_Rarity_Rarity_Mythical",
    "exotic": "tag_730_Rarity_Rarity_Legendary",
    "contraband": "tag_730_Rarity_Rarity_Contraband"
}

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
