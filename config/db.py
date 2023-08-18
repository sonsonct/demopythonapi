import mysql.connector

# Thay đổi các thông tin sau để phù hợp với cấu hình cơ sở dữ liệu của bạn
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'skinlele'
}

# Kết nối đến cơ sở dữ liệu
connection = mysql.connector.connect(**db_config)

# Tạo đối tượng cursor để thực hiện truy vấn
cursor = connection.cursor()

# query = 'SELECT * FROM custumers'
# cursor.execute(query)

# result = cursor.fetchall()

# # In ra các dòng dữ liệu
# for row in result:
#     print(row)

# # Đóng kết nối và cursor khi không cần nữa
# cursor.close()
# connection.close()
