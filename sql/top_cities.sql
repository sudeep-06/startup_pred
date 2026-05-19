SELECT
    `City  Location`,
    SUM(`Amount in USD`) AS total_funding
FROM startup_funding
GROUP BY `City  Location`
ORDER BY total_funding DESC
LIMIT 10;