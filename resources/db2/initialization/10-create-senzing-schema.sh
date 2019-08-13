#!/usr/bin/env bash

su - db2inst1 -c "
  db2 create database g2 using codeset utf-8 territory us;
  db2 connect to g2;
  db2 -tf /opt/senzing/g2/resources/schema/g2core-schema-db2-create.sql;
  db2 connect reset;
"
