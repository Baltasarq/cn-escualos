-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 28-06-2019 a las 10:33:46
-- Versión del servidor: 10.2.24-MariaDB-cll-lve
-- Versión de PHP: 7.2.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `rubenas_escualos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `administradores`
--

CREATE TABLE `administradores` (
  `dni` varchar(9) COLLATE utf8_spanish_ci NOT NULL,
  `nombre` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `email` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `password` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `administradores`
--

INSERT INTO `administradores` (`dni`, `nombre`, `email`, `password`) VALUES
('36098052N', 'Fernando Troncoso', 'cnescualos@gmail.com', 'XXXX'),
('44461157H', 'Rubén AS', 'rubenas91@gmail.com', 'neQh0RQQXI6WreVad3GSXQ=='),
('44484199Z', 'Marta Mira', 'pulpolito@gmail.com', 'XXXX'),
('44845966Z', 'Inés Marcos', 'ines.cnescualos@gmail.com', 'iKdE6TpqPPOG0czDKewVOw==');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `competiciones`
--

CREATE TABLE `competiciones` (
  `id` int(11) NOT NULL,
  `tipo` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `nombre` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `lugar` varchar(500) COLLATE utf8_spanish_ci NOT NULL,
  `ubicacion` varchar(500) COLLATE utf8_spanish_ci DEFAULT NULL,
  `fecha_competicion` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `fecha_inscripcion` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `estado` varchar(10) COLLATE utf8_spanish_ci NOT NULL DEFAULT 'cerrada',
  `pruebas` varchar(500) COLLATE utf8_spanish_ci NOT NULL,
  `relevos` varchar(500) COLLATE utf8_spanish_ci DEFAULT NULL,
  `comida` varchar(10) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `competiciones`
--

INSERT INTO `competiciones` (`id`, `tipo`, `nombre`, `lugar`, `ubicacion`, `fecha_competicion`, `fecha_inscripcion`, `estado`, `pruebas`, `relevos`, `comida`) VALUES
(2, 'campeonato', 'Campeonato Gallego de Verano', 'Piscina Rosario Dueñas (Ourense)', 'https://www.google.com/maps/place/Rosario+due%C3%B1as+Piscina/@42.3436266,-7.8731951,17z/data=!3m1!4b1!4m5!3m4!1s0xd2ffeb4bc28ed61:0x64579949a01a4eba!8m2!3d42.3436266!4d-7.8710064', '2019-06-08T17:00||2019-06-09T10:00||2019-06-09T16:00', '2019-05-27T20:00', 'abierta', '/S/||400L Femenino||400L Masculino||50E Femenino||50E Masculino||200S Femenino||200S Masculino||100M Femenino||100M Masculino/S/||50L Femenino||50L Masculino||200B Femenino||200B Masculino||50M Femenino||50M Masculino||200E Femenino||200E Masculino/S/||100E Femenino||100E Masculino||100L Femenino||100L Masculino||50B Femenino||50B Masculino', '/S/||4x50L Femenino||4x50L Masculino/S/||4x50S Mixto/S/||4x50S Femenino||4x50S Masculino', 'no||si'),
(15, 'liga', '5º Liga', 'Piscina de Santa Isabel - Santiago de Compostela', 'https://www.google.com/maps/place/Complexo+Deportivo+Santa+Isabel/@42.8861328,-8.5488724,17z/data=!3m1!4b1!4m5!3m4!1s0xd2efe5d0d43bfc5:0x7dc4328130a85d32!8m2!3d42.8861328!4d-8.5488724', '2019-05-12T10:00', '2019-05-05T23:00', 'abierta', '||100L Masculino||100L Femenino||50M Femenino||50M Masculino||50E Masculino||50E Femenino||50B Masculino||50B Femenino', '||4x50L Mixto', 'si'),
(16, 'jornada', 'I Clínic Natación Aguas Abiertas', 'Embalse Os Peares', 'https://www.google.com/maps?q=embalse+os+peares&rlz=1C1GCEA_enES768ES768&um=1&ie=UTF-8&sa=X&ved=0ahUKEwju3L-Y1KTiAhXgAGMBHbk6AzoQ_AUIDygC', '2019-06-02T11:00', '2019-05-31T22:00', 'abierta', '', '', 'si');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `escualos`
--

CREATE TABLE `escualos` (
  `nombre` varchar(30) CHARACTER SET latin1 NOT NULL,
  `sexo` varchar(1) CHARACTER SET latin1 NOT NULL,
  `ano` int(4) NOT NULL,
  `50M` varchar(5) CHARACTER SET latin1 NOT NULL,
  `50E` varchar(5) CHARACTER SET latin1 NOT NULL,
  `50B` varchar(5) CHARACTER SET latin1 NOT NULL,
  `50C` varchar(5) CHARACTER SET latin1 NOT NULL,
  `100M` varchar(6) COLLATE utf8_spanish_ci NOT NULL,
  `100E` varchar(6) COLLATE utf8_spanish_ci NOT NULL,
  `100B` varchar(6) COLLATE utf8_spanish_ci NOT NULL,
  `100C` varchar(6) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `escualos`
--

INSERT INTO `escualos` (`nombre`, `sexo`, `ano`, `50M`, `50E`, `50B`, `50C`, `100M`, `100E`, `100B`, `100C`) VALUES
('ALBA', 'M', 1985, '55', '53.2', '57.98', '42.8', '0', '116', '0', '93.78'),
('ALBACETE', 'H', 1983, '36.5', '39.13', '38.45', '29.94', '0', '0', '89.5', '67.22'),
('ALBERTO', 'H', 1971, '41.9', '45', '43.08', '34.12', '0', '0', '97.25', '79.41'),
('ALEX', 'H', 1993, '35.68', '33.73', '38', '28.17', '74.13', '0', '0', '62.98'),
('ANTUCHO', 'H', 1958, '49.01', '55', '55', '37.41', '', '', '', '92.22'),
('BOUSO', 'H', 1971, '41.54', '47.37', '41.33', '35.29', '0', '0', '92.52', '79.8'),
('CARMEN', 'M', 1976, '47', '53.35', '49.13', '40.40', '0', '109.2', '105.77', '86.21'),
('CIRA', 'M', 1981, '51.16', '42.35', '48.67', '39.22', '116.56', '88.38', '92.63', '84.51'),
('CORAL', 'M', 1987, '60', '60', '52.98', '47.43', '0', '0', '122.81', '100'),
('HUGO', 'H', 1978, '37', '38.02', '34.4', '29.31', '0', '0', '80.1', '66.27'),
('INES', 'M', 1989, '37.53', '37.38', '46', '33.56', '85.63', '81.34', '0', '74.75'),
('JESUS', 'H', 1973, '36.24', '39.32', '43.4', '30.81', '77.56', '87.36', '91.43', '68.02'),
('JOAQUIN', 'H', 1980, '50', '50', '41.66', '33', '0', '0', '89.13', '86.33'),
('MALENA', 'M', 1988, '45.99', '50', '52', '42.22', '108.55', '0', '0', '89.15'),
('MARIA DL', 'M', 1978, '45', '46.59', '53.06', '36.54', '0', '99.57', '111.34', '80.48'),
('MARIA H', 'M', 1974, '0', '52.58', '57', '55', '', '', '', '100'),
('MARTA', 'M', 1981, '43', '47', '42.65', '36.08', '0', '0', '95.62', '81.6'),
('MARTIÑO', 'H', 1988, '37.22', '41.59', '38.85', '34.86', '0', '88.16', '87.47', '81'),
('NATI', 'M', 1991, '42.6', '42', '41.1', '33.44', '0', '0', '89.76', '78.41'),
('OTE', 'H', 1989, '0', '44.55', '39.47', '34.83', '0', '0', '89.69', '79.7'),
('PAULA', 'M', 1986, '43', '46.26', '47.67', '39.51', '0', '0', '108.92', '100'),
('RAMON', 'H', 1958, '60', '60', '51.98', '41.32', '0', '0', '120.96', '97.86'),
('RAQUEL', 'M', 1988, '35.93', '0', '41.78', '32.08', '88.16', '0', '0', '75.42'),
('RUBEN', 'H', 1981, '41', '43', '41.1', '31.7', '0', '0', '92.46', '72.95'),
('SUSI', 'M', 1962, '60', '63.10', '55.23', '51.67', '0', '132.16', '125.09', '121.28'),
('TRONCOSO', 'H', 1975, '43.01', '48.77', '0', '33.28', '98.21', '110.45', '0', '76.88'),
('JOSUE', 'H', 1986, '32.18', '38', '35.5', '29.01', '77.51', '0', '77.4', '65.98'),
('PATRI', 'M', 1985, '60', '55', '53', '43', '', '', '', ''),
('PAULA MARCOS', 'M', 1990, '40', '44', '42', '34', '', '', '', ''),
('JUAN', 'H', 1970, '60', '55', '50', '38', '', '', '', ''),
('ISA', 'M', 1980, '65', '60', '58', '45', '', '', '', ''),
('CRISTEL', 'M', 1981, '60', '55', '52', '42', '', '', '', ''),
('CRISTIAN', 'H', 1994, '50', '50', '50', '35', '', '', '', ''),
('ABEL', 'H', 1986, '39', '39', '0', '33', '', '', '', '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inscripciones`
--

