-- Database and table creation script for Society Maintenance Management System
-- Open this file in MySQL Workbench and execute it.

CREATE DATABASE IF NOT EXISTS society_db12;

USE society_db12;

CREATE TABLE IF NOT EXISTS society_members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    member_name VARCHAR(100) NOT NULL,
    flat_number VARCHAR(20) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    monthly_maintenance DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    payment_status VARCHAR(20) NOT NULL DEFAULT 'Pending'
);
