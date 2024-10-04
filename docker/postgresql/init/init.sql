SELECT 'CREATE DATABASE sample' 
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'sample')\gexec

\c sample