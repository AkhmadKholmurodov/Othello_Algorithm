# Othello_Algorithm
Algorithm of Othello Game

I use Python Language for this Algorithm

이 코드에서는 Pandas를 사용하여 "othello_dataset.csv" 파일을 읽었다.​

NumPy의 vstack 함수를 사용하여 행렬을 수직으로 쌓아올리는 등의 연산이 코드에 활용되었다.​

Othello_dataset.csv 파일 안에 모든 움직임(move)들이 있다.​
Initial_board는 시작작화면의 board를 의미한다

1. who`는  세 가지 결과를 나타낸다. 'no winner = Draw', '검은 돌이 이길 때 = Black', '흰 돌이 이길 때 = White'​
2. marker는 각각의의 위치​
3. Training_value는  게임임할때 training 하는 value를 정의한다​
4.  letter_conv는 위치를 글자로 표현​
5. Increments는 보드드에서 한 위치에서 이동할때 사용하고 상하좌우 및 대각선 방향으로 이동.

- `a1Num` 및 `a1Rc`  -  게임 보드의 위치를 계산하는 데 사용.​

- `txtTraining` -  보드 상태를 적절한 숫자 값으로 변환하여 표시하는 데 사용. ​
             예:   `+` (검은 돌), `-` (흰 돌), 및 `0` (빈 공간)을 각각 `1.0`, `0.0`, 및 `0.5`로 변환한다.​
- chk  - (Check) 보드 안의 index  위치를 확인한다, 보드 안에 없으면 99 줄력​
- upd - (Update) mv하고 conv_log 실행행된때마다 Update 된다​

  - `mv` 함수는 게임에서 움직임을때 사용.​

- `conv_winner` 함수는 "Winner" 열을 해석하여 게임의 승자를 나타낸다. 0은 무승부, 1은 검은 돌, -1은 흰 돌입니다.​

- `conv_log` 함수는 게임 움직임 기록을 해석한다.

- historic_game_data  - 전의 게임할때 데이터를 저장한다​

- winning_moves_list - Winnng 움직임의 데이터 값들을 존재한다​
​
​
- training_df -  winning_moves_list에서 얻은 정보를 정리하고 저장하기 위해 만들어진 Pandas DataFrame​
-black_feature_board는 'Black' 플레이어의 이기는 이동에 대한 특징을 저장하는 NumPy 배열​
- white_label_move는 'White' 플레이어의 이긴 이동에 대한 라벨을 저장하는 NumPy 배열
- 
this is A final result of the Algorithm
![unknown](https://github.com/AkhmadKholmurodov/Othello_Algorithm/assets/87185085/4db62533-04ff-45fd-a04d-54aba3ffffab)

