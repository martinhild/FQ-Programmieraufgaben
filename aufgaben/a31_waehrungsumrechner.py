"""
Liest Betrag in Euro ein und gibt ihn in US-Dollar auf zwei Stellen gerundet aus.
"""
from utils import user_inputs

EUR_TO_USD = 1.1163

def euro_to_usd(euro):
    return euro * EUR_TO_USD

def main():
    print("Euro: ", end = "")
    euro = user_inputs.get_float()
    usd = euro_to_usd(euro)
    print(f"{euro} Euro are {usd:.2f} USD")

if __name__ == "__main__":
    main()