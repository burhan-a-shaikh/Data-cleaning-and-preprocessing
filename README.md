# Sales Data Cleaning – Internship Task 1



##  Objective

To clean a real-world sales dataset by handling missing data, formatting inconsistencies, and duplicates—preparing it for further analysis or visualization.

## 🛠 Tools Used

- **Language:** Python 3.13
- **Libraries:** pandas
- **IDE:** Visual Studio Code
- **Version Control:** Git & GitHub Desktop (Windows 11)

##  Key Cleaning Steps

1. **Missing Values**
   - Filled blank address/state fields with defaults.
   - Used median values to replace missing numerical entries.

2. **Text Standardization**
   - Lowercased and stripped whitespace from categorical columns.
   - Removed unwanted characters like tabs or newlines.

3. **Date Formatting**
   - Converted `ORDERDATE` to a consistent datetime format.

4. **Column Renaming**
   - Normalized all column names to lowercase with underscores.

5. **Data Type Fixes**
   - Converted price, quantity, and other metrics to numeric types.

6. **Duplicate Handling**
   - Removed duplicate rows based on order number, product code, and line item.

7. **New Feature**
   - Calculated `order_total` as `quantityordered * priceeach`.

##  Files

- `sales_data_sample.csv`: Original dataset (from Kaggle)
- `cleaned_sales_data.csv`: Cleaned and formatted output
- `clean_sales_dataset.py`: Python script for preprocessing

##  Dataset Source

[Kaggle - Sales Data Sample](https://www.kaggle.com/datasets/kyanyoga/sample-sales-data)

