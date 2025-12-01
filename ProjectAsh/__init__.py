import pymysql

# Use PyMySQL as the MySQLdb replacement when running on environments where
# the mysqlclient C extension cannot be built (e.g. Vercel serverless).
pymysql.install_as_MySQLdb()

