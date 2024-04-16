--  Script that create the useri replica_user and grant permissions
-- cat create_replica_user.sql | mysql -hlocalhost -uroot -p
CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY "replica";
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
GRANT SELECT ON mysql.user TO holberton_user@localhost;
FLUSH PRIVILEGES;
