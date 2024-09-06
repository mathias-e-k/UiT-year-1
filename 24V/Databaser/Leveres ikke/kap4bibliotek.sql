-- kap 4 oppg 2

-- a)
select Bok.*, Utlån.Utlånsdato from Bok right join Utlån on Bok.ISBN=Utlån.ISBN
where utlånsdato='2016-08-25'
order by Bok.Tittel;

-- b)
select year(curdate())-utgittÅr as alder, count(*) as antall
from Bok
group by alder;

-- c) 
select Bok.*, count(*) as antallUtlån
from Bok right join Utlån on Bok.ISBN=Utlån.ISBN
where year(Utlån.Utlånsdato)=2016
group by Bok.Tittel
order by count(*) desc;

-- d)
select Låner.*, count(Utlån.UtlånsNr) as lånteBøker
from Låner left join Utlån on Låner.LNr=Utlån.LNr
group by Låner.Fornavn
order by lånteBøker desc, LNr asc;
