import pymysql

# 資料庫設定
db_settings = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "arthur900530",
    "db": "health_keeper",
    "charset": "utf8"
}
try:
    # 建立Connection物件
    conn = pymysql.connect(**db_settings)
    # 建立Cursor物件
    with conn.cursor() as cursor:
        sql = 'SELECT * FROM health_keeper.hospital'
        cursor.execute(sql)
        result = cursor.fetchall()
        for r in result:
            print(r)
except Exception as ex:
    print(ex)