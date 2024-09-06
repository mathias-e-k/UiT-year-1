-- A)
SELECT KundeNr, KundeNavn, Nummer, Epost, substring(Adresse, 1, position(" " in Adresse)-1) as FakturaAdrGate, substring(Adresse, position(" " in Adresse)+1, length(Adresse)) as FakturaAdrGateNr, PostNr as FakturaPostNr 
FROM KundeInfo
where KundeType="Bedrift"
group by KundeNr; --# Må bruke group by så samme kunde ikke vises flere ganger hvis de har flere epost eller tlf nummer

-- B)
select U.UtleidDato, U.Kunde_KundeNr as KundeNr, U.UtstyrInstans_Modell_ModellID as UtstyrsId, UI.MerkeNavn, UI.ModellNavn, UI.TypeNavn
from Utleie as U
left join KundeBehandler as KB on U.KundeBehandler_KundeBehandlerNr=KB.KundeBehandlerNr
left join UtstyrInstansInfo as UI on U.UtstyrInstans_Modell_ModellID=UI.ModellID and U.UtstyrInstans_InstansID=UI.InstansID
where KB.KundeBehandlerNavn="Berit Hansen" and U.InnlevertDato is NULL;

-- C)
select count(*) as AntallKompletteUtleier 
from Utleie
where InnlevertDato is not Null 
and UtleidDato >= 20190101 and InnlevertDato <= 20200210;

-- D)
select M.ModellID, sum(U.InnlevertDato - U.UtleidDato) * M.LeiePrisDøgn as SumPerUtstyr, Me.MerkeNavn, M.ModellNavn, UT.TypeNavn
from Utleie as U
left join Modell as M on U.UtstyrInstans_Modell_ModellID=M.ModellID
left join Merke as Me on M.Merke_MerkeID=Me.MerkeID
left join UtstyrType as UT on M.UtstyrType_TypeID=UT.TypeID
group by UtstyrInstans_Modell_ModellID
having SumPerUtstyr > 0
order by SumPerUtstyr Desc;

-- E)
select count(*) as AntUtleid, UI.MerkeNavn, UI.ModellNavn, UI.TypeNavn, UI.KategoriNavn
from Utleie as U
left join UtstyrInstansInfo as UI on U.UtstyrInstans_InstansID=UI.InstansID and U.UtstyrInstans_Modell_ModellID=UI.ModellID
group by U.UtstyrInstans_Modell_ModellID
having count(*) >= all(select count(*)
			from Utleie as U
			group by U.UtstyrInstans_Modell_ModellID)
