#oppgave 1
select ename, sal, comm from emp where comm > 0.25*sal;

#oppgave 2
select ename, comm/sal, comm, sal from emp where job='Salesman' order by comm/sal desc;

#oppgave 3
select ename, sal, comm, 12 * (sal + comm) from emp where job='Salesman';

#oppgave 4
select avg(sal) from emp where job='Clerk';

#oppgave 5
select sum(sal), sum(comm) from emp where job='Salesman';

#oppgave 6
select count(comm) from emp where comm > 0;

#oppgave 7
select count(distinct job) from emp where deptno=3;

#oppgave 8
select count(*) from emp where deptno=3;

#oppgave 9
select deptno, avg(sal) as Average_salary from emp group by deptno;

#oppgave 10
select concat(dname, ' - ', loc) as Departments from dept;

#oppgave 11
select ename, job,
case
	when job='Clerk' then 1
    when job='Salesman' then 2
    when job='Manager' then 3
    when job='Analyst' then 4
    when job='President' then 5
end as job_class
from emp;

#oppgave 12
select substring(ename, 2) as name_part from emp;

#oppgave 13
select curdate() as date;
