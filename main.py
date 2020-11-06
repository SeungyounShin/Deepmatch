import streamlit as st
from setup import *
import time
from db_conn import *
import datetime
from utils import *

apps = {}

#basic setup
submit = submit_table()

#sidebar
st.sidebar.title('DeepMatch')
st.sidebar.write('🤖인공지능 기반 소개팅 매칭 서비스.')
st.sidebar.write('연애가치관/이상형 정보를 기반으로 인공지능 매칭 알고리즘이 소개팅을 주선해줍니다.')
st.sidebar.write('#소개팅#딥러닝#공대생')

#main
st.title("DeepMatch")
st.markdown("## 🧑🏻‍💻개인정보")
#나이
st.markdown("### 나이를 알려주세요~")
age = st.slider("만 나이 말고 한국식 나이를 알려주세요!", 19, 30)
#성별
st.markdown("### 성별을 알려주세요!")
sex = st.radio("남성/여성 선택", ("남성", "여성"))
#키
st.markdown("### 키를 적어주세요!")
height = st.slider("이하, 이상은 최소/최대 값으로 해주세용", 130, 210)
#체형
st.markdown("### 체형을 알려주실 수 있나요?")
body_type = st.selectbox("체형을 골라주세요", body_type_list)
#카톡아이디
st.markdown("### 카톡아이디를 알려주세요!")
kakao_id = st.text_input("카톡아이디 혹은 오픈카카오톡링크", "둘 중 하나만 적어주세요!")
#재학생인증
st.markdown("### 재학생 퀴즈!")
is_student = st.text_input("동국대에서만 들을 수 있는 명상 수업의 이름은?", "힌트 : OOO OO")

st.markdown("## 📋질문")
#선호 키
st.markdown("### 상대방의 원하는 키를 알려주세요!")
if sex == "남성":
    #남성
    expect_height = st.slider("이하나 이상은 최소/최대 값으로 해주세요", 130, 210, (150, 180))
else :
    #여성
    expect_height = st.slider("이하나 이상은 최소/최대 값으로 해주세요", 130, 210, (150, 180))
#선호 체형
st.markdown("### 상대방의 원하는 체형을 알려주실 수 있나요?")
expect_body_type = st.multiselect("복수 선택 가능합니다", body_type_list)
#Q1 :: 여사친/남사친
st.markdown("### Q1. 여사친/남사친과 단둘이 만나는 것은 어떻게 생각하시나요?")
q1 = st.selectbox("여사친/남사친", q1_list)
#Q2 :: 연락빈도
st.markdown("### Q2. 연인 사이에 연락에 대해서는 어떻게 생각하시나요?")
q2 = st.selectbox("연락의 빈도", q2_list)
#Q3 :: 스킨쉽
st.markdown("### Q3. 스킨십 대해서는 어떻게 생각하시나요?")
q3 = st.selectbox("스킨십", q3_list)
#Q4 :: SNS
st.markdown("### Q4. 연인 사진을 SNS에 올리는 것에 대해 어떻게 생각하시나요?")
q4 = st.selectbox("SNS", q4_list)
#Q5 :: 갈등해결
st.markdown("### Q5. 의견 마찰이 있을 때 어떻게 해결하는것이 맞다고 생각하시나요?")
q5 = st.selectbox("갈등해결 능력이 뛰어난 커플이 오래간다고 합니다!", q5_list)
#Q6 :: 만남
st.markdown("### Q6. 데이트 빈도에 대해서는 어떻게 생각하시나요?")
q6 = st.selectbox("같이 시간 보내기는 연애의 가장 기본 단계라고 합니다", q6_list)
#Q7 :: 정서적 공감
st.markdown("### Q7. 힘든 일이 있을 때 연인에게 이야기하는 편인가요?")
q7 = st.selectbox("정서적으로 위로를 받을 때 관계가 더 깊어진다고 합니다", q7_list)
#Q8 :: 금전
st.markdown("### Q8. 연인 사이의 돈 문제에 대해 어떻게 생각하시나요?")
q8 = st.selectbox("돈 문제", q8_list)

st.markdown("---")
if st.button("제출하기!"):
    result = (str(datetime.datetime.now()),
              int(age),
              sex_map[sex],
              str(kakao_id),
              int(height),
              str(body_type),
              str(is_student),
              str(expect_height),
              str(expect_body_type),
              q1_list.index(q1),
              q2_list.index(q2),
              q3_list.index(q3),
              q4_list.index(q4),
              q5_list.index(q5),
              q6_list.index(q6),
              q7_list.index(q7),
              q8_list.index(q8))

    if valid(result):
        if result[6]=='자아와 명상' or result[6]=='자명' or result[6]=='자아와명상':
            #재학생 인증 답을 맞췄으면
            try:
                submit.insert(result)
                submitted_id_rows = submit.search_by_kakao(result[3])
                if len(submitted_id_rows)>0:
                    st.warning("이미 제출 했습니다 (방금 제출한 내용으로 수정됩니다.)")
                else:
                    st.success("성공적으로 제출되었습니다")
            except:
                st.error("DB에 INSERT 중 문제가 발생했습니다 - (제출 형식을 다시 확인해주세요)")
        else:
             st.warning("재학생 퀴즈가 틀렸습니다!")
    else:
        st.warning("주관식을 작성해주세요!")
