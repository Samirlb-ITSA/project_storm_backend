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
-- Table structure for table `aplicantes`
--

CREATE TABLE `aplicantes` (
  `idaplicante` int(11) NOT NULL,
  `idoferta` int(11) NOT NULL,
  `idusuario` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `aplicantes`
--

INSERT INTO `aplicantes` (`idaplicante`, `idoferta`, `idusuario`) VALUES
(1, 1, 2),
(2, 1, 3);

-- --------------------------------------------------------

--
-- Table structure for table `atributos`
--

CREATE TABLE `atributos` (
  `idatributo` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `atributosxusuario`
--

CREATE TABLE `atributosxusuario` (
  `idatributosxusuario` int(11) NOT NULL,
  `idatributos` int(11) NOT NULL,
  `idusuario` int(11) NOT NULL,
  `campo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `carrera`
--

CREATE TABLE `carrera` (
  `idcarrera` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `carrera`
--

INSERT INTO `carrera` (`idcarrera`, `nombre`) VALUES
(1, 'Ing Sistemas');

-- --------------------------------------------------------

--
-- Table structure for table `empresa`
--

CREATE TABLE `empresa` (
  `idempresa` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `celular` int(11) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `nit` int(11) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `fechacreacion` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `empresa`
--

INSERT INTO `empresa` (`idempresa`, `nombre`, `correo`, `celular`, `direccion`, `nit`, `estado`, `fechacreacion`) VALUES
(1, 'Sykes', 'empresa@sykes.com', 333, 'bq', 0, 0, '2023-10-19 23:00:20'),
(2, 'Movate', 'movate@', 444, 'bq', 1234, 0, '2023-10-20 22:24:04');

-- --------------------------------------------------------

--
-- Table structure for table `ofertaslaborales`
--

CREATE TABLE `ofertaslaborales` (
  `idoferta` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `jornadalaboral` varchar(100) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `fechacreacion` datetime NOT NULL DEFAULT current_timestamp(),
  `idempresa` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ofertaslaborales`
--

INSERT INTO `ofertaslaborales` (`idoferta`, `nombre`, `jornadalaboral`, `estado`, `fechacreacion`, `idempresa`) VALUES
(1, 'programacion', 'completa', 0, '0000-00-00 00:00:00', 1),
(10, 'contaduria', 'mediotiempo', 1, '2023-10-20 21:48:34', 1),
(11, 'contaduria', 'mediotiempo', 1, '2023-10-20 21:49:23', 1),
(16, 'redes', 'diurna', 1, '2023-10-20 22:02:43', 1),
(17, 'admin', 'completa', 1, '2023-10-20 22:03:59', 1),
(18, 'Empleado', 'Continua', 1, '2023-10-20 22:33:28', 2);

-- --------------------------------------------------------

--
-- Table structure for table `rol`
--

CREATE TABLE `rol` (
  `idrol` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rol`
--

INSERT INTO `rol` (`idrol`, `nombre`) VALUES
(1, '0'),
(2, 'docente'),
(3, 'egresado');

-- --------------------------------------------------------

--
-- Table structure for table `rolxusuario`
--

CREATE TABLE `rolxusuario` (
  `rolxusuarioid` int(11) NOT NULL,
  `idusuario` int(11) NOT NULL,
  `idrol` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rolxusuario`
--

INSERT INTO `rolxusuario` (`rolxusuarioid`, `idusuario`, `idrol`) VALUES
(2, 8, 1);

-- --------------------------------------------------------

--
-- Table structure for table `usuarios`
--

CREATE TABLE `usuarios` (
  `idusuario` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `celular` int(100) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `contraseña` varchar(100) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `fechacreacion` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `usuarios`
--

INSERT INTO `usuarios` (`idusuario`, `nombre`, `apellido`, `correo`, `celular`, `direccion`, `contraseña`, `estado`, `fechacreacion`) VALUES
(2, 'Juan', 'Evilla', 'juan.evilla', 320, 'bq', '123', 0, '2023-10-19 22:57:32'),
(3, 'david', 'perez', 'david.perez', 320, 'bq', '123', 0, '2023-10-19 22:57:32'),
(4, 'pepe', 'pepe', 'pepe', 320, 'bq', '123', 0, '2023-10-19 22:57:32'),
(5, 'jua', 'jua', 'jua@@', 323232, 'bqbq', '123', 1, '2023-10-21 12:43:21'),
(6, 'juanito', 'jua', 'jua@@uni', 323232, 'bqbq', '123', 1, '2023-10-21 12:43:40'),
(8, 'juanito', 'evilla', 'jua@@uniba', 323232, 'bqbq', '123', 1, '2023-10-21 12:50:44'),
(9, 'juan', 'evilla', 'jevilla@uni.com', 320, 'bq', '123', 1, '2023-10-26 21:28:47');

-- --------------------------------------------------------

--
-- Table structure for table `usuarioxcarrera`
--

CREATE TABLE `usuarioxcarrera` (
  `idusuariocarrera` int(11) NOT NULL,
  `idusuario` int(11) NOT NULL,
  `idcarrera` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `aplicantes`
--
ALTER TABLE `aplicantes`
  ADD PRIMARY KEY (`idaplicante`),
  ADD KEY `idoferta` (`idoferta`),
  ADD KEY `idusuario` (`idusuario`);

--
-- Indexes for table `atributos`
--
ALTER TABLE `atributos`
  ADD PRIMARY KEY (`idatributo`);

--
-- Indexes for table `atributosxusuario`
--
ALTER TABLE `atributosxusuario`
  ADD PRIMARY KEY (`idatributosxusuario`),
  ADD KEY `idatributos` (`idatributos`,`idusuario`),
  ADD KEY `idusuario` (`idusuario`);

--
-- Indexes for table `carrera`
--
ALTER TABLE `carrera`
  ADD PRIMARY KEY (`idcarrera`);

--
-- Indexes for table `empresa`
--
ALTER TABLE `empresa`
  ADD PRIMARY KEY (`idempresa`);

--
-- Indexes for table `ofertaslaborales`
--
ALTER TABLE `ofertaslaborales`
  ADD PRIMARY KEY (`idoferta`),
  ADD KEY `idempresa` (`idempresa`);

--
-- Indexes for table `rol`
--
ALTER TABLE `rol`
  ADD PRIMARY KEY (`idrol`);

--
-- Indexes for table `rolxusuario`
--
ALTER TABLE `rolxusuario`
  ADD PRIMARY KEY (`rolxusuarioid`),
  ADD KEY `usuarioid` (`idusuario`),
  ADD KEY `rolid` (`idrol`);

--
-- Indexes for table `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`idusuario`),
  ADD UNIQUE KEY `correo` (`correo`);

--
-- Indexes for table `usuarioxcarrera`
--
ALTER TABLE `usuarioxcarrera`
  ADD PRIMARY KEY (`idusuariocarrera`),
  ADD KEY `idusuario` (`idusuario`),
  ADD KEY `idcarrera` (`idcarrera`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `aplicantes`
--
ALTER TABLE `aplicantes`
  MODIFY `idaplicante` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `atributos`
--
ALTER TABLE `atributos`
  MODIFY `idatributo` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `atributosxusuario`
--
ALTER TABLE `atributosxusuario`
  MODIFY `idatributosxusuario` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `carrera`
--
ALTER TABLE `carrera`
  MODIFY `idcarrera` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `empresa`
--
ALTER TABLE `empresa`
  MODIFY `idempresa` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `ofertaslaborales`
--
ALTER TABLE `ofertaslaborales`
  MODIFY `idoferta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `rol`
--
ALTER TABLE `rol`
  MODIFY `idrol` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `rolxusuario`
--
ALTER TABLE `rolxusuario`
  MODIFY `rolxusuarioid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `idusuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `usuarioxcarrera`
--
ALTER TABLE `usuarioxcarrera`
  MODIFY `idusuariocarrera` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `aplicantes`
--
ALTER TABLE `aplicantes`
  ADD CONSTRAINT `aplicantes_ibfk_1` FOREIGN KEY (`idusuario`) REFERENCES `usuarios` (`idusuario`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `aplicantes_ibfk_2` FOREIGN KEY (`idoferta`) REFERENCES `ofertaslaborales` (`idoferta`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `atributosxusuario`
--
ALTER TABLE `atributosxusuario`
  ADD CONSTRAINT `atributosxusuario_ibfk_1` FOREIGN KEY (`idusuario`) REFERENCES `usuarios` (`idusuario`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `atributosxusuario_ibfk_2` FOREIGN KEY (`idatributos`) REFERENCES `atributos` (`idatributo`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `ofertaslaborales`
--
ALTER TABLE `ofertaslaborales`
  ADD CONSTRAINT `ofertaslaborales_ibfk_1` FOREIGN KEY (`idempresa`) REFERENCES `empresa` (`idempresa`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `rolxusuario`
--
ALTER TABLE `rolxusuario`
  ADD CONSTRAINT `rolxusuario_ibfk_1` FOREIGN KEY (`idusuario`) REFERENCES `usuarios` (`idusuario`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `rolxusuario_ibfk_2` FOREIGN KEY (`idrol`) REFERENCES `rol` (`idrol`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `usuarioxcarrera`
--
ALTER TABLE `usuarioxcarrera`
  ADD CONSTRAINT `usuarioxcarrera_ibfk_1` FOREIGN KEY (`idusuario`) REFERENCES `usuarios` (`idusuario`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `usuarioxcarrera_ibfk_2` FOREIGN KEY (`idcarrera`) REFERENCES `carrera` (`idcarrera`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
