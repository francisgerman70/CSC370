-- Retrieve the Post that has the highest
-- score, summed over itself and all its children
-- 1.1 marks: <8 operators
-- 1.0 marks: <10 operators
-- 0.9 marks: <12 operators
-- 0.8 marks: correct answer

-- Replace this comment line with the actual query

SELECT `Id`,`Score`
FROM `Post`
WHERE `Score` = (SELECT MAX(`Score`) FROM `Post`);


WITH RECURSIVE `descendant` AS (
    SELECT  `Id`
            `ParentId`,
            0 AS `level`
    FROM `Post`
    WHERE `Id` = 1
 
    UNION ALL
 
    SELECT  `p`.`Id`,
            `p`.`ParentId`,
            level + 1
    FROM `Post` as `p`
JOIN `descendant` as `d`
ON `p`.`ParentId` = `d`.`Id`
)
 
SELECT  `d`.`Id` AS `descendant_id`,
        `d`.`level`
FROM descendant d
JOIN family_tree a
ON d.parent_id = a.id
ORDER BY level, ancestor_id;