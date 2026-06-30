import random
import time

def build_fix_message(fields):
    trade = []
    for key, value in fields.items():
        word = f"{key}={value}"
        trade.append(word)
        
    s = "|".join(trade)

    return s

def make_random_trade():
    message = "8"
    ticker = random.choice(["AAPL", "TSLA", "MSFT"])
    side = random.randint(1, 2)
    quantity = random.randrange(1, 1000)
    price = random.randint(1, 200)

    return {"35": message, "55": ticker, "54": side, "38": quantity, "44": price}    

for i in range(10):
    time.sleep(1)
    print(build_fix_message(make_random_trade()))