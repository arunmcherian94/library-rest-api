-- MySQL dump 10.13  Distrib 5.6.37, for Linux (x86_64)
--
-- Host: localhost    Database: librarydb
-- ------------------------------------------------------
-- Server version	5.6.37

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
-- Table structure for table `auth_group`
--
USE librarydb;

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add permission',3,'add_permission'),(8,'Can change permission',3,'change_permission'),(9,'Can delete permission',3,'delete_permission'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add author',7,'add_author'),(20,'Can change author',7,'change_author'),(21,'Can delete author',7,'delete_author'),(22,'Can add member',8,'add_member'),(23,'Can change member',8,'change_member'),(24,'Can delete member',8,'delete_member'),(25,'Can add book',9,'add_book'),(26,'Can change book',9,'change_book'),(27,'Can delete book',9,'delete_book'),(28,'Can add book action',10,'add_bookaction'),(29,'Can change book action',10,'change_bookaction'),(30,'Can delete book action',10,'delete_bookaction'),(31,'Can add book_master',11,'add_book_master'),(32,'Can change book_master',11,'change_book_master'),(33,'Can delete book_master',11,'delete_book_master');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `crud_author`
--

DROP TABLE IF EXISTS `crud_author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `crud_author` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(40) DEFAULT NULL,
  `last_name` varchar(40) DEFAULT NULL,
  `email` varchar(254) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `crud_author`
--

LOCK TABLES `crud_author` WRITE;
/*!40000 ALTER TABLE `crud_author` DISABLE KEYS */;
INSERT INTO `crud_author` VALUES (1,'Thomas','Cormen','thomas.cormen@gmail.com');
/*!40000 ALTER TABLE `crud_author` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `crud_book`
--

DROP TABLE IF EXISTS `crud_book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `crud_book` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `last_borrowed_date` datetime(6) NOT NULL,
  `book_id` char(32) NOT NULL,
  `available` tinyint(1) NOT NULL,
  `book_master_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `crud_book_book_master_id_85024731_fk_crud_book_master_id` (`book_master_id`),
  CONSTRAINT `crud_book_book_master_id_85024731_fk_crud_book_master_id` FOREIGN KEY (`book_master_id`) REFERENCES `crud_book_master` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `crud_book`
--

LOCK TABLES `crud_book` WRITE;
/*!40000 ALTER TABLE `crud_book` DISABLE KEYS */;
INSERT INTO `crud_book` VALUES (1,'2018-02-07 20:04:18.370782','cdf1907869494facb7b358f01f8eb552',1,1),(2,'2018-02-07 20:05:45.836502','84ac9a10c4ae4d76b9453ed2624b2a66',0,2);
/*!40000 ALTER TABLE `crud_book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `crud_book_master`
--

DROP TABLE IF EXISTS `crud_book_master`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `crud_book_master` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `isbn` varchar(13) NOT NULL,
  `title` varchar(100) DEFAULT NULL,
  `no_of_copies` int(11) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `added_on` datetime(6) NOT NULL,
  `modified_on` datetime(6) NOT NULL,
  `misc_details` varchar(1024) DEFAULT NULL,
  `author_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `isbn` (`isbn`),
  KEY `crud_book_master_author_id_b671a732_fk_crud_author_id` (`author_id`),
  CONSTRAINT `crud_book_master_author_id_b671a732_fk_crud_author_id` FOREIGN KEY (`author_id`) REFERENCES `crud_author` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `crud_book_master`
--

LOCK TABLES `crud_book_master` WRITE;
/*!40000 ALTER TABLE `crud_book_master` DISABLE KEYS */;
INSERT INTO `crud_book_master` VALUES (1,'12345','Introduction to Algorithms 2',1,0,'2018-02-07 20:04:18.242954','2018-02-08 07:03:10.962753',NULL,1),(2,'12344','Introduction to Algorithms',1,0,'2018-02-07 20:05:45.649010','2018-02-07 20:05:45.649080',NULL,1);
/*!40000 ALTER TABLE `crud_book_master` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `crud_bookaction`
--

DROP TABLE IF EXISTS `crud_bookaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `crud_bookaction` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `borrowed_date` datetime(6) DEFAULT NULL,
  `due_date` datetime(6) NOT NULL,
  `is_returned` tinyint(1) NOT NULL,
  `fine_collected` decimal(6,2) NOT NULL,
  `copy_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `crud_bookaction_copy_id_d5ac81e1_fk_crud_book_id` (`copy_id`),
  CONSTRAINT `crud_bookaction_copy_id_d5ac81e1_fk_crud_book_id` FOREIGN KEY (`copy_id`) REFERENCES `crud_book` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `crud_bookaction`
--

LOCK TABLES `crud_bookaction` WRITE;
/*!40000 ALTER TABLE `crud_bookaction` DISABLE KEYS */;
INSERT INTO `crud_bookaction` VALUES (1,'2018-02-07 20:30:11.134993','2018-02-14 20:30:11.135000',1,0.00,2),(2,'2018-02-07 21:01:33.316856','2018-02-14 21:01:33.316865',1,0.00,2),(3,'2018-02-07 21:03:35.064042','2018-02-14 21:03:35.064049',0,0.00,2);
/*!40000 ALTER TABLE `crud_bookaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `crud_bookaction_member`
--

