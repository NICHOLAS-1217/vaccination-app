-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: psp_assignment_db
-- ------------------------------------------------------
-- Server version	8.0.27

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
-- Table structure for table `admin_login`
--

DROP TABLE IF EXISTS `admin_login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin_login` (
  `admin_ID` int NOT NULL AUTO_INCREMENT,
  `admin_name` varchar(50) NOT NULL,
  `admin_email` varchar(30) NOT NULL,
  `admin_pass` varchar(30) NOT NULL,
  PRIMARY KEY (`admin_ID`),
  UNIQUE KEY `admin_email` (`admin_email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_login`
--

LOCK TABLES `admin_login` WRITE;
/*!40000 ALTER TABLE `admin_login` DISABLE KEYS */;
INSERT INTO `admin_login` VALUES (1,'ABU','abu123@gmail.com','abu123');
/*!40000 ALTER TABLE `admin_login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registration`
--

DROP TABLE IF EXISTS `registration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registration` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `IC` varchar(30) NOT NULL,
  `name` varchar(50) NOT NULL,
  `age` varchar(30) NOT NULL,
  `phone` varchar(30) NOT NULL,
  `postcode` int NOT NULL,
  `address` longtext NOT NULL,
  `email` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `risk` varchar(30) DEFAULT NULL,
  `occupation` varchar(30) DEFAULT NULL,
  `under_quarantine` varchar(30) DEFAULT NULL,
  `priority_ranking` int DEFAULT NULL,
  `location` int DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `time` varchar(50) DEFAULT NULL,
  `RVSP` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `IC` (`IC`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registration`
--

LOCK TABLES `registration` WRITE;
/*!40000 ALTER TABLE `registration` DISABLE KEYS */;
INSERT INTO `registration` VALUES (1,'031217010851','ALI','18','0177183063',81000,'Jalan Tualang','ali123@gmail.com','ali123','low_risk','student','NO',1,102,'2022-10-10','1pm','YES'),(2,'063214565255','HUAN','25','0125568895',50000,'Jalan Kopi','huan123@gmail.com','huan123','low_risk','health-care worker','NO',5,103,'2022-10-06','2pm','YES'),(3,'046234859965','JOYCE','30','0167713398',82000,'Jalan Rambutan','joyce123@gmail.com','joyce123','high_risk','others','NO',2,103,'2022-10-06','2pm','NO'),(4,'986663256485','SPIDERMAN','17','0189913356',30000,'Jalan Marvel','spiderman123@gmail.com','spiderman123','low_risk','transportation','NO',4,102,'2022-05-06','10am','YES'),(5,'544313862201','BATMAN','30','0198886762',63000,'Jalan Gotham','batman123@gmail.com','batman123','low_risk','others','NO',3,103,'2022-12-17','3pm','NO'),(6,'630014895668','JENNIE','26','0168895356',65000,'Jalan Black Pink','jennie123@gmail.com','jennie123',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(7,'530067289665','LISA','24','0198867235',67000,'Jalan Black Pink','lisa123@gmail.com','lisa123',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(8,'599886475662','ROSE','24','0173889654',61000,'Jalan Black Pink','rose123@gmail.com','rose123',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(9,'530889657716','JISOO','27','0189954639',54000,'Jalan Black Pink','jisoo123@gmail.com','jisoo123',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(10,'567889562111','KAIRU','17','0198876366',51000,'Jalan Kuching','kairu123@gmail.com','kairu123',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(11,'630021489956','ALEX','61','0178865533',51700,'Jalan Adam','alex123@gmail.com','alex123',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(12,'659876333541','ADAM','65','0127233896',51700,'Jalan Alex','adam123@gmail.com','adam123',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(13,'889645388176','ADRIANA','50','0145998633',12000,'Jalan Anjing','adriana123@gmail.com','adriana123',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(14,'967543668521','DEEVARAJ','45','0126698733',56000,'Jalan Rambutan','deevaraj123@gmail.com','deevaraj123',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(15,'059998674211','EREN','19','0145596325',54771,'Jalan AOT','eren123@gmail.com','eren123',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(16,'045998166988','MIKASA','19','0196635552',54771,'Jalan AOT','mikasa123@gmail.com','mikasa123',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(17,'076665899954','GOKU','20','0186665487',70000,'Jalan Dragon Ball','goku123@gmail.com','goku123',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(18,'049338675510','SUPERMAN','21','0156632558',74000,'Jalan Super','superman123@gmail.com','superman123',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(19,'561112364799','JARON','69','0167715688',54000,'Jalan Bengkok','jaron123@gmail.com','jaron123',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(20,'543218698874','AHMED','100','0178996541',62000,'Jalan Old','ahmed123@gmail.com','ahmed123',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(21,'062315489658','THANOS','100','0128566956',81000,'Jalan Marvel','thanos123@gmail.com','thanos123','low_risk','health-care worker','NO',5,104,'2022-10-25','3pm','YES');
/*!40000 ALTER TABLE `registration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vac_centre`
--

DROP TABLE IF EXISTS `vac_centre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vac_centre` (
  `location_id` int NOT NULL AUTO_INCREMENT,
  `location_name` varchar(50) NOT NULL,
  `location_address` varchar(50) NOT NULL,
  `location_postcode` int NOT NULL,
  `capacity_per_hour` int NOT NULL,
  PRIMARY KEY (`location_id`),
  UNIQUE KEY `location_address` (`location_address`)
) ENGINE=InnoDB AUTO_INCREMENT=105 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vac_centre`
--

LOCK TABLES `vac_centre` WRITE;
/*!40000 ALTER TABLE `vac_centre` DISABLE KEYS */;
INSERT INTO `vac_centre` VALUES (101,'MESOPOTAMIA','Bandar Mesopotamia',50000,150),(102,'INDUS','Bandar Indus',83000,200),(103,'HUANG HE','Bandar Hwang He',63000,300),(104,'MESIR PURBA','Bandar Mesir Purba',84000,400);
/*!40000 ALTER TABLE `vac_centre` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-17 21:35:44
