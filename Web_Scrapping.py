import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import os

# Website URL
url = "https://dummyjson.com/products?limit=100"

# Get webpage
response = requests.get(url)

# Convert JSON into readable format
data = response.json()

# Extract product data
products = data["products"]

# Store scraped data
product_data = []

# Extract information from each product
for product in products:

    product_id = product.get("id")
    title = product.get("title")
    price = product.get("price")
    category = product.get("category")
    brand = product.get("brand", "Not Available")
    rating = product.get("rating")
    stock = product.get("stock")
    discount = product.get("discountPercentage")

    # Handle missing brand
    if not brand:
        brand = "Not Available"

    product_data.append({
        "Product_ID": product_id,
        "Title": title,
        "Price": price,
        "Category": category,
        "Brand": brand,
        "Rating": rating,
        "Stock": stock,
        "Discount_Percentage": discount
    })

# Create DataFrame
df = pd.DataFrame(product_data)

# Display dataset
print("\nDataset:")
print(df)

# Basic Analysis
print("\nTotal Products:", len(df))
print("Average Price:", round(df["Price"].mean(), 2))
print("Highest Price:", df["Price"].max())
print("Lowest Price:", df["Price"].min())
print("Average Rating:", round(df["Rating"].mean(), 2))

# Category Analysis
category_counts = df["Category"].value_counts()

print("\nCategory Distribution:")
print(category_counts)

# Get current project folder
folder = os.path.dirname(os.path.abspath(__file__))

# Save dataset
csv_path = os.path.join(folder, "product_dataset.csv")
df.to_csv(csv_path, index=False)

# Create Category Distribution Chart
plt.figure(figsize=(12, 6))

plt.bar(
    category_counts.index,
    category_counts.values
)

plt.title("Product Category Distribution")
plt.xlabel("Category")
plt.ylabel("Number of Products")

plt.xticks(rotation=45)
plt.tight_layout()

# Save chart
chart_path = os.path.join(
    folder,
    "category_distribution.png"
)

plt.savefig(chart_path)

# Display chart
plt.show()

print("\nDataset and chart created successfully!")
print("Total Records:", len(df))
print("CSV File:", csv_path)
print("Chart File:", chart_path)