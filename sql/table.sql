--创建Database
CREATE DATABASE JXBIGDATA


--创建绩效人员表
--id代表id值，name代表名字，department部门

DROP TABLE IF EXISTS jx_person;
CREATE TABLE jx_person(
id int(4) primary key auto_increment,
pname varchar(12) not null,
department varchar(64) not null
);

--创建热线统计表
--id主键没含义ipsn_id（外键约束）人员编码 cpsn_name人员名称callin 呼入数callans呼入答复callgood好评	callbad差评
DROP TABLE IF EXISTS jx_hotline;
CREATE TABLE jx_hotline(
id int(4) primary key auto_increment,
ipsn_id int(4) ,
cpsn_name varchar(12) not null,
callin int(4),
callans int(4),
callgood int(4),
callbad int(4),
constraint fk_hot_id foreign key (ipsn_id) references jx_person(id)
);

--创建支持网统计表
--id主键没含义ipsn_id（外键约束）人员编码 cpsn_name人员名称 issueans 支持网答复数
DROP TABLE IF EXISTS jx_issue;
CREATE TABLE jx_issue(
id int(4) primary key auto_increment,
ipsn_id int(4) ,
cpsn_name varchar(12) not null,
issueans int(4),
constraint fk_issue_id foreign key (ipsn_id) references jx_person(id)
);

--创建支持网IM统计表
--id主键没含义ipsn_id（外键约束）人员编码 cpsn_name人员名称 imvalidans  im有效回答
DROP TABLE IF EXISTS jx_webim;
CREATE TABLE jx_webim(
id int(4) primary key auto_increment,
ipsn_id int(4) ,
cpsn_name varchar(12) not null,
imvalidans  int(4),
constraint fk_webim_id foreign key (ipsn_id) references jx_person(id)
);

--创建社区统计表
--id主键没含义ipsn_id（外键约束）人员编码 cpsn_name人员名称 floors 楼层数
DROP TABLE IF EXISTS jx_community;
CREATE TABLE jx_community(
id int(4) primary key auto_increment,
ipsn_id int(4) ,
cpsn_name varchar(12) not null,
floors int(4),
constraint fk_comun_id foreign key (ipsn_id) references jx_person(id)
);

--创建绩效统计表
--id 主键	ipsn_id 人员编码cpsn_name人员名称daypoint每日要求绩效issuepoint支持网绩效impoint im绩效hotlinepoint热线绩效communitypoint社区绩效wecompoint企业微信绩效otherpoint其他绩效totalpoint总绩效desirepoint 需求绩效compercent绩效完成百分比
DROP TABLE IF EXISTS jx_statistics;
CREATE TABLE jx_statistics(
id int(4) primary key auto_increment,
ipsn_id int(4) ,
cpsn_name varchar(12) not null,
season int(4),
daypoint int(4),
workday int(4),
issuepoint float,
impoint float,
hotlinepoint float,
communitypoint float,
wecompoint float,
otherpoint float,
totalpoint float,
desirepoint float,
compercent float,
constraint fk_stat_id foreign key (ipsn_id) references jx_person(id)
);


--创建其他绩效统计表
--id 主键	ipsn_id 人员编码cpsn_name人员名称season季度值（1-4）huibopoint回拨分	shangjipoint商机分uptnpoint Up提能分insidefnpoint内部培训分partnerfnpoint伙伴赋能分examplepoint案例分yuliaopoint语料分kaoshipoint考试分chutipoint出题分opluspoint其他加分	oreducepoint其他减分sumpoint合计分
DROP TABLE IF EXISTS jx_otherstat;
CREATE TABLE jx_otherstat(
id int(4) primary key auto_increment,
ipsn_id int(4) ,
cpsn_name varchar(12) not null,
season int(4),
huibopoint float,
shangjipoint float,
uptnpoint float,
insidefnpoint float,
partnerfnpoint float,
examplepoint float,
yuliaopoint float,
kaoshipoint float,
chutipoint float,
opluspoint float,
oreducepoint float,
sumpoint float,
constraint fk_ostat_id foreign key (ipsn_id) references jx_person(id)
);


--创建热线周统计表
--id_day主键hot_date日期callin呼入callans呼入答复callpercent接通率
DROP TABLE IF EXISTS jx_hotlineweek;
CREATE TABLE jx_hotlineweek(
id_day int(4) primary key auto_increment,
hot_date date,
callin int(4),
callans int(4),
callpercent float
);


--创建IM周统计表
--id_day主键im_date日期dialogcount 总服务数validcount 有效答复validpercent 有效服务率
DROP TABLE IF EXISTS jx_webimweek;
CREATE TABLE jx_webimweek(
id_day int(4) primary key auto_increment,
im_date date,
dialogcount int(4),
validcount int(4),
validpercent float
);


