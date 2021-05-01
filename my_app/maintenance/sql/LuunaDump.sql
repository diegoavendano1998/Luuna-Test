-- MySQL dump 10.13  Distrib 5.7.33, for Linux (x86_64)
--
-- Host: localhost    Database: lunnatest
-- ------------------------------------------------------
-- Server version	5.7.33-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `alerts`
--

LOCK TABLES `alerts` WRITE;
/*!40000 ALTER TABLE `alerts` DISABLE KEYS */;
INSERT INTO `alerts` VALUES (1,'hello',1),(2,'<flask_login.mixins.AnonymousUserMixin object at 0x7fea9415aa58> delete the product dfsafds',1),(3,'fsad ha sido eliminado',1),(4,'nuevo ha sido añadido.',1),(5,'P5 cambio el sku a 0005',0),(6,'P5 cambio el sku a 005',0),(7,'P5 cambio el precio a $22.00',0),(8,'P5 cambio la categoría a 3',0),(9,'P4 cambio el sku a 0004',0),(10,'P4 cambio el precio a $12.00',0),(11,'P4 cambio la categoría a 3',0),(12,'test cambio el precio a $44.00',0),(13,'test cambio la categoría a 8',0);
/*!40000 ALTER TABLE `alerts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES (1,'Categoria 1',0,'This is category 1'),(2,'Categoria 2',0,'Yes, category 2'),(3,'Categoria 3',0,'Another category'),(4,'Categoria 4',0,'The last one ... Yet!'),(5,'Categoria 5',0,'Yep, another one'),(7,'Categoría 6',0,'This is the sixth category'),(8,'Categoria 7',0,'7 is a lucky number');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'001','P1','Producto 1','Nike',15,1,NULL,'2021-04-30 07:19:15',0),(3,'003','P3','Producto 3','Adidas',21,4,NULL,'2021-04-30 07:19:15',0),(4,'0004','P4','Producto 4','New Reebok',12,3,'','2021-04-30 07:19:15',0),(5,'005','P5','Producto 5','Nike',22,3,'','2021-04-30 07:19:15',0),(7,'006','P6','Producto 6','Nike',11,2,NULL,'2021-04-30 07:19:15',0),(11,'0000','test','test desc','test brand',44,8,'','2021-04-30 17:51:12',0),(12,'0000','test','test desc','test brand',44,2,'','2021-04-30 17:54:13',0),(13,'0000','test','test desc','test brand',44,2,'','2021-04-30 17:54:35',0),(17,'09999','some name','some desc','some brand',55,5,'','2021-04-30 18:09:08',0),(19,'0887','New','Super New','Newest',21,4,'','2021-05-01 04:31:39',0),(20,'82','nuevo','relusciente','limpioooooooooo',13,5,'','2021-05-01 04:34:01',0);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (6,'admin'),(1,'regular');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `tracks`
--

LOCK TABLES `tracks` WRITE;
/*!40000 ALTER TABLE `tracks` DISABLE KEYS */;
INSERT INTO `tracks` VALUES (1,11,'administrator',7,'P6','2021-05-01 08:43:33'),(2,11,'administrator',5,'P5','2021-05-01 08:43:33'),(3,11,'administrator',17,'some name','2021-05-01 08:43:33'),(4,11,'administrator',3,'P3','2021-05-01 09:34:03');
/*!40000 ALTER TABLE `tracks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `user_roles`
--

LOCK TABLES `user_roles` WRITE;
/*!40000 ALTER TABLE `user_roles` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'usuario','12','regular',1,'3@3.com',NULL),(3,'diego','diego','regular',1,'diegoavendano1998@gmail.com',NULL),(4,'diego2','Diegox10','admin',1,'user1@user.com',NULL),(5,'someName','123','regular',1,'fasd@fasd.com',NULL),(9,'toño','toño','regular',1,'tono@tono.com',NULL),(10,'guest','12','regular',1,'12@12.com',NULL),(11,'administrator','12','admin',1,'a@a.com',NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-01  7:26:52
