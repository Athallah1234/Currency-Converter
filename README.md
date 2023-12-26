# Currency Converter App

This simple Currency Converter application allows users to convert between different currencies using real-time exchange rates. It is implemented in Python using the Tkinter library for the graphical user interface and the forex_python library to fetch currency exchange rates.

## Features

- **User-friendly Interface**: The application provides a clean and intuitive interface for users to input the amount, select the source and target currencies, and view the converted result.
- **Real-time Exchange Rates**: The app fetches real-time exchange rates using the forex_python library, ensuring accurate and up-to-date currency conversions.
- **Decimal Precision Control**: Users can specify the precision of the decimal places in the converted result, providing flexibility in displaying the desired level of detail.
- **Error Handling**: The application includes robust error handling to deal with invalid inputs (e.g., non-numeric values, invalid currency selections) and other exceptions that may arise during the conversion process.
- **Logging**: Errors are logged to a file (currency_converter.log), facilitating troubleshooting and providing a record of issues encountered.

## Usage

1. **Clone the Repository**:
   ``python
   git clone https://github.com/your-username/currency-converter-app.git
   cd currency-converter-app
   ``
2. **Install Dependencies**:
   ``python
   pip install -r requirements.txt
   ``
3. **Run the Application**:
   ``python
   python currency_converter.py
   ``
4. **Input Information**:
   - Enter the amount to convert.
   - Select the source and target currencies from the dropdown lists.
   - Optionally, adjust the decimal precision.
   - Click the "Convert" button to perform the currency conversion.
5. **Swap Currencies**:
   - Use the "Swap Currencies" button to quickly switch between the source and target currencies.
6. **Handle Errors**:
   - The application provides informative error messages for invalid inputs or network-related issues.
