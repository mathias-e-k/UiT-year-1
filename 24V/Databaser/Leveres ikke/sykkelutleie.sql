DROP TABLE IF EXISTS `Utleie` ;
DROP TABLE IF EXISTS `Sykkel` ;
DROP TABLE IF EXISTS `Modell` ;
DROP TABLE IF EXISTS `Kunde` ;


CREATE TABLE `stud_v24_mka224`.`Modell` 
    ( `MNr` INT NOT NULL AUTO_INCREMENT, 
    `Modellnavn` VARCHAR(45) NOT NULL , 
    `Dagpris` INT NOT NULL , 
    PRIMARY KEY (`MNr`), 
    UNIQUE `Modellnavn_UQ` (`Modellnavn`)
    ) ENGINE = InnoDB; 

CREATE TABLE `stud_v24_mka224`.`Sykkel` 
    ( `MNr` INT NOT NULL , 
    `KopiNr` INT NOT NULL , 
    `Ramme` VARCHAR(45) , 
    `Farge` VARCHAR(45) , 
    PRIMARY KEY (`MNr`, `KopiNr`),
    CONSTRAINT fk_sykkel_modell_mnr FOREIGN KEY (`MNr`) REFERENCES `Modell`(`MNr`)
    ) ENGINE = InnoDB; 

CREATE TABLE `stud_v24_mka224`.`Kunde` 
    ( `KNr` INT NOT NULL AUTO_INCREMENT , 
    `Fornavn` VARCHAR(45) NOT NULL , 
    `Etternavn` VARCHAR(45) NOT NULL , 
    `Mobil` VARCHAR(45) , 
    PRIMARY KEY (`KNr`)
    ) ENGINE = InnoDB; 

CREATE TABLE `stud_v24_mka224`.`Utleie` 
    ( `KNr` INT NOT NULL , 
    `MNr` INT NOT NULL , 
    `KopiNr` INT NOT NULL , 
    `TidUt` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP , 
    `TidInn` DATETIME NULL , 
    PRIMARY KEY (`KNr`, `MNr`, `KopiNr`, `TidUt`),
    UNIQUE `utleie_UQ` (`MNr`, `KopiNr`, `TidInn`),
    CONSTRAINT fk_utleie_kunde FOREIGN KEY (`KNr`) REFERENCES `Kunde`(`KNr`),
    CONSTRAINT fk_utleie_sykkel FOREIGN KEY (`MNr`, `KopiNr`) REFERENCES `Sykkel`(`MNr`, `KopiNr`)
    ) ENGINE = InnoDB; 

INSERT INTO `Kunde` (`KNr`, `Fornavn`, `Etternavn`, `Mobil`) 
    VALUES (NULL, 'Mia', 'A', '12312123'), (NULL, 'Lol', 'ol', '112');

INSERT INTO `Modell` (`MNr`, `Modellnavn`, `Dagpris`) 
    VALUES (NULL, 'Cross', '200'), (NULL, 'Cool', '100'), (NULL, 'slow 2000', '25');

INSERT INTO `Sykkel` (`MNr`, `KopiNr`, `Ramme`, `Farge`) 
    VALUES ('2', '1', 's', 'Black'), ('2', '2', 'B', 'RED'), ('1', '1', 'M', 'Purple');

INSERT INTO `Utleie` (`KNr`, `MNr`, `KopiNr`, `TidUt`, `TidInn`) 
    VALUES ('1', '1', '1', current_timestamp(), NULL), ('2', '2', '2', current_timestamp(), NULL);