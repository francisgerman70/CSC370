-- Retrieve the postid and display name of the user who posted it
-- for *all* posts that have linked to at least twenty other posts,
-- ordered by postId
-- 1.1 marks: <8 operators
-- 1.0 marks: <9 operators
-- 0.9 marks: <11 operators
-- 0.8 marks: correct answer

-- Replace this comment line with the actual query
select `Id`, `DisplayName`
from `User`
    natural JOIN
    ()


select `PostId`
from (select `PostId`, count(`PostId`) as linked
from `Link`
group by `PostId`) as l
where linked >=20;


select `PostId`, `DisplayName`
from `User`
    natural JOIN
    (select `PostId`
from (select `PostId`, count(`PostId`) as linked
from `Link`
group by `PostId`) as l
where linked >=20) as h;


SELECT DISTINCT `PostId`, `DisplayName`
FROM (select `PostId`, count(`PostId`) as linked
from `Link`
group by `PostId`) as l
left JOIN `User`
ON `PostId` = `Id`
where linked >=20
order by `PostId`;


SELECT DISTINCT `PostId`, `DisplayName`
FROM (select `PostId`, count(`PostId`) as linked
from `Link`
group by `PostId`) as l
left JOIN `Post` as `p`
ON `OwnerUserId` = `Id`
natural join (select DISTINCT `DisplayName`, `Id` from `User` as `u`) as w
where linked >=20
order by `PostId`;

select  `DisplayName`,`Id`
from `User`
where `DisplayName` in ('Ari B. Friedman');

select  `PostId`,`Id`
from `Link`
ORDER by `Id` ASC;
where `PostId` in ('4024');

SELECT DISTINCT `PostId`, `DisplayName`
FROM (select `PostId`, count(`PostId`) as linked
from `Link`
group by `PostId`) as l
left join `Post` as p on (`OwnerUserId` = `l`.`Id`)
left join `User` as u on (`OwnerUserId` = `u`.`Id`)
where linked >=20
order by `PostId`;


SELECT DISTINCT `PostId`, `DisplayName`
FROM (select `PostId`, count(`PostId`) as linked
from `Link`
group by `PostId`) as `l`
left JOIN `Post` as `p`
ON `OwnerUserId` = `l`.`Id`
left JOIN `User` as `u`
ON `OwnerUserId` = `u`.`Id`
where linked >=20
order by `PostId`;

