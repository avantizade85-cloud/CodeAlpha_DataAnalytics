# Web Scraping using Python
## CodeAlpha Data Analytics Internship – Task 1

## 📌 Project Overview
This project is completed as part of the CodeAlpha Data Analytics Internship.
This project focuses on Task 1: Web Scraping using Python.
The objective is to collect product data from an online API.
The DummyJSON Products API is used as the data source.
A total of 100 product records are collected from the API.
The collected data is processed using Python and Pandas.
Basic data cleaning and analysis are performed on the dataset.
Product categories are also analyzed using Pandas.
A category distribution chart is created using Matplotlib.
The final dataset is saved in CSV format.

## 🎯 Objectives
- Collect product data using Python.
- Extract 100 product records from an online API.
- Store the collected data in a structured DataFrame.
- Clean and process the collected product information.
- Handle missing brand values.
- Perform basic statistical analysis.
- Analyze product categories.
- Create a category distribution visualization.
- Save the final dataset as a CSV file.

## 🌐 Data Source
The product data is collected from the DummyJSON Products API.
API Endpoint: https://dummyjson.com/products?limit=100
The API provides product-related information.
The available information includes product ID and title.
It also includes price, category, and brand.
The API also provides rating, stock, and discount percentage.

## 🛠️ Technologies Used
- Python
- Requests
- Pandas
- Matplotlib
- DummyJSON Products API

## 📊 Dataset Information
The final dataset contains 100 product records.
The dataset contains 8 columns.
Product_ID represents the unique product identification number.
Title represents the name of the product.
Price represents the product price.
Category represents the product category.
Brand represents the product brand.
Rating represents the product rating.
Stock represents the available stock quantity.
Discount_Percentage represents the product discount percentage.

## 🧹 Data Cleaning
Basic data cleaning is performed on the collected data.
Missing or empty brand values are handled appropriately.
Missing brand values are replaced with "Not Available".
This makes the dataset more consistent for analysis.

## 📈 Data Analysis
The total number of products is calculated.
The average product price is calculated.
The highest product price is identified.
The lowest product price is identified.
The average product rating is calculated.
Product category distribution is analyzed.
Total Products: 100
Average Price: 646.68
Highest Price: 13,999.99
Lowest Price: 0.79
Average Rating: 3.85

## 📊 Category Distribution
Kitchen Accessories contains 30 products.
Groceries contains 27 products.
Men's Watches contains 6 products.
Beauty contains 5 products.
Fragrances contains 5 products.
Furniture contains 5 products.
Home Decoration contains 5 products.
Laptops contains 5 products.
Men's Shirts contains 5 products.
Men's Shoes contains 5 products.
Mobile Accessories contains 2 products.
A category distribution chart is created using Matplotlib.

## 📁 Project Files
Web_Scrapping.py contains the Python source code.
product_dataset.csv contains the 100 collected product records.
category_distribution.png contains the category distribution chart.
README.md contains the project documentation.

## 📚 Learning Outcomes
This project provided practical experience in Python programming.
It improved understanding of web scraping and API data collection.
It provided experience in handling JSON data.
It improved knowledge of Pandas DataFrames.
It provided experience in data cleaning and processing.
It introduced basic statistical analysis.
It improved understanding of data aggregation.
It provided practical experience in data visualization.
It provided experience in generating CSV files.
It demonstrated a basic real-world data analytics task.


## 📝 Conclusion
This project successfully completed Task 1 of the CodeAlpha Data Analytics Internship.
Using Python and the DummyJSON Products API, web scraping was performed to collect product data.
A total of 100 product records were successfully collected.
The collected data was processed and a CSV file containing 100 records was created.
The final CSV file is named product_dataset.csv.
The data was cleaned and analyzed using Pandas.
A category distribution chart was created using Matplotlib.
Overall, this project provided practical experience in web scraping, data collection, data cleaning, data analysis, CSV file creation, and data visualization.
The task was successfully completed with 100 product records and the required output files.
