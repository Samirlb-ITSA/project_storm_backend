-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 28, 2023 at 06:49 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `storm`
--

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `userid` int(11) NOT NULL,
  `firstname` varchar(100) NOT NULL,
  `lastname` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `cellphone` int(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `creationdate` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `users`
  ADD PRIMARY KEY (`userid`),
  ADD UNIQUE KEY `email` (`email`);

ALTER TABLE `users`
  MODIFY `userid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`userid`, `firstname`, `lastname`, `email`, `cellphone`, `address`, `password`, `status`, `creationdate`) VALUES
(2, 'Juan', 'Evilla', 'juan.evilla', 320, 'bq', '123', 0, '2023-10-19 22:57:32'),
(3, 'david', 'perez', 'david.perez', 320, 'bq', '123', 0, '2023-10-19 22:57:32'),
(4, 'pepe', 'pepe', 'pepe', 320, 'bq', '123', 0, '2023-10-19 22:57:32'),
(5, 'jua', 'jua', 'jua@@', 323232, 'bqbq', '123', 1, '2023-10-21 12:43:21'),
(6, 'juanito', 'jua', 'jua@@uni', 323232, 'bqbq', '123', 1, '2023-10-21 12:43:40'),
(8, 'juanito', 'evilla', 'jua@@uniba', 323232, 'bqbq', '123', 1, '2023-10-21 12:50:44'),
(9, 'juan', 'evilla', 'jevilla@uni.com', 320, 'bq', '123', 1, '2023-10-26 21:28:47');

-- --------------------------------------------------------

--
-- Table structure for table `company`
--

CREATE TABLE `company` (
  `companyid` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `cellphone` int(11) NOT NULL,
  `address` varchar(100) NOT NULL,
  `nit` int(11) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `creationdate` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `company`
  ADD PRIMARY KEY (`companyid`);

ALTER TABLE `company`
  MODIFY `companyid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Dumping data for table `company`
--

INSERT INTO `company` (`companyid`, `name`, `email`, `cellphone`, `address`, `nit`, `status`, `creationdate`) VALUES
(1, 'Sykes', 'company@sykes.com', 333, 'bq', 0, 0, '2023-10-19 23:00:20'),
(2, 'Movate', 'movate@', 444, 'bq', 1234, 0, '2023-10-20 22:24:04');

-- --------------------------------------------------------

--
-- Table structure for table `joboffers`
--

CREATE TABLE `joboffers` (
  `offerid` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `workday` varchar(100) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `creationdate` datetime NOT NULL DEFAULT current_timestamp(),
  `companyid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `joboffers`
  ADD PRIMARY KEY (`offerid`),
  ADD KEY `companyid` (`companyid`);

ALTER TABLE `joboffers`
  MODIFY `offerid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

ALTER TABLE `joboffers`
  ADD CONSTRAINT `joboffers_ibfk_1` FOREIGN KEY (`companyid`) REFERENCES `company` (`companyid`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Dumping data for table `joboffers`
--

INSERT INTO `joboffers` (`offerid`, `name`, `workday`, `status`, `creationdate`, `companyid`) VALUES
(1, 'programming', 'fulltime', 0, '0000-00-00 00:00:00', 1),
(10, 'accounting', 'parttime', 1, '2023-10-20 21:48:34', 1),
(11, 'accounting', 'parttime', 1, '2023-10-20 21:49:23', 1),
(16, 'networks', 'daytime', 1, '2023-10-20 22:02:43', 1),
(17, 'admin', 'fulltime', 1, '2023-10-20 22:03:59', 1),
(18, 'Employee', 'Continuous', 1, '2023-10-20 22:33:28', 2);

-- --------------------------------------------------------

--
-- Table structure for table `applicants`
--

CREATE TABLE `applicants` (
  `applicantid` int(11) NOT NULL,
  `offerid` int(11) NOT NULL,
  `userid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `applicants`
  ADD PRIMARY KEY (`applicantid`),
  ADD KEY `offerid` (`offerid`),
  ADD KEY `userid` (`userid`);

ALTER TABLE `applicants`
  MODIFY `applicantid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

ALTER TABLE `applicants`
  ADD CONSTRAINT `applicants_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `users` (`userid`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `applicants_ibfk_2` FOREIGN KEY (`offerid`) REFERENCES `joboffers` (`offerid`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Dumping data for table `applicants`
--

INSERT INTO `applicants` (`applicantid`, `offerid`, `userid`) VALUES
(1, 1, 2),
(2, 1, 3);

-- --------------------------------------------------------

--
-- Table structure for table `attributes`
--

CREATE TABLE `attributes` (
  `attributeid` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `attributes`
  ADD PRIMARY KEY (`attributeid`);

ALTER TABLE `attributes`
  MODIFY `attributeid` int(11) NOT NULL AUTO_INCREMENT;

-- --------------------------------------------------------

--
-- Table structure for table `attributesxuser`
--

CREATE TABLE `attributesxuser` (
  `attributesxuserid` int(11) NOT NULL,
  `attributeid` int(11) NOT NULL,
  `userid` int(11) NOT NULL,
  `field` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `attributesxuser`
  ADD PRIMARY KEY (`attributesxuserid`),
  ADD KEY `attributeid` (`attributeid`,`userid`),
  ADD KEY `userid` (`userid`);

ALTER TABLE `attributesxuser`
  MODIFY `attributesxuserid` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `attributesxuser`
  ADD CONSTRAINT `attributesxuser_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `users` (`userid`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `attributesxuser_ibfk_2` FOREIGN KEY (`attributeid`) REFERENCES `attributes` (`attributeid`) ON DELETE NO ACTION ON UPDATE NO ACTION;

-- --------------------------------------------------------

--
-- Table structure for table `career`
--

CREATE TABLE `career` (
  `careerid` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `career`
  ADD PRIMARY KEY (`careerid`);

ALTER TABLE `career`
  MODIFY `careerid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Dumping data for table `career`
--

INSERT INTO `career` (`careerid`, `name`) VALUES
(1, 'Ing Sistemas');

-- --------------------------------------------------------

--
-- Table structure for table `role`
--

CREATE TABLE `role` (
  `roleid` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `role`
  ADD PRIMARY KEY (`roleid`);

ALTER TABLE `role`
  MODIFY `roleid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Dumping data for table `role`
--

INSERT INTO `role` (`roleid`, `name`) VALUES
(1, '0'),
(2, 'teacher'),
(3, 'graduate');

-- --------------------------------------------------------

--
-- Table structure for table `rolexuser`
--

CREATE TABLE `rolexuser` (
  `rolexuserid` int(11) NOT NULL,
  `userid` int(11) NOT NULL,
  `roleid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `rolexuser`
  ADD PRIMARY KEY (`rolexuserid`),
  ADD KEY `userid` (`userid`),
  ADD KEY `roleid` (`roleid`);

ALTER TABLE `rolexuser`
  MODIFY `rolexuserid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

ALTER TABLE `rolexuser`
  ADD CONSTRAINT `rolexuser_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `users` (`userid`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `rolexuser_ibfk_2` FOREIGN KEY (`roleid`) REFERENCES `role` (`roleid`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Dumping data for table `rolexuser`
--

INSERT INTO `rolexuser` (`rolexuserid`, `userid`, `roleid`) VALUES
(2, 8, 1);

-- --------------------------------------------------------

--
-- Table structure for table `userxcareer`
--

CREATE TABLE `userxcareer` (
  `usercareerid` int(11) NOT NULL,
  `userid` int(11) NOT NULL,
  `careerid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `userxcareer`
  ADD PRIMARY KEY (`usercareerid`),
  ADD KEY `userid` (`userid`),
  ADD KEY `careerid` (`careerid`);

ALTER TABLE `userxcareer`
  MODIFY `usercareerid` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `userxcareer`
  ADD CONSTRAINT `userxcareer_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `users` (`userid`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `userxcareer_ibfk_2` FOREIGN KEY (`careerid`) REFERENCES `career` (`careerid`) ON DELETE NO ACTION ON UPDATE NO ACTION;

COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;