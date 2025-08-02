# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 09:05:20 2025

@author: 오정우
넷플릭스 데이터 분석 프로젝트/ netflix_titles.csv, netflix_logo.jpg

"""
import pandas

"""
내가 그걸 가지고 뭘 할지 평상시에 생각 안 했을 경우
1. 복지패널 데이터를 평소에 안 보다보니 어려움

코드화 시킬 때 어려운 점
1. 데이터에 대한 지식이 거의 없을 경우 (h14_ 같은 걸 머리속에 익혀있어야)

텍스트 분석, 동영상 분석, 이미지 분석, DB 분석 중 분석에 대한

텍스트 분석이라고 하더라도
실제 글을 읽어서 분석할 건지 기존 통계를 활용하는 분석을 할 건지

나: 텍스트 분석 -> 실제 글을 읽고 분석하는 분석가가 되고 싶어!
"""
# 분석할 때 필요한 라이브러리가 뭘까 고민?
'''
사용 라이브러리:
    numpy: 수치 해석을 위해 사용 (결측치작업, 수치화작업 시 사용)
    판다스: 데이터를 분석하고, 전처리하기 위해 사용 (데이터프레임,시리즈)
    matplotlib / seaborn: 데이터에 대한 시각화 작업
    워드클라우드 : 특정 텍스트 강조
    
데이터 분석 목표
    데이터를 빠르게 파악하고,
    전처리를 수행한 후
    여러 인사이트 도출(******)
    
데이터 전처리
    데이터 결측치 처리
    피처 엔지니어링(특성을 뽑아서 새로운 데이터로 쳐리) => 특정 데이터프레임의 변수 생성 = 파생변수(어떤 데이터로 인해서 파생되었다)
    
데이터 시각화 처리 : 요청 기업의 브랜드 색상을 사용
    1. 브랜드 색상
        데이터 시각화 하기 전에 색상 미리 정해주는 것 매우 중요
        색상을 데이터의 성격에 맞게 선택.
        중요도에 따라 강조방법 계획, => 시각화 효과를 극대화!
        
    2. 파이 차트
        데이터의 카테고리별 비율을 시각화하는데 최적화
        비율을 쉽게 비교할 수 있꼬,
        각 카테고리의 상대적 중요성 한 눈에 파악 가능.
        => 넷플릭스에서 영화와 TV 쇼의 비율을 시각화.
        
    3. 막대 그래프
        데이터의 항목 간 비교를 명확하게 시각화하는 데 유용
        각 장르의 빈도를 막대 그래프로 시각화.
        => 넷플릭스에서 어떤 장르가 가장 많이 등장하는 지를 파악.
        
    4. 히트맵
        데이터의 밀도나 강도를 색상으로 시각화하며
        복잡한 데이터셋에서 패턴, 트랜드 파악 용이!
        나이 그룹별로 국가별 콘텐츠 비율을 시각화
        => 각 국가가 어떤 나이 그룹을 타겟으로 하는 콘텐츠가 많은 지를 분석
        => 각 콘텐츠를 통해 국가별 시청층을 이해.
        => 각 국가의 시청 트랜드, 콘텐츠 기획에 대한 인사이트 도출!
        
    5. 워드크라우드
        텍스트 기반 데이터에서 빈도가 높은 단어를 시각적으로 강조
        => 데이터의 주요 주제, 키워드를 한눈에 파악
        넷플릭스에서 콘텐츠 설명에서 자주 등장하는 단어들을 시각화,
        => 어떤 주제나, 키워드가 자주 나오는 지를
        => 콘텐츠의 주요 테마 파악,
        => 마케팅, 콘텐츠 기획, 전략, 사용자 분석, 등 유용한 인사이트 파악을 돕고자 제작
'''

"""
1. 넷플릭스 데이터 파악
"""
''' 1-1. 데이터 분석 라이브러리'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt ####정우야 plt를 자주 쓰잖아 기억해
import seaborn as sns ###정우야 sns를 자주 쓰잖아 기억해

''' 1-2. csv 로드'''
# data 폴더의 csv 파일을 로드하여 netflix 변수에 저장 (협업할 땐 미리 다 정하고 가야한다)
netflix = pd.read_csv('./data/netflix_titles.csv') ###정우야 pd.read_csv지 open이냐!
netflix.head() #확인용

''' 1-3. 데이터 내용 확인 : 컬럼(변수) 확인 '''
# 데이터프레임.columns
netflix.columns
'''
Index(['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added',
       'release_year', 'rating', 'duration', 'listed_in', 'description'],
      dtype='object')
만일 list(netflix.columns)로 하면 세로로 나타내줘서 편해

텍스트 파일 만들어서 얘는 각각의 변수가 어떤 역할인지 반드시 다 써야한다 "https://cafe.naver.com/common/storyphoto/viewer.html?src=https%3A%2F%2Fcafeptthumb-phinf.pstatic.net%2FMjAyNTAyMTRfMjcx%2FMDAxNzM5NDg4MzgyOTA5.AOA1vBTRW4CuBtq0rlnS1ViZw4RA3RshcC54GtO8wBAg.CRVz96O1psVcgcWqj6qbbi-XzuRcCHvuZdylokh58jUg.PNG%2Fimage.png%3Ftype%3Dw1600" 참조
'''
list(netflix.columns)
# 데이터프레임을 직접 보고 어떻게 쪼개고 어떻게 분석할건지를 먼저 보는게 중요 키보드 잡는게 중요한게 아니라

''' 1-4 열에 대한 요약 정보 확인 :데이터프레임.info() '''
netflix.info()
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 8807 entries, 0 to 8806 # 행에 대한 총 갯수 8807개이고 0번부터 8806번까지 붙어있다
Data columns (total 12 columns): # 컬럼은 총 12개로 나누어져 있다
 #   Column        Non-Null Count  Dtype 
---  ------        --------------  ----- 
 0   show_id       8807 non-null   object
 1   type          8807 non-null   object
 2   title         8807 non-null   object
 3   director      6173 non-null   object  #6173개밖에 없네? 결측치가 있겠구나
 4   cast          7982 non-null   object  #결측치 존재
 5   country       7976 non-null   object  #결측치 존재
 6   date_added    8797 non-null   object  #결측치 존재
 7   release_year  8807 non-null   int64      # 이 7번 연도만 숫자로 되어있네
 8   rating        8803 non-null   object  #결측치 존재
 9   duration      8804 non-null   object  #결측치 존재
 10  listed_in     8807 non-null   object
 11  description   8807 non-null   object
dtypes: int64(1), object(11)
memory usage: 825.8+ KB
"""

