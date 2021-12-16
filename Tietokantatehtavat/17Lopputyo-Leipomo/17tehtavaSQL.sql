CREATE TABLE a_tyyppi (
	tyyppi_num INT NOT NULL PRIMARY KEY,
	tyyppi VARCHAR(150) NOT NULL
);

CREATE TABLE jm_ma (
	id INT NOT NULL PRIMARY KEY,
	tyyppi VARCHAR(150) NOT NULL
);

CREATE TABLE tuotteet (
	tuote_num INT NOT NULL PRIMARY KEY,
	tuote_tyyppi VARCHAR(150)
);

CREATE TABLE hinta (
	hinta_id INT NOT NULL PRIMARY KEY,
	hinta INT NOT NULL,
	a_tyyppi_num INT NOT NULL,
	tuote_num INT NOT NULL
	CONSTRAINT FK_hinta_a_tyyppi FOREIGN KEY (a_tyyppi_num)
	REFERENCES a_tyyppi(tyyppi_num),
	CONSTRAINT FK_hinta_tuotteet FOREIGN KEY (tuote_num)
	REFERENCES tuotteet(tuote_num)
);

CREATE TABLE a_tiedot (
	asiakas_num INT NOT NULL IDENTITY(1,1),
	nimi VARCHAR(150) NOT NULL,
	puh VARCHAR(150) NOT NULL,
	osoite VARCHAR(150) NOT NULL,
	a_tyyppi_num INT NOT NULL,
	Jm_ma_num INT,
	PRIMARY KEY (asiakas_num),
	CONSTRAINT FK_a_tiedot_a_tyyppi FOREIGN KEY (a_tyyppi_num)
	REFERENCES a_tyyppi(tyyppi_num),
	CONSTRAINT FK_a_tiedot_jm_ma FOREIGN KEY (Jm_ma_num)
	REFERENCES jm_ma(id)
);

CREATE TABLE maksu (
	id INT NOT NULL PRIMARY KEY,
	maksu_tyyppi VARCHAR(150) NOT NULL
);

CREATE TABLE tilaukset (
	tilaus_id INT NOT NULL IDENTITY(1,1),
	masku_tyyppi INT NOT NULL PRIMARY KEY,
	asiakas_num INT NOT NULL,
	hinta_id INT NOT NULL,
	CONSTRAINT FK_tilaukset_a_tiedot FOREIGN KEY (asiakas_num)
	REFERENCES a_tiedot(asiakas_num),
	CONSTRAINT FK_tilaukset_hinta FOREIGN KEY (hinta_id)
	REFERENCES hinta(hinta_id),
	CONSTRAINT FK_tilausket_maksu FOREIGN KEY (masku_tyyppi)
	REFERENCES maksu(id)
);











