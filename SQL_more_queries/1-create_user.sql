-- a script that creates the MySQL server user user_0d_1.
DELIMITER //
CREATE PROCEDURE createIfNonexistent()
BEGIN
    DECLARE existence INT DEFAULT 0;
    SELECT COUNT(*) INTO existence FROM mysql.user WHERE user = 'user_0d_1' and host = 'localhost';
    IF existence = 0 THEN
        CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
    END IF;
    GRANT ALL PRIVILEGES on *.* TO 'user_0d_1'@'localhost';
END //
DELIMITER ;

CALL createIfNonexistent();
