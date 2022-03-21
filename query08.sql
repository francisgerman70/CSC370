-- Note: Aspects of this are *very* tricky
-- Retrieve the display name of all users who have
-- never posted a post that has been linked by another post
-- ordered ascending
-- 1.1 marks: <8 operators
-- 1.0 marks: <10 operators
-- 0.8 marks: correct answer

-- Replace this comment line with the actual query
SELECT DISTINCT `DisplayName` FROM()

SELECT DISTINCT `DisplayName` FROM
(SELECT DISTINCT `DisplayName`, count(`CreationDate`) as `posted` 
FROM (SELECT DISTINCT `P`.`CreationDate`, `U`.`DisplayName`
FROM `Post` AS `p`
INNER JOIN `User` AS `U`
ON `P`.`OwnerUserId` = `U`.`Id`) AS c
GROUP BY `DisplayName`)AS G;


SELECT `P`.`CreationDate`, `U`.`DisplayName`, `L`.`CreationDate`
FROM `User` AS `U`
INNER JOIN `Post` AS `P`
ON `P`.`OwnerUserId` = `U`.`Id`
INNER JOIN `Link` AS `L`
ON `P`.`OwnerUserId` = `L`.`RelatedPostId`;


SELECT `CreationDate`
FROM `Link`;

SELECT `CreationDate`
FROM `Post`;

SELECT `DisplayName` FROM
(SELECT `P`.`CreationDate`, `U`.`DisplayName`, `L`.`CreationDate`
FROM `User` AS `U`
INNER JOIN `Post` AS `P`
ON `P`.`OwnerUserId` = `U`.`Id`
INNER JOIN `Link` AS `L`
ON `P`.`OwnerUserId` = `L`.`RelatedPostId`) AS d;


SELECT DISTINCT `CreationDate`, `Id`
FROM `Post` AS `p`;

SELECT DISTINCT `CreationDate`, `Id`
FROM `Link` AS `L`;

SELECT `DisplayName`
FROM `User` 
WHERE NOT EXISTS (SELECT DISTINCT `P`.`CreationDate`,`P`.`OwnerUserId`,`L`.`CreationDate`, `L`.`RelatedPostId`, `U`.`DisplayName`
FROM `Post` AS `p`
INNER JOIN `Link` AS `L`
ON `P`.`OwnerUserId` = `L`.`RelatedPostId`
INNER JOIN `User` AS `U`
ON `P`.`OwnerUserId` = `U`.`Id`) ;

SELECT `OwnerUserId`
FROM (SELECT DISTINCT `P`.`CreationDate`,`P`.`OwnerUserId`,`L`.`CreationDate`, `L`.`RelatedPostId`, `U`.`DisplayName`
FROM `Post` AS `p`
INNER JOIN `Link` AS `L`
ON `P`.`OwnerUserId` = `L`.`RelatedPostId`
INNER JOIN `User` AS `U`
ON `P`.`OwnerUserId` = `U`.`Id`) AS A;
