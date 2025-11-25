DROP DATABASE IF EXISTS final_project;
CREATE DATABASE final_project;
USE final_project;

CREATE TABLE Test (
  id INTEGER,
  name TEXT,
  email TEXT,
  birthday DATE,
  interests TEXT,
  PRIMARY KEY (id)
)