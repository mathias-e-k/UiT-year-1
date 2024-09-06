#oppgave 1
select date_format(now(), "%Y-%m-%d %H:%i:%S") as Date;

#oppgave 2
select * from emp where comm is null or comm = 0;

#oppgave 3
select * from emp where comm != 500;

#oppgave 4
select ename, job from emp where job = (select job from emp where ename="Jones");

#oppgave 5
select ename, job from emp where deptno=1 and job in (select distinct job from emp where deptno=3);

#oppgave 6
select ename, job from emp where deptno=1 and job not in (select distinct job from emp where deptno=3);

#oppgave 7
select ename, job, deptno, sal from emp where (job, sal) = (select job, sal from emp where ename="Ford");

#oppgave 8
select ename, job, deptno, sal from emp 
where job=(select job from emp where ename="Jones") or sal >= (select sal from emp where ename="Ford")
order by job, sal;

#oppgave 9
select ename, job from emp 
where deptno=1 and job in (select job from emp where deptno in (select deptno from dept where dname="Sales"));

#oppgave 10
select ename, job, sal from emp where sal = (select sal from emp where ename="Scott")
union
select ename, job, sal from emp where sal = (select sal from emp where ename="Ward");

#oppgave 11
select ename, job from emp 
where job in (select job from emp where deptno=(select deptno from dept where loc="Chicago"))
order by job;

#oppgave 12
select ename as Name, sal as Salary, sal/tot_sal*100
from emp, (select sum(sal) as tot_sal from emp) as totSalg
order by sal;

#oppgave 13
select d1.dname as Department, d2.dsal as Sum, dsal/tot_sal*100 as Prosentvis
from dept as d1, (select deptno, sum(sal) as dsal from emp group by deptno) as d2, (select sum(sal) as tot_sal from emp) as totSalg
where d1.deptno=d2.deptno
order by Sum asc;
