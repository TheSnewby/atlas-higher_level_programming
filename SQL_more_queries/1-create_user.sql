-- a script that creates the MySQL server user user_0d_1.
SELECT COUNT(*) INTO existance FROM mysql.user WHERE user = 'user_0d_1' and host = 'localhost';
IF existance = 0 THEN
    CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
    GRANT ALL PRIVILEGES on *.* TO 'user_0d_1'@'localhost';
END IF
