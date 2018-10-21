
## Clone the repo

git clone

##  Install all the dependencies

pip install -r requirements.txt 

## Start mysql server 

sudo service mysql start
mysql -u root

## Set up Database

CREATE DATABASE weavedin;

## Run Custom commands

import all the commands in invoice.sql and items.sql

## python app.py

Server is up and running on localhost

## If you face any problem running the server 

$ sudo mysql -u root
mysql> USE mysql;
mysql> UPDATE user SET plugin='mysql_native_password' WHERE User='root';
mysql> FLUSH PRIVILEGES;
mysql> exit;

 
 
