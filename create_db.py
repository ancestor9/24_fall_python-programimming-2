
import sqlite3
from faker import Faker

# 가상 데이터 생성
fake = Faker()

# SQLite3 연결
conn = sqlite3.connect('fake_data.db')
cursor = conn.cursor()

# 사용자 테이블 생성
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    address TEXT
)
''')

# 가상 데이터 100개 삽입
for _ in range(100):
    name = fake.name()
    email = fake.email()
    address = fake.address()
    
    cursor.execute('''
    INSERT INTO users (name, email, address) VALUES (?, ?, ?)
    ''', (name, email, address))

conn.commit()
conn.close()

print("100개의 가상 데이터가 생성되었습니다.")
