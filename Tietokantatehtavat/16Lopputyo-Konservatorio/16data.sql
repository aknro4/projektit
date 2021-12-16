USE [16Tehtava]
GO
SET IDENTITY_INSERT [dbo].[soittimet] ON 

INSERT [dbo].[soittimet] ([soitin_num], [merkki], [soitin]) VALUES (1, N'Yamaha', N'Piano')
INSERT [dbo].[soittimet] ([soitin_num], [merkki], [soitin]) VALUES (2, N'Martin', N'Kitara')
INSERT [dbo].[soittimet] ([soitin_num], [merkki], [soitin]) VALUES (3, N'Yamaha', N'Uru')
INSERT [dbo].[soittimet] ([soitin_num], [merkki], [soitin]) VALUES (4, N'Gear4music', N'Marakassit')
INSERT [dbo].[soittimet] ([soitin_num], [merkki], [soitin]) VALUES (5, N'Yamaha', N'Rumpu')
SET IDENTITY_INSERT [dbo].[soittimet] OFF
GO
SET IDENTITY_INSERT [dbo].[opettajat] ON 

INSERT [dbo].[opettajat] ([opettaja_num], [nimi], [puhn], [osoite]) VALUES (1, N'John Lister', N'315-754-6989', N'4399 Saint Marys Avenue')
INSERT [dbo].[opettajat] ([opettaja_num], [nimi], [puhn], [osoite]) VALUES (2, N'Robert Connor', N'336-283-6278', N'584 Bryan Street')
INSERT [dbo].[opettajat] ([opettaja_num], [nimi], [puhn], [osoite]) VALUES (3, N'Debbie Vega', N'214-822-3620', N'2461 Liberty Street')
SET IDENTITY_INSERT [dbo].[opettajat] OFF
GO
SET IDENTITY_INSERT [dbo].[opiskelijat] ON 

INSERT [dbo].[opiskelijat] ([op_numero], [nimi], [puhn], [osoite], [opettaja_num]) VALUES (2, N'Murielle Sithembile', N'217-721-1612', N'4686 Parker Drive', 1)
INSERT [dbo].[opiskelijat] ([op_numero], [nimi], [puhn], [osoite], [opettaja_num]) VALUES (3, N'Marie Yoder', N'818-552-9005', N'829 Joy Lane', 3)
INSERT [dbo].[opiskelijat] ([op_numero], [nimi], [puhn], [osoite], [opettaja_num]) VALUES (4, N'Karen Dixon', N'540-819-7860', N'3396 Meadowview Drive', 2)
INSERT [dbo].[opiskelijat] ([op_numero], [nimi], [puhn], [osoite], [opettaja_num]) VALUES (5, N'Rose Doe', N'337-550-8207', N'3362 Sarah Drive', 2)
INSERT [dbo].[opiskelijat] ([op_numero], [nimi], [puhn], [osoite], [opettaja_num]) VALUES (6, N'Erna Griffith', N'206-495-3882', N'301 Elliot Avenue', 3)
INSERT [dbo].[opiskelijat] ([op_numero], [nimi], [puhn], [osoite], [opettaja_num]) VALUES (7, N'James Lyons', N'301-699-4684', N'1801 Adams Avenue', 2)
INSERT [dbo].[opiskelijat] ([op_numero], [nimi], [puhn], [osoite], [opettaja_num]) VALUES (8, N'Sabrina Palmer', N'603-536-2362', N'2126 Elliott Street', 1)
INSERT [dbo].[opiskelijat] ([op_numero], [nimi], [puhn], [osoite], [opettaja_num]) VALUES (9, N'Tasha Camarillo', N'484-204-2790', N'3977 Elmwood Avenue', 1)
INSERT [dbo].[opiskelijat] ([op_numero], [nimi], [puhn], [osoite], [opettaja_num]) VALUES (10, N'Evelyn Atkinson', N'860-366-6720', N'4825 Lochmere Lane', 2)
INSERT [dbo].[opiskelijat] ([op_numero], [nimi], [puhn], [osoite], [opettaja_num]) VALUES (11, N'Donald Anthony', N'561-988-4744', N'4952 Pleasant Hill Road', 1)
SET IDENTITY_INSERT [dbo].[opiskelijat] OFF
GO
SET IDENTITY_INSERT [dbo].[kaytossa] ON 

INSERT [dbo].[kaytossa] ([id], [soitin_num], [opiskelija_num]) VALUES (1, 3, 2)
INSERT [dbo].[kaytossa] ([id], [soitin_num], [opiskelija_num]) VALUES (2, 5, 3)
INSERT [dbo].[kaytossa] ([id], [soitin_num], [opiskelija_num]) VALUES (3, 2, 6)
INSERT [dbo].[kaytossa] ([id], [soitin_num], [opiskelija_num]) VALUES (4, 2, 9)
INSERT [dbo].[kaytossa] ([id], [soitin_num], [opiskelija_num]) VALUES (5, 5, 10)
INSERT [dbo].[kaytossa] ([id], [soitin_num], [opiskelija_num]) VALUES (8, 2, 5)
INSERT [dbo].[kaytossa] ([id], [soitin_num], [opiskelija_num]) VALUES (9, 4, 4)
INSERT [dbo].[kaytossa] ([id], [soitin_num], [opiskelija_num]) VALUES (10, 1, 7)
INSERT [dbo].[kaytossa] ([id], [soitin_num], [opiskelija_num]) VALUES (11, 2, 8)
INSERT [dbo].[kaytossa] ([id], [soitin_num], [opiskelija_num]) VALUES (12, 3, 11)
INSERT [dbo].[kaytossa] ([id], [soitin_num], [opiskelija_num]) VALUES (16, 4, 3)
INSERT [dbo].[kaytossa] ([id], [soitin_num], [opiskelija_num]) VALUES (17, 1, 4)
INSERT [dbo].[kaytossa] ([id], [soitin_num], [opiskelija_num]) VALUES (18, 2, 5)
SET IDENTITY_INSERT [dbo].[kaytossa] OFF
GO
