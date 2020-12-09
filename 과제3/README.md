  # 미션3 - 루빅스 큐브 구현하기 수행

  ## 요구사항 구현 리스트
    
  - 루빅스 큐브 값 초기화와 명령어 수행을 횟수를 기억하는 기능 구현

    - 루빅스 큐브의 클래스 선언
    - 생성자안에 Cube의 초기값과 Command_Count값 선언
    
    - 큐브의 윗면 파란색 , 큐브의 아랫면 빨간색 , 큐브의 앞면 오렌지색 , 큐브의 뒷면 노란색 , 큐브의 왼쪽면 흰색 , 큐브의 오른쪽면 초록색 (큐브의 초기상태 전개도와 동일)




  - 루빅스 큐브 전개도를 출력 해주는 기능 구현
   
    - 큐브 한쪽면의 위쪽만 출력해주는 기능     Print_Cube_Upper
    - 큐브 한쪽면의 아래쪽 만 출력해주는 기능   Print_Cube_Lower
    - 큐브 한쪽면의 가운데 만 출력해주는 기능   Print_Cube_Center
  
  
    - 큐브 전개도 전체에서 가운데 부분만을 출력해주는 기능 (흰색,오렌지색,초록색,노란색) Print_Total_Cube_Center
    - 큐브 전개도 전체에서 맨 위부분만 출력해주는 기능 (파란색) Print_Total_Cube_Upper 
    - 큐브의 전개도에서 맨 아래부분을 출력해주는 기능 (빨간색) Print_Total_Cube_Lower
    
    
    - 큐브의 전개도 전체를 한번에 출력해주는 기능 Print_Total_Cube
    
     
  - 루빅스 큐브를 돌려주는 기능 구현
    
    - 루빅스 큐브의 한쪽 큐브면을 시계 방향으로 돌려주는  Clock_Wise 함수
    - 루빅스 큐브의 한쪽 큐브면을 반시계 방향으로 돌려주는 AntiClock_Wise 함수
    
    - 루빅스 큐브의 윗면을 시계 방향으로 돌려주는   Upper_Rotate_Clock 함수
    - 루빅스 큐브의 윗면을 반시계 방향으로 돌려주는  Upper_Rotate_Anti_ClockWise 함수
    
    - 루빅스 큐브의 아랫면을 시계 방향으로 돌려주는    Lower_Rotate_ClockWise 함수
    - 루빅스 큐브의 아랫면을 반시계 방향으로 돌려주는   Lower_Rotate_Anti_ClockWise 함수
    
    
