USE [master]
GO
/****** Object:  Database [16Tehtava]    Script Date: 18.11.2021 11.13.40 ******/
CREATE DATABASE [16Tehtava]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'16Tehtava', FILENAME = N'C:\Users\aarok\16Tehtava.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'16Tehtava_log', FILENAME = N'C:\Users\aarok\16Tehtava_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
GO
ALTER DATABASE [16Tehtava] SET COMPATIBILITY_LEVEL = 130
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [16Tehtava].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [16Tehtava] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [16Tehtava] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [16Tehtava] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [16Tehtava] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [16Tehtava] SET ARITHABORT OFF 
GO
ALTER DATABASE [16Tehtava] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [16Tehtava] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [16Tehtava] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [16Tehtava] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [16Tehtava] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [16Tehtava] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [16Tehtava] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [16Tehtava] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [16Tehtava] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [16Tehtava] SET  DISABLE_BROKER 
GO
ALTER DATABASE [16Tehtava] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [16Tehtava] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [16Tehtava] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [16Tehtava] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [16Tehtava] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [16Tehtava] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [16Tehtava] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [16Tehtava] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [16Tehtava] SET  MULTI_USER 
GO
ALTER DATABASE [16Tehtava] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [16Tehtava] SET DB_CHAINING OFF 
GO
ALTER DATABASE [16Tehtava] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [16Tehtava] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [16Tehtava] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [16Tehtava] SET QUERY_STORE = OFF
GO
USE [16Tehtava]
GO
ALTER DATABASE SCOPED CONFIGURATION SET LEGACY_CARDINALITY_ESTIMATION = OFF;
GO
ALTER DATABASE SCOPED CONFIGURATION SET MAXDOP = 0;
GO
ALTER DATABASE SCOPED CONFIGURATION SET PARAMETER_SNIFFING = ON;
GO
ALTER DATABASE SCOPED CONFIGURATION SET QUERY_OPTIMIZER_HOTFIXES = OFF;
GO
USE [16Tehtava]
GO
/****** Object:  Table [dbo].[kaytossa]    Script Date: 18.11.2021 11.13.40 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[kaytossa](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[soitin_num] [int] NOT NULL,
	[opiskelija_num] [int] NOT NULL,
 CONSTRAINT [PK_kaytossa] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[opettajat]    Script Date: 18.11.2021 11.13.40 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[opettajat](
	[opettaja_num] [int] IDENTITY(1,1) NOT NULL,
	[nimi] [varchar](150) NOT NULL,
	[puhn] [varchar](150) NOT NULL,
	[osoite] [varchar](150) NOT NULL,
 CONSTRAINT [PK_opettajat] PRIMARY KEY CLUSTERED 
(
	[opettaja_num] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[opiskelijat]    Script Date: 18.11.2021 11.13.40 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[opiskelijat](
	[op_numero] [int] IDENTITY(1,1) NOT NULL,
	[nimi] [varchar](150) NOT NULL,
	[puhn] [varchar](150) NOT NULL,
	[osoite] [varchar](150) NOT NULL,
	[opettaja_num] [int] NOT NULL,
 CONSTRAINT [PK_opiskelijat] PRIMARY KEY CLUSTERED 
(
	[op_numero] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[soittimet]    Script Date: 18.11.2021 11.13.40 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[soittimet](
	[soitin_num] [int] IDENTITY(1,1) NOT NULL,
	[merkki] [varchar](150) NOT NULL,
	[soitin] [varchar](150) NOT NULL,
 CONSTRAINT [PK_soittimet] PRIMARY KEY CLUSTERED 
(
	[soitin_num] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[kaytossa]  WITH CHECK ADD  CONSTRAINT [FK_kaytossa_opiskelijat] FOREIGN KEY([opiskelija_num])
REFERENCES [dbo].[opiskelijat] ([op_numero])
GO
ALTER TABLE [dbo].[kaytossa] CHECK CONSTRAINT [FK_kaytossa_opiskelijat]
GO
ALTER TABLE [dbo].[kaytossa]  WITH CHECK ADD  CONSTRAINT [FK_kaytossa_soittimet] FOREIGN KEY([soitin_num])
REFERENCES [dbo].[soittimet] ([soitin_num])
GO
ALTER TABLE [dbo].[kaytossa] CHECK CONSTRAINT [FK_kaytossa_soittimet]
GO
ALTER TABLE [dbo].[opiskelijat]  WITH CHECK ADD  CONSTRAINT [FK_opiskelijat_opettajat] FOREIGN KEY([opettaja_num])
REFERENCES [dbo].[opettajat] ([opettaja_num])
GO
ALTER TABLE [dbo].[opiskelijat] CHECK CONSTRAINT [FK_opiskelijat_opettajat]
GO
USE [master]
GO
ALTER DATABASE [16Tehtava] SET  READ_WRITE 
GO
