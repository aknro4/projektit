CREATE TABLE Rastit (
	rasti_id INT NOT NULL PRIMARY KEY IDENTITY(1,1),
	osallistuja_id INT NOT NULL,
	Lahtoaika varchar(150),
	Rasti1 varchar(150),
	Rasti2 varchar(150),
	Rasti3 varchar(150),
	Rasti4 varchar(150),
	Rasti5 varchar(150),
	Rasti6 varchar(150),
	Rasti7 varchar(150),
	Rasti8 varchar(150),
	Rasti9 varchar(150),
	Rasti10 varchar(150),
	Loppuaika varchar(150)
);

ALTER TABLE Suunnistus
ADD PRIMARY KEY (ID);

ALTER TABLE Suunnistus
ADD RastitID INT;

ALTER TABLE Suunnistus
ADD CONSTRAINT FK_Suunnistus_Kisa FOREIGN KEY (RastitID)
	REFERENCES Rastit(rasti_id);

CREATE TABLE Sarja (
	sarja_id INT NOT NULL PRIMARY KEY,
	sarja_nimi VARCHAR(150) NOT NULL
);

INSERT Sarja (sarja_id,sarja_nimi)
VALUES 
	(1, 'Miehet'),
	(2,'Naiset')
;


UPDATE Suunnistus 
SET Sarja = 1 WHERE sarja = 'Miehet';

UPDATE Suunnistus
SET Sarja = 2 WHERE Sarja = 'Naiset';

ALTER TABLE Suunnistus
ADD CONSTRAINT FK_Sunnistus_sarja FOREIGN KEY (sarja)
	REFERENCES sarja(sarja_id);


CREATE TABLE Osallistuja_tiedot (
	osallistuja_id INT NOT NULL PRIMARY KEY ,
	nimi VARCHAR(150),
	osoite VARCHAR(150),
	seura VARCHAR (150),
	ika INT
);

INSERT INTO Osallistuja_tiedot (osallistuja_id,nimi,osoite,seura,ika)
SELECT id,Nimi,Osoite,Seura,ika
FROM Suunnistus;

ALTER TABLE Suunnistus
ADD CONSTRAINT FK_Suunnistus_Osallistuja_tiedot FOREIGN KEY (ID)
	REFERENCES Osallistuja_tiedot(osallistuja_id);



CREATE TABLE Kisa (
	kisa_id INT NOT NULL PRIMARY KEY,
	kisa_nimi VARCHAR(150)
);

INSERT INTO Kisa(kisa_id,kisa_nimi)
VALUES 
	(1,'Kuntorastit Laajavuori'),
	(2, 'Kuntorastit Touruvuori'),
	(3,'Kuntorastit V‰‰r‰m‰ki')
;

UPDATE Suunnistus
SET Kisa = 1 WHERE kisa = 'Kuntorastit Laajavuori';

UPDATE Suunnistus
SET Kisa = 2 WHERE kisa = 'Kuntorastit Touruvuori';

UPDATE Suunnistus
SET Kisa = 3 WHERE kisa = 'Kuntorastit V‰‰r‰m‰ki';

ALTER TABLE Suunnistus
ADD CONSTRAINT FK_Suunnistus_kisa FOREIGN KEY (kisa)
	REFERENCES Kisa(kisa_id);

ALTER TABLE Suunnistus 
DROP COLUMN Rasti1,Rasti2,Rasti3,Rasti4,Rasti5,Rasti6,Rasti7,Rasti8,Rasti9,Rasti10,Lahtoaika,Loppuaika,Nimi,osoite,seura,ika;

