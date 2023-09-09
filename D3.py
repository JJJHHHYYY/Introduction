import streamlit as st
from PIL import Image

st.set_page_config(
    page_title = "자기소개", page_icon="🙃"
)


menu = st.sidebar.selectbox("MENU",['자기소개','학교소개','동아리소개','관심분야'])

if menu == '자기소개':
    st.header('자기소개🎈')
    me = st.selectbox(' ',['기본 정보', '나의 좌우명', '목표'])
    if me == '기본 정보':
        st.subheader('기본 정보📃')
        st.write("이름 : 여지훈")
        st.write("나이 : 만 17세")
        st.write("소속 : 대구경원고등학교")

    elif me == '나의 좌우명':
        st.subheader('나의 좌우명🥇')
        st.title('"아는것만으로는 충분하지 않다. 적용할 줄 알아야한다."')
        st.write('이소룡의 어록 중 하나인 "아는것만으로는 충분하지 않다. 적용할 줄 알아야한다"는 나의 좌우명이다',
                 '프로그래밍을 처음 접했을 때 나는 배우기만 하면 누구든 프로그램을 만들 수 있는줄 알았다.',
                 '하지만 배우는 것만으론 그 무엇도 할 수 없었고 배운것을 스스로 응용할 줄 알아야된다는 것을 깨달았다.',
                 '앞서 말한 이소룡의 어록은 앞서 나의 경험에서만 아니라 모든 상황에서 적용된다고 생각하여 나의 좌우명이 됐다.')

    else:
        st.header('목표')
        st.subheader('0순위 : 대한민국 1등 기업 창업')
        st.subheader('1순위 : 대학🖋')
        st.write('현재 가장 첫번째 목표는 좋은 대학에 가서 좋은 수업을 듣는 것이다. 높은 대학을 가면 높은 사람들 있고 그 사람들로부터 많은 것을 배우고 싶다.')
        st.subheader('2순위 : 공부📚')
        st.write('1순위를 이루기 위해, 또 1등 기업을 만들기 위해선 공부가 필수적이다. 할 수 있는 뭐든 배우고 공부하고 싶다.')
        st.subheader('3순위 : 자신감')
        st.write('1,2순위를 이뤘다면 그 다음 나에게 필요한건 자신감이라고 생각한다. 무엇이든 앞서 이뤄낸것을 토대로 이뤄낼 수 있다는 자신감을 가지고 인생을 살아갈 것이다.')

elif menu == '학교소개':
    st.header('학교소개🖋')
    me = st.selectbox(' ', ['기본 정보', '장점','최근 이슈'])
    if me == '기본 정보':
        st.subheader('기본 정보')
        st.write('설립 : 1975년 12월 1일')
        st.write('학생 : 남 796명, 여 0명')
        st.write('주소 : 대구광역시 달서구 새방로 77 - https://map.naver.com/p/entry/place/11594090?c=15.00,0,0,0,dh')
        st.write('전화 : 053 - 235 - 5600')
        st.write('교훈 : "내모습을 나타내자"')
        st.write('로고')
        image = Image.open('ㄱㅇㄱㄺ.PNG')
        st.image(image)
    elif me == '장점':
        st.subheader('1. 수성구 제외 대구 최고 수준 입결')
        st.write('매년 경북대, 부산대 150명 이상 배출')
        st.write('매년 5명 이상 서울대 배출')
        st.write('2023년 의예과 17명 배출')
        st.write('2023년 수능 대구전체 수석 배출')
        st.subheader('2.교육과정')
        st.write('과학중점학교')
        st.write('이과생 전교생 중 약 80%이상')
        st.write('2학년 과탐, 수학 전과목 이수로 3학년 내신 최소 1과목만 나옴.')
        st.write('교육과정 외에도 창의과학관이 존재해 다른 일반계고 보다 다양한 과학실험, 생기부활동이 많음.')
        st.write('사립계 일반고라 선생님들의 열정이 엄청나고 입결에 진심임.')
    else:
        st.subheader('최근 이슈')
        st.write('와룔산 산사태로 인한 강당, 식당 붕괴')
        image = Image.open('학교 붕괴1.jpg')
        image2 = Image.open('학교붕괴2.jpg')
        st.image(image2)
        st.image(image)


elif menu == '동아리소개':
    st.header('동아리소개💻')
    st.subheader('다빈치코드')
    st.write('개요 : 학생 자율 동아리로 코딩 동아리이다.')
    st.write('다양한 활동을 하며 경원고의 전통 동아리 중 하나로 대학에서도 알아주는 동아리이다.(현재는 모름..)')

else:
    st.header('관심분야🛒')
    st.write('관심분야 : 웹 응용 프로그래밍')
    st.write('공동교육과정 수업을 들으면서 정말 간단하고 쉽게 웹을 개발 할 수 있다는 점을 깨달았고 평소 상상만 해왔던 프로그램을 제작해 볼 수 있다고 생각했다',
             '특히 과학 실험 데이터를 가지고 시각 데이터를 볼 수 있는 웹을 제작해보고싶다.')