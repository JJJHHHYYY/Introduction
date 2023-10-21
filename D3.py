import streamlit as st
from PIL import Image
import pandas as pd

st.set_page_config(
    page_title = "자기소개", page_icon="🙃",#layout="wide"
)



menu = st.sidebar.selectbox("MENU",['자기소개🎈','학교소개🖋','동아리소개','관심분야'])

if menu == '자기소개🎈':
    st.header('자기소개🎈')
    tab1,tab2,tab3 = st.tabs(['기본 정보','좌우명','목표'])

    with tab1:
        st.header('기본 정보📃')
        st.write("이름 : 여지훈")
        st.write("나이 : 만 17세")
        st.write("소속 : 대구경원고등학교")

    with tab2:
        st.header('나의 좌우명🥇')
        st.title('"아는것만으로는 충분하지 않다. 적용할 줄 알아야한다."')
        st.write('이소룡의 어록 중 하나인 "아는것만으로는 충분하지 않다. 적용할 줄 알아야한다"는 나의 좌우명이다',
                 '프로그래밍을 처음 접했을 때 나는 배우기만 하면 누구든 프로그램을 만들 수 있는줄 알았다.',
                 '하지만 배우는 것만으론 그 무엇도 할 수 없었고 배운것을 스스로 응용할 줄 알아야된다는 것을 깨달았다.',
                 '앞서 말한 이소룡의 어록은 앞서 나의 경험에서만 아니라 모든 상황에서 적용된다고 생각하여 나의 좌우명이 됐다.')

    with tab3:
        st.header('목표')
        st.subheader('0순위 : 대한민국 1등 기업 창업')
        st.subheader('1순위 : 대학🖋')
        st.write('현재 가장 첫번째 목표는 좋은 대학에 가서 좋은 수업을 듣는 것이다. 높은 대학을 가면 높은 사람들 있고 그 사람들로부터 많은 것을 배우고 싶다.')
        st.subheader('2순위 : 공부📚')
        st.write('1순위를 이루기 위해, 또 1등 기업을 만들기 위해선 공부가 필수적이다. 할 수 있는 뭐든 배우고 공부하고 싶다.')
        st.subheader('3순위 : 자신감')
        st.write('1,2순위를 이뤘다면 그 다음 나에게 필요한건 자신감이라고 생각한다. 무엇이든 앞서 이뤄낸것을 토대로 이뤄낼 수 있다는 자신감을 가지고 인생을 살아갈 것이다.')

elif menu == '학교소개🖋':
    col1, col2 = st.columns([1,15])
    with col1:
        image = Image.open('ㄱㅇㄱㄺ.PNG')
        st.image(image)
    with col2:
        st.header("대구경원고등학교")

    tab1, tab2, tab3 = st.tabs(['기본 정보', '학교 상징', '장점'])



    with tab1:
        st.subheader('기본 정보')
        st.write('이름 : 대구경원고등학교')
        st.write('설립 : 1975년 12월 1일')
        st.write('학생 : 남 796명, 여 0명')
        st.write('전화 : 053 - 235 - 5600')
        st.write('주소 : 대구광역시 달서구 새방로 77')
        data = pd.DataFrame({
            'latitude': [35.86647],
            'longitude': [128.5245]
        })
        st.map(data)

    with tab2:
        st.header('학교 상징')
        st.image(Image.open('ㄱㅇㄱㄱㅎ.PNG'))
        st.image(Image.open('ㄱㅇㄳㅈ.PNG'))



    with tab3:
        st.subheader('1. 수성구 제외 대구 최고 수준 입결')
        st.image(Image.open('ㄱㅇㄱㅈㅈ1.PNG'))
        st.image(Image.open('ㄱㅇㄱㅈㅈ2.PNG'))
        st.subheader('2.교육')
        st.write('과학중점학교')
        st.write('다양한 교내,교외 활동 추진')
        st.write('학생들의 엄청난 학구열')
        st.subheader('야자 참여율 100%!!')




elif menu == '동아리소개':
    st.header('동아리소개💻')
    st.subheader('다빈치코드')
    st.write('코딩과 관련된 다양한 활동을 하며 경원고의 전통 동아리 중 하나로 대학에서도 알아주는 동아리')
    st.image(Image.open('ㄷㅇㄹ.jpg'))


else:
    st.header('관심분야🛒')
    st.write('관심분야 : 프로그래밍')
    st.write('중학교 시절부터 코딩에 관심을 가지고 Python, C, C# 등 다양한 프로그래밍 언어를 배움')
    st.subheader('Pygame을 사용해 만든 게임')
    st.video('https://youtu.be/Ei2wPa0Mp5w')