"""
2. 넷플릭스 데이터셋 결측치 처리
"""
'''
넷플릭스 결측치 비율 확인하고 처리
일반적으로
  결측치 비율이 5% 미만일 경우
    => 일부만 존재: 따라서 삭제
    => 데이터 손실을 최소화, 분석의 신뢰성에는 영향을 미치지 않는다
  
  결측치 비율이 5%~20% 사이
    => 결측치 비중이 꽤 큰편이므로 대체 방향을 모색
    => 평균 / 중간값/ 최빈값 활용 방안 검토
  결측치 비율이 20% 이상
    => 열 전체를 삭제
    => 데이터 손실이 커지기 때문에 신중한 판단 필요
    => 특히, 데이터셋이 작거나, 해당 변수가 중요한 역할을 할 경우,
        => 모델 기반 대체나, 예측 모델을 통해 결측치를 보완!
    * 결측치가 20% 이상일 경우
    변수에 대한 중요성, 분석목적, 데이터의 양을 종합적으로 고려

결측치: 데이터프레임.isna()
결측치 갯수:데이터 프레임.isna().sum()
결측치 비율: 데이터 프레임.isna().sum() / len(데이터프레임) * 100
'''
for i in netflix.columns :
    missingValueRate = netflix[i].isna().sum() / len(netflix) * 100
    
    if missingValueRate > 0 :
        print("{} null rate: {}%".format(i,round(missingValueRate, 2)))   #round(~~) 결측치 비율을 소수점 둘째 자리까지 반올림 첫 번째 {} → i (열 이름) 값이 들어감, 두 번째 {} → round(missingValueRate, 2) (소수점 둘째 자리까지 반올림한 결측치 비율) 값이 들어감