DROP TABLE IF EXISTS `crud_bookaction_member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `crud_bookaction_member` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bookaction_id` int(11) NOT NULL,
  `member_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `crud_bookaction_member_bookaction_id_member_id_fc9dac27_uniq` (`bookaction_id`,`member_id`),
  KEY `crud_bookaction_member_member_id_f0145bd4_fk_crud_member_id` (`member_id`),
  CONSTRAINT `crud_bookaction_memb_bookaction_id_714bd2b4_fk_crud_book` FOREIGN KEY (`bookaction_id`) REFERENCES `crud_bookaction` (`id`),
  CONSTRAINT `crud_bookaction_member_member_id_f0145bd4_fk_crud_member_id` FOREIGN KEY (`member_id`) REFERENCES `crud_member` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `crud_bookaction_member`
--

LOCK TABLES `crud_bookaction_member` WRITE;
/*!40000 ALTER TABLE `crud_bookaction_member` DISABLE KEYS */;
INSERT INTO `crud_bookaction_member` VALUES (1,1,1),(2,2,1),(3,3,1);
/*!40000 ALTER TABLE `crud_bookaction_member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `crud_member`
--

DROP TABLE IF EXISTS `crud_member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `crud_member` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(40) DEFAULT NULL,
  `last_name` varchar(40) DEFAULT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(32) DEFAULT NULL,
  `phone` varchar(32) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `joined_on` datetime(6) NOT NULL,
  `modified_on` datetime(6) NOT NULL,
  `member_type` varchar(1) NOT NULL,
  `expires_on` date NOT NULL,
  `misc_details` varchar(1024) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `crud_member`
--

LOCK TABLES `crud_member` WRITE;
/*!40000 ALTER TABLE `crud_member` DISABLE KEYS */;
INSERT INTO `crud_member` VALUES (1,'Arun','Cherian','arun.cherian@gmail.com',NULL,'+919538487913',1,0,'2018-02-07 19:59:33.506807','2018-02-07 20:28:30.430064','A','2018-12-01',NULL),(2,'Tony','Cherian','tony@gmail.com',NULL,'+919538487915',1,0,'2018-02-08 07:53:31.972589','2018-02-08 07:53:31.972918','A','2018-11-01',NULL);
/*!40000 ALTER TABLE `crud_member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(2,'auth','group'),(3,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'crud','author'),(9,'crud','book'),(10,'crud','bookaction'),(11,'crud','book_master'),(8,'crud','member'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-02-07 19:01:42.274529'),(2,'auth','0001_initial','2018-02-07 19:01:53.973990'),(3,'admin','0001_initial','2018-02-07 19:01:56.522387'),(4,'admin','0002_logentry_remove_auto_add','2018-02-07 19:01:56.700583'),(5,'contenttypes','0002_remove_content_type_name','2018-02-07 19:01:58.162092'),(6,'auth','0002_alter_permission_name_max_length','2018-02-07 19:01:59.129547'),(7,'auth','0003_alter_user_email_max_length','2018-02-07 19:02:00.122527'),(8,'auth','0004_alter_user_username_opts','2018-02-07 19:02:00.191999'),(9,'auth','0005_alter_user_last_login_null','2018-02-07 19:02:00.925635'),(10,'auth','0006_require_contenttypes_0002','2018-02-07 19:02:00.980471'),(11,'auth','0007_alter_validators_add_error_messages','2018-02-07 19:02:01.050316'),(12,'auth','0008_alter_user_username_max_length','2018-02-07 19:02:03.196228'),(13,'crud','0001_initial','2018-02-07 19:02:12.306182'),(14,'sessions','0001_initial','2018-02-07 19:02:13.119498');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-02-08 15:42:16
