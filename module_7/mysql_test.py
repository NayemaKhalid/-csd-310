--create database 
create database pysports;
--use pysports database 
use pysports;
--create user
create user 'pysports_user'@'localhost' identified with mysql_native_password by 'MYSQL8ISGREAT!';
--grant user privileges
grant all privileges on pysports.*to 'pysports_user'@'localhost';
--drop user 
drop user if exists 'pysports_user'@'localhost';
--create table team 
create table team (
  team_id int not null auto_increment; 
  team_name varchar(75) not null, 
  mascot varchar(75) not null, 
  primary key (team_id)
);
--create player table and set the foreign key 
create table player(
  player_id int  not null auto_increment, 
  first_name varchar(75) not null, 
  last_name varchar(75) not null, 
  team_id int not null, 
  primary key (player_id),
  constraint fk_team 
  foreign key (team_id)
  references team (team_id)
);
--insert team records 
insert into team (team_name, mascot)
values ('Team Gandalf' , 'White Wizards');
--drop table player if they are present 
drop table if exists player;
--select team_id from team table where team name matches 
select team_id from team where tame_name = 'Team Sauron';