"""
director null rate: 29.91%  <= 제거, 우리가 분석하는데 중요한 요소가 아니기 때문에
cast null rate: 9.37%       <=대체(컬럼의 해당 값)
country null rate: 9.44%    <= 대체(컬럼의 해당값)
date_added null rate: 0.11% <= 제거(컬럼의 해당행만 제거)
rating null rate: 0.05% <= 
duration null rate: 0.03%
"""
''' 2-1 country의 결측치(9.44%) 대체 : fillna('No Data') '''
netflix['country'] = netflix['country'].fillna('No Data')
"""
Out[13]: 
0    United States
1     South Africa
2          No Data
3          No Data
4            India
Name: country, dtype: object
"""
''' 2-2. director/cast 대체 : replace(np.nan,'No Data') '''
netflix['director'] = netflix['director'].replace(np.nan, 'No Data')
#하고 나면 확인하는 습관을 들여 옆에 netflix['director']이라고 쳐보기만 하면 돼
"""
0       Kirsten Johnson
1               No Data
2       Julien Leclercq
3               No Data
4               No Data
      
8802      David Fincher
8803            No Data
8804    Ruben Fleischer
8805       Peter Hewitt
8806        Mozez Singh
Name: director, Length: 8807, dtype: object
"""
''' 2-3 date_added/rating/duration 결측치가 있는 행 제거 : dropna() '''
#dropna() : axis = / inplace = True(이게 있어야 제거를 실제로 해서 적용해) (행을 지우려면 axis=0)
# dataframe 전체 행을 지우는 거니까 dataframe.dropna(~~ 이런식으로 가는거지)
netflix.dropna(axis = 0, inplace = True) # 7965개로 줄어들었네..?

'''결측치 갯수로 재 확인 : isnull().sum() / isna().sum()'''
netflix.isnull().sum()
'''
show_id         0
type            0
title           0
director        0
cast            0
country         0
date_added      0
release_year    0
rating          0
duration        0
listed_in       0
description     0
dtype: int64

3. 넷플릭스 피처 엔지니어링

피처 엔지니어링 : 데이터프레임의 기존 변수를 조합하거나,
                    새로운 변수를 만드는 것을 의미.
데이터 분석 / 머신러닝 모델을 학습시킬 때 매우 중요!
현업: 예측 모델이 데이터의 패턴을 잘 이해하고 학습할 수 있는 기준!!!

피처 엔지니어링을 명확하고 의미있는 피처를 만들어 사용하면,
모델의 결과를 쉽게 해석할 수 있다!!!
데이터의 다양한 측면을 고려하여 더 정확한 분석을 할 수 있다!

# 코딩하다 막히는 부분은 chatgpt한테 물어봐도 되나 피처 엔지니어링을! 어떤 걸 찾을지 뭘 찾을지 고민하는 게 핵심 그 다음이 코드
''' 

''' 3-1. 넷플릭스 시청 등급 변수 '''
'넷플릭스 데이터프레임 rating #등급표시 변수를 이용하여 파생 변수명 age_group(시청등급)으로 활용'
'All(모든)/ Older kids(어린이) / Teens(청소년 초반) / Young Adults(청소년 후반)/ Adults(성인)'
netflix['age_group'] = netflix['rating']
"""
netflix['rating']
Out[23]: 
1       TV-MA
2       TV-MA
4       TV-MA
5       TV-MA
6          PG
 
8801    TV-MA
8802        R
8804        R
8805       PG
8806    TV-14
Name: rating, Length: 7965, dtype: object
"""
age_group_dic = {
    'G': 'ALL',             #전체
    'TV-G': 'ALL',
    'TV-Y': 'ALL',
    'PG': 'Older Kids',         #7세 이상
    'TV-Y7': 'Older Kids',
    'TV-Y7-FV': 'Older Kids',
    'TV-PG': 'Older Kids',
    'PG-13': 'Teens',           # 13세 이상
    'TV-14': 'Young Adults',    # 16세 이상
    'NC-17': 'Adults',          # 18세 이상
    'NR': 'Adults',             # 등급 보류
    'UR': 'Adults',             # 무삭제 등급
    'R': 'Adults',
    'TV-MA': 'Adults'
    }

# map()를 이용하여 rating 컬럼의 값을 딕셔너리 기반으로 변환하여
# age_group 컬럼에 저장
netflix['age_group'] = netflix['age_group'].map(age_group_dic)

netflix.head(2)
"""
  show_id     type  ...                                        description age_group
1      s2  TV Show  ...  After crossing paths at a party, a Cape Town t...    Adults
2      s3  TV Show  ...  To protect his family from a powerful drug lor...    Adults

[2 rows x 13 columns]
"""
# => 피처 엔지니어링을 통해 데이터의 가독성, 효율성을 높일 수 있다.

