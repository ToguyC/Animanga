-- MySQL dump 10.13  Distrib 8.0.16, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: tpi
-- ------------------------------------------------------
-- Server version	8.0.16

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

USE `tpi`;

--
-- Table structure for table `anime`
--

DROP TABLE IF EXISTS `anime`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8 ;
CREATE TABLE `anime` (
  `idAnime` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `type` int(11) NOT NULL,
  `episodes` int(3) NOT NULL,
  `status` int(11) NOT NULL,
  `picture` varchar(200) NOT NULL,
  `thumbnail` varchar(200) NOT NULL,
  `synonyms` text DEFAULT NULL,
  `modificationDate` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`idAnime`),
  KEY `type` (`type`),
  KEY `status` (`status`),
  FULLTEXT KEY `title` (`title`),
  CONSTRAINT `anime_ibfk_1` FOREIGN KEY (`type`) REFERENCES `type` (`idType`),
  CONSTRAINT `anime_ibfk_2` FOREIGN KEY (`status`) REFERENCES `status` (`idStatus`)
) ENGINE=InnoDB AUTO_INCREMENT=23613 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `list`
--

DROP TABLE IF EXISTS `list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8 ;
CREATE TABLE `list` (
  `idList` int(11) NOT NULL AUTO_INCREMENT,
  `nameList` varchar(45) NOT NULL,
  `modificationDate` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`idList`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `list_has_anime`
--

DROP TABLE IF EXISTS `list_has_anime`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8 ;
CREATE TABLE `list_has_anime` (
  `idListHasAnime` INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `idList` int(11) NOT NULL,
  `idAnime` int(11) NOT NULL,
  `modificationDate` timestamp NULL DEFAULT NULL,
  KEY `fk_list_has_anime_anime1_idx` (`idAnime`),
  KEY `fk_list_has_anime_list1_idx` (`idList`),
  CONSTRAINT `fk_list_has_anime_anime1` FOREIGN KEY (`idAnime`) REFERENCES `anime` (`idAnime`),
  CONSTRAINT `fk_list_has_anime_list1` FOREIGN KEY (`idList`) REFERENCES `list` (`idList`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `status`
--

DROP TABLE IF EXISTS `status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8 ;
CREATE TABLE `status` (
  `idStatus` int(11) NOT NULL AUTO_INCREMENT,
  `nameStatus` varchar(20) NOT NULL,
  `modificationDate` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`idStatus`),
  UNIQUE KEY `nameStatus` (`nameStatus`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `type`
--

DROP TABLE IF EXISTS `type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8 ;
CREATE TABLE `type` (
  `idType` int(11) NOT NULL AUTO_INCREMENT,
  `nameType` varchar(10) NOT NULL,
  `modificationDate` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`idType`),
  UNIQUE KEY `nameType` (`nameType`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `url`
--

DROP TABLE IF EXISTS `url`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8 ;
CREATE TABLE `url` (
  `idUrl` int(11) NOT NULL AUTO_INCREMENT,
  `urlName` varchar(45) NOT NULL,
  `idAnime` int(11) NOT NULL,
  `isRelation` tinyint(1) NOT NULL,
  `modificationDate` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`idUrl`),
  KEY `idAnime` (`idAnime`),
  CONSTRAINT `url_ibfk_1` FOREIGN KEY (`idAnime`) REFERENCES `anime` (`idAnime`)
) ENGINE=InnoDB AUTO_INCREMENT=138875 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8 ;
CREATE TABLE `user` (
  `idUser` int(11) NOT NULL AUTO_INCREMENT,
  `emailUser` varchar(45) NOT NULL,
  `password` varchar(64) NOT NULL,
  `nicknameUser` varchar(45) NOT NULL,
  `modificationDate` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`idUser`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `user_has_favorite`
--

DROP TABLE IF EXISTS `user_has_favorite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8 ;
CREATE TABLE `user_has_favorite` (
  `idUserHasFavorite` INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `idUser` int(11) NOT NULL,
  `idAnime` int(11) NOT NULL,
  `orderId` int(11) NOT NULL,
  `modificationDate` timestamp NULL DEFAULT NULL,
  KEY `fk_user_has_anime_anime1_idx` (`idAnime`),
  KEY `fk_user_has_anime_user1_idx` (`idUser`),
  CONSTRAINT `fk_user_has_anime_anime1` FOREIGN KEY (`idAnime`) REFERENCES `anime` (`idAnime`),
  CONSTRAINT `fk_user_has_anime_user1` FOREIGN KEY (`idUser`) REFERENCES `user` (`idUser`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `user_has_list`
--

DROP TABLE IF EXISTS `user_has_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8 ;
CREATE TABLE `user_has_list` (
  `idUserHasList` INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `idUser` int(11) NOT NULL,
  `idList` int(11) NOT NULL,
  `modificationDate` timestamp NULL DEFAULT NULL,
  KEY `fk_user_has_list_list1_idx` (`idList`),
  KEY `fk_user_has_list_user1_idx` (`idUser`),
  CONSTRAINT `fk_user_has_list_list1` FOREIGN KEY (`idList`) REFERENCES `list` (`idList`),
  CONSTRAINT `fk_user_has_list_user1` FOREIGN KEY (`idUser`) REFERENCES `user` (`idUser`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-27 13:42:24