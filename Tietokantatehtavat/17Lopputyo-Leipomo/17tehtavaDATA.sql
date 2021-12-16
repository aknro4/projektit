
INSERT INTO a_tyyppi(tyyppi_num, tyyppi)
VALUES 
	(1, 'Organisaatio'),
	(2, 'yksityis_henkio')
;

INSERT INTO jm_ma (id, tyyppi)
VALUES 
	(1, 'jalleen_myyja'),
	(2, 'muu_asiakas')
;

INSERT INTO maksu (id,maksu_tyyppi)
VALUES 
	(1, 'Kateinen'),
	(2, 'Lasku')
;

INSERT INTO tuotteet (tuote_num, tuote_tyyppi)
VALUES 
	(1, 'Suklaa_kakku'),
	(2, 'Mansikka_Muffini'),
	(3, 'Mutakakku'),
	(4, 'Aurajuustokierre'),
	(5, 'Crossaint'),
	(6, 'Hedelmakakku'),
	(7, 'Kasvispiirakka'),
	(8, 'Juustoleipakakku'),
	(9, 'Mustikka_cup_cake'),
	(10, 'Vadelmaunelma')
;

INSERT INTO a_tiedot (nimi,puh,osoite,a_tyyppi_num, Jm_ma_num)
VALUES 
	('Betty Kauffman', 215-665-9415, '4267 Rocky Road',2, 2),
	('Pat Mims', 309-264-8178, '3924 Apple Lane',2, 2),
	('Bee_Herkut', 504-578-3107, '3236 Big Indian', 1, 1),
	('Glady Reid',412-526-4949, '174 Stiles Street', 2, 2),
	('Munkit',270-778-1702, '1555 Coffman Alley', 1, 2),
	('Jimmin_keittio', 228-572-6104, '950 Kelley Road', 1,1),
	('Glenn Miller', 360-626-0706, '3704 Mutton Town Road',2, 2),
	('Mummon_piirakat', 512-515-8282, '4412 Ashton Lane', 1,1)
;

INSERT INTO hinta (hinta_id, hinta ,a_tyyppi_num ,tuote_num)
VALUES 
	(1,26, 1, 1),
	(2,20, 2, 1),

	(3,32, 1, 2),
	(4,26, 2, 2),

	(5,27, 1, 3),
	(6,21, 2, 3), 

	(7,10,1, 4),
	(8,7, 2, 4),
	
	(9,19, 1, 5),
	(10,12, 2, 5),

	(11,33, 1, 6),
	(12,26, 2, 6),

	(13,19, 1, 7),
	(14,12, 2, 7),

	(15,6, 1, 8),
	(16,4, 2, 8),

	(17,31, 1, 9),
	(18,26, 2, 9),

	(19,35, 1, 10),
	(20,26, 2, 10)
;

INSERT INTO tilaukset (masku_tyyppi,asiakas_num,hinta_id)
VALUES 
	(2, 3, 4),
	(1, 7, 1),
	(2, 6, 8),
	(1, 1, 3),
	(1, 4, 17),
	(1, 2, 11),
	(2, 8, 16),
	(1, 1, 5),
	(1, 7, 9),
	(1, 4, 3),
	(2, 5, 8)
;