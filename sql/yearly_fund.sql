SELECT
    YEAR(STR_TO_DATE(`Date dd/mm/yyyy`, '%d/%m/%Y')) AS funding_year,
    SUM(`Amount in USD`) AS total_funding
FROM startup_funding
GROUP BY funding_year
ORDER BY funding_year;