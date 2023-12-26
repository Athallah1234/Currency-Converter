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
   ```python
   git clone https://github.com/Athallah1234/Currency-Converter.git
   cd currency-converter-app
   ```
2. **Install Dependencies**:
   ```python
   pip install -r requirements.txt
   ```
3. **Run the Application**:
   ```python
   python currency_converter.py
   ```
4. **Input Information**:
   - Enter the amount to convert.
   - Select the source and target currencies from the dropdown lists.
   - Optionally, adjust the decimal precision.
   - Click the "Convert" button to perform the currency conversion.
5. **Swap Currencies**:
   - Use the "Swap Currencies" button to quickly switch between the source and target currencies.
6. **Handle Errors**:
   - The application provides informative error messages for invalid inputs or network-related issues.

## Contributing

We welcome contributions from the community! To contribute to the Currency Converter App, follow these steps:

1. **Fork the Repository**:
   - Click the "Fork" button at the top-right corner of this repository to create your own copy.
2. **Clone Your Fork**:
   ```python
   git clone https://github.com/Athallah1234/Currency-Converter.git
   cd currency-converter-app
   ```
3. **Create a Branch**:
   - Create a new branch for your feature or bug fix.
     ```python
     git checkout -b feature-name
     ```
4. **Make Changes**:
   - Implement your changes or additions to the code.
5. **Test Your Changes**:
   - Ensure that your modifications work as intended.
6. **Push Changes**:
   - Push your changes to your fork.
     ```python
     git push origin feature-name
     ```
7. **Create a Pull Request**:
   - Open a pull request from your fork to the main repository.
8. **Discuss and Review**:
   - Engage in discussions, address feedback, and iterate on your changes.
9. **Merge**:
   - Once your changes are approved, they will be merged into the main codebase.

## License

This Currency Converter App is open-source and available under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code.
