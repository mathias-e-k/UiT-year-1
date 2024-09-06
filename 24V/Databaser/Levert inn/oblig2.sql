#oppgave 1
select * from emp where deptno=1 and job not in ('Manager','Clerk');

#oppgave 2
select * from emp where sal between 1200 and 1300;

#oppgave 3
select ename, job, deptno from emp where job in ('Clerk','Analyst','Salesman');

#oppgave 4
select ename, job, sal from emp where sal not between 1200 and 1400;

#oppgave 5
select ename, job, deptno from emp where job not in ('Clerk','Analyst','Salesman');

#oppgave 6
select ename, job, deptno from emp where ename like 'M%';

#oppgave 7
select ename, job, deptno from emp where ename like 'Al__n';

#oppgave 8
select sal, ename, deptno from emp where deptno=3 order by sal asc;

#oppgave 9
select sal, ename, deptno from emp where deptno=3 order by sal desc;

#oppgave 10
select ename, job, sal from emp order by job, sal desc;

#oppgave 11
select ename, loc from emp inner join dept on emp.deptno=dept.deptno where ename='Allen';

#oppgave 12
select dept.deptno, dname, job, ename from dept left join emp on dept.deptno=emp.deptno where dept.deptno between 3 and 4;

#oppgave 13
select dept.deptno, dname, loc from dept left join emp on emp.deptno=dept.deptno group by deptno having count(emp.deptno)=0;
