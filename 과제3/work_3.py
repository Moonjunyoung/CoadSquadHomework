def List_to_CorrectCommandlist(Command_list): # 들어오는 명령어를 올바른 명령어로 바꾸어주는 함수
    Command_List_Index = 0
    Change_Command_list=[]
    while Command_List_Index < len(Command_list):
        if Command_list[Command_List_Index] == "'": # 1. ' 이 들어온경우 
            Change_Command_list[-1] += "'"
        elif len(Change_Command_list)!=0 and str(Change_Command_list[-1]).isnumeric(): #2. 숫자인경우
             for i in range(int(Change_Command_list.pop())):
                 Change_Command_list.append(Command_list[Command_List_Index])
        else:
            Change_Command_list.append(Command_list[Command_List_Index])

        Command_List_Index += 1

    return Change_Command_list


class Cube:
    def __init__(self):
        self.cube = [[['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],  # 윗면 파란색  0
                     [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']],  # 아랫면 빨간색 1
                     [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']],  # 앞면 오렌지색  2
                     [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']],  # 뒷면 노란색 3
                     [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],  # 왼쪽면 흰색 4
                     [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']]]  # 오른쪽면 초록색 5
        self.Command_Count=0 # 명령어 횟수를 기록
    

    # 1. 루빅스 큐브의 전개도를 출력해주는 기능
    def Print_Cube_Upper(self,Cube_Number): #  현재 큐브의 맨 위쪽를 출력
        for j in range(3):
            print("".join(self.cube[Cube_Number][0][j]),end=' ')
    def Print_Cube_Lower(self,Cube_Number): #  현재 큐브의 맨 아래쪽를 출력
        for j in range(3):
            print("".join(self.cube[Cube_Number][2][j]),end=' ')
    def Print_Cube_Center(self,Cube_Number): # 현재 큐브의 가운데를 출력
        for j in range(3):
            print("".join(self.cube[Cube_Number][1][j]),end=' ')
    
    def Print_Total_Cube_Center(self): #  큐브의 전개도에서 가운데 부분을 출력 (흰색,오렌지색,초록색,노랑색)
        Center_Cube_Number=[4,2,5,3]
        for i in Center_Cube_Number:
            self.Print_Cube_Upper(i)
            print('\t\t\t',end='')
        print()
        for i in Center_Cube_Number:
            self.Print_Cube_Center(i)
            print('\t\t\t',end='')
        print()
        for i in Center_Cube_Number:
            self.Print_Cube_Lower(i)
            print('\t\t\t',end='')

    def Print_Total_Cube_Upper(self): # 큐브의 전개도에서 맨 위 부분을 출력 (파란색)
        print('\t'*6, end='')
        self.Print_Cube_Upper(0)
        print()
        print('\t'*6, end='')
        self.Print_Cube_Center(0)
        print()
        print('\t'*6, end='')
        self.Print_Cube_Lower(0)

    def Print_Total_Cube_Lower(self): # 큐브의 전개도에서 맨 아래부분을 출력 (빨간색)
        print('\t' * 6, end='')
        self.Print_Cube_Upper(1)
        print()
        print('\t' * 6, end='')
        self.Print_Cube_Center(1)
        print()
        print('\t' * 6, end='')
        self.Print_Cube_Lower(1)

    def Print_Total_Cube(self): ## 큐브의 전개도 전체를 출력 (큐브전체 출력)
        self.Print_Total_Cube_Upper()
        print()
        self.Print_Total_Cube_Center()
        print()
        self.Print_Total_Cube_Lower()
        print()
        print()


    # 2. 큐브면을 시계 방향 및 반시계방향으로 돌려주는 함수
    
    def Clock_Wise(self,cube):  # 2-1. 현재 큐브의 상태를 시계방향으로 돌려준다.
        Temp_Cube = [[0 for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                Temp_Cube[i][j] = cube[2 - j][i]
        return Temp_Cube
    
    def Anti_Clockwise(self,cube): # 2-2. 현재 큐브의 상태를 반시계 방향으로 돌려준다.
        Temp_Cube = [[0 for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                Temp_Cube[i][j] = cube[j][2 - i]
        return Temp_Cube


    # 3. U,U',L,L',R,R',F,F',D,D',B,B' 동작을 수행시키는 기능

    def Upper_Rotate_Clock(self): #  3-1-1 U 큐브 윗면 을 시계 방향으로 돌려준다
        cube=self.cube
        # 왼쪽면 맨위 = 앞면 맨위, 뒷면 맨위 = 왼쪽면 맨위 , 오른쪽면 맨위 = 뒷면 맨위 , 앞면 맨위 = 오른쪽면 맨위
        cube[4][0], cube[3][0], cube[5][0], cube[2][0] = cube[2][0], cube[4][0], cube[3][0], cube[5][0]
        # 윗면을 시계 방향으로 회전시킨다.
        cube[0]=self.Clock_Wise(cube[0])

    def Upper_Rotate_Anti_ClockWise(self): # 3-1-1 U' 큐브 윗면을 반시계 방향으로 돌려준다.
        cube=self.cube
        # 오른쪽면 맨위 = 앞면 맨위 , 뒷면 맨위 = 오른쪽면 맨위  , 왼쪽면 맨위 = 뒷면 맨위  , 앞면 맨위 = 왼쪽면 맨위
        cube[5][0], cube[3][0], cube[4][0], cube[2][0] = cube[2][0], cube[5][0], cube[3][0], cube[4][0]
        # 윗면을 반시계 방향으로 회전 시킨다.
        cube[0] = self.Anti_Clockwise(cube[0])

    def Lower_Rotate_ClockWise(self): # 3-2-1 D 큐브 아랫면을 시계방향으로 돌린다.
        # 오른쪽면 맨 아래 = 앞면 맨아래 , 뒷면 맨 아래 = 오른쪽면 맨아래 , 왼쪽면 맨 아래 = 뒷면 맨아래 , 앞면 맨아래 = 왼쪽면 맨아래
        cube=self.cube
        cube[5][2], cube[3][2], cube[4][2], cube[2][2] = cube[2][2], cube[5][2], cube[3][2], cube[4][2]
        cube[1] = self.Clock_Wise(cube[1]) #아랫면을 시계방향으로 돌린다

    def Lower_Rotate_Anti_ClockWise(self): # 3-2-1  D' 큐브 아랫면을 반시계 방향으로 돌린다.
        cube=self.cube
        # 왼쪽면 맨아래 = 앞면 맨아래 , 뒷면 맨아래 = 왼쪽면 맨 아래 , 오른쪽면 맨아래 = 뒷면 맨아래 , 앞면 맨아래 = 오른쪽면 맨아래
        cube[4][2], cube[3][2], cube[5][2], cube[2][2] = cube[2][2], cube[4][2], cube[3][2], cube[5][2]
        cube[1] = self.Anti_Clockwise(cube[1]) ##아랫면을 반시계 방향으로 돌림


    def Front_Rotate_ClockWise(self): #3-3-1 F 큐브의 앞면을 시계방향으로 돌린다
        cube=self.cube
        # 1. 왼쪽면 맨 끝에있는값
        LeftCube_Col_0_2,LeftCube_Col_1_2,LeftCube_Col_2_2 = cube[4][0][2], cube[4][1][2], cube[4][2][2]
        cube[4][0][2], cube[4][1][2], cube[4][2][2] = cube[1][0][0], cube[1][0][1], cube[1][0][2]
        # 2. 아랫면 맨위에있는값 =  오른쪽면 맨왼쪽에 있는값들
        cube[1][0][0], cube[1][0][1], cube[1][0][2] = cube[5][2][0], cube[5][1][0], cube[5][0][0]
        # 3. 오른쪽면 맨왼쪽값 = 윗면 아래쪽에 있는값
        cube[5][2][0], cube[5][1][0], cube[5][0][0] = cube[0][2][2], cube[0][2][1], cube[0][2][0]
        # 4. 윗면 아래쪽에있는값들 = 왼쪽면 맨 오른쪽에있는 값
        cube[0][2][2], cube[0][2][1], cube[0][2][0] = LeftCube_Col_0_2,LeftCube_Col_1_2,LeftCube_Col_2_2
        # 앞면을 시계방향으로 회전
        cube[2] = self.Clock_Wise(cube[2])

    def Front_Rotate_AntiClockWise(self): # 3-3-2  F' 큐브의 앞면을 반시계 방향으로 돌린다.
        cube=self.cube
        # 1. 왼쪽면 맨끝에 있는 값
        LeftCube_Col_0_2,LeftCube_Col_1_2,LeftCube_Col_2_2 = cube[4][0][2], cube[4][1][2], cube[4][2][2]
        cube[4][0][2], cube[4][1][2], cube[4][2][2] = cube[0][2][2], cube[0][2][1], cube[0][2][0]
        # 2. 윗면 아래쪽에 있는 값 = 오른쪽면 맨 왼쪽값들
        cube[0][2][2], cube[0][2][1], cube[0][2][0] = cube[5][2][0], cube[5][1][0], cube[5][0][0]
        # 3. 오른쪽면 맨 왼쪽 값들 = 아랫면 맨위 값
        cube[5][2][0], cube[5][1][0], cube[5][0][0] = cube[1][0][0], cube[1][0][1], cube[1][0][2]
        # 4. 아랫면 맨위 에있는 값 = 왼쪽면 맨 오른쪽에있는 값
        cube[1][0][0], cube[1][0][1], cube[1][0][2] = LeftCube_Col_0_2,LeftCube_Col_1_2,LeftCube_Col_2_2
        #반시계 방향으로 회전
        cube[2] = self.Anti_Clockwise(cube[2])
    
    def Back_Rotate_ClockWise(self): # 3-4-1 B 큐브의 뒷면을 시계 방향으로 돌린다.
        cube=self.cube
        LeftCube_col_0_0,LeftCube_col_1_0,LeftCube_col_2_0= cube[4][0][0], cube[4][1][0], cube[4][2][0]
        # 1. 왼쪽면 맨 왼쪽 값 = 윗면 맨 위쪽 값
        cube[4][0][0], cube[4][1][0], cube[4][2][0] = cube[0][0][2], cube[0][0][1], cube[0][0][0]
        # 2 . 윗면 맨 위쪽값들 = 오른쪽 면 맨 오른쪽 값
        cube[0][0][2], cube[0][0][1], cube[0][0][0] = cube[5][2][2], cube[5][1][2], cube[5][0][2]
        # 3. 오른쪽면 오른쪽 값 = 아랫면 맨 아래쪽값
        cube[5][2][2], cube[5][1][2], cube[5][0][2] = cube[1][2][0], cube[1][2][1], cube[1][2][2]
        # 4. 아랫면 맨 아래쪽값들 = 왼쪽면 맨 왼쪽값
        cube[1][2][0], cube[1][2][1], cube[1][2][2] = LeftCube_col_0_0,LeftCube_col_1_0,LeftCube_col_2_0
        cube[3] = self.Clock_Wise(cube[3])

    def Back_Rotate_AntiClockWise(self): # 3-4-2 B' 큐브의 뒷면을 반시계 방향으로 돌린다.
        cube=self.cube
        LeftCube_col_0_0, LeftCube_col_1_0, LeftCube_col_2_0= cube[4][0][0], cube[4][1][0], cube[4][2][0]
        # 1. 왼쪽면 맨 왼쪽값 = 아랫면 맨아래값
        cube[4][0][0], cube[4][1][0], cube[4][2][0] = cube[1][2][0], cube[1][2][1], cube[1][2][2]
        # 2. 아랫면 맨 아래 쪽 값 = 오른쪽면 맨 오른쪽 값
        cube[1][2][0], cube[1][2][1], cube[1][2][2] = cube[5][2][2], cube[5][1][2], cube[5][0][2]
        # 3. 오른쪽면 맨 오른쪽 값 = 윗면 맨 위쪽 값들
        cube[5][2][2], cube[5][1][2], cube[5][0][2] = cube[0][0][2], cube[0][0][1], cube[0][0][0]
        # 4. 윗면 맨 위쪽 값 = 왼쪽면 맨 왼쪽값들
        cube[0][0][2], cube[0][0][1], cube[0][0][0] = LeftCube_col_0_0,LeftCube_col_1_0,LeftCube_col_2_0
        cube[3] = self.Anti_Clockwise(cube[3])

    def Left_Rotate_ClockWise(self): # 3-5-1 L 큐브의 왼쪽면을 시계 방향으로 돌린다.
        cube=self.cube
        # 1. 윗면 맨 왼쪽 값 = 뒷면 맨 오른쪽 값
        Upper_Cube_col_0_0,Upper_Cube_col_1_0,Upper_Cube_col_2_0 = cube[0][0][0], cube[0][1][0], cube[0][2][0]
        cube[0][0][0], cube[0][1][0], cube[0][2][0] = cube[3][2][2], cube[3][1][2], cube[3][0][2]
        # 2. 뒷면 맨 왼쪽 값 = 아랫면 맨 왼쪽값
        cube[3][2][2], cube[3][1][2], cube[3][0][2] = cube[1][0][0], cube[1][1][0], cube[1][2][0]
        # 3. 아랫면 맨 왼쪽값 = 앞면 맨 왼쪽 값
        cube[1][0][0], cube[1][1][0], cube[1][2][0] = cube[2][0][0], cube[2][1][0], cube[2][2][0]
        # 4. 앞면 맨 왼쪽값 = 윗면 맨 왼쪽 값
        cube[2][0][0], cube[2][1][0], cube[2][2][0] = Upper_Cube_col_0_0,Upper_Cube_col_1_0,Upper_Cube_col_2_0
        cube[4] = self.Clock_Wise(cube[4])
    
    def Left_Rotate_AntiClockWise(self): # 3-5-2 L' 큐브의 왼쪽면을 반시계방향으로 돌린다.
        cube=self.cube
        Upper_Cube_col_0_0, Upper_Cube_col_1_0, Upper_Cube_col_2_0 = cube[0][0][0], cube[0][1][0], cube[0][2][0]
        # 1. 윗면 맨 왼쪽 값 = 앞면 맨 왼쪽값
        cube[0][0][0], cube[0][1][0], cube[0][2][0] = cube[2][0][0], cube[2][1][0], cube[2][2][0]
        # 2. 앞면 맨 왼쪽값 = 아랫면 맨 왼쪽값
        cube[2][0][0], cube[2][1][0], cube[2][2][0] = cube[1][0][0], cube[1][1][0], cube[1][2][0]
        # 3. 아랫면 맨 왼쪽값 = 뒷면 맨 오른쪽값
        cube[1][0][0], cube[1][1][0], cube[1][2][0] = cube[3][2][2], cube[3][1][2], cube[3][0][2]
        # 4. 뒷면 맨 오른쪽값 = 윗면 맨 왼쪽값
        cube[3][2][2], cube[3][1][2], cube[3][0][2] =Upper_Cube_col_0_0, Upper_Cube_col_1_0, Upper_Cube_col_2_0
        cube[4] = self.Anti_Clockwise(cube[4])

    def Right_Rotate_ClockWise(self): # 3-6-1 R  큐브의 오른쪽면을 시계방향으로 돌린다.
        cube=self.cube
        UpperCube_col_0_2,UpperCube_col_1_2,UpperCube_col_2_2 = cube[0][0][2], cube[0][1][2], cube[0][2][2]
        # 1. 윗면 맨 오른쪽 값 = 앞면 맨 오른쪽 값
        cube[0][0][2], cube[0][1][2], cube[0][2][2] = cube[2][0][2], cube[2][1][2], cube[2][2][2]
        # 2. 앞면 맨 오른쪽 값 = 아랫면 맨 오른쪽 값
        cube[2][0][2], cube[2][1][2], cube[2][2][2] = cube[1][0][2], cube[1][1][2], cube[1][2][2]
        # 3. 아랫면 맨 오른쪽 값 = 뒷면 맨왼쪽값
        cube[1][0][2], cube[1][1][2], cube[1][2][2] = cube[3][2][0], cube[3][1][0], cube[3][0][0]
        # 4. 뒷면 맨 왼쪽값 = 윗면 맨 오른쪽값
        cube[3][2][0], cube[3][1][0], cube[3][0][0] = UpperCube_col_0_2,UpperCube_col_1_2,UpperCube_col_2_2
        cube[5] = self.Clock_Wise(cube[5])

    def Right_Rotate_AntiClockWise(self): # 3-6-2 R' 큐브의 오른쪽면을 반시계방향으로 돌린다.
        cube=self.cube
        UpperCube_col_0_2, UpperCube_col_1_2, UpperCube_col_2_2 = cube[0][0][2], cube[0][1][2], cube[0][2][2]
        # 1. 윗면 맨 오른쪽 값 = 뒷면 맨 왼쪽값
        cube[0][0][2], cube[0][1][2], cube[0][2][2] = cube[3][2][0], cube[3][1][0], cube[3][0][0]
        # 2. 뒷면 맨 왼쪽값 = 아랫면 맨오른쪽값
        cube[3][2][0], cube[3][1][0], cube[3][0][0] = cube[1][0][2], cube[1][1][2], cube[1][2][2]
        # 3. 아랫면 맨 오른쪽 값 = 앞면 맨 오른쪽값
        cube[1][0][2], cube[1][1][2], cube[1][2][2] = cube[2][0][2], cube[2][1][2], cube[2][2][2]
        # 4. 앞면 맨 오른쪽값 = 윗면 맨 오른쪽값
        cube[2][0][2], cube[2][1][2], cube[2][2][2] = UpperCube_col_0_2,UpperCube_col_1_2,UpperCube_col_2_2
        cube[5] = self.Anti_Clockwise(cube[5])

class Cube_Game:
    def __init__(self,start_time):
       self.Start_Time=start_time # 큐브게임의 시작시간을 저장
       self.Command_Count=0 # 명령어 횟수를 기록




while True: # 들어오는 명령어에 따라 큐브를 돌려준다.
    Command_List = list(input("CUBE>").strip())
    Command_List = List_to_CorrectCommandlist(Command_List)
    for command in Command_List:
        if command == 'Q':
            exit(0)
        elif command== 'U':
             print('U')
             cube.Upper_Rotate_Clock()
        elif command== "U'":
             print("U'")
             cube.Upper_Rotate_Anti_ClockWise()
        elif command=='L':
             print('L')
             cube.Left_Rotate_ClockWise()
        elif command=="L'":
             print("L'")
             cube.Left_Rotate_AntiClockWise()
        elif command=='F':
             print('F')
             cube.Front_Rotate_ClockWise()
        elif command=="F'":
             print("F'")
             cube.Front_Rotate_AntiClockWise()
        elif command=="R":
             print('R')
             cube.Right_Rotate_ClockWise()
        elif command=="R'":
             print("R'")
             cube.Right_Rotate_AntiClockWise()
        elif command=='B':
            print('B')
            cube.Back_Rotate_ClockWise()
        elif command=="B'":
             print("B'")
             cube.Back_Rotate_AntiClockWise()
        elif command=='D':
             print('D')
             cube.Lower_Rotate_ClockWise()
        elif command=="D'":
             print("D'")
             cube.Lower_Rotate_Anti_ClockWise()
        else: #잘못된 명령어가 들어올시
            continue

        cube.Print_Total_Cube() # 큐브를 돌렸으니 현재 큐브를 출력
