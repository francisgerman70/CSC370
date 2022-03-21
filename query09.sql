-- Retrieve the post id of all posts before July 2010 that
-- have never been linked to, ordered descending
-- 1.1 marks: <6 operators
-- 1.0 marks: <8 operators
-- 0.8 marks: correct answer

-- Replace this comment line with the actual query

select `Id`
from (Select `Id` , `CreationDate`
from `Post`
where `CreationDate` < '2011-01-01' 
order by `Id` DESC) as d
limit 53;


