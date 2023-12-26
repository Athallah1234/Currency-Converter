import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates
import logging
import traceback

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        # Set up variables
        self.amount_var = tk.DoubleVar()
        self.from_currency_var = tk.StringVar()
        self.to_currency_var = tk.StringVar()
        self.precision_var = tk.IntVar(value=2)  # Default precision is set to 2
        self.result_var = tk.StringVar()

        # Set up logging
        logging.basicConfig(filename='currency_converter.log', level=logging.ERROR)

        # Create and place widgets
        self.create_widgets()
        self.place_widgets()

    def create_widgets(self):
        # Labels
        tk.Label(self.root, text="Amount:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.root, text="From Currency:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.root, text="To Currency:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.root, text="Result:").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.root, text="Decimal Precision:").grid(row=5, column=0, padx=10, pady=10, sticky="w")

        # Entry widgets
        ttk.Entry(self.root, textvariable=self.amount_var).grid(row=0, column=1, padx=10, pady=10)
        ttk.Combobox(self.root, values=self.get_currency_list(), textvariable=self.from_currency_var).grid(row=1, column=1, padx=10, pady=10)
        ttk.Combobox(self.root, values=self.get_currency_list(), textvariable=self.to_currency_var).grid(row=2, column=1, padx=10, pady=10)

        # Result label
        ttk.Label(self.root, textvariable=self.result_var).grid(row=4, column=1, padx=10, pady=10, sticky="w")

        # Precision entry
        ttk.Entry(self.root, textvariable=self.precision_var).grid(row=5, column=1, padx=10, pady=10)

        # Convert button
        ttk.Button(self.root, text="Convert", command=self.convert_currency).grid(row=3, column=1, pady=10)

        # Swap button
        ttk.Button(self.root, text="Swap Currencies", command=self.swap_currencies).grid(row=3, column=0, pady=10)

    def place_widgets(self):
        # Adjust column weights
        self.root.columnconfigure(1, weight=1)

        # Set row and column weights
        for i in range(6):
            self.root.rowconfigure(i, weight=1)

    def get_currency_list(self):
        # Fetch a list of currency codes
        currency_rates = CurrencyRates()
        currencies = currency_rates.get_rates('USD')
        return list(currencies.keys())

    def convert_currency(self):
        try:
            # Get user inputs
            amount = float(self.amount_var.get())
            from_currency = self.from_currency_var.get()
            to_currency = self.to_currency_var.get()
            precision = int(self.precision_var.get())

            # Validate currencies
            if from_currency not in self.get_currency_list() or to_currency not in self.get_currency_list():
                raise ValueError("Invalid currency selection.")

            # Perform currency conversion
            currency_rates = CurrencyRates()
            rate = currency_rates.get_rate(from_currency, to_currency)
            result = round(amount * rate, precision)

            # Update result label
            self.result_var.set(f"{amount} {from_currency} = {result} {to_currency}")

        except ValueError as ve:
            # Handle invalid input (non-numeric or invalid currency)
            self.result_var.set(str(ve))
            self.log_error(ve)
        except Exception as e:
            # Handle other exceptions (e.g., network issues)
            self.result_var.set(f"Error: {str(e)}")
            self.log_error(e)

    def swap_currencies(self):
        # Get current values
        current_from_currency = self.from_currency_var.get()
        current_to_currency = self.to_currency_var.get()

        # Swap values
        self.from_currency_var.set(current_to_currency)
        self.to_currency_var.set(current_from_currency)

    def log_error(self, error):
        # Log the error to the file
        logging.error("Error occurred: %s", str(error))
        logging.error(traceback.format_exc())

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()

