-- create and delete operations must be execute from other database
CREATE DATABASE sm_profiles;

-- kill all conections to this database 
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'sm_profiles';

-- delete database
DROP DATABASE sm_profiles;