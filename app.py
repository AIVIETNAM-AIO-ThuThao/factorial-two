import streamlit as st
import math
import random

# Cấu hình trang có đười ươi
st.set_page_config(
    page_title="🦍🦍 Giai thừa",
    layout="wide",  
    page_icon="🦍"
)

# Logo trang không thể thiếu khỉ đột
st.logo(
    image="assets/khi.png",
)

st.title("Giai thừa!")
st.header("Ai thông minh hơn khỉ đột? 🦍 🦍 🦍")
st.markdown("---")

# Tạo dict chứa câu hỏi, đáp án, câu trả lời, chấm điểm
if "questions" not in st.session_state:
    n = random.randint(1, 10)
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

# Nhận đáp án từ người dùng
q["answer"] = st.text_input(
    key="cau_1",  
    disabled=st.session_state.da_nop
)

# Nộp
if st.button("Sure!", disabled=st.session_state.da_nop):
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

# Kết quả sau khi đã nộp bài
if st.session_state.da_nop:  
    if q["right_wrong"]:
        # TRƯỜNG HỢP ĐÚNG
        st.success(f"ĐÚNG! {q['n']}! = {q['fact']}")
        st.video("assets/video.mp4", width=400, autoplay=True)
        st.balloons()
        
    else:
        # TRƯỜNG HỢP SAI
        st.error("SAI!")
        st.image("assets/image.png")
    
    
    
    