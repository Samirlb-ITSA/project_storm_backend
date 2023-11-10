-- Connect to your PostgreSQL database
\c storm

-- Create tables

CREATE TABLE users (
  userid SERIAL PRIMARY KEY,
  firstname VARCHAR(100) NOT NULL,
  lastname VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  cellphone INTEGER NOT NULL,
  address VARCHAR(100) NOT NULL,
  password VARCHAR(100) NOT NULL,
  status SMALLINT NOT NULL,
  creationdate TIMESTAMP NOT NULL DEFAULT current_timestamp
);

INSERT INTO users (userid, firstname, lastname, email, cellphone, address, password, status, creationdate) VALUES
(2, 'Juan', 'Evilla', 'juan.evilla', 320, 'bq', '123', 0, '2023-10-19 22:57:32'),
(3, 'david', 'perez', 'david.perez', 320, 'bq', '123', 0, '2023-10-19 22:57:32'),
(4, 'pepe', 'pepe', 'pepe', 320, 'bq', '123', 0, '2023-10-19 22:57:32'),
(5, 'jua', 'jua', 'jua@@', 323232, 'bqbq', '123', 1, '2023-10-21 12:43:21'),
(6, 'juanito', 'jua', 'jua@@uni', 323232, 'bqbq', '123', 1, '2023-10-21 12:43:40'),
(8, 'juanito', 'evilla', 'jua@@uniba', 323232, 'bqbq', '123', 1, '2023-10-21 12:50:44'),
(9, 'juan', 'evilla', 'jevilla@uni.com', 320, 'bq', '123', 1, '2023-10-26 21:28:47');

CREATE TABLE company (
  companyid SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL,
  cellphone INTEGER NOT NULL,
  address VARCHAR(100) NOT NULL,
  nit INTEGER NOT NULL,
  status SMALLINT NOT NULL,
  creationdate TIMESTAMP NOT NULL DEFAULT current_timestamp
);

INSERT INTO company (companyid, name, email, cellphone, address, nit, status, creationdate) VALUES
(1, 'Sykes', 'company@sykes.com', 333, 'bq', 0, 0, '2023-10-19 23:00:20'),
(2, 'Movate', 'movate@', 444, 'bq', 1234, 0, '2023-10-20 22:24:04');

CREATE TABLE joboffers (
  offerid SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  workday VARCHAR(100) NOT NULL,
  status SMALLINT NOT NULL,
  creationdate TIMESTAMP NOT NULL DEFAULT current_timestamp,
  companyid INTEGER NOT NULL REFERENCES company(companyid) ON DELETE NO ACTION ON UPDATE NO ACTION
);

INSERT INTO joboffers (offerid, name, workday, status, creationdate, companyid) VALUES
(1, 'programming', 'fulltime', 0, '2023-10-20 21:48:34', 1),
(10, 'accounting', 'parttime', 1, '2023-10-20 21:48:34', 1),
(11, 'accounting', 'parttime', 1, '2023-10-20 21:49:23', 1),
(16, 'networks', 'daytime', 1, '2023-10-20 22:02:43', 1),
(17, 'admin', 'fulltime', 1, '2023-10-20 22:03:59', 1),
(18, 'Employee', 'Continuous', 1, '2023-10-20 22:33:28', 2);

CREATE TABLE applicants (
  applicantid SERIAL PRIMARY KEY,
  offerid INTEGER NOT NULL REFERENCES joboffers(offerid) ON DELETE NO ACTION ON UPDATE NO ACTION,
  userid INTEGER NOT NULL REFERENCES users(userid) ON DELETE NO ACTION ON UPDATE NO ACTION
);

INSERT INTO applicants (applicantid, offerid, userid) VALUES
(1, 1, 2),
(2, 1, 3);

CREATE TABLE attributes (
  attributeid SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL
);

-- --------------------------------------------------------

--
-- Table structure for table `attributesxuser`

CREATE TABLE attributesxuser (
  attributesxuserid SERIAL PRIMARY KEY,
  attributeid INTEGER NOT NULL REFERENCES attributes(attributeid) ON DELETE NO ACTION ON UPDATE NO ACTION,
  userid INTEGER NOT NULL REFERENCES users(userid) ON DELETE NO ACTION ON UPDATE NO ACTION,
  field VARCHAR(100) NOT NULL
);

CREATE TABLE career (
  careerid SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL
);

INSERT INTO career (careerid, name) VALUES
(1, 'Ing Sistemas');

CREATE TABLE role (
  roleid SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL
);

INSERT INTO role (roleid, name) VALUES
(1, '0'),
(2, 'teacher'),
(3, 'graduate');

CREATE TABLE rolexuser (
  rolexuserid SERIAL PRIMARY KEY,
  userid INTEGER NOT NULL REFERENCES users(userid) ON DELETE NO ACTION ON UPDATE NO ACTION,
  roleid INTEGER NOT NULL REFERENCES role(roleid) ON DELETE NO ACTION ON UPDATE NO ACTION
);

INSERT INTO rolexuser (rolexuserid, userid, roleid) VALUES
(2, 8, 1);

CREATE TABLE userxcareer (
  usercareerid SERIAL PRIMARY KEY,
  userid INTEGER NOT NULL REFERENCES users(userid) ON DELETE NO ACTION ON UPDATE NO ACTION,
  careerid INTEGER NOT NULL REFERENCES career(careerid) ON DELETE NO ACTION ON UPDATE NO ACTION
);