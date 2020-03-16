# project_NBA_predict
미국 프로농구의 경기결과를 예측하는 프로젝트
농구의 PER과 WS를 필두로 다양한 지표를 사용하였다
직전시즌 팀평균을 이용하여 경기결과를 예측한 결과 
약 60~63%의 정확도를 가지는 모델을 얻을 수 있었다

----비고----------------------------------------------

              precision    recall  f1-score   support

        away       0.58      0.30      0.40      1168
        home       0.65      0.85      0.74      1755

    accuracy                           0.63      2923
   macro avg       0.61      0.58      0.57      2923
weighted avg       0.62      0.63      0.60      2923

--------------------------------------------------------
사용데이터:
BPM: 플레이어 기여도 공/수
VORP:대체선수대비 생산력 지표 야구의 WAR
WS:승리기여도 공/수

https://github.com/namwon94/Project_Baseball

https://www.basketballreference.com/leagues/NBA_2019_advanced.html#advanced_stats::ws - winshare

http://insider.espn.com/nba/hollinger/statistics - per

https://stats.nba.com/teams/advanced/?sort=OFF_RATING&dir=-1 - offrtg/defrtg