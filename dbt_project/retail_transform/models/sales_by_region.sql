SELECT
  region,
  SUM(quantity_sold) AS total_quantity,
  SUM(total_sales) AS total_sales
FROM {{ ref('clean_sales') }}
GROUP BY region
ORDER BY total_sales DESC
