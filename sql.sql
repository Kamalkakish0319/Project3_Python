create database diet;

use diet;

create table diet (
 id int unsigned auto_increment not null,
 total_calories int not null,
 total_carbs int not null,
 total_fat int not null,
 total_protein int not null,
 weight int not null,
 primary key (id)
);