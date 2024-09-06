-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Feb 29, 2024 at 01:01 PM
-- Server version: 10.5.18-MariaDB
-- PHP Version: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `stud_v24_mka224`
--

-- --------------------------------------------------------

--
-- Table structure for table `FakturaAdresse`
--

CREATE TABLE `FakturaAdresse` (
  `PostNr` char(4) NOT NULL,
  `Poststed` varchar(45) NOT NULL,
  `Adresse` varchar(45) NOT NULL,
  `Kunde_KundeNr` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `FakturaAdresse`
--

INSERT INTO `FakturaAdresse` (`PostNr`, `Poststed`, `Adresse`, `Kunde_KundeNr`) VALUES
('9001', 'Tromsø', 'Murergata 1', 8988),
('8001', 'Bodø', 'Øvregata 332', 10002),
('8000', 'Bodø', 'Nedreveien 223', 11122),
('8501', 'Narvik', 'Fjelltoppen 4', 20011);

-- --------------------------------------------------------

--
-- Table structure for table `Kunde`
--

CREATE TABLE `Kunde` (
  `KundeNr` int(11) NOT NULL,
  `KundeNavn` varchar(100) NOT NULL,
  `KundeType_KundeType` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `Kunde`
--

INSERT INTO `Kunde` (`KundeNr`, `KundeNavn`, `KundeType_KundeType`) VALUES
(8988, 'Murer Pedersen ANS', 'Bedrift'),
(10002, 'Grøft og Kant AS', 'Bedrift'),
(11122, 'Lokalbyggern AS', 'Bedrift'),
(20011, 'Anders Andersen', 'Privat');

-- --------------------------------------------------------

--
-- Table structure for table `KundeBehandler`
--

CREATE TABLE `KundeBehandler` (
  `KundeBehandlerNr` int(11) NOT NULL,
  `KundeBehandlerNavn` varchar(100) NOT NULL,
  `KundeBehandlerTlf` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `KundeBehandler`
--

INSERT INTO `KundeBehandler` (`KundeBehandlerNr`, `KundeBehandlerNavn`, `KundeBehandlerTlf`) VALUES
(1, 'Hilde Pettersen', '10090999'),
(2, 'Berit Hansen', '10191999'),
(3, 'Hans Hansen', '10291999');

-- --------------------------------------------------------

--
-- Table structure for table `KundeEpost`
--

CREATE TABLE `KundeEpost` (
  `Epost` varchar(100) NOT NULL,
  `Kunde_KundeNr` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `KundeEpost`
--

INSERT INTO `KundeEpost` (`Epost`, `Kunde_KundeNr`) VALUES
('aa@post.no', 20011),
('gm@uuiitt.nu', 10002),
('lok_bygg@no.no', 11122),
('mu_pe@ånnlain.no', 8988);

-- --------------------------------------------------------

--
-- Stand-in structure for view `KundeInfo`
-- (See below for the actual view)
--
CREATE TABLE `KundeInfo` (
`KundeType` varchar(15)
,`KundeNr` int(11)
,`KundeNavn` varchar(100)
,`Epost` varchar(100)
,`Nummer` varchar(45)
,`PostNr` char(4)
,`Poststed` varchar(45)
,`Adresse` varchar(45)
);

-- --------------------------------------------------------

--
-- Table structure for table `KundeTelefonnummer`
--

CREATE TABLE `KundeTelefonnummer` (
  `Nummer` varchar(45) NOT NULL,
  `Kunde_KundeNr` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `KundeTelefonnummer`
--

INSERT INTO `KundeTelefonnummer` (`Nummer`, `Kunde_KundeNr`) VALUES
('22122333', 20011),
('769000111', 10002),
('76900112', 20011),
('7766554', 11122),
('90099888', 8988),
('99988777', 20011),
('99988877', 10002);

-- --------------------------------------------------------

--
-- Table structure for table `KundeType`
--

CREATE TABLE `KundeType` (
  `KundeType` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `KundeType`
--

INSERT INTO `KundeType` (`KundeType`) VALUES
('Bedrift'),
('Privat');

-- --------------------------------------------------------

--
-- Table structure for table `LeveringsAdresse`
--

CREATE TABLE `LeveringsAdresse` (
  `Utleie_UtleieID` int(11) NOT NULL,
  `Postnr` char(4) NOT NULL,
  `Poststed` varchar(45) NOT NULL,
  `Adresse` varchar(45) NOT NULL,
  `LeveresKunde` varchar(6) NOT NULL,
  `Leveringskostnad` decimal(8,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `LeveringsAdresse`
--

INSERT INTO `LeveringsAdresse` (`Utleie_UtleieID`, `Postnr`, `Poststed`, `Adresse`, `LeveresKunde`, `Leveringskostnad`) VALUES
(1, '8500', 'Narvik', 'Fjelltoppen 3', 'Ja', '150.00'),
(2, '8000', 'Bodø', 'Lillegata 233', 'Ja', '500.00'),
(3, '8000', 'Bodø', 'Veien 124', 'Nei', '0.00'),
(4, '9000', 'Tromsø', 'Murergata 2', 'Ja', '200.00'),
(5, '8500', 'Narvik', 'Fjelltoppen 3', 'Nei', '0.00'),
(6, '8000', 'Bodø', 'Veien 124', 'Nei', '0.00');

-- --------------------------------------------------------

--
-- Table structure for table `Merke`
--

CREATE TABLE `Merke` (
  `MerkeID` int(11) NOT NULL,
  `MerkeNavn` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `Merke`
--

INSERT INTO `Merke` (`MerkeID`, `MerkeNavn`) VALUES
(1, 'Stanley'),
(2, 'Hitachi'),
(3, 'Haki Stilas'),
(4, 'Atika'),
(5, 'ESSVE');

-- --------------------------------------------------------

--
-- Table structure for table `Modell`
--

CREATE TABLE `Modell` (
  `ModellID` int(11) NOT NULL,
  `ModellNavn` varchar(45) NOT NULL,
  `UtstyrBeskrivelse` varchar(1000) DEFAULT NULL,
  `UtstyrType_TypeID` int(11) NOT NULL,
  `Merke_MerkeID` int(11) NOT NULL,
  `LeiePrisDøgn` decimal(8,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `Modell`
--

INSERT INTO `Modell` (`ModellID`, `ModellNavn`, `UtstyrBeskrivelse`, `UtstyrType_TypeID`, `Merke_MerkeID`, `LeiePrisDøgn`) VALUES
(233, 'Vento 6L', 'Liten og hendig, med en motor på 1,5HK. Regulerbart trykk opp till 8bar, 180L luft i minuttet. ', 1, 1, '79.00'),
(234, 'COIL CN-15-65', 'ESSVE Coilpistol beregnet for spikring av bjelkelag, reisverk, kledning, utforinger, panel, sponplater m.m. Smidig spikerpistol med maskinkropp i magnesium, justerbart utblås og beltekrok.', 5, 5, '100.00'),
(1001, 'ZX10U-6', 'Minigraveren ZX10U-6 fra Hitachi er vår minste minigraver og er laget for bruk på trange og små plasser', 2, 2, '1200.00'),
(7653, '150', 'Stilas på ca 150 kvadratmeter.', 3, 3, '350.00'),
(7654, '130l 600w', 'Atika betongblander med kapasitet på 130 l og 600 W. Bruker 230 V. IP44', 4, 4, '230.00');

-- --------------------------------------------------------

--
-- Table structure for table `Utleie`
--

CREATE TABLE `Utleie` (
  `UtleieID` int(11) NOT NULL,
  `UtleidDato` date NOT NULL,
  `InnlevertDato` date DEFAULT NULL,
  `Betalingsmåte` varchar(15) NOT NULL,
  `Kunde_KundeNr` int(11) NOT NULL,
  `UtstyrInstans_InstansID` int(11) NOT NULL,
  `UtstyrInstans_Modell_ModellID` int(11) NOT NULL,
  `KundeBehandler_KundeBehandlerNr` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `Utleie`
--

INSERT INTO `Utleie` (`UtleieID`, `UtleidDato`, `InnlevertDato`, `Betalingsmåte`, `Kunde_KundeNr`, `UtstyrInstans_InstansID`, `UtstyrInstans_Modell_ModellID`, `KundeBehandler_KundeBehandlerNr`) VALUES
(1, '2021-02-01', NULL, 'Kort', 20011, 1, 233, 1),
(2, '2021-02-05', '2021-02-08', 'Kontant', 10002, 1, 1001, 1),
(3, '2021-02-05', NULL, 'Kort', 11122, 1, 7653, 2),
(4, '2020-02-04', '2020-02-10', 'Vipps', 8988, 1, 7654, 2),
(5, '2019-03-05', '2019-03-06', 'Kontant', 20011, 2, 233, 2),
(6, '2019-02-01', '2019-02-03', 'Kort', 11122, 1, 234, 3);

-- --------------------------------------------------------

--
-- Table structure for table `UtstyrInstans`
--

CREATE TABLE `UtstyrInstans` (
  `InstansID` int(11) NOT NULL,
  `Modell_ModellID` int(11) NOT NULL,
  `SistVedlikeholdt` date NOT NULL,
  `NesteVedlikehold` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `UtstyrInstans`
--

INSERT INTO `UtstyrInstans` (`InstansID`, `Modell_ModellID`, `SistVedlikeholdt`, `NesteVedlikehold`) VALUES
(1, 233, '2018-04-03', '2021-04-03'),
(1, 234, '2021-02-10', '2022-02-10'),
(1, 1001, '2019-09-01', '2022-09-01'),
(1, 7653, '2016-12-11', '2021-12-11'),
(1, 7654, '2019-03-20', '2024-03-20'),
(2, 233, '2017-01-02', '2022-01-02'),
(2, 234, '2021-02-10', '2022-02-10'),
(2, 7653, '2016-12-11', '2021-12-11'),
(2, 7654, '2017-01-02', '2022-01-02'),
(3, 233, '2018-04-03', '2021-04-03'),
(3, 234, '2021-02-10', '2022-02-10'),
(3, 7654, '2018-04-03', '2021-04-03'),
(4, 233, '2018-04-03', '2021-04-03'),
(4, 234, '2021-02-10', '2022-02-10'),
(4, 7654, '2018-04-03', '2021-04-03'),
(5, 233, '2018-04-03', '2021-04-03'),
(5, 234, '2021-02-10', '2022-02-10'),
(5, 7654, '2018-04-03', '2021-04-03'),
(6, 233, '2018-04-03', '2021-04-03'),
(6, 234, '2021-02-10', '2022-02-10'),
(6, 7654, '2018-04-03', '2021-04-03'),
(7, 233, '2018-04-03', '2021-04-03'),
(7, 234, '2021-02-10', '2022-02-10'),
(7, 7654, '2018-04-03', '2021-04-03'),
(8, 233, '2018-04-03', '2021-04-03'),
(8, 234, '2021-02-10', '2022-02-10'),
(8, 7654, '2018-04-03', '2021-04-03'),
(9, 233, '2018-04-03', '2021-04-03'),
(9, 234, '2021-02-10', '2022-02-10'),
(10, 233, '2018-04-03', '2021-04-03'),
(10, 234, '2021-02-10', '2022-02-10'),
(11, 234, '2021-02-10', '2022-02-10'),
(12, 234, '2021-02-10', '2022-02-10'),
(13, 234, '2021-02-10', '2022-02-10'),
(14, 234, '2021-02-10', '2022-02-10'),
(15, 234, '2021-02-10', '2022-02-10'),
(16, 234, '2021-02-10', '2022-02-10'),
(17, 234, '2021-02-10', '2022-02-10'),
(18, 234, '2021-02-10', '2022-02-10'),
(19, 234, '2021-02-10', '2022-02-10'),
(20, 234, '2021-02-10', '2022-02-10'),
(21, 234, '2021-02-10', '2022-02-10'),
(22, 234, '2021-02-10', '2022-02-10'),
(23, 234, '2021-02-10', '2022-02-10'),
(24, 234, '2021-02-10', '2022-02-10'),
(25, 234, '2021-02-10', '2022-02-10'),
(26, 234, '2021-02-10', '2022-02-10'),
(27, 234, '2021-02-10', '2022-02-10'),
(28, 234, '2021-02-10', '2022-02-10'),
(29, 234, '2021-02-10', '2022-02-10'),
(30, 234, '2021-02-10', '2022-02-10'),
(31, 234, '2021-02-10', '2022-02-10'),
(32, 234, '2021-02-10', '2022-02-10'),
(33, 234, '2021-02-10', '2022-02-10'),
(34, 234, '2021-02-10', '2022-02-10'),
(35, 234, '2021-02-10', '2022-02-10'),
(36, 234, '2021-02-10', '2022-02-10'),
(37, 234, '2021-02-10', '2022-02-10'),
(38, 234, '2021-02-10', '2022-02-10'),
(39, 234, '2021-02-10', '2022-02-10'),
(40, 234, '2021-02-10', '2022-02-10'),
(41, 234, '2021-02-10', '2022-02-10'),
(42, 234, '2021-02-10', '2022-02-10'),
(43, 234, '2021-02-10', '2022-02-10'),
(44, 234, '2021-02-10', '2022-02-10'),
(45, 234, '2021-02-10', '2022-02-10'),
(46, 234, '2021-02-10', '2022-02-10'),
(47, 234, '2021-02-10', '2022-02-10'),
(48, 234, '2021-02-10', '2022-02-10'),
(49, 234, '2021-02-10', '2022-02-10'),
(50, 234, '2021-02-10', '2022-02-10');

-- --------------------------------------------------------

--
-- Stand-in structure for view `UtstyrInstansInfo`
-- (See below for the actual view)
--
CREATE TABLE `UtstyrInstansInfo` (
`InstansID` int(11)
,`ModellNavn` varchar(45)
,`MerkeNavn` varchar(45)
,`ModellID` int(11)
,`TypeNavn` varchar(45)
,`KategoriNavn` varchar(45)
,`LeiePrisDøgn` decimal(8,2)
,`SistVedlikeholdt` date
,`NesteVedlikehold` date
);

-- --------------------------------------------------------

--
-- Table structure for table `UtstyrKategori`
--

CREATE TABLE `UtstyrKategori` (
  `KategoriID` int(11) NOT NULL,
  `KategoriNavn` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `UtstyrKategori`
--

INSERT INTO `UtstyrKategori` (`KategoriID`, `KategoriNavn`) VALUES
(1, 'Lette maskiner'),
(2, 'Tunge maskiner'),
(3, 'Anleggsutstyr');

-- --------------------------------------------------------

--
-- Table structure for table `UtstyrType`
--

CREATE TABLE `UtstyrType` (
  `TypeID` int(11) NOT NULL,
  `TypeNavn` varchar(45) NOT NULL,
  `UtstyrKategori_KategoriID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `UtstyrType`
--

INSERT INTO `UtstyrType` (`TypeID`, `TypeNavn`, `UtstyrKategori_KategoriID`) VALUES
(1, 'Kompressor', 1),
(2, 'Minigraver', 2),
(3, 'Stilas', 3),
(4, 'Sementblander', 3),
(5, 'Spikerpistol', 1);

-- --------------------------------------------------------

--
-- Structure for view `KundeInfo`
--
DROP TABLE IF EXISTS `KundeInfo`;

CREATE ALGORITHM=UNDEFINED DEFINER=`stud_v24_mka224`@`%` SQL SECURITY DEFINER VIEW `KundeInfo`  AS  select `KT`.`KundeType` AS `KundeType`,`K`.`KundeNr` AS `KundeNr`,`K`.`KundeNavn` AS `KundeNavn`,`KE`.`Epost` AS `Epost`,`KTlf`.`Nummer` AS `Nummer`,`FA`.`PostNr` AS `PostNr`,`FA`.`Poststed` AS `Poststed`,`FA`.`Adresse` AS `Adresse` from ((((`KundeType` `KT` left join `Kunde` `K` on(`K`.`KundeType_KundeType` = `KT`.`KundeType`)) left join `FakturaAdresse` `FA` on(`K`.`KundeNr` = `FA`.`Kunde_KundeNr`)) left join `KundeEpost` `KE` on(`K`.`KundeNr` = `KE`.`Kunde_KundeNr`)) left join `KundeTelefonnummer` `KTlf` on(`K`.`KundeNr` = `KTlf`.`Kunde_KundeNr`)) ;

-- --------------------------------------------------------

--
-- Structure for view `UtstyrInstansInfo`
--
DROP TABLE IF EXISTS `UtstyrInstansInfo`;

CREATE ALGORITHM=UNDEFINED DEFINER=`stud_v24_mka224`@`%` SQL SECURITY DEFINER VIEW `UtstyrInstansInfo`  AS  select `UI`.`InstansID` AS `InstansID`,`Mo`.`ModellNavn` AS `ModellNavn`,`Me`.`MerkeNavn` AS `MerkeNavn`,`Mo`.`ModellID` AS `ModellID`,`UT`.`TypeNavn` AS `TypeNavn`,`UK`.`KategoriNavn` AS `KategoriNavn`,`Mo`.`LeiePrisDøgn` AS `LeiePrisDøgn`,`UI`.`SistVedlikeholdt` AS `SistVedlikeholdt`,`UI`.`NesteVedlikehold` AS `NesteVedlikehold` from ((((`UtstyrInstans` `UI` left join `Modell` `Mo` on(`UI`.`Modell_ModellID` = `Mo`.`ModellID`)) left join `Merke` `Me` on(`Mo`.`Merke_MerkeID` = `Me`.`MerkeID`)) left join `UtstyrType` `UT` on(`Mo`.`UtstyrType_TypeID` = `UT`.`TypeID`)) left join `UtstyrKategori` `UK` on(`UT`.`UtstyrKategori_KategoriID` = `UK`.`KategoriID`)) ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `FakturaAdresse`
--
ALTER TABLE `FakturaAdresse`
  ADD PRIMARY KEY (`Kunde_KundeNr`),
  ADD KEY `fk_Fakturaadresse_Kunde1_idx` (`Kunde_KundeNr`);

--
-- Indexes for table `Kunde`
--
ALTER TABLE `Kunde`
  ADD PRIMARY KEY (`KundeNr`),
  ADD KEY `fk_Kunde_KundeType1_idx` (`KundeType_KundeType`);

--
-- Indexes for table `KundeBehandler`
--
ALTER TABLE `KundeBehandler`
  ADD PRIMARY KEY (`KundeBehandlerNr`);

--
-- Indexes for table `KundeEpost`
--
ALTER TABLE `KundeEpost`
  ADD PRIMARY KEY (`Epost`,`Kunde_KundeNr`),
  ADD KEY `fk_KundeEpost_Kunde1_idx` (`Kunde_KundeNr`);

--
-- Indexes for table `KundeTelefonnummer`
--
ALTER TABLE `KundeTelefonnummer`
  ADD PRIMARY KEY (`Nummer`,`Kunde_KundeNr`),
  ADD KEY `fk_KundeTelefonnummer_Kunde1_idx` (`Kunde_KundeNr`);

--
-- Indexes for table `KundeType`
--
ALTER TABLE `KundeType`
  ADD PRIMARY KEY (`KundeType`);

--
-- Indexes for table `LeveringsAdresse`
--
ALTER TABLE `LeveringsAdresse`
  ADD PRIMARY KEY (`Utleie_UtleieID`),
  ADD KEY `fk_Leveringsadresse_Utstyrsleie1_idx` (`Utleie_UtleieID`);

--
-- Indexes for table `Merke`
--
ALTER TABLE `Merke`
  ADD PRIMARY KEY (`MerkeID`);

--
-- Indexes for table `Modell`
--
ALTER TABLE `Modell`
  ADD PRIMARY KEY (`ModellID`),
  ADD KEY `indexModellNavn` (`ModellNavn`),
  ADD KEY `fk_Modell_UtstyrsType1_idx` (`UtstyrType_TypeID`),
  ADD KEY `fk_Modell_Merke1_idx` (`Merke_MerkeID`);

--
-- Indexes for table `Utleie`
--
ALTER TABLE `Utleie`
  ADD PRIMARY KEY (`UtleieID`),
  ADD KEY `fk_Kunde_has_UtstyrsInstans_Kunde1_idx` (`Kunde_KundeNr`),
  ADD KEY `fk_Utstyrsleie_Kundebehandler1_idx` (`KundeBehandler_KundeBehandlerNr`),
  ADD KEY `fk_utstyrinstans_idx` (`UtstyrInstans_InstansID`,`UtstyrInstans_Modell_ModellID`);

--
-- Indexes for table `UtstyrInstans`
--
ALTER TABLE `UtstyrInstans`
  ADD PRIMARY KEY (`InstansID`,`Modell_ModellID`),
  ADD KEY `fk_UtstyrsInstans_Modell1_idx` (`Modell_ModellID`);

--
-- Indexes for table `UtstyrKategori`
--
ALTER TABLE `UtstyrKategori`
  ADD PRIMARY KEY (`KategoriID`);

--
-- Indexes for table `UtstyrType`
--
ALTER TABLE `UtstyrType`
  ADD PRIMARY KEY (`TypeID`),
  ADD KEY `fk_UtstyrsType_UtstyrsKategori1_idx` (`UtstyrKategori_KategoriID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `KundeBehandler`
--
ALTER TABLE `KundeBehandler`
  MODIFY `KundeBehandlerNr` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `Merke`
--
ALTER TABLE `Merke`
  MODIFY `MerkeID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `Utleie`
--
ALTER TABLE `Utleie`
  MODIFY `UtleieID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `UtstyrKategori`
--
ALTER TABLE `UtstyrKategori`
  MODIFY `KategoriID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `UtstyrType`
--
ALTER TABLE `UtstyrType`
  MODIFY `TypeID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `FakturaAdresse`
--
ALTER TABLE `FakturaAdresse`
  ADD CONSTRAINT `fk_Fakturaadresse_Kunde1` FOREIGN KEY (`Kunde_KundeNr`) REFERENCES `Kunde` (`KundeNr`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `Kunde`
--
ALTER TABLE `Kunde`
  ADD CONSTRAINT `fk_Kunde_KundeType1` FOREIGN KEY (`KundeType_KundeType`) REFERENCES `KundeType` (`KundeType`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `KundeEpost`
--
ALTER TABLE `KundeEpost`
  ADD CONSTRAINT `fk_KundeEpost_Kunde1` FOREIGN KEY (`Kunde_KundeNr`) REFERENCES `Kunde` (`KundeNr`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `KundeTelefonnummer`
--
ALTER TABLE `KundeTelefonnummer`
  ADD CONSTRAINT `fk_KundeTelefonnummer_Kunde1` FOREIGN KEY (`Kunde_KundeNr`) REFERENCES `Kunde` (`KundeNr`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `LeveringsAdresse`
--
ALTER TABLE `LeveringsAdresse`
  ADD CONSTRAINT `fk_Leveringsadresse_Utstyrsleie1` FOREIGN KEY (`Utleie_UtleieID`) REFERENCES `Utleie` (`UtleieID`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `Modell`
--
ALTER TABLE `Modell`
  ADD CONSTRAINT `fk_Modell_Merke1` FOREIGN KEY (`Merke_MerkeID`) REFERENCES `Merke` (`MerkeID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Modell_UtstyrsType1` FOREIGN KEY (`UtstyrType_TypeID`) REFERENCES `UtstyrType` (`TypeID`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `Utleie`
--
ALTER TABLE `Utleie`
  ADD CONSTRAINT `fk_Kunde_has_UtstyrsInstans_Kunde1` FOREIGN KEY (`Kunde_KundeNr`) REFERENCES `Kunde` (`KundeNr`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Utstyrsleie_Kundebehandler1` FOREIGN KEY (`KundeBehandler_KundeBehandlerNr`) REFERENCES `KundeBehandler` (`KundeBehandlerNr`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_utstyrinstans` FOREIGN KEY (`UtstyrInstans_InstansID`,`UtstyrInstans_Modell_ModellID`) REFERENCES `UtstyrInstans` (`InstansID`, `Modell_ModellID`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `UtstyrInstans`
--
ALTER TABLE `UtstyrInstans`
  ADD CONSTRAINT `fk_UtstyrsInstans_Modell1` FOREIGN KEY (`Modell_ModellID`) REFERENCES `Modell` (`ModellID`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `UtstyrType`
--
ALTER TABLE `UtstyrType`
  ADD CONSTRAINT `fk_UtstyrsType_UtstyrsKategori1` FOREIGN KEY (`UtstyrKategori_KategoriID`) REFERENCES `UtstyrKategori` (`KategoriID`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
