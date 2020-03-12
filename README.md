# project_NBA_predict
미국 프로농구의 경기결과를 예측하는 프로젝트
농구의 PER과 WS를 필두로 다양한 지표를 사용하였다
직전시즌 팀평균을 이용하여 경기결과를 예측한 결과 
약 60~63%의 정확도를 가지는 모델을 얻을 수 있었다

----비고----------------------------------------------

              precision    recall  f1-score   support

        away       0.54      0.33      0.41      1142
        home       0.66      0.82      0.73      1781

    accuracy                           0.63      2923
   macro avg       0.60      0.58      0.57      2923
weighted avg       0.61      0.63      0.61      2923

--------------------------------------------------------

https://github.com/namwon94/Project_Baseball



https://www.basketballreference.com/leagues/NBA_2019_advanced.html#advanced_stats::ws - winshare

http://insider.espn.com/nba/hollinger/statistics - per

https://stats.nba.com/teams/advanced/?sort=OFF_RATING&dir=-1 - offrtg/defrtg