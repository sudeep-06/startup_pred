SELECT
    `Investors Name`,
    COUNT(*) AS total_investments
FROM startup_funding
GROUP BY `Investors Name`
ORDER BY total_investments DESC
LIMIT 10;