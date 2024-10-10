
import streamlit as st
import requests

# FastAPI에서 데이터를 가져오는 함수
def get_users():
    response = requests.get("http://localhost:8000/users")
    if response.status_code == 200:
        return response.json()["users"]
    else:
        return []

# 웹 페이지 구성
st.title("가상 사용자 데이터 조회")

users = get_users()

if users:
    for user in users:
        st.write(f"**Name**: {user['name']}")
        st.write(f"**Email**: {user['email']}")
        st.write(f"**Address**: {user['address']}")
        st.write("---")
else:
    st.write("사용자 데이터를 가져오는 데 실패했습니다.")