''' 3-2 전처리가 완료된 데이터를 CSV 파일로 저장: to_csv() '''
# to_csv('파일명', index=False)
netflix.to_csv('./result/netflix_preprocessed.csv' , index=False)
# 전체적으로 끝났으면 이와 같이 저장을 시켜줘야 처음부터 끝까지 다 실행시킬 필요가 없지

''' 4. 넷플릭스 시각화하기
전처리된 넷플릭스 파일 읽기 : netflix_preprocessed.csv

시각화 라이브러리
'''
''' 4-1. 시각화 라이브러리 '''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

''' 4-2. 전처리 데이터 읽기 '''
netflix = pd.read_csv('./result/netflix_preprocessed.csv')
netflix.info()

"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 7965 entries, 0 to 7964
Data columns (total 13 columns):
 #   Column        Non-Null Count  Dtype 
---  ------        --------------  ----- 
 0   show_id       7965 non-null   object
 1   type          7965 non-null   object
 2   title         7965 non-null   object
 3   director      7965 non-null   object
 4   cast          7965 non-null   object
 5   country       7965 non-null   object
 6   date_added    7965 non-null   object
 7   release_year  7965 non-null   int64 
 8   rating        7965 non-null   object
 9   duration      7965 non-null   object
 10  listed_in     7965 non-null   object
 11  description   7965 non-null   object
 12  age_group     7965 non-null   object
dtypes: int64(1), object(12)
memory usage: 809.1+ KB
"""

''' 4-3. 넷플릭스 브랜드 색상 시각화 : sns.palplot('색상'.'색상')'''
sns.palplot(['#221f1f', '#b20710', '#e50914', '#f5f5f1']) #무조건 순서대로 나오나 보다
plt.title('Netflix brand palette',  #제목
          loc = 'left',             #정렬 기준
          fontfamily = 'serif',     # 글꼴
          fontsize = 15,            #글씨크기(pt 단위)
          y = 1.2)                  # 제목의 y축 위치 값
plt.show()

''' 4-4. 넷플릭스 파이 차트 : Movies & TV shows'''
# netflix['type'] =>value_count()
type_counts = netflix['type'].value_counts()
"""
Out[34]: 
type
Movie      5651
TV Show    2314
Name: count, dtype: int64
"""
plt.figure(figsize=(5,5))
# type_counts.index로 하면 라벨이 movie로 해줄거 아니야 인덱스인거
plt.pie(type_counts, labels=type_counts.index, autopct = '%0.f%%',
        startangle=100, explode = [0.05, 0.05],shadow = True,
        colors = ['#b20710', '#221f1f'])

plt.suptitle('which type did people like?', fontfamily = 'serif', fontsize=15, fontweight ='bold') #title보다 큰 아이
plt.title('on Netflix', fontfamily='serif', fontsize=12)
plt.show()

''' 4-5 넷플릭스 막대 그래프
어떤 장르가 인기가 가장 많은지.....
listed_in
'''

netflix['listed_in']
'''
0         International TV Shows, TV Dramas, TV Mysteries
1       Crime TV Shows, International TV Shows, TV Act...
2       International TV Shows, Romantic TV Shows, TV ...
3                      TV Dramas, TV Horror, TV Mysteries
4                                Children & Family Movies
                       
7960              Dramas, International Movies, Thrillers
7961                       Cult Movies, Dramas, Thrillers
7962                              Comedies, Horror Movies
7963                   Children & Family Movies, Comedies
7964       Dramas, International Movies, Music & Musicals
Name: listed_in, Length: 7965, dtype: object
'''
# 넷플릭스 데이터셋의 장르별 등장 횟수(빈도) 계산
genres = netflix['listed_in'].str.split('. ', expand=True) \
                             .stack()                       \
                             .value_counts()

# expand = True : 분할된 결과를 확장하여 여러 열로 변환
# 분할된 문자가 개별적인 열로 배치되어 데이터프레임을 생성

"""
이건 어떻게 등장했는가??

1단계
netflix['listed_in'].str.split(', ', expand=True)

2단계
netflix['listed_in'].str.split(', ', expand=True).stack()
# stack() : 개별적인 행으로 정리... 해서 차곡차곡 쌓아주는 아이

3단계
netflix['listed_in'].str.split(', ', expand=True).stack().value_counts()

Movies             5376
T                  4353
Internationa       3814
Dramas             3171
Shows              2632
                   2479
