import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_area"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the table containing the country data
table = soup.find("table", class_="wikitable sortable")

# Extract the table headers
headers = [header.text.strip() for header in table.find_all("th")]

# Create a new CSV file
csv_filename = "countries_by_area.csv"
with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)  # Write the table headers

    # Find the table rows
    rows = table.find_all("tr")

    # Iterate over each row (skipping the header row)
    for row in rows[1:]:
        # Extract the data from each cell in the row
        cells = row.find_all("td")
        row_data = [cell.text.strip() for cell in cells]

        # Write the row data to the CSV file
        writer.writerow(row_data)

print(f"Data has been scraped and saved to {csv_filename}.")
