-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: b6_full_stack
-- ------------------------------------------------------
-- Server version	8.0.30

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
-- Table structure for table `booking`
--

DROP TABLE IF EXISTS `booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `booking` (
  `bookingID` int NOT NULL AUTO_INCREMENT,
  `userEmail` varchar(255) DEFAULT NULL,
  `providerEmail` varchar(255) DEFAULT NULL,
  `paymentID` varchar(255) DEFAULT NULL,
  `bookingDate` date DEFAULT NULL,
  `amount` int DEFAULT NULL,
  PRIMARY KEY (`bookingID`),
  KEY `userdelete_idx` (`userEmail`),
  CONSTRAINT `userdelete` FOREIGN KEY (`userEmail`) REFERENCES `user` (`email`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=104 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booking`
--

LOCK TABLES `booking` WRITE;
/*!40000 ALTER TABLE `booking` DISABLE KEYS */;
INSERT INTO `booking` VALUES (101,'hello@gmail.com','lee@gmail.com','pay_Or5D22a04Y4PJD','2024-08-30',1),(102,'hello@gmail.com','lee@gmail.com','pay_OsCSviqttfvOUz','2024-09-04',1),(103,'minku@gmail.com','lee@gmail.com','pay_OsCjmG8KwMfGWp','2024-09-06',1);
/*!40000 ALTER TABLE `booking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `provider`
--

DROP TABLE IF EXISTS `provider`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `provider` (
  `firstName` varchar(255) DEFAULT NULL,
  `lastName` varchar(255) DEFAULT NULL,
  `mobile` varchar(255) DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `state` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `address` tinytext,
  `skill` varchar(255) DEFAULT NULL,
  `charges` int DEFAULT NULL,
  `exp` varchar(255) DEFAULT NULL,
  `photo` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `provider`
--

LOCK TABLES `provider` WRITE;
/*!40000 ALTER TABLE `provider` DISABLE KEYS */;
INSERT INTO `provider` VALUES ('alex','bodra','3434343434','alex@gmail.com','Jharkhand',' Ranchi ','hatia ','electrician',400,'3','1723831983.jpg','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'),('kunal','mahato','98989898','kunal@gmail.com','Jharkhand',' Ranchi ','bangdinhg','cleaner',400,'3','1723863883.jpg','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'),('lee','pee','4434343434','lee@gmail.com','Jharkhand',' Ranchi ','ranchi lalpur','electrician',1,'3','1724413549.png','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'),('monu','kumar','3434343434','monu@gmail.com','Jharkhand',' Ranchi ','hatia railway ','cleaner',900,'3','1723863590.jpg','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'),('priya','kumari','3434343434','priya@gmail.com','Jharkhand',' Ranchi ','ranchi','cleaner',400,'3','1723832412.png','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'),('sristi','sharma','2424242526','sristi@gmail.com','Jharkhand',' Ranchi ','hatia ,oberia road','gardener',500,'3','1723559525.jpg','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'),('tanya','kumari','89898989898','tanya@gmail.com','Chandigarh',' Chandigarh ','hatia , morabadi ','cleaner',700,'2','1723476415.png','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'),('tinku','kumar','2424242526','tinku@gmail.com','Goa',' Jua ','hatia , goa','cleaner',400,'2','1723559434.png','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'),('tinku','jink','2424242526','tinky@gmail.com','Jharkhand',' Ranchi ','inku','cleaner',600,'1','1723863971.jpg','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3');
/*!40000 ALTER TABLE `provider` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `review`
--

DROP TABLE IF EXISTS `review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `review` (
  `review_id` int NOT NULL AUTO_INCREMENT,
  `userEmail` varchar(255) DEFAULT NULL,
  `providerEmail` varchar(255) DEFAULT NULL,
  `comment` mediumtext,
  `star` int DEFAULT NULL,
  PRIMARY KEY (`review_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `review`
--

LOCK TABLES `review` WRITE;
/*!40000 ALTER TABLE `review` DISABLE KEYS */;
INSERT INTO `review` VALUES (1,'minku@gmail.com','None','it was a  good service',4),(2,'minku@gmail.com','None','it was a  good service',4),(3,'minku@gmail.com','None','good ',4),(4,'minku@gmail.com','None','good ve',4),(5,'minku@gmail.com','None','very good',4),(6,'minku@gmail.com','kunal@gmail.com','very good',4),(7,'minku@gmail.com','kunal@gmail.com','very',5),(8,'minku@gmail.com','kunal@gmail.com','it was good',2),(9,'minku@gmail.com','lee@gmail.com','good',4);
/*!40000 ALTER TABLE `review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `firstName` varchar(255) DEFAULT NULL,
  `lastName` varchar(255) DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `mobile` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `state` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('alex','bodra','alexbodra125@gmail.com','3434343434',' Betapur ','Andaman & Nicobar','123'),('l','a','da@gmail.com','67474834849',' Cachar ','Assam','03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4'),('finku','kumar','finku@gmail.com','3434343434',' Bastar ','Chhattisgarh','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'),('harish','singh','harish@gmail.com','8809400853','ranchi','jharkhand','1234'),('inknsfedfdfd','dfdaf','hello@gmail.com','3434343434',' Achampet ','Andhra Pradesh','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'),('iinku','kumar','iinku@gmail.com','3434343434',' Dhakuakhana ','Assam','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'),('ik','n','ik@gmail.com','123453567',' Bareja ','Gujarat','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'),('tinku','kumar','kin@gmail.com','8384848484',' Dhemaji ','Assam','03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4'),('minku','kumar','minku@gmail.com','4434343434',' Ranchi ','Jharkhand','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'),('ninku','kumar','ninku@gmail.com','4434343434',' Kalaktung ','Arunachal Pradesh','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'),('pinki','tinki','pinki@gmail.com','3434343434',' Ranchi ','Jharkhand','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'),('pk','po','pk@gmail.com','2424242526',' Kargil ','Jammu & Kashmir','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'),('priti','kumari','priti@gmail.com','2343434343',' Kameng ','Arunachal Pradesh','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'),('roshan','singh','ro@gmail.com','3434343434',' Baroda ','Gujarat','03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4'),('roshan','kumar','ros@gmail.com','7874847484',' Mani Marja','Chandigarh','123'),('soni','monu','soni@gmail.com','3434343434',' Ranchi ','Jharkhand','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'),('tinku','kumar','tinku@gmail.com','3434343434',' Kameng ','Arunachal Pradesh','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'),('winku','kumar','winku@gmail.com','4434343434',' Benipatti ','Bihar','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-13 16:40:41
