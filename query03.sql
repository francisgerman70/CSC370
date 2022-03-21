-- Retrieve the name of all unique Badges that have been awarded
-- at least one hundred times after July 1, 2017, ordered
-- by increasing name
-- 1.1 marks: <6 operators
-- 1.0 marks: <7 operators
-- 0.8 marks: correct answer

-- Replace this comment line with the actual query

SELECT DISTINCT
   `Name`
FROM
(SELECT DISTINCT  count(`Name`) as `cnt`, `Name`
FROM (SELECT `Name`,`Date` FROM `Badge`
WHERE `Date` > '2017-07-31') as inn
GROUP BY `Name`) as innerTable
WHERE `cnt` >= 100
ORDER BY `Name` ASC;

