SELECT
  product_id,
  product_name,
  SUM(quantity_sold) AS total_sold,
  SUM(total_sales) AS total_earned
FROM {{ ref('clean_sales') }}
GROUP BY product_id, product_name
ORDER BY total_earned DESC
LIMIT 10
