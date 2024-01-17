-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 17, 2024 at 01:55 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gsc_ticket`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer_seat_cinema`
--

CREATE TABLE `customer_seat_cinema` (
  `reserve_seat` varchar(20) NOT NULL,
  `quantity_of_adult` varchar(20) NOT NULL,
  `quantity_of_children` varchar(20) NOT NULL,
  `total_price` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer_seat_cinema`
--

INSERT INTO `customer_seat_cinema` (`reserve_seat`, `quantity_of_adult`, `quantity_of_children`, `total_price`) VALUES
('B1', '4', '2', 'Total Price: RM 200'),
('A6', '4', '2', 'Total Price: RM 200'),
('A5', '3', '1', 'Total Price: RM 120');

-- --------------------------------------------------------

--
-- Table structure for table `showtime_selection`
--

CREATE TABLE `showtime_selection` (
  `Date_label` varchar(30) NOT NULL,
  `Movie_label` varchar(30) NOT NULL,
  `Time_label` varchar(30) NOT NULL,
  `Experience_label` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `showtime_selection`
--

INSERT INTO `showtime_selection` (`Date_label`, `Movie_label`, `Time_label`, `Experience_label`) VALUES
('2024-01-17', 'Endless Journey', '10:00 a.m - 12:15 p.m', 'SkyBox'),
('2024-01-17', 'Endless Journey', '10:00 a.m - 12:15 p.m', 'Onyx'),
('2024-01-17', 'Endless Journey', '9:00 p.m -12:00 p.m', 'PREMIERE'),
('2024-01-19', 'Endless Journey', '9:00 p.m -12:00 p.m', 'PREMIERE'),
('2024-01-22', 'Aquaman', '10:00 a.m - 12:15 p.m', 'SkyBox'),
('2024-01-22', 'Endless Journey', '4:00 p.m - 6:00 p.m', 'Standard Class');

-- --------------------------------------------------------

--
-- Table structure for table `user_registration`
--

CREATE TABLE `user_registration` (
  `Name` varchar(30) NOT NULL,
  `Age` varchar(2) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `Phone_Number` varchar(10) NOT NULL,
  `Email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_registration`
--

INSERT INTO `user_registration` (`Name`, `Age`, `Gender`, `Phone_Number`, `Email`) VALUES
('karina', '25', 'Female', '0143657890', ''),
('malek', '21', 'Male', '0187654699', 'malek@gmail.com');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
