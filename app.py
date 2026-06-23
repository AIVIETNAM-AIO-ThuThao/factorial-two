import streamlit as st
import math
import random

# Cấu hình trang
st.set_page_config(
    page_title="Giai thừa",
    layout="wide",  
    page_icon="🦍"
)

# Logo trang
st.logo(
    image="https://img.icons8.com/color/96/000000/orangutan.png",
)

st.title("Giai thừa")
st.header("Hãy giải 1 bài toán về giai thừa nhé! 🦍 🦍 🦍")
st.markdown("---")

# Tạo dict chứa câu hỏi
if "questions" not in st.session_state:
    n = random.randint(1, 20)
    st.session_state.questions = [{
        "n": n,
        "fact": math.factorial(n),
        "answer": None,
        "right_wrong": None
    }]
    st.session_state.da_nop = False  # Cờ nộp bài, mặc định False

# Câu hỏi
q = st.session_state.questions[0]   #Câu hỏi đầu tiên

st.subheader("Câu hỏi nè!")
st.write(f"**Tính:** {q['n']}! = ?")

# Nhập đáp án
q["answer"] = st.text_input(
    "Đáp án của bạn:", 
    key="cau_1",  
    disabled=st.session_state.da_nop
)

# Nộp
if st.button("Nộp bài", disabled=st.session_state.da_nop):
    st.session_state.da_nop = True      #đổi trạng thái rồi mới kiểm tra  
    if q["answer"] and q["answer"].strip():
        try:
            if int(q["answer"]) == q["fact"]:
                q["right_wrong"] = True
            else:
                q["right_wrong"] = False
        except:
            q["right_wrong"] = False
    else:
        q["right_wrong"] = False
    
    st.rerun()

# Kết quả
if st.session_state.da_nop:  # ✅ Kiểm tra đã nộp bài chưa
    st.subheader("Kết quả")
    
    if q["right_wrong"]:
        # TRƯỜNG HỢP ĐÚNG
        st.success(f"ĐÚNG! {q['n']}! = {q['fact']}")
        st.video("assets/video.mp4")
        st.balloons()
        
    else:
        # TRƯỜNG HỢP SAI
        st.error("SAI!")
        st.image("assets/image.png")
    
    
    
    