CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- --------------------------------------------------------
-- Table structure for table `users`
CREATE TABLE users (
  userid UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  firstname VARCHAR(100) NOT NULL,
  lastname VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  cellphone VARCHAR(20) NOT NULL,
  address VARCHAR(100) NOT NULL,
  password VARCHAR(100) NOT NULL,
  status BOOLEAN NOT NULL,
  creationdate TIMESTAMP NOT NULL DEFAULT current_timestamp
);

-- --------------------------------------------------------
-- Table structure for table `company`
CREATE TABLE company (
  companyid UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  name VARCHAR(100) UNIQUE NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  cellphone INTEGER NOT NULL,
  address VARCHAR(100) NOT NULL,
  nit INTEGER NOT NULL,
  status BOOLEAN NOT NULL,
  creationdate TIMESTAMP NOT NULL DEFAULT current_timestamp
);

-- --------------------------------------------------------
-- Table structure for table `job_offers`
CREATE TABLE job_offers (
  offerid UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  name VARCHAR(100) NOT NULL,
  workday VARCHAR(100) NOT NULL,
  status BOOLEAN NOT NULL,
  creationdate TIMESTAMP NOT NULL DEFAULT current_timestamp,
  companyid UUID NOT NULL REFERENCES company(companyid) ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- --------------------------------------------------------
-- Table structure for table `applicants`
CREATE TABLE applicants (
  applicantid UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  offerid UUID NOT NULL REFERENCES job_offers(offerid) ON DELETE NO ACTION ON UPDATE NO ACTION,
  userid UUID NOT NULL REFERENCES users(userid) ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- --------------------------------------------------------
-- Table structure for table `attributes`
CREATE TABLE attributes (
  attributeid UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  name VARCHAR(100) UNIQUE NOT NULL
);

-- --------------------------------------------------------
-- Table structure for table `attributes_user`
CREATE TABLE attributes_user (
  attributesxuserid UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  attributeid UUID NOT NULL REFERENCES attributes(attributeid) ON DELETE NO ACTION ON UPDATE NO ACTION,
  userid UUID NOT NULL REFERENCES users(userid) ON DELETE NO ACTION ON UPDATE NO ACTION,
  field VARCHAR(100) NOT NULL
);

-- --------------------------------------------------------
-- Table structure for table `faculties`
CREATE TABLE faculties (
  facultyid UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  name VARCHAR(100) UNIQUE NOT NULL
);

-- --------------------------------------------------------
-- Table structure for table `career`
CREATE TABLE career (
  careerid UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  status BOOLEAN NOT NULL,
  name VARCHAR(100) UNIQUE NOT NULL,
  facultyid UUID NOT NULL REFERENCES faculties(facultyid) ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- --------------------------------------------------------
-- Table structure for table `role`
CREATE TABLE role (
  roleid UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  name VARCHAR(100) UNIQUE NOT NULL
);

-- --------------------------------------------------------
-- Table structure for table `role_user`
CREATE TABLE role_user (
  rolexuserid UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  userid UUID NOT NULL REFERENCES users(userid) ON DELETE NO ACTION ON UPDATE NO ACTION,
  roleid UUID NOT NULL REFERENCES role(roleid) ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- --------------------------------------------------------
-- Table structure for table `user_career`
CREATE TABLE user_career (
  usercareerid UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  userid UUID NOT NULL REFERENCES users(userid) ON DELETE NO ACTION ON UPDATE NO ACTION,
  careerid UUID NOT NULL REFERENCES career(careerid) ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- --------------------------------------------------------
-- Table structure for table `history_status`
CREATE TABLE history_status (
  statusid UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  name VARCHAR(100) NOT NULL
);

-- --------------------------------------------------------
-- Table structure for table `job_offer_history`
CREATE TABLE job_offer_history (
  historyid UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  offerid UUID NOT NULL REFERENCES job_offers(offerid) ON DELETE NO ACTION ON UPDATE NO ACTION,
  userid UUID NOT NULL REFERENCES users(userid) ON DELETE NO ACTION ON UPDATE NO ACTION,
  statusid UUID NOT NULL REFERENCES history_status(statusid) ON DELETE NO ACTION ON UPDATE NO ACTION,
  changedate TIMESTAMP NOT NULL DEFAULT current_timestamp
);

-- Insert roles
INSERT INTO role (roleid, name) VALUES
('d6f414a0-1e8f-432c-a5f6-9dfa482b6142', 'Admin'),
('a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d', 'Graduate'),
('b1c2d3e4-5f6a-7b8c-9d0e-1f2a3b4c5d6e', 'Teacher');

-- Insert user
INSERT INTO users (userid, firstname, lastname, email, cellphone, address, password, status, creationdate) 
VALUES ('e6f414a0-1e8f-432c-a5f6-9dfa482b6143', 'Samir', 'Lora', 'selora@unibarranquilla.edu.co', '3001234578', 'Cualquier lugar', '$2b$12$olcKBExeWfmrvsbbQbXYHuVaUuYLWOihoPwy4cfX0D7uMTT9gyVv2', TRUE, current_timestamp);

INSERT INTO users (userid, firstname, lastname, email, cellphone, address, password, status, creationdate) 
VALUES ('b2f414a0-1e8f-432c-a5f6-9dfa482b6143', 'Juan', 'Evilla', 'jdevilla@unibarranquilla.edu.co', '3001245678', 'Cualquier lugar', '$2b$12$olcKBExeWfmrvsbbQbXYHuVaUuYLWOihoPwy4cfX0D7uMTT9gyVv2', TRUE, current_timestamp);

-- Insert role for user
INSERT INTO role_user (rolexuserid, userid, roleid) 
VALUES ('f6a4b3c2-1d2e-3f4a-5b6c-7d8e9f0a1b2c', 'e6f414a0-1e8f-432c-a5f6-9dfa482b6143', 'd6f414a0-1e8f-432c-a5f6-9dfa482b6142');

INSERT INTO role_user (rolexuserid, userid, roleid) 
VALUES ('f2a4b3c2-1d2e-3f4a-5b6c-7d8e9f0a1b2c', 'b2f414a0-1e8f-432c-a5f6-9dfa482b6143', 'd6f414a0-1e8f-432c-a5f6-9dfa482b6142');

-- Insert history Status
INSERT INTO history_status (statusid, name) VALUES
('d6f414a0-1e8f-432c-a5f6-9dfa482b6142', 'applied'),
('a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d', 'in progress'),
('b1c2d3e4-5f6a-7b8c-9d0e-1f2a3b4c5d6e', 'selected'),
('c1d2e3f4-5a6b-7c8d-9e0f-1a2b3c4d5e6f', 'rejected'),
('fc387434-5fec-48c9-9500-8ad3df4c0aea', 'accepted');