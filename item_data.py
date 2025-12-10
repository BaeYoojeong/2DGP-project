# item_data.py

ITEM_PRICES = {
    "farm_cabbage03.png": 10,
    "farm_carrot03.png": 20
}

def get_price(item_name):
    return ITEM_PRICES.get(item_name, None)
