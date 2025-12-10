# item_data.py

ITEM_PRICES = {
    "farm_cabbage03.png": 30,
}

def get_price(item_name):
    return ITEM_PRICES.get(item_name, None)
