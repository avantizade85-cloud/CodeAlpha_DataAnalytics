# Task 1 - Web Scraping

## Project Overview

This project is completed as part of the CodeAlpha Data Analytics Internship.

The objective of this project is to collect book information from a public website using Python web scraping techniques and create a structured dataset.

## Website Used

Books to Scrape

Website:
https://books.toscrape.com/

## Tools and Technologies

- Python
- Requests
- BeautifulSoup
- Pandas
- Matplotlib
- VS Code

## Data Collected

The following information was extracted from the website:

- Book Title
- Price
- Availability
- Rating

A total of 20 books were scraped from the website.

## Web Scraping Process

1. Sent a request to the website using the Requests library.
2. Retrieved the HTML content of the webpage.
3. Used BeautifulSoup to parse the HTML.
4. Identified the HTML elements containing book information.
5. Extracted the title, price, availability, and rating of each book.
6. Cleaned the price values and converted them into numeric format.
7. Stored the scraped data in a Pandas DataFrame.
8. Exported the dataset as a CSV file.

## Basic Analysis

The scraped dataset was also used to calculate:

- Total number of books
- Average book price
- Highest book price
- Lowest book price
- Rating distribution

## Results

- Total Books: 20
- Average Price: £38.05
- Highest Price: £57.25
- Lowest Price: £13.99
- All 20 books were available in stock.

## Output Files

- `webscrapping.py` - Python web scraping code
- `books_dataset.csv` - Scraped book dataset
- `rating_distribution.png` - Book rating distribution chart
- `README.md` - Project documentation

## Conclusion

The project successfully demonstrates how Python can be used to scrape publicly available web data. BeautifulSoup was used to extract structured information from the webpage, while Pandas was used to organize and save the collected data as a CSV dataset.
