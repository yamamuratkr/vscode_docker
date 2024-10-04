SELECT 'CREATE DATABASE sample' 
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'sample')\gexec

\c sample

CREATE TABLE IF NOT EXISTS sample_text
(sample_text TEXT);

INSERT INTO sample_text (sample_text)
VALUES ('簡単にVS CodeとDockerでDjangoのWebアプリ環境が構築できたよ!!');