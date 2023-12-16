-- Дані для таблиці "company"
INSERT INTO company (company_name, company_addres, contact_person, contact_email)
VALUES
  ('Company A', 'Company_address A', 'person A', 'companyA@gmail.com'),
  ('Company B', 'Company_address B', 'person B', 'companyB@gmail.com'),
  ('Company C', 'Company_address C', 'person C', 'companyC@gmail.com'),
  ('Company D', 'Company_address D', 'person D', 'companyD@gmail.com'),
  ('Company E', 'Company_address E', 'person E', 'companyE@gmail.com'),
  ('Company F', 'Company_address F', 'person F', 'companyF@gmail.com'),
  ('Company G', 'Company_address G', 'person G', 'companyG@gmail.com'),
  ('Company H', 'Company_address H', 'person H', 'companyH@gmail.com'),
  ('Company I', 'Company_address I', 'person I', 'companyI@gmail.com'),
  ('Company J', 'Company_address J', 'person J', 'companyJ@gmail.com');

-- Дані для таблиці "gps"
INSERT INTO gps (gps_latitude, gps_longitude)
VALUES
  (41, 2),
  (21, 1),
  (31, 3),
  (11, 4),
  (51, 5),
  (36, 10),
  (34, 19),
  (49, 3),
  (63, 17),
  (15, 21);

-- Дані для таблиці "masters"
INSERT INTO masters (master_name, master_surname, master_phone)
VALUES
  ('Kris', 'Master_A', 9191),
  ('Sophi', 'Master_B', 9292),
  ('Andrey', 'Master_C', 9393),
  ('Alex', 'Master_D', 9494),
  ('Taras', 'Master_E', 9595),
  ('Oleg', 'Master_F', 9696),
  ('Ivan', 'Master_G', 9797),
  ('Anna', 'Master_H', 9898),
  ('Sasha', 'Master_I', 9999),
  ('Mickle', 'Master_J', 9090);

-- Дані для таблиці "payment"--
INSERT INTO payment (record_id, payment_date, payment_amoun)
VALUES
  (1, '2010-08-13', 1500),
  (3, '2013-08-13', 750),
  (2, '2012-11-30', 900),
  (5, '2021-08-05', 1500),
  (4, '2015-01-28', 889),
  (6, '2022-08-06', 889),
  (7, '2022-09-14', 980),
  (8, '2022-12-31', 1040),
  (9, '2023-04-23', 1235),
  (10, '2023-05-17', 1125);

-- Дані для таблиці "service_master_availability"
INSERT INTO service_master_availability (master_id, available_date)
VALUES
  (1, '2023-11-12'),
  (1, '2023-11-15'),
  (2, '2023-10-31'),
  (2, '2023-11-04'),
  (3, '2023-12-02'),
  (3, '2023-12-10'),
  (4, '2023-10-28'),
  (4, '2023-10-29'),
  (5, '2023-11-19'),
  (5, '2023-11-23');

-- Дані для таблиці "service_master_prices"--
INSERT INTO service_master_prices (service_id, master_id, price)
VALUES
  (1, 1, 200),
  (1, 2, 176),
  (1, 5, 210),
  (2, 3, 420),
  (2, 1, 380),
  (2, 4, 395),
  (3, 3, 150),
  (3, 4, 134),
  (3, 5, 125),
  (4, 2, 540),
  (4, 3, 538),
  (4, 4, 600),
  (5, 5, 300),
  (5, 2, 256),
  (5, 1, 305);

  -- Дані для таблиці "service_records"
INSERT INTO service_records (terminal_id, service_id, master_id, service_date, duration, total_price)
VALUES
  (3, 2, 3, '2010-08-10', 10, 1300),
  (1, 3, 1, '2012-11-30', 6, 700),
  (3, 5, 5, '2013-08-10', 3, 500),
  (5, 2, 2, '2015-01-24', 9, 1300),
  (4, 1, 4, '2021-08-01', 4, 689),
  (6, 10, 6, '2022-08-01', 11, 735),
  (10, 6, 7, '2022-09-11', 7, 780),
  (8, 8, 10, '2022-12-28', 5, 840),
  (7, 7, 9, '2023-04-21', 8, 1035),
  (9, 9, 8, '2023-05-14', 2, 920);


-- Дані для таблиці "services"--
INSERT INTO services (service_id, service_type)
VALUES
  (1, 'ordinary'),
  (2, 'major repairs'),
  (3, 'taking cash'),
  (4, 'update'),
  (5, 'check'),
  (6, 'BLOCK'),
  (7, 'deactivate'),
  (8, 'configuration help'),
  (9, 'hardware support'),
  (10, 'configuring POS terminal');


-- Дані для таблиці "terminal_services"
INSERT INTO terminal_services (terminal_id, service_id)
VALUES
  (1, 4),
  (2, 2),
  (4, 1),
  (3, 3),
  (5, 4),
  (1, 5),
  (4, 8),
  (2, 4),
  (3, 2),
  (5, 7),
  (5, 8);

-- Дані для таблиці "terminals"
INSERT INTO terminals (address, company_id, gps_id, installation_date)
VALUES
  ('terminal_address A', 1, 3, '2010-10-20'),
  ('terminal_address B', 1, 3, '2005-09-21'),
  ('terminal_address C', 1, 3, '2014-01-12'),
  ('terminal_address D', 1, 3, '2009-10-20'),
  ('terminal_address E', 1, 3, '2023-12-30'),
  ('terminal_address F', 1, 3, '2023-12-30'),
  ('terminal_address G', 1, 3, '2023-12-30'),
  ('terminal_address H', 1, 3, '2023-12-30'),
  ('terminal_address I', 1, 3, '2023-12-30'),
  ('terminal_address J', 1, 3, '2023-12-30');
