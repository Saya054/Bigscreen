--����Database
CREATE DATABASE JXBIGDATA


--������Ч��Ա��
--id����idֵ��name�������֣�department����

DROP TABLE IF EXISTS jx_person;
CREATE TABLE jx_person(
id int(4) primary key auto_increment,
pname varchar(12) not null,
department varchar(64) not null
);

--��������ͳ�Ʊ�
--id����û����ipsn_id�����Լ������Ա���� cpsn_name��Ա����callin ������callans�����callgood����	callbad����
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

--����֧����ͳ�Ʊ�
--id����û����ipsn_id�����Լ������Ա���� cpsn_name��Ա���� issueans ֧��������
DROP TABLE IF EXISTS jx_issue;
CREATE TABLE jx_issue(
id int(4) primary key auto_increment,
ipsn_id int(4) ,
cpsn_name varchar(12) not null,
issueans int(4),
constraint fk_issue_id foreign key (ipsn_id) references jx_person(id)
);

--����֧����IMͳ�Ʊ�
--id����û����ipsn_id�����Լ������Ա���� cpsn_name��Ա���� imvalidans  im��Ч�ش�
DROP TABLE IF EXISTS jx_webim;
CREATE TABLE jx_webim(
id int(4) primary key auto_increment,
ipsn_id int(4) ,
cpsn_name varchar(12) not null,
imvalidans  int(4),
constraint fk_webim_id foreign key (ipsn_id) references jx_person(id)
);

--��������ͳ�Ʊ�
--id����û����ipsn_id�����Լ������Ա���� cpsn_name��Ա���� floors ¥����
DROP TABLE IF EXISTS jx_community;
CREATE TABLE jx_community(
id int(4) primary key auto_increment,
ipsn_id int(4) ,
cpsn_name varchar(12) not null,
floors int(4),
constraint fk_comun_id foreign key (ipsn_id) references jx_person(id)
);

--������Чͳ�Ʊ�
--id ����	ipsn_id ��Ա����cpsn_name��Ա����daypointÿ��Ҫ��Чissuepoint֧������Чimpoint im��Чhotlinepoint���߼�Чcommunitypoint������Чwecompoint��ҵ΢�ż�Чotherpoint������Чtotalpoint�ܼ�Чdesirepoint ����Чcompercent��Ч��ɰٷֱ�
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


--����������Чͳ�Ʊ�
--id ����	ipsn_id ��Ա����cpsn_name��Ա����season����ֵ��1-4��huibopoint�ز���	shangjipoint�̻���uptnpoint Up���ܷ�insidefnpoint�ڲ���ѵ��partnerfnpoint��鸳�ܷ�examplepoint������yuliaopoint���Ϸ�kaoshipoint���Է�chutipoint�����opluspoint�����ӷ�	oreducepoint��������sumpoint�ϼƷ�
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


--����������ͳ�Ʊ�
--id_day����hot_date����callin����callans�����callpercent��ͨ��
DROP TABLE IF EXISTS jx_hotlineweek;
CREATE TABLE jx_hotlineweek(
id_day int(4) primary key auto_increment,
hot_date date,
callin int(4),
callans int(4),
callpercent float
);


--����IM��ͳ�Ʊ�
--id_day����im_date����dialogcount �ܷ�����validcount ��Ч��validpercent ��Ч������
DROP TABLE IF EXISTS jx_webimweek;
CREATE TABLE jx_webimweek(
id_day int(4) primary key auto_increment,
im_date date,
dialogcount int(4),
validcount int(4),
validpercent float
);