CREATE TABLE `inscripciones` (
  `id_competicion` int(11) NOT NULL,
  `dni` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `fecha` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `prueba1` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `tiempo1` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `prueba2` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `tiempo2` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `prueba3` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `tiempo3` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `relevos` varchar(10) COLLATE utf8_spanish_ci DEFAULT NULL,
  `comida` varchar(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `acompanantes` varchar(10) COLLATE utf8_spanish_ci DEFAULT NULL,
  `observaciones` mediumtext COLLATE utf8_spanish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `inscripciones`
--

INSERT INTO `inscripciones` (`id_competicion`, `dni`, `fecha`, `prueba1`, `tiempo1`, `prueba2`, `tiempo2`, `prueba3`, `tiempo3`, `relevos`, `comida`, `acompanantes`, `observaciones`) VALUES
(15, '34999787c', '25-04-2019 16:48:41', '100L Femenino', '110', '50B Femenino', '53', NULL, NULL, 'si', 'si', '2', ''),
(15, '44845966z', '25-04-2019 18:32:22', '50M Femenino', '37', '50E Femenino', '35', NULL, NULL, 'si', 'si', '1', ''),
(15, '44450014f', '26-04-2019 15:37:59', '50M Masculino', '35.85', '50B Masculino', '36.68', NULL, NULL, 'si', 'si', '0', 'Puedo cambiar la mariposa por 50 espalda a decisión de puntuar mejor para el equipo elegí la mariposa por separarla de la prueba de braza Podéis cambiarme sin problema de prueba ????'),
(15, '34984082R', '26-04-2019 20:55:11', '100L Masculino', '69', '50M Masculino', '35:41', NULL, NULL, 'si', 'no', '0', 'Realizado ingreso y enviado correo'),
(15, '34919280j', '26-04-2019 23:43:00', '100L Masculino', '105', NULL, NULL, NULL, NULL, 'si', 'si', '0', ''),
(15, '35575275w', '28-04-2019 10:21:29', '100L Masculino', '68', '50M Masculino', '33', NULL, NULL, 'si', 'pendiente', '0', ''),
(15, '34971277f', '28-04-2019 18:54:42', '100L Masculino', '68', '50B Masculino', '35.04', NULL, NULL, 'si', 'no', '0', ''),
(15, '77411359Y', '28-04-2019 21:00:41', '100L Femenino', '115', '50B Femenino', '53', NULL, NULL, 'no', 'si', '0', ''),
(15, '44656680h', '29-04-2019 21:39:26', '100L Femenino', '77', '50B Femenino', '43', NULL, NULL, 'si', 'no', '0', ''),
(15, '36043465G', '02-05-2019 09:28:03', '50E Femenino', '65', '50B Femenino', '55', NULL, NULL, 'si', 'si', '0', ''),
(15, '36098052n', '02-05-2019 09:46:17', NULL, NULL, NULL, NULL, NULL, NULL, 'si', 'no', '0', 'Debido al cambio de fecha no podre asistir!!'),
(15, 'y0064514j', '02-05-2019 12:26:20', '50M Femenino', '55', '50E Femenino', '52', NULL, NULL, 'si', 'si', '3', 'Gracias ;)'),
(15, '44445489J', '02-05-2019 19:57:01', '50M Masculino', '42.9', '50B Masculino', '41.66', NULL, NULL, 'si', 'si', '0', ''),
(15, '35476977y', '03-05-2019 22:00:59', '100L Masculino', '80', '50B Masculino', '42', NULL, NULL, 'si', 'si', '0', ''),
(15, '34918894H', '03-05-2019 22:44:47', '100L Masculino', '105', '50B Masculino', '55', NULL, NULL, 'si', 'si', '0', ''),
(15, '44461157h', '04-05-2019 11:56:12', '100L Masculino', '72.9', '50M Masculino', '42', NULL, NULL, 'si', 'si', '0', 'Adjunto justificante de Bel y mío.\r\nSi ves que coincido con Albacete, puedes cambiarme alguna por el 50B o lo que sea.'),
(15, '11968801s', '04-05-2019 22:17:54', '50E Femenino', '49.33', '50B Femenino', '49.29', NULL, NULL, 'si', 'si', '0', ''),
(15, '44845967s', '05-05-2019 10:49:56', '100L Femenino', '72', '50M Femenino', '40', NULL, NULL, 'si', 'pendiente', '0', ''),
(15, '34999505z', '05-05-2019 11:51:16', '100L Femenino', '87', '50B Femenino', '48', NULL, NULL, 'si', 'si', '0', 'Al final sí que puedo ir !!! '),
(16, '44845966z', '20-05-2019 23:11:47', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'si', '0', 'Me encanta esta aplicación :)'),
(16, 'y0064514j', '21-05-2019 00:56:55', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(16, '36043465G', '21-05-2019 08:35:14', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Lo siento muchísimoiooooo, tengo una boda...'),
(16, '53170509y', '21-05-2019 09:47:24', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'si', '0', ''),
(2, '44450014f', '21-05-2019 12:27:56', '200S Masculino', '186.28', '200B Masculino', '192.04', '50B Masculino', '36.68', 'si||si||si', '||si', '||0', ''),
(16, '34999787c', '21-05-2019 15:43:18', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'si', '0', ''),
(2, '44461157h', '21-05-2019 23:29:54', '200S Masculino', '188', '200B Masculino', '201', '50B Masculino', '41.1', 'si||si||si', '||si', '||0', ''),
(2, '34999787c', '21-05-2019 23:30:20', '400L Femenino', '440', '200B Femenino', '240', '50B Femenino', '50.3', 'si||si||si', '||si', '||0', ''),
(16, '36098052n', '22-05-2019 18:47:59', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'si', '0', ''),
(16, '34984082r', '23-05-2019 15:26:32', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'si', '1', 'Pendiente de confirmar el acompañante esa misma semana.\r\nSaludos'),
(2, '34984082r', '23-05-2019 15:54:32', '400L Masculino', '299', '200B Masculino', '187.08', '200E Masculino', '180.36', 'si||si||no', '||si', '||1', 'Enviare justificante de ingreso por correo electronico'),
(2, '44462120s', '23-05-2019 18:19:18', '50E Masculino', '50', '50L Masculino', '36', '50B Masculino', '45', 'si||si||si', '||si', '||0', ''),
(16, '44462120s', '23-05-2019 18:20:07', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(2, '44487569a', '23-05-2019 22:47:04', '50M Femenino', '49.08', '100L Femenino', '90', NULL, NULL, 'no||si||si', '||si', '||0', ''),
(2, '34919280j', '23-05-2019 22:56:13', '400L Masculino', '482', '50L Masculino', '39', '100L Masculino', '92', 'si||si||no', '||no', '||0', 'O pago de inscripción en todas as competicións, xa o realicei ao principio da tempada.\r\nO domingo non podo quedarme a xantar e, con toda probabilidade, tampouco poda participar na proba dos 100 L da tarde. Apúntome ca condición de que me poda borrar sen ningún problema en caso necesario. Á remuda da 3ª sesión xa non me apunto por razóns obvias.\r\nUn saúdo.'),
(2, '35575275w', '24-05-2019 08:14:53', '200S Masculino', '160', '200B Masculino', '180', '50B Masculino', '36', 'si||si||si', '||si', '||0', ''),
(16, '44656820c', '24-05-2019 09:27:16', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Si voy es un par de horas que nado en ortigueira a la tarde. '),
(2, '44656820c', '24-05-2019 09:30:59', '400L Masculino', '376', NULL, NULL, NULL, NULL, 'no||no||no', '||no', '||0', ''),
(16, '44461157h', '24-05-2019 10:00:33', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'si', '2', ''),
(2, '34981299R', '24-05-2019 11:45:06', '200S Masculino', '202.21', '50M Masculino', '41.9', '50B Masculino', '43.08', 'si||si||si', '||si', '||0', 'En galego!!!!!!!!!!!!!!!!'),
(16, '34981299R', '24-05-2019 11:45:26', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(2, '36043465G', '24-05-2019 17:46:26', '50E Femenino', '65', '200B Femenino', '266', '50B Femenino', '55', 'si||si||si', '||si', '||0', 'Quedan en mi cuenta escualos 15 euros justitos...'),
(2, '14302319e', '24-05-2019 18:51:02', '200S Femenino', '207.97', '200B Femenino', '229.85', '100L Femenino', '80.48', 'si||si||si', '||si', '||0', 'Puede que mis cachorros vengan a comer, cosa que me supone un tremendo engorro.. pero aún no lo sé con seguridad :)'),
(2, '34980175G', '24-05-2019 20:11:06', '50L Masculino', '38', '200B Masculino', '237', NULL, NULL, 'si||si||si', '||pendiente', '||0', ''),
(2, '46096607F', '24-05-2019 21:22:59', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(16, '46096607F', '24-05-2019 21:23:25', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'si', '0', ''),
(2, '11968801s', '25-05-2019 10:16:04', '400L Femenino', '421.39', '200B Femenino', '232.77', '50B Femenino', '49.29', 'si||si||si', '||si', '||0', ''),
(16, '44493665g', '25-05-2019 14:09:54', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(2, '44493665g', '25-05-2019 14:11:13', '50L Masculino', '31.17', '100L Masculino', '77', NULL, NULL, 'si||si||si', '||no', '||0', ''),
(2, 'y0064514j', '25-05-2019 18:28:57', '50E Femenino', '52', '50M Femenino', '54', '100E Femenino', '116', 'si||si||si', '||si', '||0', 'Para los relevos, lo que decidáis ;) '),
(2, '34999505z', '25-05-2019 22:09:39', '200S Femenino', '201', '200E Femenino', '188', '100L Femenino', '87', 'si||si||si', '||si', '||0', ''),
(16, '44484199z', '25-05-2019 23:42:18', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'si', '2', ''),
(2, '44446970e', '26-05-2019 10:53:39', '200E Masculino', '196,97', '100E Masculino', '86,42', NULL, NULL, 'no||si||si', '||si', '||0', 'El sabado no me apunte porque no puedo ir. Ingrese 6€ porque ya tenia 9€ de bote. Me apunte a los relevos pero dadle prioridad al resto que no estoy entrenando y con mucho curro y mi espalda se resiente.... jajajaja'),
(2, '34918894H', '26-05-2019 11:52:21', '200B Masculino', '220', '50B Masculino', '55', NULL, NULL, 'si||si||si', '||si', '||0', ''),
(16, '45146110P', '26-05-2019 17:57:26', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'no', '0', ''),
(2, '34971277f', '26-05-2019 18:17:25', '50E Masculino', '39,38', '200B Masculino', '188', '50B Masculino', '35,04', 'si||si||si', '||si', '||0', ''),
(2, '34976521f', '26-05-2019 21:23:13', '50E Femenino', '3240', '50L Femenino', '55', '50B Femenino', '57', 'si||no||si', '||pendiente', '||0', ''),
(2, '44484199z', '26-05-2019 22:28:46', '400L Femenino', '370', '200B Femenino', '210', '50B Femenino', '44,2', 'si||si||si', '||si', '||0', ''),
(2, '44484198j', '26-05-2019 23:13:31', '50E Femenino', '46', '50M Femenino', '42', '50B Femenino', '47', 'si||si||si', '||si', '||0', ''),
(2, '47076515T', '27-05-2019 08:13:07', '400L Masculino', '340', '50L Masculino', '29', '100L Masculino', '67', 'si||si||si', '||si', '||0', 'Tengo dudas en poder asistir a la jornada del domingo por motivos laborales pero hasta unos días antes seguro no lo sabré. '),
(2, '44656680h', '27-05-2019 11:31:17', '50E Femenino', '42', '50L Femenino', '34', '50B Femenino', '43', 'si||si||si', '||si', '||0', ''),
(2, '36098052n', '27-05-2019 12:17:17', '400L Masculino', '420', '200E Masculino', '230', '100E Masculino', '110', 'si||no||si', '||si', '||0', 'Gracias!!!!! :)'),
(2, '77411359Y', '27-05-2019 15:25:25', '50L Femenino', '47,43', '200B Femenino', '4,24', NULL, NULL, 'no||no||no', '||no', '||0', ''),
(2, '44845966z', '27-05-2019 18:59:47', '50E Femenino', '37,26', '50M Femenino', '37,49', '200E Femenino', '230', 'si||si||si', '||si', '||0', 'Gracias!!!!'),
(16, '34999505z', '29-05-2019 20:18:52', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'si', '0', ''),
(16, '44446970e', '29-05-2019 20:21:00', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'si', '0', ''),
(16, '76730204L', '30-05-2019 09:44:25', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'si', '0', ''),
(16, '35476977y', '30-05-2019 10:11:57', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'si', '1', 'Fer y Joa');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `dni` varchar(9) COLLATE utf8_spanish_ci NOT NULL,
  `nombre` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `sexo` varchar(1) COLLATE utf8_spanish_ci NOT NULL,
  `ano_nacimiento` int(4) NOT NULL,
  `email` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `50L` varchar(10) COLLATE utf8_spanish_ci DEFAULT NULL,
  `100L` varchar(10) COLLATE utf8_spanish_ci DEFAULT NULL,
  `200L` varchar(10) COLLATE utf8_spanish_ci DEFAULT NULL,
  `400L` varchar(10) COLLATE utf8_spanish_ci DEFAULT NULL,
  `800L` varchar(10) COLLATE utf8_spanish_ci DEFAULT NULL,
  `1500L` varchar(10) COLLATE utf8_spanish_ci DEFAULT NULL,
  `50B` varchar(10) COLLATE utf8_spanish_ci DEFAULT NULL,
  `100B` varchar(10) COLLATE utf8_spanish_ci DEFAULT NULL,
  `200B` varchar(10) COLLATE utf8_spanish_ci DEFAULT NULL,
  `50E` varchar(10) COLLATE utf8_spanish_ci DEFAULT NULL,
  `100E` varchar(10) COLLATE utf8_spanish_ci DEFAULT NULL,
  `200E` varchar(10) COLLATE utf8_spanish_ci DEFAULT NULL,
  `50M` varchar(10) COLLATE utf8_spanish_ci DEFAULT NULL,
  `100M` varchar(10) COLLATE utf8_spanish_ci DEFAULT NULL,
  `200M` varchar(10) COLLATE utf8_spanish_ci DEFAULT NULL,
  `100S` varchar(10) COLLATE utf8_spanish_ci DEFAULT NULL,
  `200S` varchar(10) COLLATE utf8_spanish_ci DEFAULT NULL,
  `400S` varchar(10) COLLATE utf8_spanish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`dni`, `nombre`, `sexo`, `ano_nacimiento`, `email`, `50L`, `100L`, `200L`, `400L`, `800L`, `1500L`, `50B`, `100B`, `200B`, `50E`, `100E`, `200E`, `50M`, `100M`, `200M`, `100S`, `200S`, `400S`) VALUES
('07991555K', 'Martín García, Alba', 'M', 1985, 'albamariamg85@gmail.com', '42.8', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('11968801S', 'Rodriguez Liebana, Carmen', 'M', 1976, 'mclieb@gmail.com', '40.4', NULL, NULL, '421.39', NULL, NULL, '49.29', NULL, '232.77', '49.33', NULL, NULL, '47.72', NULL, NULL, NULL, NULL, NULL),
('14302319E', 'De Lorenzo Fernández, María', 'M', 1978, 'delorenzo.maria@gmail.com', '36.73', '80.48', NULL, NULL, NULL, NULL, '51.56', NULL, '229.85', '46.59', NULL, NULL, '50.66', NULL, NULL, NULL, '207.97', NULL),
('34918894H', 'Perdiz Gonzalez, Jose Ramón', 'H', 1958, 'jramon@perdizseguros.com', '41.5', '100', NULL, NULL, NULL, NULL, '55', NULL, '220', NULL, NULL, NULL, '52', NULL, NULL, NULL, NULL, NULL),
('34919280J', 'Espinosa Suances, Antucho', 'H', 1958, 'antuchoespinosa@redfarma.org', '39', '92', NULL, '482', NULL, NULL, NULL, NULL, NULL, '55', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('34961763S', 'Garrote Velasco, Gil', 'H', 0, 'gil@uvigo.es', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('34971277F', 'Nogueira Pinto, Hugo', 'H', 1978, 'hugo1978@me.com', '29.31', '68', NULL, NULL, NULL, NULL, '35.04', NULL, '188', '39,38', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('34976521F', 'Hernandez Martin, María', 'M', 1974, 'shumira@gmail.com', '55', '107', NULL, NULL, NULL, NULL, '57', NULL, NULL, '52.58', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('34980175G', 'Gomez Iglesias, Juan', 'H', 1970, 'mantenjardin@yahoo.es', '38', '80', '185', NULL, NULL, NULL, NULL, NULL, '237', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('34981299R', 'Fernández Martínez, Alberto', 'H', 1971, 'albertofernandezmar@gmail.com', '34.42', '79.41', '170.91', '379.25', NULL, NULL, '43.08', '96.25', '212.33', NULL, NULL, NULL, '41.9', '', NULL, '88.04', '202.21', '430'),
('34984082R', 'Quintas Barros, Jesús Carlos', 'H', 1973, 'jecarqui@gmail.com', '30.81', '65', '141.2', '299', NULL, '1165.32', NULL, NULL, '187.08', NULL, NULL, '180.36', '35.41', '76.82', '173.05', '80.69', NULL, '338.28'),
('34999505Z', 'Sanchez Ledo, Cira', 'M', 1981, 'cirasanle@hotmail.com', '39', '87', NULL, NULL, NULL, NULL, '48', NULL, NULL, '40', NULL, '188', NULL, NULL, NULL, NULL, '201', NULL),
('34999787C', 'Cid Alvarez, Isabel', 'M', 1980, 'belcid@hotmail.com', '41', '100', NULL, '440', NULL, NULL, '50.3', NULL, '240', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('35476977Y', 'Padín Charlín, Joaquín', 'H', 1980, 'joaquin.padincharlin@hotmail.com', '33', '80', NULL, NULL, NULL, NULL, '42', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('35575275W', 'Pazos Alonso, Josue', 'H', 1986, 'pazosalonso@hotmail.com', '29.01', '65', NULL, NULL, NULL, NULL, '36', '78', '180', NULL, NULL, NULL, '33', NULL, NULL, '73', '160', NULL),
('35608875E', 'Reboreda Martinez, Zenaida', 'M', 1999, 'zenaidareboredamrtnz@gmail.com', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('36043465G', 'Reboreda Morillo, Susana', 'M', 1962, 'rmorillo@uvigo.es', '51.67', NULL, NULL, NULL, NULL, NULL, '55', NULL, '266', '65', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('36098052N', 'Troncoso Caamaño, Fernando', 'H', 1975, 'cnescualos@gmail.com', '35', '80', NULL, '420', NULL, NULL, NULL, NULL, NULL, '50', '110', '230', '40', NULL, NULL, NULL, NULL, NULL),
('44092307L', 'Lamas Perez, Alejandro', 'H', 1993, 'alexlp181293@gmail.com', '28.17', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('44445489J', 'Bouso Fuentecilla, Fernando', 'H', 1971, 'ferbou@mundo-r.com', '35.29', NULL, NULL, NULL, NULL, NULL, '41.66', NULL, NULL, NULL, NULL, NULL, '42.90', NULL, NULL, NULL, NULL, NULL),
('44446970E', 'Mares Gonzalez, Abel', 'H', 1986, 'abel.mares.gonzalez@gmail.com', '31.26', '75', '169.86', '362.6', NULL, NULL, NULL, NULL, NULL, '40.73', '86.42', '196.97', '40.73', NULL, '230.4', '84.04', '191.38', '409.93'),
('44450014F', 'Fortes Novoa, Martiño', 'H', 1988, 'martinho.fortes@gmail.com', '32', NULL, NULL, NULL, NULL, NULL, '36', '84', '192', '39', '88', '181', '35', NULL, '', '83', '186', NULL),
('44461157H', 'Álvarez Silva, Rubén', 'H', 1981, 'ruben.alvarezsilva@yahoo.es', '30,24', '72,95', '170,45', '358,39', '726,45', '1504', '41,1', '90,04', '201,56', '46,68', NULL, NULL, '39,86', NULL, NULL, '88,6', '188,31', NULL),
('44462120S', 'Montesinos Ceballos, Sergio', 'H', 1979, 'sergiom.c.tf3@gmail.com', '32', NULL, NULL, NULL, NULL, NULL, '45', NULL, NULL, '50', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('44474458W', 'Villar Prol, Ramón', 'H', 1980, 'ramonvp80@gmail.com', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('44484198J', 'Mira Vazquez, Paula', 'M', 1986, 'paulamiravazquez@hotmail.com', '39,51', NULL, NULL, NULL, NULL, NULL, '47,65', NULL, NULL, '46,26', NULL, NULL, '42,53', NULL, NULL, NULL, NULL, NULL),
('44484199Z', 'Mira Vazquez, Marta', 'M', 1981, 'pulpolito@gmail.com', '36,08', NULL, NULL, '370', NULL, NULL, '44,2', '96', '210', '50', NULL, NULL, '45', NULL, NULL, NULL, NULL, NULL),
('44486687H', 'Regodeseves Alonso, Patricia', 'M', 1985, 'patricia.regodesevesalonso@gmail.com', '43', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('44487569A', 'Vazquez Villares, Malena', 'M', 1988, 'malenavazquezvillares@gmail.com', '42.22', '90', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '49.08', NULL, NULL, NULL, NULL, NULL),
('44493665G', 'Gomez Gonzalez, Cristian', 'H', 1994, 'gomezcristian336@gmail.com', '31.17', '77', NULL, NULL, NULL, NULL, '42.14', NULL, NULL, NULL, '88.67', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('44656521C', 'Lorenzo Martín, Javier', 'H', 1989, 'javier.ote.ote@gmail.com', '34.83', NULL, NULL, NULL, NULL, NULL, '39.47', NULL, NULL, '44.55', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('44656680H', 'Rivas Carcacia, Natalia', 'M', 1991, 'natalia._101@hotmail.com', '34', '77', NULL, NULL, NULL, NULL, '43', NULL, NULL, '42', NULL, NULL, '42.6', NULL, NULL, NULL, NULL, NULL),
('44656820C', 'Rodriguez Outeiriño, Alejandro', 'H', 1990, 'alejandro.oute@gmail.com', '37', '90', NULL, '376', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('44845966Z', 'Marcos Carregal, Inés', 'M', 1989, 'ines.marcos.carregal@gmail.com', '33.56', '84.36', '168.64', '420', '784.36', NULL, '55', NULL, NULL, '37.26', '110', '230', '37.49', '85.93', NULL, '89.05', '194.52', NULL),
('44845967S', 'Marcos Carregal, Paula', 'M', 1990, 'paulamarcos90@gmail.com', '34', '72', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '40', NULL, NULL, NULL, NULL, NULL),
('45141462Y', 'Sanchez Lorenzo, Daniel', 'H', 1996, 'sanchezcnpo@gmail.com', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('45146110P', 'Gómez Fernández, Uxia ', 'M', 2003, 'uxia883@gmail.com', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('46096607F', 'Cotos Suarez, Maria', 'M', 2000, 'mariacotosuarez@gmail.com', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('47076515T', 'Sevilla Aroca, Javier', 'H', 1983, 'seviaroca14@hotmail.com', '29,4', '67', '146,35', '340', NULL, NULL, '38', '85,17', '190,85', '39,13', NULL, NULL, '36', NULL, NULL, '78', '180,68', NULL),
('53170509Y', 'GARCIA PEREZ-SCHOFIELD, Baltasar', 'H', 1974, 'baltasarq@gmail.com', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('76730204L', 'García Carballo, Loli', 'M', 1983, 'loly.carballo.garcia@gmail.com', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('76733751R', 'Garcia Prados, Guillermo', 'H', 1987, 'ggarciaprados@gmail.com', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('77355898K', 'Serrano Cobo, María del mar', 'M', 1985, 'msercob@gmail.com', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('77411359Y', 'Gonzalez Fernandez, Coral', 'M', 1987, 'coral_gonf@hotmail.com', '47.43', '115', NULL, NULL, NULL, NULL, '53', NULL, '4,24', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('Y0064514J', 'Martin, Christelle', 'M', 1981, 'cristel.martin@hotmail.es', '46', '114', '241,31', NULL, NULL, NULL, '54', NULL, NULL, '52', '116', NULL, '54', NULL, NULL, '110,65', NULL, NULL);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `administradores`
--
ALTER TABLE `administradores`
  ADD PRIMARY KEY (`dni`);

--
-- Indices de la tabla `competiciones`
--
ALTER TABLE `competiciones`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`dni`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `competiciones`
--
ALTER TABLE `competiciones`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
