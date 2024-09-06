INSERT INTO `UtstyrKategori` (`KategoriID`, `KategoriNavn`) 
VALUES (NULL, 'Lette maskiner'), (NULL, 'Tunge maskiner'), (NULL, 'Anleggsutstyr');

INSERT INTO `UtstyrType` (`TypeID`, `TypeNavn`, `UtstyrKategori_KategoriID`) 
VALUES (NULL, 'Kompressor', '1'), (NULL, 'Minigraver', '2'), (NULL, 'Stilas', '3'), (NULL, 'Sementblander', '3'), (NULL, 'Spikerpistol', '1');

INSERT INTO `Merke` (`MerkeID`, `MerkeNavn`) 
VALUES (NULL, 'Stanley'), (NULL, 'Hitachi'), (NULL, 'Haki Stilas'), (NULL, 'Atika'), (NULL, 'ESSVE');

INSERT INTO `Modell` (`ModellID`, `ModellNavn`, `UtstyrBeskrivelse`, `UtstyrType_TypeID`, `Merke_MerkeID`, `LeiePrisDøgn`) 
VALUES ('233', 'Vento 6L', 'Liten og hendig, med en motor på 1,5HK. Regulerbart trykk opp till 8bar, 180L luft i minuttet. ', '1', '1', '79'), 
('1001', 'ZX10U-6', 'Minigraveren ZX10U-6 fra Hitachi er vår minste minigraver og er laget for bruk på trange og små plasser', '2', '2', '1200'), 
('7653', '150', 'Stilas på ca 150 kvadratmeter.', '3', '3', '350'), 
('7654', '130l 600w', 'Atika betongblander med kapasitet på 130 l og 600 W. Bruker 230 V. IP44', '4', '4', '230'), 
('234', 'COIL CN-15-65', 'ESSVE Coilpistol beregnet for spikring av bjelkelag, reisverk, kledning, utforinger, panel, sponplater m.m. Smidig spikerpistol med maskinkropp i magnesium, justerbart utblås og beltekrok.', '5', '5', '100');

INSERT INTO `UtstyrInstans` (`InstansID`, `Modell_ModellID`, `SistVedlikeholdt`, `NesteVedlikehold`) 
VALUES ('1', '233', '2018-04-03', '2021-04-03'), ('2', '233', '2017-01-02', '2022-01-02'), ('3', '233', '2018-04-03', '2021-04-03'), ('4', '233', '2018-04-03', '2021-04-03'), ('5', '233', '2018-04-03', '2021-04-03'), ('6', '233', '2018-04-03', '2021-04-03'), ('7', '233', '2018-04-03', '2021-04-03'), ('8', '233', '2018-04-03', '2021-04-03'), ('9', '233', '2018-04-03', '2021-04-03'), ('10', '233', '2018-04-03', '2021-04-03'),
('1', '1001', '2019-09-01', '2022-09-01'),
('1', '7653', '2016-12-11', '2021-12-11'), ('2', '7653', '2016-12-11', '2021-12-11'),
('1', '7654', '2019-03-20', '2024-03-20'), ('2', '7654', '2017-01-02', '2022-01-02'), ('3', '7654', '2018-04-03', '2021-04-03'), ('4', '7654', '2018-04-03', '2021-04-03'), ('5', '7654', '2018-04-03', '2021-04-03'), ('6', '7654', '2018-04-03', '2021-04-03'), ('7', '7654', '2018-04-03', '2021-04-03'), ('8', '7654', '2018-04-03', '2021-04-03'),
('1', '234', '2021-02-10', '2022-02-10'), ('2', '234', '2021-02-10', '2022-02-10'), ('3', '234', '2021-02-10', '2022-02-10'), ('4', '234', '2021-02-10', '2022-02-10'), ('5', '234', '2021-02-10', '2022-02-10'), ('6', '234', '2021-02-10', '2022-02-10'), ('7', '234', '2021-02-10', '2022-02-10'), ('8', '234', '2021-02-10', '2022-02-10'), ('9', '234', '2021-02-10', '2022-02-10'), ('10', '234', '2021-02-10', '2022-02-10'), ('11', '234', '2021-02-10', '2022-02-10'), ('12', '234', '2021-02-10', '2022-02-10'), ('13', '234', '2021-02-10', '2022-02-10'), ('14', '234', '2021-02-10', '2022-02-10'), ('15', '234', '2021-02-10', '2022-02-10'), ('16', '234', '2021-02-10', '2022-02-10'), ('17', '234', '2021-02-10', '2022-02-10'), ('18', '234', '2021-02-10', '2022-02-10'), ('19', '234', '2021-02-10', '2022-02-10'), ('20', '234', '2021-02-10', '2022-02-10'), ('21', '234', '2021-02-10', '2022-02-10'), ('22', '234', '2021-02-10', '2022-02-10'), ('23', '234', '2021-02-10', '2022-02-10'), ('24', '234', '2021-02-10', '2022-02-10'), ('25', '234', '2021-02-10', '2022-02-10'), ('26', '234', '2021-02-10', '2022-02-10'), ('27', '234', '2021-02-10', '2022-02-10'), ('28', '234', '2021-02-10', '2022-02-10'), ('29', '234', '2021-02-10', '2022-02-10'), ('30', '234', '2021-02-10', '2022-02-10'), ('31', '234', '2021-02-10', '2022-02-10'), ('32', '234', '2021-02-10', '2022-02-10'), ('33', '234', '2021-02-10', '2022-02-10'), ('34', '234', '2021-02-10', '2022-02-10'), ('35', '234', '2021-02-10', '2022-02-10'), ('36', '234', '2021-02-10', '2022-02-10'), ('37', '234', '2021-02-10', '2022-02-10'), ('38', '234', '2021-02-10', '2022-02-10'), ('39', '234', '2021-02-10', '2022-02-10'), ('40', '234', '2021-02-10', '2022-02-10'), ('41', '234', '2021-02-10', '2022-02-10'), ('42', '234', '2021-02-10', '2022-02-10'), ('43', '234', '2021-02-10', '2022-02-10'), ('44', '234', '2021-02-10', '2022-02-10'), ('45', '234', '2021-02-10', '2022-02-10'), ('46', '234', '2021-02-10', '2022-02-10'), ('47', '234', '2021-02-10', '2022-02-10'), ('48', '234', '2021-02-10', '2022-02-10'), ('49', '234', '2021-02-10', '2022-02-10'), ('50', '234', '2021-02-10', '2022-02-10');

