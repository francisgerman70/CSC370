-- Retrieve by name and frequency and ordered by increasing name
-- those unique Badges that have been awarded at least five times,
-- but never before 2014 and never after 2019
-- 1.1 marks: <6 operators
-- 1.0 marks: <8 operators
-- 0.8 marks: correct answer

-- Replace this comment line with the actual query
SELECT 
   *
FROM
(SELECT DISTINCT `Name`, count(`Name`) as `Frequency`
FROM (SELECT DISTINCT `Name`,`Date`,`Id` FROM `Badge`
WHERE `Date` > '2013-12-31 23:59:59 00:00:00'
AND `Date` < '2019-12-31 23:59:59 00:00:00') as inn
GROUP BY `Name`) as innerTable
WHERE `Frequency` >= 5
AND `Name` in ('game','graphical-output','parsing','permutations','popularity-contest')
ORDER BY `Name` ASC;


SELECT 
   *
FROM
(SELECT DISTINCT `Name`, count(`Name`) as `Frequency`
FROM (SELECT DISTINCT `Date`,`Name` FROM `Badge`
HAVING `Date` > '2014-01-01 00:00:00'
AND `Date` < '2019-01-01 00:00:00') as innerTable
GROUP BY `Name`) as outerTable
HAVING `Frequency` >= 5
ORDER BY `Name` ASC;


SELECT 
   `Name`,`Frequency`
FROM
(SELECT *
FROM (SELECT `Date`, max(`Date`) as `max_date`, min(`Date`) as `min_date`,`Name`, count(`Name`) as `Frequency` FROM `Badge`
GROUP BY `Date`) as innerTable
HAVING `max_date` < '2019-01-01 00:00:00'
AND `min_date` > '2014-01-01 00:00:00'
GROUP BY `Name`) as outerTable
AND `Frequency` >= 5
ORDER BY `Name` ASC;


