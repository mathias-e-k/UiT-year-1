DROP TABLE IF EXISTS `Skadesak` ;
DROP TABLE IF EXISTS `Forsikring` ;
DROP TABLE IF EXISTS `Kunde` ;

CREATE TABLE `stud_v24_mka224`.`Kunde` 
( 
    `KundeNr` INT NOT NULL AUTO_INCREMENT ,
    `FødselsDato` DATE NOT NULL , 
    `Fornavn` VARCHAR(45) NOT NULL , 
    `Etternavn` VARCHAR(45) NOT NULL , 
    PRIMARY KEY (`KundeNr`)
) ENGINE = InnoDB; 

CREATE TABLE `stud_v24_mka224`.`Forsikring` 
( 
    `ForsNr` INT NOT NULL AUTO_INCREMENT , 
    `KundeNr` INT NOT NULL , 
    `RegNr` VARCHAR(25) NOT NULL , 
    `RegAar` YEAR NOT NULL , 
    `KmPrAar` INT NOT NULL , 
    `ForsType` VARCHAR(25) NOT NULL , 
    `Bonus` DECIMAL(4,4) NOT NULL , 
    `AarsPremie` INT NOT NULL , 
    PRIMARY KEY (`ForsNr`),
    CONSTRAINT fk_forsikring_kunde FOREIGN KEY (`KundeNr`) REFERENCES `Kunde`(`KundeNr`),
    CONSTRAINT ForsTypeRegel CHECK (`ForsType` IN ('Ansvar', 'Delkasko', 'Kasko')),
    CONSTRAINT BonusRegel CHECK (`Bonus` BETWEEN 0 and 1)
) ENGINE = InnoDB; 

CREATE TABLE `stud_v24_mka224`.`Skadesak` 
( 
    `SaksNr` INT NOT NULL AUTO_INCREMENT , 
    `ForsNr` INT NOT NULL , 
    `RegDato` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    `SkadeType` VARCHAR(25) NOT NULL , 
    PRIMARY KEY (`SaksNr`),
    CONSTRAINT fk_skadesak_forsikring FOREIGN KEY (`ForsNr`) REFERENCES `Forsikring`(`ForsNr`)
) ENGINE = InnoDB; 

INSERT INTO `Kunde` (`KundeNr`, `FødselsDato`, `Fornavn`, `Etternavn`) 
    VALUES (NULL, '2022-10-01', 'Mat', 'i'), (NULL, '2020-03-24', 'Mia', 'Maren');

INSERT INTO `Forsikring` (`ForsNr`, `KundeNr`, `RegNr`, `RegAar`, `KmPrAar`, `ForsType`, `Bonus`, `AarsPremie`) 
    VALUES (NULL, '1', 'abc', '2009', '1000', 'Kasko', '0.8', '100'), (NULL, '2', 'sn 99', '2025', '9999', 'Ansvar', '0.2', '10');

INSERT INTO `Skadesak` (`SaksNr`, `ForsNr`, `RegDato`, `SkadeType`) 
    VALUES (NULL, '1', current_timestamp(), 'ow'), (NULL, '2', current_timestamp(), 'aaaa');