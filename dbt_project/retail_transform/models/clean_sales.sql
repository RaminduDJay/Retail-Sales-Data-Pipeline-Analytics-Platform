SELECT
  date,
  store_id,
  product_id,
  INITCAP(product_name) AS product_name,
  INITCAP(category) AS category,
  INITCAP(region) AS region,
  quantity_sold,
  unit_price,
  quantity_sold * unit_price AS total_sales
FROM {{ source('sales', 'sales_raw') }}
WHERE quantity_sold > 0
