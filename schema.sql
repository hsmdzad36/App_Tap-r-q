-- Task 1: SQL Server
IF DB_ID('UniversityDB') IS NULL CREATE DATABASE UniversityDB;
GO
USE UniversityDB;
GO
IF OBJECT_ID('Students') IS NULL
CREATE TABLE Students (
    Id    INT IDENTITY(1,1) PRIMARY KEY,
    Name  NVARCHAR(100) NOT NULL,
    Score INT NOT NULL CHECK (Score BETWEEN 0 AND 100)
);
GO
IF NOT EXISTS (SELECT 1 FROM Students)
INSERT INTO Students (Name, Score) VALUES
 (N'Ali',85),(N'Leyla',72),(N'Murad',48),(N'Aysel',91),(N'Kamran',63);
GO
CREATE OR ALTER PROCEDURE GetStudentResult
    @StudentName NVARCHAR(100)
AS
BEGIN
    SET NOCOUNT ON;
    SELECT Name, Score,
           CASE WHEN Score >= 90 THEN 'A'
                WHEN Score >= 80 THEN 'B'
                WHEN Score >= 70 THEN 'C'
                WHEN Score >= 60 THEN 'D'
                ELSE 'F' END AS Grade
    FROM Students
    WHERE Name = @StudentName;
END
GO
-- EXEC GetStudentResult @StudentName = N'Ali';
