# NZBGet MySQL Plugin #
[![License](https://img.shields.io/badge/license-GPL-blue.svg)](http://www.gnu.org/licenses/)
[![Build Status](https://img.shields.io/travis/nzbget/nzbget/develop.svg)](https://travis-ci.org/nzbget/nzbget)

This Plugin for NZBGet inserts a record into a user specified MySQL database.  It only requires these configuration options:
- the hostname of the mysql database server
- the port mysql is listening on (optional)
- the mysql username
- the mysql password
- the name of the mysql database
- the table to insert the records into

This script is written in python and it requires the installation of the pymsql module: `sudo pip install pymysql`

The purpose of this script is to allow you to create a dashboard or other reporting around your downloads.  You can use Grafana or write your own frontend to create neat glanceboards.

Here's a very simple example:
![Simple Grafana Table](https://raw.githubusercontent.com/chrisbergeron/nzbget-mysql/master/screenshots/grafana-nzbget-table.png)

Fell free to create a Pull Request (PR) and submit improvements.  I'm new to Python and there are a lot of areas for improvement in this plugin.

## Installation: ##
Download and copy the Mysql-Log.py file from this repo into your `NZBGet/scripts` directory.  Alternatively, you can clone this repo directly into the /scripts/ directory:
```
# This directory will be where YOUR NZBGet installation is (/opt/nzbget/ in this example)
cd /opt/nzbget/scripts
git clone https://github.com/chrisbergeron/nzbget-mysql.git
mv nzbget-mysql/Mysql-Log.py .
```

## MySQL / MariaDB Configuration ##
You can use the included SQL file to create the mysql database and table.  You can customize the mysql database and table names.  Create them with:
```
mysql -u username -p -h db-hostname database_name < create-database.sql.txt
Enter password:
```
Alternatively, you can create the database manually:
```
mysql> CREATE DATABASE nzbs;
mysql> CREATE TABLE `mynzbs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nzb` varchar(255) DEFAULT NULL,
  `entry_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);
mysql> quit
```
The end result should be a table with 3 columns:
```
+------------+--------------+------+-----+-------------------+-----------------------------+
| Field      | Type         | Null | Key | Default           | Extra                       |
+------------+--------------+------+-----+-------------------+-----------------------------+
| id         | int(11)      | NO   | PRI | NULL              | auto_increment              |
| nzb        | varchar(255) | YES  |     | NULL              |                             |
| entry_date | timestamp    | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
+------------+--------------+------+-----+-------------------+-----------------------------+
```

## NZBGet-MySQL Configuration ##
In NZBGet go to `Settings` and at the bottom left you should see `MYSQL-LOG`:
![Configuring Plugin](https://raw.githubusercontent.com/chrisbergeron/nzbget-mysql/master/screenshots/configuring-plugin.png)

Add the hostname of your MySQL instance and the Port number it's listening on (default is 3306).

If configured properly, you'll see lines like this in your NZBGet `Messages`:
![Sample Log Output](https://raw.githubusercontent.com/chrisbergeron/nzbget-mysql/master/screenshots/nzbget-example-log-entry.png)

## Roadmap: ##
- [ ] Separate Show Name, Episode Name, Season and Episode info, Quality and Crew into separate rows
- [ ] Log NZBGet status codes

## Questions / Comments? ##

- [Mysql-Log.py forum post](https://forum.nzbget.net/viewtopic.php?f=8&t=3263) - conversation about this script/plugin
- [Home page (nzbget.net)](http://nzbget.net) - for first time visitors, learn more about NZBGet
- [Forum](http://forum.nzbget.net) - get support, share your ideas, extension scripts, etc
- [My Blog Post](http://chrisbergeron.com/2018/07/12/nzbget-mysql/) - introductory post