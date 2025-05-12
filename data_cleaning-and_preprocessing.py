import pandas as pd

def preprocess_sales_data(input_path, output_path):
    try:
        data = pd.read_csv(input_path, encoding='ISO-8859-1')
    except Exception as error:
        print("Failed to read CSV:", error)
        return

    # Filling common missing values
    filler = {
        'ADDRESSLINE2': '',
        'STATE': '',
        'POSTALCODE': '',
        'TERRITORY': 'not_specified'
    }
    data.fillna(value=filler, inplace=True)

    # Replace missing numeric data with median
    numeric = data.select_dtypes(include='number').columns
    data[numeric] = data[numeric].fillna(data[numeric].median())

    # Clean and normalize text columns
    text_fields = [
        'COUNTRY', 'STATUS', 'DEALSIZE', 'PRODUCTLINE', 'CITY', 'CUSTOMERNAME',
        'PRODUCTCODE', 'ADDRESSLINE1', 'ADDRESSLINE2', 'STATE', 'POSTALCODE',
        'TERRITORY', 'CONTACTLASTNAME', 'CONTACTFIRSTNAME'
    ]
    for field in text_fields:
        if field in data.columns:
            data[field] = data[field].astype(str).str.lower().str.strip().str.replace(r'[\r\n\t]', '', regex=True)

    # Format date column
    if 'ORDERDATE' in data.columns:
        data['ORDERDATE'] = pd.to_datetime(data['ORDERDATE'], errors='coerce')
        data.dropna(subset=['ORDERDATE'], inplace=True)

    # Clean column headers
    data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_')

    # Ensure correct numeric formats
    for col in ['quantityordered', 'priceeach', 'sales', 'msrp']:
        if col in data.columns:
            data[col] = pd.to_numeric(data[col], errors='coerce')

    # Compute total value per order line
    if {'quantityordered', 'priceeach'}.issubset(data.columns):
        data['order_total'] = data['quantityordered'] * data['priceeach']

    # Drop duplicate entries based on key identifiers
    if {'ordernumber', 'productcode', 'orderlinenumber'}.issubset(data.columns):
        data.drop_duplicates(subset=['ordernumber', 'productcode', 'orderlinenumber'], inplace=True)

    # Save the final cleaned data
    try:
        data.to_csv(output_path, index=False)
        print(f"Cleaned file saved at: {output_path}")
    except Exception as error:
        print("Saving failed:", error)

if __name__ == "__main__":
    preprocess_sales_data("sales_data_sample.csv", "cleaned_sales_data.csv")
