
import tkinter as tk
from tkinter import ttk
import requests

class BitcoinPriceConverter(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("400x180")
        self.title("Bitcoin-Preis-Rechner")

        BitcoinToEuroFrame(self).pack(fill='both')

class BitcoinToEuroFrame(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        self.COINDESK_API_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"
        self.euro_value = tk.StringVar(value="Hier wird dann der Preis in Euro angezeigt")

        bitcoin_label = ttk.Label(self, text="Anzahl Bitcoin:", font=("Arial", 15))
        bitcoin_label.pack(side="top", fill="x", padx=5, pady=2)

        self.bitcoin_entry = ttk.Entry(self, font=("Arial", 15))
        self.bitcoin_entry.pack(side="top", fill="x", padx=5, pady=2)

        euro_label = ttk.Label(self, text="Preis in Euro:", font=("Arial", 15))
        euro_label.pack(side="top", fill="x", padx=5, pady=2)

        euro_display = ttk.Label(self, textvariable=self.euro_value, font=("Arial", 15))
        euro_display.pack(side="top", fill="x", padx=5, pady=2)

        calculate_button = ttk.Button(self, text="Berechnung durchführen", command=self.calculate_price)
        calculate_button.pack(side="bottom", fill="x", padx=10, pady=10)

    def calculate_price(self):
        try:
            response = requests.get(self.COINDESK_API_URL)
            response_dict = response.json()
            current_bitcoin_price_euro = response_dict["bpi"]["EUR"]["rate_float"]
            calculated_price_euro = float(self.bitcoin_entry.get()) * current_bitcoin_price_euro
            self.euro_value.set("{:.2f}".format(calculated_price_euro))
        except ValueError:
            print("Bitte gültigen Zahlenwert eingeben!")

root = BitcoinPriceConverter()

root.mainloop()