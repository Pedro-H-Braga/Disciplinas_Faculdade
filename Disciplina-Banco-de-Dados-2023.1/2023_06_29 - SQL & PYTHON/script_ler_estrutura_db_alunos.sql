-- ------------------------------------------------------------
  SELECT tables.table_name, tables.table_schema
    FROM information_schema.tables
   WHERE table_schema NOT IN ('pg_catalog', 'information_schema')
     AND table_type = 'BASE TABLE' 
ORDER BY table_name;

-- ------------------------------------------------------------
  SELECT column_name
    FROM information_schema.columns 
   WHERE table_schema NOT IN ('pg_catalog', 'information_schema')
     AND table_name = 
ORDER BY table_name, ordinal_position;

-- ------------------------------------------------------------
