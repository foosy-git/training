import pymysql

config = {
    'host': 'database-fsy.cppzltfflrtn.us-east-2.rds.amazonaws.com',
    'user': 'root',
    'password': 'XXX',
    #'database': 'database_fsy',
    #'ssl': {'ca': '/path/to/rds-ca-2022-us-west-2.pem'} # if using SSL
}
mysql_conn = pymysql.connect(**config)
mysql_cur = mysql_conn.cursor()
