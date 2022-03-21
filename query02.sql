-- Retrieve the name of all unique Badges obtained by the
-- user with ID 3 awarded after 2011, together with the
-- first date after 2011 in which that user obtained that badge.
-- Order the results by increasing Badge Name.
-- 1.1 marks: <5 operators
-- 1.0 marks: <7 operators
-- 0.8 marks: correct answer

-- Replace this comment line with the actual query
SELECT DISTINCT `Name`, MIN(`Date`) AS `Date` 
FROM 
(SELECT DISTINCT `Name`, `Date`, 
row_number() over(partition by `Name` order by `Name`) as `rn`
from `Badge`
WHERE `UserId` = 3
And `Date` > '2011-12-12'
ORDER BY `Name`) t
GROUP BY `Name`;

