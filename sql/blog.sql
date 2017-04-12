drop table if exists user;
-- 用户基础数据表
CREATE table user (
   id INT AUTO_INCREMENT PRIMARY KEY,
   avatar VARCHAR(255),       --用户的头像
   name VARCHAR(20),          --用户的名字
   mail VARCHAR(255),         --用户的有邮箱
   mobile VARCHAR(11),        --用户的手机号
   birthday TIMESTAMP,        --用户的生日
   sex VARCHAR(1),            --用户的性别
   create_time TIMESTAMP      --创建时间
);

-- 用户账户表
DROP TABLE if EXISTS user_auth;
CREATE TABLE user_auth(
   id int AUTO_INCREMENT PRIMARY KEY,
   user_id int,               --关联用户id
   account VARCHAR (255),     --用户帐号
   password VARCHAR (255),    --用户密码
   salt VARCHAR(10),          --用户密码随机数
   create_time TIMESTAMP      --创建时间
);

-- 用户增长数据表，记录用户变化等级数据
DROP TABLE if EXISTS user_record;
CREATE TABLE user_record(
  id int AUTO_INCREMENT PRIMARY KEY,
  user_id int,                --关联用户id
  record int,                 --记录用户成长值
  type VARCHAR (255),         --用户类型，可以根据成长值，也可以跟具其他的
  create_time TIMESTAMP       --创建时间
);

-- 用户交互信息表
DROP TABLE if EXISTS user_interaction;
CREATE TABLE user_interaction(
  id int AUTO_INCREMENT PRIMARY KEY,
  user_id int,                --当前用户id
  watch_user_id int,          --关注的用户id
  create_time TIMESTAMP       --创建时间
);

-- blog内容表
DROP TABLE if EXISTS content;
CREATE table content (
  id int AUTO_INCREMENT PRIMARY KEY,
  user_id int,                --关联用户表
  title VARCHAR(255),         --blog的标题
  content TEXT,               --blog的内容，可能是副文本格式
  create_time TIMESTAMP       --创建时间
);


-- blog的内容交互，评论的数据
DROP TABLE if EXISTS content_interaction;
CREATE table content_interaction(
  id int AUTO_INCREMENT PRIMARY KEY,
  content_id int,             --内容id
  user_id int,                --当前用户的id
  replay_user_id int,         --回复的用户的id
  content TEXT,               --回复的内容
  create_time TIMESTAMP       --创建时间
);



