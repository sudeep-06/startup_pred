SELECT
    `Industry Vertical`,
    SUM(`Amount in USD`) AS total_funding
FROM startup_funding
GROUP BY `Industry Vertical`
ORDER BY total_funding DESC
LIMIT 10;