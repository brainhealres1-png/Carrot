import streamlit as st

st.set_page_config(page_title="Carrot", layout="centered")

st.title("🥕 Carrot")
st.write("이름을 입력해주세요")

name = st.text_input("이름:", placeholder="예: 홍길동")

if st.button("제출"):
    if name:
        st.success(f"안녕하세요, {name}님! 👋")
    else:
        st.error("이름을 입력해주세요.")
