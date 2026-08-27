# Web Scraping using Python

## CodeAlpha Data Analytics Internship – Task 1

### 📌 Project Overview

This project is completed as part of the **CodeAlpha Data Analytics Internship**.

**Task 1: Web Scraping using Python**

The objective of this task is to collect product data from an online API using Python, process and clean the collected data, perform basic data analysis, and create a meaningful data visualization.

For this project, the **DummyJSON Products API** was used to collect **100 product records**. The collected data was processed using Pandas, analyzed using basic statistical methods, and visualized using Matplotlib.

The final processed dataset was successfully saved as a **CSV file containing 100 product records**, and a category distribution chart was created.

---

## 🎯 Task Objectives

The main objectives of this task are:

- Collect product data using Python.
- Extract 100 product records from an online API.
- Convert JSON data into a structured Pandas DataFrame.
- Clean and organize the collected data.
- Handle missing brand values.
- Perform basic data analysis.
- Analyze product categories.
- Create a product category distribution chart.
- Save the processed data as a CSV file.

---

## 🌐 Data Source

Product data was collected from the **DummyJSON Products API**.

**API Endpoint:**

https://dummyjson.com/products?limit=100

The API provides product information such as:

- Product ID
- Product Title
- Price
- Category
- Brand
- Rating
- Stock
- Discount Percentage

---

## 🛠️ Technologies Used

| Technology / Library | Purpose |
|---|---|
| Python | Programming and data processing |
| Requests | Fetching product data from the API |
| Pandas | Data cleaning, processing and analysis |
| Matplotlib | Data visualization |
| DummyJSON API | Product data source |

---

## 🔄 Project Workflow

```text
DummyJSON Products API
        ↓
Send API Request
        ↓
Receive JSON Data
        ↓
Extract 100 Product Records
        ↓
Create Pandas DataFrame
        ↓
Clean and Process Data
        ↓
Handle Missing Brand Values
        ↓
Perform Data Analysis
        ↓
Analyze Product Categories
        ↓
Create Visualization
        ↓
Save Dataset as CSV
