#oppgave 1
select * from dept;

#oppgave 2
select * from emp;

#oppgave 3
select job from emp;

#oppgave 4
select distinct job from emp;

#oppgave 5
select dname as Department from dept;

#oppgave 6
select * from emp where deptno = 3;

#oppgave 7
select ename, empno, deptno from emp where job = "Clerk";

#oppgave 8
select dname, deptno from dept where deptno > 2;

#oppgave 9
select ename, sal, comm from emp where comm > sal;

#oppgave 10
select ename, sal, deptno from emp where deptno = 3 and job = "Salesman" and sal >= 1500;

#oppgave 11
select ename, sal, job from emp where job = "Manager" or sal > 3000;

#oppgave 12
select * from emp where job = "Manager" or job = "Clerk" and deptno = 1;

#oppgave 13
select ename, job, deptno from emp where job = "Manager" and deptno != 3;