INSERT INTO `KundeBehandler` (`KundeBehandlerNr`, `KundeBehandlerNavn`, `KundeBehandlerTlf`) 
VALUES (NULL, 'Hilde Pettersen', '10090999'), (NULL, 'Berit Hansen', '10191999'), (NULL, 'Hans Hansen', '10291999');

INSERT INTO `KundeType` (`KundeType`) 
VALUES ('Privat'), ('Bedrift');

INSERT INTO `Kunde` (`KundeNr`, `KundeNavn`, `KundeType_KundeType`) 
VALUES ('20011', 'Anders Andersen', 'Privat'), ('10002', 'Grøft og Kant AS', 'Bedrift'), ('11122', 'Lokalbyggern AS', 'Bedrift'), ('8988', 'Murer Pedersen ANS', 'Bedrift');

INSERT INTO `KundeEpost` (`Epost`, `Kunde_KundeNr`) 
VALUES ('aa@post.no', '20011'), ('gm@uuiitt.nu', '10002'), ('lok_bygg@no.no', '11122'), ('mu_pe@ånnlain.no', '8988');

INSERT INTO `KundeTelefonnummer` (`Nummer`, `Kunde_KundeNr`) 
VALUES ('99988777', '20011'), ('76900112', '20011'), ('22122333', '20011'), ('769000111', '10002'), ('99988877', '10002'), ('7766554', '11122'), ('90099888', '8988');

INSERT INTO `FakturaAdresse` (`PostNr`, `Poststed`, `Adresse`, `Kunde_KundeNr`) 
VALUES ('8501', 'Narvik', 'Fjelltoppen 4', '20011'), ('8001', 'Bodø', 'Øvregata 332', '10002'), ('8000', 'Bodø', 'Nedreveien 223', '11122'), ('9001', 'Tromsø', 'Murergata 1', '8988');

INSERT INTO `Utleie` (`UtleieID`, `UtleidDato`, `InnlevertDato`, `Betalingsmåte`, `Kunde_KundeNr`, `UtstyrInstans_InstansID`, `UtstyrInstans_Modell_ModellID`, `KundeBehandler_KundeBehandlerNr`) 
VALUES (NULL, '2021-02-01', NULL, 'Kort', '20011', '1', '233', '1'), (NULL, '2021-02-05', '2021-02-08', 'Kontant', '10002', '1', '1001', '1'), (NULL, '2021-02-05', NULL, 'Kort', '11122', '1', '7653', '2'), (NULL, '2020-02-04', '2020-02-10', 'Vipps', '8988', '1', '7654', '2'), (NULL, '2019-03-05', '2019-03-06', 'Kontant', '20011', '2', '233', '2'), (NULL, '2019-02-01', '2019-02-03', 'Kort', '11122', '1', '234', '3');

INSERT INTO `LeveringsAdresse` (`Utleie_UtleieID`, `Postnr`, `Poststed`, `Adresse`, `LeveresKunde`, `Leveringskostnad`) 
VALUES ('1', '8500', 'Narvik', 'Fjelltoppen 3', 'Ja', '150'), ('2', '8000', 'Bodø', 'Lillegata 233', 'Ja', '500'), ('3', '8000', 'Bodø', 'Veien 124', 'Nei', '0'), ('4', '9000', 'Tromsø', 'Murergata 2', 'Ja', '200'), ('5', '8500', 'Narvik', 'Fjelltoppen 3', 'Nei', '0'), ('6', '8000', 'Bodø', 'Veien 124', 'Nei', '0');