Comedies           2211
Actio              1018
...
Name: count, dtype: int64
"""

plt.figure(figsize=(12,6))

sns.barplot(x = genres.values, y = genres.index, hue = genres.index, palette = 'RdGy')#genres를 넣어주면 왜 안돼 위처럼 시리즈로 index count가 같이 나와버리잖아. 값을 꺼내려면 genres.value
                                # 그래프를 점점더 어둡게 만드는 hue
                                
plt.title('', fontsize=16)
plt.xlabel('Count', fontsize=14)
plt.ylabel('Genre', fontsize=14)

plt.grid(axis='x') # x를 기준으로 grid 그리겠다
plt.show()

'''
넷플릭스의 전체적인 콘텐츠 전략을 확인 할 수 있다.
넷플릭스는 드라마와 국제 영화에 집중.
=> 글로벌 콘텐츠 제공과 깊이있는 스토리 라인으로
    시청자들의 다양한 취향을 만족시키려는 듯...
    
=> 다양한 영화 장르를 제공함으로써
    시청자들에게 보다 풍부한 선택지를 제공.
    
=> 넷플릭스의 콘텐츠 전략은
장르의 다양성과 글로벌 사용자들의 요구를
동시에 충족하기 위한 방향으로 나아가는 듯
'''
'''
4-3. 넷플릭스 히트맵
넷플릭스 데이터셋을 이용하여 각 나라의 콘텐츠 수를 집계.
각 나라에서 어느 나이 그룹이 어떤 콘텐츠를 소비하는 지 분석, 특정 나이층의 시청 선호도를 파악하여 마케팅 전략을 세우고자...
특정 나라에서 특정 나이 그룹을 위한 콘텐츠가 부족하다면
해당 연령층을 겨냥한 새로운 컨텐츠를 개발!!!
country, / age_group / / genres
'''

# 1. 넷플릭스 데이터의 title이라는 열에서 => Sankofa인 행의 데이터 확인!
netflix[netflix['title'].str.contains('Sankofa', na=False, case = False)]
#  str.contains 함수 어떤 문자가 포함이 되어 있는지 아닌지 파악하는 함수
#case 변수: 대소문자 구분하지 말고 찾아라
# Python python

#country' 열의 값을 , 를 기준으로 구분 => list
#출력할 최대 행 수를 None(무한대)으로 설정해서 모두 출력
pd.set_option('display.max_rows', None)
#pd.set_option() : 판다스 라이브러리의 출력 옵션을 설정하는 함수
# 'display.max_rows', None: 전체 행을 생략없이 출력 가능 (아래 처럼 쫙 나오게 됨)

# United Stats, Ghana, Korea ... 이런식으로 되어 있기 때문에 ...으로 생략된 요소를 없애라는 것
#, 쉼표로 country 열의 값을 파이썬 리스트
netflix['country'] = netflix['country'].str.split(', ')
"""
7895     [Germany, United States, United Kingdom, Canada]
7896                                      [United States]
7897                                      [United States]
7898                                     [United Kingdom]
7899                                     [United Kingdom]
7900                                      [United States]
7901                                      [United States]
7902                                             [Taiwan]
7903                                     [United Kingdom]
7904                                     [United Kingdom]
7905                                     [United Kingdom]
7906                                      [United States]
7907                                      [United States]
7908          [United States, East Germany, West Germany]
그랬더니 진짜 이런식으로 쫙 나왔어
"""
#3. 파이썬 리스트로 바꾼 country 열의 값에 explode() 함수를 적용하여
# 개별 행으로 분리
netflix_age_country = netflix.explode('country')

# 4. 확인 : title 열의 값이 'Sankofa'인 행 전체를 확인하여
 #           country 열과 age_group 열의 값이 어떻게 이루어져 있는지 확인
netflix_age_country[netflix_age_country['title'].str.contains('Sankofa', na=False, case = False)]

# 5. 각 나이 그룹에 따른 국가별 넷플릭스 컨텐츠 수
netflix_age_country_unstack = netflix_age_country.groupby('age_group')\
                              ['country'].value_counts().unstack()
                              # groupby 된 상황에서는 <pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000022D2A681970> 이런식으로 풀어서 안 나와져 있음
# unstack() : 그룹화된 데이터를 풀어서 다시 데이터프레임으로 전환

# 특정 나이 그룹에 따른 특정 나라별 콘텐츠로 필터링
# 6-1 연령
age_order = ['ALL', 'Older Kids', 'Teens', 'Adults']

# 6-2 국가
country_order = ['United States', 'India', 'United Kingdom', 'Canada', 'Japan', 'France', 'South Korea',
                 'Spain', 'Mexico', 'Turkey']

# 6-3. 필터링 : .loc[]
# 행: age_order / 열 : country_order
netflix_age_country_unstack = netflix_age_country_unstack. \
                                loc[age_order, country_order]
                                
                                
# 6-4. 결측치 처리 : 0
netflix_age_country_unstack = netflix_age_country_unstack.fillna(0)

# 6.5. 나이 그룹에 따른 국가별 콘텐츠 비율
#      각 열의 값을 각 열의 합으로 나누기 : div()
#       axis = 1
netflix_age_country_unstack = netflix_age_country_unstack.div(
                              netflix_age_country_unstack.sum(axis=0),axis=1)
# div 함수 어떤 값을 무엇으로 나누겠다!
# div(열의 합을 각 열의 값으로) 나누기
#div(~~.sum(axis=0), axis=1)
# U.S  => 열의 합 : 255(ALL), + 694(O,K) + ~~~~
# 결론적으로 데이터에 대한 정규화작업이 이루어짐, 단위가 큰 수와 단위가 아주 작은 수 => 0~1 실수로 변환

plt.figure(figsize=(15,5))

# 사용자 정의 컬러맵
cmap = plt.matplotlib.colors.LinearSegmentedColormap.from_list(' ', ['#221f1f', '#B20710', '#f5f5f1'])

# from_list('색팔레트 이름', ['색상', '색상', .....])
# '#221ㄹ1ㄹ' => # : enldml tnrk 16wlstn, tortkdrkqtdlf ruddn tkdyd

sns.heatmap(netflix_age_country_unstack,
            cmap = cmap,     # 시각화 시키는 컬러맵
            linewidth = 2.5 , # 각 셀을 분할한 선의 너비
            annot=True,         # 각 셀에 데이터 값 표시
            fmt = '.0%') # 문자열 형식화 코드 # fmt = '.0f' 문자열로써 표시하겠다

plt.suptitle('Total content by country', fontweight = 'bold',fontfamily = 'serif', fontsize =15)

plt.title('~~', fontfamily = 'serif', fontsize =12)

plt.show()


"""
7.넷플릭스 워드 클라우드
pip install wordcloud
"""
# 워드 클라우드 생성에 필요한 모듈
from wordcloud import WordCloud

# 워드 클라우드를 원하는 형태로 그리기 위해 그림을 불러오는 패키지
from PIL import Image

plt.figure(figsize=(15, 5))

# netflix['description']
# wordcloud에서 작동할 수 있도록 데이터프레임을
# list로 1차 변환시키고, str(문자열)로 2차 변환
text = str(list(netflix['description']))

# 로고 이미지 열고 : 'netflix_logo.jpg' => Image.open()
# 넘파이 배열로 변환해주어야 숫자로 변환해줘야 함
# np.array()
mask = np.array(Image.open('./data/netflix_logo.jpg')) # 문제가 된 이유는 import Image가 안됐어
# mask = : 단어를 그릴 위치 설정, 흰색(#FFFFFF) 항목은 마스킹 된 것으로 간주 (배경을 투명하게 만들면 넘파이 필요 없음)
cmap = plt.matplotlib.colors.LinearSegmentedColormap.from_list(' ', ['#221f1f', '#B20710', '#f5f5f1'])

# 워드 클라우드 생성 
# 워드 클라우드 생성 : WordCloud().generate(text)
# WordCloud()
# background_color =    # 배경색
# width = px단위        # 1400
# height = px단위       # 1400
# max_words =           # 노출 빈도가 가장 큰 단어부터 최대 ? 단어만 출력
# mask =                # 이미지를 이용할 경우에만, 넘파이 배열
# colormap =            # 각 단어의 색상
wordclouds = WordCloud(background_color = 'white', width = 1400, height = 1400,
                      max_words = 170,
                      mask = mask,
                      colormap = cmap).generate(text)

plt.suptitle('Movies and TV shows',
             fontweight = 'bold', fontfamily = 'serif', fontsize = 15)

# 워드클라우드 결과를 Plots 창에 나타내기 : plt.imshow(워드클라우드 객체형)
plt.imshow(wordclouds)

plt.axis('off') # 축 감추기
plt.show()