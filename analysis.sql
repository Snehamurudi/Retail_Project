SELECT Discount,
       AVG(Profit) AS Avg_Profit
FROM Superstore
GROUP BY Discount
ORDER BY Discount;
