-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 29.03.2021 klo 09:09
-- Palvelimen versio: 10.4.17-MariaDB
-- PHP Version: 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `lennot`
--

-- --------------------------------------------------------

--
-- Rakenne taululle `lennot`
--

CREATE TABLE `lennot` (
  `LentoID` int(11) NOT NULL,
  `Kohdemaa` varchar(255) NOT NULL,
  `Kaupunki` varchar(255) NOT NULL,
  `Aika` varchar(255) NOT NULL,
  `Kone` varchar(20) NOT NULL,
  `LipunHinta` decimal(10,2) NOT NULL,
  `VapaatPaikat` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Vedos taulusta `lennot`
--

INSERT INTO `lennot` (`LentoID`, `Kohdemaa`, `Kaupunki`, `Aika`, `Kone`, `LipunHinta`, `VapaatPaikat`) VALUES
(1, 'Suomi', 'Oulu', 'Aamu', 'Q400', '65.50', 15),
(2, 'Suomi', 'Oulu', 'Ilta', 'Q400', '65.75', 15),
(3, 'Suomi', 'Helsinki', 'Päivä', 'A220-300', '74.55', 0),
(4, 'Suomi', 'Rovaniemi', 'Päivä', 'Q400', '78.94', 3),
(5, 'Norja', 'Oslo', 'Aamu', 'Q400', '125.45', 40),
(6, 'Norja', 'Oslo', 'Aamu', 'A220-300', '132.53', 14),
(7, 'Norja', 'Bergen', 'Päivä', 'Q400', '86.45', 23),
(8, 'Norja', 'Bergen', 'Aamu', 'Q400', '75.88', 3),
(9, 'Ruotsi', 'Arlanda', 'Päivä', 'Q400', '98.12', 200),
(10, 'Ruotsi', 'Arlanda', 'Aamu', 'Q400', '99.49', 12),
(11, 'Ruotsi', 'Arlanda', 'Päivä', 'A220-300', '102.24', 50),
(12, 'Suomi', 'Helsinki', 'Päivä', 'Q400', '78.50', 0),
(13, 'Suomi', 'Rovaniemi', 'Päivä', 'Q400', '88.34', 16),
(14, 'Suomi', 'Helsinki', 'Päivä', 'A220-300', '87.32', 10),
(15, 'Norja', 'Bergen', 'Päivä', 'A220-100', '199.93', 7),
(16, 'Norja', 'Bergen', 'Ilta', 'A220-300', '213.05', 8),
(17, 'Suomi', 'Helsinki', 'Aamu', 'Q400', '81.20', 16),
(18, 'Suomi', 'Helsinki', 'Aamu', 'A220-100', '99.00', 20),
(19, 'Suomi', 'Oulu', 'Päivä', 'A220-100', '234.40', 7),
(20, 'Norja', 'Bergen', 'Ilta', 'A220-100', '134.90', 30),
(21, 'Norja', 'Bergen', 'Päivä', 'A220-300', '144.10', 8),
(22, 'Ruotsi', 'Göteborg', 'Ilta', 'A220-300', '55.00', 34),
(23, 'Ruotsi', 'Göteborg', 'Aamu', 'A220-300', '61.00', 12),
(24, 'Islanti', 'Keflaki', 'Ilta', 'A220-300', '63.00', 15),
(25, 'Ruotsi', 'Malmö', 'Ilta', 'Q400', '75.00', 32),
(26, 'Ruotsi', 'Malmö', 'Aamu', 'A220-300', '82.00', 0),
(27, 'Norja', 'Trondheim', 'Ilta', 'A220-300', '81.00', 16),
(28, 'Tanska ', 'Kööpenhamina', 'Ilta', 'A220-300', '91.00', 3),
(29, 'Ruotsi', 'Göteborg', 'Ilta', 'A220-300', '55.00', 34),
(30, 'Tanska', 'Billund', 'Ilta', 'A220-300', '61.00', 12),
(31, 'Islanti', 'Keflaki', 'Ilta', 'A220-300', '63.00', 11),
(32, 'Tanska', 'Billund', 'Aamu', 'Q400', '75.00', 32),
(33, 'Tanska', 'Kööpenhamina', 'Ilta', 'A220-300', '82.00', 12),
(34, 'Norja', 'Trondheim', 'Ilta', 'A220-300', '81.00', 16),
(35, 'Tanska ', 'Kööpenhamina', 'Ilta', 'A220-300', '91.00', 33);

-- --------------------------------------------------------

--
-- Rakenne taululle `matkustajat`
--

CREATE TABLE `matkustajat` (
  `id` int(11) NOT NULL,
  `maara` int(50) NOT NULL,
  `LentoID` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Rakenne taululle `tilaustiedot`
--

CREATE TABLE `tilaustiedot` (
  `TilausID` int(11) NOT NULL,
  `Aika` varchar(20) NOT NULL,
  `PVM` date NOT NULL,
  `Kaupunki` varchar(20) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `LennonID` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Vedos taulusta `tilaustiedot`
--

INSERT INTO `tilaustiedot` (`TilausID`, `Aika`, `PVM`, `Kaupunki`, `Email`, `LennonID`) VALUES
(8, 'Päivä', '0000-00-00', 'Helsinki', 'qsq@gmail.com', 14),
(12, 'Päivä', '0000-00-00', 'Helsinki', 'awdsad@gmail.com', 3),
(15, 'Päivä', '2021-03-25', 'Helsinki', 'was@gmail.com', 12),
(16, 'Päivä', '2021-04-03', 'Helsinki', 'was@gmail.com', 3),
(17, 'Päivä', '2021-04-03', 'Helsinki', 'wads@gmail.com', 12),
(18, 'Päivä', '2021-03-27', 'Helsinki', 'wads@gmail.com', 3),
(19, 'Päivä', '2021-04-04', 'Helsinki', 'was@gmail.com', 3),
(20, 'Päivä', '2021-04-04', 'Helsinki', 'was@gmail.com', 3),
(21, 'Aamu', '2021-03-27', 'Helsinki', 'wads@gmail.com', 17),
(22, 'Päivä', '2021-04-02', 'Helsinki', 'dwa@gmail.com', 3),
(23, 'Päivä', '2021-03-28', 'Helsinki', 'awdsad@gmail.com', 3),
(24, 'Päivä', '2021-04-11', 'Helsinki', 'awd@gmail.com', 3),
(25, 'Päivä', '2021-04-03', 'Helsinki', 'wdasd@gmail.com', 3),
(26, 'Päivä', '2021-04-02', 'Helsinki', 'wads@gmail.com', 3),
(27, 'Päivä', '2021-04-03', 'Helsinki', 'wads@gmail.com', 3),
(28, 'Päivä', '0000-00-00', 'Helsinki', 'dw@gmail.com', 3),
(29, 'Päivä', '0000-00-00', 'Helsinki', 'wdasd@gmail.com', 12),
(30, 'Aamu', '2021-04-03', 'Malmö', 'wads@gmail.com', 26),
(31, 'Aamu', '2021-04-03', 'Malmö', 'wads@gmail.com', 26),
(32, 'Päivä', '2021-04-03', 'Helsinki', 'wads@gmail.com', 14),
(33, 'Päivä', '2021-04-03', 'Helsinki', 'wads@gmail.com', 14),
(34, 'Päivä', '2021-04-03', 'Helsinki', 'wads@gmail.com', 14),
(35, 'Päivä', '2021-04-03', 'Helsinki', 'wads@gmail.com', 14),
(36, 'Päivä', '2021-04-03', 'Helsinki', 'wads@gmail.com', 14),
(37, 'Päivä', '2021-04-03', 'Helsinki', 'wads@gmail.com', 14),
(38, 'Päivä', '2021-04-03', 'Helsinki', 'wads@gmail.com', 14),
(39, 'Päivä', '2021-04-03', 'Helsinki', 'wads@gmail.com', 14),
(40, 'Päivä', '2021-04-03', 'Helsinki', 'wads@gmail.com', 14),
(41, 'Päivä', '2021-04-01', 'Helsinki', 'dw@gmail.com', 3),
(42, 'Päivä', '2021-04-01', 'Helsinki', 'dw@gmail.com', 3),
(43, 'Päivä', '2021-04-01', 'Helsinki', 'dw@gmail.com', 3),
(44, 'Päivä', '2021-04-01', 'Helsinki', 'dw@gmail.com', 3),
(45, 'Päivä', '2021-04-01', 'Helsinki', 'dw@gmail.com', 3),
(46, 'Päivä', '2021-04-01', 'Helsinki', 'dw@gmail.com', 3),
(47, 'Päivä', '2021-04-04', 'Helsinki', 'Testi@gmail.com', 12),
(48, 'Päivä', '0000-00-00', 'Helsinki', 'wads@gmail.com', 3),
(49, 'Päivä', '2021-04-04', 'Helsinki', 'wad@gmail.com', 14);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `lennot`
--
ALTER TABLE `lennot`
  ADD PRIMARY KEY (`LentoID`);

--
-- Indexes for table `matkustajat`
--
ALTER TABLE `matkustajat`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tilaustiedot`
--
ALTER TABLE `tilaustiedot`
  ADD PRIMARY KEY (`TilausID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `lennot`
--
ALTER TABLE `lennot`
  MODIFY `LentoID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `matkustajat`
--
ALTER TABLE `matkustajat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `tilaustiedot`
--
ALTER TABLE `tilaustiedot`
  MODIFY `TilausID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
