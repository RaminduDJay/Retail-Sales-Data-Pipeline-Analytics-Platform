import csv
import random
from datetime import datetime, timedelta

# Configuration
row_count = 10_000
output_file = "sales_data.csv"

# Sample values
store_ids = [101, 102, 103, 104, 105]
products = [
    (501, "Coca-Cola 500ml", "Beverages", 1.50),
    (502, "Pepsi 500ml", "Beverages", 1.40),
    (601, "Sunlight Detergent 1kg", "Household", 3.00),
    (701, "Anchor Full Cream 1L", "Dairy", 2.80),
    (801, "Kist Mango Jam 500g", "Food", 2.20),
    (802, "Maliban Marie 400g", "Food", 1.60),
    (901, "Signal Toothpaste 120g", "Toiletries", 2.50),
]
regions = ["Western", "Central", "Southern", "Northern", "Eastern"]

# Generate random sales data
def generate_sales_data():
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["date", "store_id", "product_id", "product_name", "category", "region", "quantity_sold", "unit_price", "total_sales"])
        
        for _ in range(row_count):
            date = datetime(2025, 5, 1) + timedelta(days=random.randint(0, 29))
            store_id = random.choice(store_ids)
            product = random.choice(products)
            region = random.choice(regions)
            quantity_sold = random.randint(1, 50)
            unit_price = product[3]
            total_sales = round(quantity_sold * unit_price, 2)
            
            writer.writerow([
                date.strftime("%Y-%m-%d"),
                store_id,
                product[0],
                product[1],
                product[2],
                region,
                quantity_sold,
                unit_price,
                total_sales
            ])

    print(f"✅ Generated {row_count} rows in {output_file}")

# Run the script
if __name__ == "__main__":
    generate_sales_data()
