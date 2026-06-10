-- 先明确指标口径，再替换表名、字段名和日期范围
WITH base AS (
    SELECT
        customer_id,
        order_date,
        revenue
    FROM source_table
    WHERE order_date >= '2026-01-01'
),
customer_summary AS (
    SELECT
        customer_id,
        COUNT(*) AS order_count,
        SUM(revenue) AS total_revenue
    FROM base
    GROUP BY customer_id
)
SELECT
    customer_id,
    order_count,
    total_revenue
FROM customer_summary
ORDER BY total_revenue DESC;
