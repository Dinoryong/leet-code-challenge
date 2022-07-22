# Write your MySQL query statement below
SELECT NAME, POPULATION, AREA FROM WORLD WHERE AREA >= 3000000 UNION SELECT name, population, area FROM world WHERE population >= 25000000;