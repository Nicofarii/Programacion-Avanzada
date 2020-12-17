-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 17-12-2020 a las 19:50:25
-- Versión del servidor: 10.4.16-MariaDB
-- Versión de PHP: 7.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `agenda1`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `citas`
--

CREATE TABLE `citas` (
  `cit_id` int(11) NOT NULL COMMENT 'identificador de la cita',
  `con_id` int(11) NOT NULL COMMENT 'identificador del contacto',
  `cit_lugar` text NOT NULL COMMENT 'lugar de la cita',
  `cit_fecha` date NOT NULL COMMENT 'fecha de la cita',
  `cit_hora` time NOT NULL COMMENT 'hora de la cita',
  `cit_descripcion` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='tabla de las citas con los contactos';

--
-- Volcado de datos para la tabla `citas`
--

INSERT INTO `citas` (`cit_id`, `con_id`, `cit_lugar`, `cit_fecha`, `cit_hora`, `cit_descripcion`) VALUES
(3, 1, 'laboratorio', '2020-12-31', '10:10:00', 'tesis grado '),
(4, 3, 'parque', '2020-12-17', '12:48:00', 'jugar a la pelota'),
(5, 2, 'biblioteca', '2020-12-20', '14:00:00', 'Entrega de trabajo de grado'),
(8, 4, 'casa', '2020-12-17', '12:48:00', 'para cena familiar'),
(10, 5, 'Gimnacio', '2020-12-15', '15:15:00', 'pecho y espalda'),
(14, 8, 'Colegio La Paz', '2021-11-10', '20:03:00', 'Matricula estudiantes nuevos'),
(15, 7, 'Consejo superior', '2020-12-14', '22:30:00', 'Conferencia estudiantes nuevos'),
(17, 9, 'Chorro de Quevedo', '2020-12-24', '14:15:00', 'Reunion con los parceros');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `contactos`
--

CREATE TABLE `contactos` (
  `con_id` int(11) NOT NULL COMMENT 'identificador del contacto',
  `usu_id` int(11) NOT NULL,
  `con_nombre` varchar(50) NOT NULL COMMENT 'nombre del contacto',
  `con_apellido` varchar(50) NOT NULL COMMENT 'apellido del contacto',
  `con_direccion` varchar(250) NOT NULL COMMENT 'dirección del contacto',
  `con_telefono` varchar(20) NOT NULL COMMENT 'teléfono del contacto',
  `con_email` varchar(25) NOT NULL COMMENT 'correo electrónico del contacto'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='tabla de los contactos de la agenda';

--
-- Volcado de datos para la tabla `contactos`
--

INSERT INTO `contactos` (`con_id`, `usu_id`, `con_nombre`, `con_apellido`, `con_direccion`, `con_telefono`, `con_email`) VALUES
(1, 1, 'Juan Miguel', 'Diaz Perez', 'Calle 3ra 20-50 ', '3124565656', 'jmiguel@mail.com'),
(2, 1, 'Ana Juliana', 'Hernandez Riaño', 'Autonorte 170-34', '3115434343', 'ajuliana@mail.com'),
(3, 3, 'Pedro ', 'Parrado', 'trans 34 56-97', '3117898989', 'pparrado@mail.com'),
(4, 3, 'José', 'Higuera', 'Trans 12 67-98', '3145678900', 'jhiguera@mail.com'),
(5, 1, 'jose', 'jimenez', 'cra 1 #2-3', '123456789', 'jose@email.com'),
(7, 2, 'Francisco', 'Jose de Caldas', 'Calle 40 ', '321456789', 'josefra@email.com'),
(8, 5, 'Jairo', 'Aguilar', 'monserrate', '120487', 'jairo@email.com'),
(9, 6, 'Nicolas', 'Farias', 'cra 19d 1c 46', '3046068828', 'nimendezf@correo.udistrit');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `usu_id` int(11) NOT NULL,
  `usu_nombre` varchar(30) NOT NULL,
  `usu_clave` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`usu_id`, `usu_nombre`, `usu_clave`) VALUES
(1, 'admin', 'da39a3ee5e6b4b0d3255bfef95601890afd80709'),
(2, 'usuario1', 'ada6d34bca926b40be00893cabc0aeae138ea2a0'),
(3, 'usuario3', 'cd016c515962508538b851783fee065726058a4a'),
(5, 'Jairo', '2d9b1ec56b464dad9dcfe29975adfbecf19e68df'),
(6, 'Nicolas', 'f8b74df5965d9389218f437437468c3dc7357c7e');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `citas`
--
ALTER TABLE `citas`
  ADD PRIMARY KEY (`cit_id`),
  ADD KEY `fk_citas_contactos` (`con_id`);

--
-- Indices de la tabla `contactos`
--
ALTER TABLE `contactos`
  ADD PRIMARY KEY (`con_id`),
  ADD KEY `fk_contactos_usuarios` (`usu_id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`usu_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `citas`
--
ALTER TABLE `citas`
  MODIFY `cit_id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'identificador de la cita', AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT de la tabla `contactos`
--
ALTER TABLE `contactos`
  MODIFY `con_id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'identificador del contacto', AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `usu_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `citas`
--
ALTER TABLE `citas`
  ADD CONSTRAINT `fk_citas_contactos` FOREIGN KEY (`con_id`) REFERENCES `contactos` (`con_id`);

--
-- Filtros para la tabla `contactos`
--
ALTER TABLE `contactos`
  ADD CONSTRAINT `fk_contactos_usuarios` FOREIGN KEY (`usu_id`) REFERENCES `usuarios` (`usu_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
