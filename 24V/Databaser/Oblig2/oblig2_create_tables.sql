-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Table `KundeBehandler`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `KundeBehandler` (
  `KundeBehandlerNr` INT NOT NULL AUTO_INCREMENT,
  `KundeBehandlerNavn` VARCHAR(100) NOT NULL,
  `KundeBehandlerTlf` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`KundeBehandlerNr`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `UtstyrKategori`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `UtstyrKategori` (
  `KategoriID` INT NOT NULL AUTO_INCREMENT,
  `KategoriNavn` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`KategoriID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `UtstyrType`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `UtstyrType` (
  `TypeID` INT NOT NULL AUTO_INCREMENT,
  `TypeNavn` VARCHAR(45) NOT NULL,
  `UtstyrKategori_KategoriID` INT NOT NULL,
  PRIMARY KEY (`TypeID`),
  INDEX `fk_UtstyrsType_UtstyrsKategori1_idx` (`UtstyrKategori_KategoriID` ASC) VISIBLE,
  CONSTRAINT `fk_UtstyrsType_UtstyrsKategori1`
    FOREIGN KEY (`UtstyrKategori_KategoriID`)
    REFERENCES `UtstyrKategori` (`KategoriID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Merke`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Merke` (
  `MerkeID` INT NOT NULL AUTO_INCREMENT,
  `MerkeNavn` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`MerkeID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Modell`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Modell` (
  `ModellID` INT NOT NULL,
  `ModellNavn` VARCHAR(45) NOT NULL,
  `UtstyrBeskrivelse` VARCHAR(1000) NULL,
  `UtstyrType_TypeID` INT NOT NULL,
  `Merke_MerkeID` INT NOT NULL,
  `LeiePrisDøgn` DECIMAL(8,2) NOT NULL,
  PRIMARY KEY (`ModellID`),
  INDEX `indexModellNavn` (`ModellNavn` ASC),
  INDEX `fk_Modell_UtstyrsType1_idx` (`UtstyrType_TypeID` ASC) VISIBLE,
  INDEX `fk_Modell_Merke1_idx` (`Merke_MerkeID` ASC) VISIBLE,
  CONSTRAINT `fk_Modell_UtstyrsType1`
    FOREIGN KEY (`UtstyrType_TypeID`)
    REFERENCES `UtstyrType` (`TypeID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Modell_Merke1`
    FOREIGN KEY (`Merke_MerkeID`)
    REFERENCES `Merke` (`MerkeID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `UtstyrInstans`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `UtstyrInstans` (
  `InstansID` INT NOT NULL AUTO_INCREMENT,
  `Modell_ModellID` INT NOT NULL,
  `SistVedlikeholdt` DATE NOT NULL,
  `NesteVedlikehold` DATE NOT NULL,
  PRIMARY KEY (`InstansID`, `Modell_ModellID`),
  INDEX `fk_UtstyrsInstans_Modell1_idx` (`Modell_ModellID` ASC) VISIBLE,
  CONSTRAINT `fk_UtstyrsInstans_Modell1`
    FOREIGN KEY (`Modell_ModellID`)
    REFERENCES `Modell` (`ModellID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `KundeType`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `KundeType` (
  `KundeType` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`KundeType`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Kunde`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Kunde` (
  `KundeNr` INT NOT NULL,
  `KundeNavn` VARCHAR(100) NOT NULL,
  `KundeType_KundeType` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`KundeNr`),
  INDEX `fk_Kunde_KundeType1_idx` (`KundeType_KundeType` ASC) VISIBLE,
  CONSTRAINT `fk_Kunde_KundeType1`
    FOREIGN KEY (`KundeType_KundeType`)
    REFERENCES `KundeType` (`KundeType`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `KundeTelefonnummer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `KundeTelefonnummer` (
  `Nummer` VARCHAR(45) NOT NULL,
  `Kunde_KundeNr` INT NOT NULL,
  PRIMARY KEY (`Nummer`, `Kunde_KundeNr`),
  INDEX `fk_KundeTelefonnummer_Kunde1_idx` (`Kunde_KundeNr` ASC) VISIBLE,
  CONSTRAINT `fk_KundeTelefonnummer_Kunde1`
    FOREIGN KEY (`Kunde_KundeNr`)
    REFERENCES `Kunde` (`KundeNr`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `KundeEpost`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `KundeEpost` (
  `Epost` VARCHAR(100) NOT NULL,
  `Kunde_KundeNr` INT NOT NULL,
  PRIMARY KEY (`Epost`, `Kunde_KundeNr`),
  INDEX `fk_KundeEpost_Kunde1_idx` (`Kunde_KundeNr` ASC) VISIBLE,
  CONSTRAINT `fk_KundeEpost_Kunde1`
    FOREIGN KEY (`Kunde_KundeNr`)
    REFERENCES `Kunde` (`KundeNr`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FakturaAdresse`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `FakturaAdresse` (
  `PostNr` CHAR(4) NOT NULL,
  `Poststed` VARCHAR(45) NOT NULL,
  `Adresse` VARCHAR(45) NOT NULL,
  `Kunde_KundeNr` INT NOT NULL,
  PRIMARY KEY (`Kunde_KundeNr`),
  INDEX `fk_Fakturaadresse_Kunde1_idx` (`Kunde_KundeNr` ASC) VISIBLE,
  CONSTRAINT `fk_Fakturaadresse_Kunde1`
    FOREIGN KEY (`Kunde_KundeNr`)
    REFERENCES `Kunde` (`KundeNr`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Utleie`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Utleie` (
  `UtleieID` INT NOT NULL AUTO_INCREMENT,
  `UtleidDato` DATE NOT NULL,
  `InnlevertDato` DATE NULL,
  `Betalingsmåte` VARCHAR(15) NOT NULL,
  `Kunde_KundeNr` INT NOT NULL,
  `UtstyrInstans_InstansID` INT NOT NULL,
  `UtstyrInstans_Modell_ModellID` INT NOT NULL,
  `KundeBehandler_KundeBehandlerNr` INT NOT NULL,
  PRIMARY KEY (`UtleieID`),
  INDEX `fk_Kunde_has_UtstyrsInstans_UtstyrsInstans1_idx` (`UtstyrInstans_InstansID` ASC, `UtstyrInstans_Modell_ModellID` ASC) VISIBLE,
  INDEX `fk_Kunde_has_UtstyrsInstans_Kunde1_idx` (`Kunde_KundeNr` ASC) VISIBLE,
  INDEX `fk_Utstyrsleie_Kundebehandler1_idx` (`KundeBehandler_KundeBehandlerNr` ASC) VISIBLE,
  CONSTRAINT `fk_Kunde_has_UtstyrsInstans_Kunde1`
    FOREIGN KEY (`Kunde_KundeNr`)
    REFERENCES `Kunde` (`KundeNr`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Kunde_has_UtstyrsInstans_UtstyrsInstans1`
    FOREIGN KEY (`UtstyrInstans_InstansID` , `UtstyrInstans_Modell_ModellID`)
    REFERENCES `UtstyrInstans` (`InstansID` , `Modell_ModellID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Utstyrsleie_Kundebehandler1`
    FOREIGN KEY (`KundeBehandler_KundeBehandlerNr`)
    REFERENCES `KundeBehandler` (`KundeBehandlerNr`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LeveringsAdresse`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LeveringsAdresse` (
  `Utleie_UtleieID` INT NOT NULL,
  `Postnr` CHAR(4) NOT NULL,
  `Poststed` VARCHAR(45) NOT NULL,
  `Adresse` VARCHAR(45) NOT NULL,
  `LeveresKunde` VARCHAR(6) NOT NULL,
  `Leveringskostnad` DECIMAL(8,2) NOT NULL,
  PRIMARY KEY (`Utleie_UtleieID`),
  INDEX `fk_Leveringsadresse_Utstyrsleie1_idx` (`Utleie_UtleieID` ASC) VISIBLE,
  CONSTRAINT `fk_Leveringsadresse_Utstyrsleie1`
    FOREIGN KEY (`Utleie_UtleieID`)
    REFERENCES `Utleie` (`UtleieID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Placeholder table for view `KundeInfo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `KundeInfo` (`KundeType` INT, `KundeNr` INT, `KundeNavn` INT, `Epost` INT, `Nummer` INT, `PostNr` INT, `Poststed` INT, `Adresse` INT);

-- -----------------------------------------------------
-- Placeholder table for view `UtstyrInstansInfo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `UtstyrInstansInfo` (`InstansID` INT, `ModellNavn` INT, `MerkeNavn` INT, `ModellID` INT, `TypeNavn` INT, `KategoriNavn` INT, `LeiePrisDøgn` INT, `SistVedlikeholdt` INT, `NesteVedlikehold` INT);

-- -----------------------------------------------------
-- View `KundeInfo`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `KundeInfo`;
CREATE  OR REPLACE VIEW `KundeInfo` AS
select KT.KundeType, K.KundeNr, K.KundeNavn, KE.Epost, KTlf.Nummer, FA.PostNr, FA.Poststed, FA.Adresse
from KundeType as KT
left join Kunde as K on K.KundeType_KundeType=KT.KundeType
left join FakturaAdresse as FA on K.KundeNr=FA.Kunde_KundeNr
left join KundeEpost as KE on K.KundeNr=KE.Kunde_KundeNr
left join KundeTelefonnummer as KTlf on K.KundeNr=KTlf.Kunde_KundeNr;

-- -----------------------------------------------------
-- View `UtstyrInstansInfo`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `UtstyrInstansInfo`;
CREATE  OR REPLACE VIEW `UtstyrInstansInfo` AS
select UI.InstansID, Mo.ModellNavn, Me.MerkeNavn, Mo.ModellID, UT.TypeNavn, UK.KategoriNavn, Mo.LeiePrisDøgn, UI.SistVedlikeholdt, UI.NesteVedlikehold
from UtstyrInstans as UI
left join Modell as Mo on UI.Modell_ModellID=Mo.ModellID
left join Merke as Me on Mo.Merke_MerkeID=Me.MerkeID
left join UtstyrType as UT on Mo.UtstyrType_TypeID=UT.TypeID
left join UtstyrKategori as UK on UT.UtstyrKategori_KategoriID=UK.KategoriID;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
