-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: banking
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accountdetails`
--

DROP TABLE IF EXISTS `accountdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accountdetails` (
  `accno` varchar(15) NOT NULL,
  `name` char(60) NOT NULL,
  `typeofacc` char(10) NOT NULL,
  `amount` int NOT NULL,
  `address` varchar(100) NOT NULL,
  `state` char(50) NOT NULL,
  `country` char(60) NOT NULL,
  `DOB` varchar(15) NOT NULL,
  `accopdate` varchar(15) NOT NULL,
  `aadharno` varchar(15) NOT NULL,
  `pan` int DEFAULT NULL,
  `lockerno` varchar(20) DEFAULT NULL,
  `passbookno` varchar(50) NOT NULL,
  `debitcardno` varchar(50) DEFAULT NULL,
  `creditcardno` varchar(50) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`accno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accountdetails`
--

LOCK TABLES `accountdetails` WRITE;
/*!40000 ALTER TABLE `accountdetails` DISABLE KEYS */;
INSERT INTO `accountdetails` VALUES ('45645645600','Amit Sir','Savings',10000,'14/9 Malviya nagar new delhi','Delhi','India','24/09/1975','25/10/2020','741185229633',0,'0','45645645600','78978978900','--','--'),('75375375300','Vasudev Kumar','Savings',50000000,'19/5 L block Chatarpur','Delhi','India','13/01/2003','25/10/2020','753684258951',0,'0','74174174100','78978978900','96396396300','--'),('78978978900','Chaitanya Kathuria','Savings',20000000,'14/9 H6 block malviya nagar New delhi Delhi 110017','Delhi','India','13/08/1989','21/10/2020','963963963023',0,'0','74185296300','--','--','--');
/*!40000 ALTER TABLE `accountdetails` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-25 10:02:19
