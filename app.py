import streamlit as st
import math
import random

# Cấu hình trang
st.set_page_config(
    page_title="Giai thừa",
    layout="wide"
    page_icon="🦍"
)
# lồng logo
st.logo(
    image="https://img.icons8.com/color/96/000000/orangutan.png",
)


st.title("Thử thách Giai thừa")
st.header("Hãy giải 5 bài toán về giai thừa nhé!")
st.markdown("***")

# Lưu lịch sử với session_state
# Kiểm tra dữ liệu đã có
if "questions" not in st.session_state:
    # Nếu chưa có, tạo danh sách rỗng để chứa 5 question
    st.session_state.questions = []
    
    # Tạo 5 câu hỏi hú họa
    for i in range(5):
        n = random.randint(1, 20)
        
        # Thêm câu hỏi vào danh sách với 4 thông tin: số n cần tính giai thừa; fact: đáp án; answer: câu trả lời (ban đầu là None)
        # - dung_sai: kết quả đúng/sai (ban đầu là None)
        st.session_state.questions.append({
            "n": n,
            "fact": math.factorial(n),
            "answer": None,
            "right_wrong": None
        })
    
    # # gán cờ false cho việc người dùng nộp bài
    st.session_state.da_nop = False 
# Hiển thị 5 câu hỏi ra màn hình

for i, q in enumerate(st.session_state.questions):
    st.write(f"Câu {i+1}: {q['n']}! = ?")
    
    # Cho người dùng nhập đáp án
    # - key=f"cau_{i}"": key cho mỗi ô nhập
    # - disabled=st.session_state.da_nop: vô hiệu hóa nếu đã nộp bài
    q["answer"] = st.text_input(
        f"Đáp án câu {i+1}", 
        key=f"cau_{i}", 
        disabled=st.session_state.da_nop
    )

# Tạo nút "Submit", disabled=True khi đã nộp để không bấm lại
if st.button("Submit", disabled=st.session_state.da_nop):
    # đổi cờ nộp bài => true
    st.session_state.da_nop = True
    
    # Tạo biến đếm số câu trả lời đúng
    count = 0
    # Duyệt qua từng câu hỏi để kiểm tra câu trả lời
    for q in st.session_state.questions:
        if q["answer"] and q["answer"].strip():
            try:
                # Chuyển đổi câu trả lời từ string => int và so sánh
                if int(q["answer"]) == q["fact"]:
                    # Nếu đúng: đánh dấu True và tăng biến đếm
                    q["right_wrong"] = True
                    count += 1
                else:
                    # Nếu sai: đánh dấu False
                    q["right_wrong"] = False
            except:
                # Nếu người dùng nhập không phải số, coi như sai
                q["right_wrong"] = False
    
    # Lưu số câu đúng vào session_state và tính tỷ lệ %
    st.session_state.so_cau_dung = count
    st.session_state.ty_le = (count / 5) * 100
    
    # Làm mới trang để hiển thị kết quả
    st.rerun()

    
    # Nếu tỷ lệ đúng lớn hơn 80%
    if st.session_state.ty_le > 80:
        # Phát video từ YouTube (có thể thay link khác)
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        
        st.balloons()  # Bóng bay bay lên
        
    else:
        # Nếu tỷ lệ đúng ≤ 80%, hiển thị ảnh cáo cát
        st.warning(f"😅 Bạn làm đúng {st.session_state.ty_le:.0f}% (≤80%)")
        st.image(image.png)