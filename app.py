import streamlit as st
import urllib.parse

st.set_page_config(page_title="대입 기출문제 학습 도우미", layout="wide")

st.markdown("## 📚 대입 수능, 모의고사 기출문제 검색기")
st.write("조건을 입력하고 아래의 버튼을 클릭하면 정답 확인, 유튜브 강의, PDF 다운로드 검색 결과가 즉시 새 창으로 열립니다.")

# --- 1. 검색 필터 구성 ---
col1, col2, col3 = st.columns(3)
with col1:
    grades = ["고3", "고2", "고1"]
    grade = st.selectbox("학년", grades, index=0)
with col2:
    years = [f"{year}" for year in range(2027, 2003, -1)]
    year = st.selectbox("년도", years)
with col3:
    months = ["3월", "4월", "5월", "6월", "7월", "9월", "10월", "11월(수능)"]
    month = st.selectbox("월", months)

col4, col5, col6 = st.columns(3)
with col4:
    subjects = [
        "국어", "국어(언어와 매체)", "국어(화법과 작문)", "영어", 
        "수학", "수학(미적분)", "수학(확률과 통계)", "수학(기하)", 
        "물리I", "화학I", "생명과학I", "지구과학I", "물리II", "화학II", "생명과학II", "지구과학II", "생활과 윤리", "사회문화", "한국지리", "세계지리", "동아시아사", "세계사", "경제", "정치와 법", "윤리와 사상"
    ]
    subject = st.selectbox("과목", subjects)
with col5:
    types = ["선택 안 함", "가형", "나형", "홀수형", "짝수형"]
    exam_type = st.selectbox("유형", types)
with col6:
    q_num = st.number_input("문제 번호", min_value=1, max_value=45, step=1)

st.markdown("---")

# --- 2. 검색어 및 URL 실시간 생성 로직 ---
# 사용자가 필터를 바꿀 때마다 URL이 실시간으로 백그라운드에서 업데이트됩니다.
type_str = f" {exam_type}" if exam_type != "선택 안 함" else ""
full_query = f"{grade} {year}년 {month} {subject}{type_str} {q_num}번"
base_info_no_qnum = f"{grade} {year}년 {month} {subject}{type_str}"

# 1) 구글 정답 검색 URL
google_ans_query = f"{full_query} 정답"
google_ans_url = f"https://www.google.com/search?q={urllib.parse.quote(google_ans_query)}"

# 2) 유튜브 동영상 검색 URL
youtube_url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(full_query)}"

# 3) 문제 PDF 다운로드 검색 URL
pdf_query = f"{base_info_no_qnum} PDF"
pdf_url = f"https://www.google.com/search?q={urllib.parse.quote(pdf_query)}"


# --- 3. 즉시 이동 버튼 출력 ---
st.markdown("#### 🚀 원하시는 검색 버튼을 클릭하세요")

# 3개의 버튼을 나란히 배치하기 위해 columns 활용
btn_col1, btn_col2, btn_col3 = st.columns(3)

with btn_col1:
    st.link_button("💡 문제 정답 검색", google_ans_url, use_container_width=True)
    
with btn_col2:
    st.link_button("📺 유튜브 동영상 검색", youtube_url, type="primary", use_container_width=True)
    
with btn_col3:
    st.link_button("📥 문제 PDF 다운로드 검색", pdf_url, use_container_width=True)

st.write("")
