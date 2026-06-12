import streamlit as st

# 웹 페이지 제목 설정
st.title("🏃‍♂️ 키(Height) 데이터 홀/짝 정렬 애플리케이션")
st.write("입력된 키 데이터를 인덱스 기준으로 분류하고 버블 정렬하는 웹 앱입니다.")

st.divider()

# 1. 입력부 (Streamlit 위젯 사용)
st.subheader("1. 데이터 입력")
# 사용자에게 기본값 제공 및 직접 입력 유도
user_input = st.text_input(
    "키(height) 목록을 쉼표(,)로 구분해서 입력하세요:",
    value="148, 178, 169, 165, 156, 173, 179, 162, 185, 175"
)

# 입력받은 문자열을 숫자 리스트로 변환
try:
    heights = [int(x.strip()) for x in user_input.split(",") if x.strip()]
except ValueError:
    st.error("⚠️ 올바른 숫자 형식으로 입력해주세요. (예: 160, 170, 180)")
    st.stop()

# 현재 전체 데이터 보여주기
st.info(f"입력된 원본 데이터 ({len(heights)}개): {heights}")


# 2. 로직 처리부 (기존 코드 기반 분류 및 버블 정렬)
line1 = [] # 0, 2, 4... 인덱스 데이터 (컴퓨터 기준 짝수, 사람 기준 1, 3, 5... 홀수번)
line2 = [] # 1, 3, 5... 인덱스 데이터 (컴퓨터 기준 홀수, 사람 기준 2, 4, 6... 짝수번)

# 기존 코드의 인덱스 분기 로직 반영
for i in range(len(heights)):
    if i % 2 == 0:
        line1.append(heights[i])
    else:
        line2.append(heights[i])

# 버블 정렬 알고리즘 적용 (line1)
for i in range(len(line1) - 1):
    for j in range(len(line1) - 1 - i):
        if line1[j] > line1[j + 1]:
            line1[j], line1[j + 1] = line1[j + 1], line1[j]

# 버블 정렬 알고리즘 적용 (line2)
for i in range(len(line2) - 1):
    for j in range(len(line2) - 1 - i):
        if line2[j] > line2[j + 1]:
            line2[j], line2[j + 1] = line2[j + 1], line2[j]


# 3. 출력부 (st.write, st.success, st.dataframe 등 활용)
st.divider()
st.subheader("2. 정렬 및 분류 결과")

# 가로로 깔끔하게 배치하기 위해 Streamlit 컬럼(Column) 사용
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🔴 홀수번 줄 (Line 1)")
    st.metric(label="데이터 개수", value=f"{len(line1)}개")
    st.write("**정렬된 데이터:**", line1)

with col2:
    st.markdown("### 🔵 짝수번 줄 (Line 2)")
    st.metric(label="데이터 개수", value=f"{len(line2)}개")
    st.write("**정렬된 데이터:**", line2)

st.divider()

# 최종 성공 메시지 및 데이터프레임 시각화
st.success("🎉 성공적으로 분류 및 정렬이 완료되었습니다!")

# 표 형태로 깔끔하게 결합하여 보여주기
# 홀수번과 짝수번의 길이가 다를 수 있으므로 딕셔너리로 묶어 표현
max_len = max(len(line1), len(line2))
padded_line1 = line1 + [None] * (max_len - len(line1))
padded_line2 = line2 + [None] * (max_len - len(line2))

result_df = {
    "홀수번 줄 (Line 1)": padded_line1,
    "짝수번 줄 (Line 2)": padded_line2
}

st.write("📊 **최종 정렬 데이터 테이블**")
st.dataframe(result_df, use_container_width=True)