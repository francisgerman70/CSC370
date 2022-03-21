-- Retrieve the name and Date of all Badges obtained by the user with ID 3 awarded after 2011
-- 1.1 marks: <3 operators
-- 1.0 marks: <4 operators
-- 0.8 marks: correct answer

-- Replace this comment line with the actual query
SELECT `Name`,`Date` FROM `Badge`
WHERE `UserId` = 3
And `Date` > '2011-12-12'
ORDER BY `Date` ASC;

