-- Kap 5 Oppg 1
-- a) 
select Fornavn, Etternavn, 
case
	when year(curdate()) - Fødselsår < 18 then concat(Kjønn, year(curdate()) - Fødselsår)
    when year(curdate()) - Fødselsår >= 18 then Kjønn
end as Klasse
from Medlem;


CREATE VIEW MedlemMedKlasse(MedlemsNr, Fornavn, Etternavn, Kjønn, Fødselsår, Klasse) AS
SELECT MedlemsNr, Fornavn, Etternavn, Kjønn, Fødselsår,
  IF(YEAR(CURDATE())-Fødselsår < 18, CONCAT(Kjønn, YEAR(CURDATE())-Fødselsår), Kjønn)
FROM Medlem;

-- c)
select Distinct M1.*
from Medlem as M1, Resultat as R1
where M1.MedlemsNr=R1.MedlemsNr and 
R1.Tid <= (select min(R2.Tid)
		from Medlem as M2, Resultat as R2
		where M2.MedlemsNr=R2.MedlemsNr and
        R1.LøpsNr=R2.LøpsNr);

-- d) 
select Medlem.*
from Medlem left join Resultat on Medlem.MedlemsNr=Resultat.MedlemsNr
where Resultat.MedlemsNr is null;



select * from Løp;
select * from Resultat;
select * from Medlem;