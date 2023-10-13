/* Write your PL/SQL query statement below */
select max(num) as num from(SELECT num,count(num)as count from mynumbers group by num)
where count=1;