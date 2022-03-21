-- Retrieve by name and frequency the twenty unique Badges that have been awarded the most often after 2019
-- 1.1 marks: <7 operators
-- 1.0 marks: <9 operators
-- 0.8 marks: correct answer

-- Replace this comment line with the actual query
SELECT
   *
FROM
(SELECT DISTINCT  `Name`, count(`Name`) as `Frequency`
FROM (SELECT `Name`,`Date` FROM `Badge`
WHERE `Date` > '2019-12-31') as inn
GROUP BY `Name`) as innerTable
ORDER BY `Frequency` DESC
LIMIT 20;
