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


