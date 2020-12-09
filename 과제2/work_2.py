def List_to_CorrectCommandlist(command_list):
    idx = 0
    tmp=[]
    while idx < len(command_list):
        if command_list[idx] == "'":
            tmp[-1] += "'"
        else:
            tmp.append(command_list[idx])
        idx += 1
    return tmp

class Cube:
    def __init__(self):
        self.cube=[['R','R','W'],['G','C','W'],['G','B','B']] # 0. 3x3 초기큐브 값 설정

    def Set_Cube_Upper(self,upper_cube): # 1-1. upper_cube의값으로 최상단 큐브값 설정
        for i in range(len(upper_cube)):
            self.cube[0][i]=upper_cube[i]
    def Set_Cube_Lower(self,lower_cube): # 1-2. lower_cube의값으로 최하단 큐브값 설정
        for i in range(len(lower_cube)):
            self.cube[2][i]=lower_cube[i]
    def Set_Cube_Left(self, left_cube): # 1-3  left_cube의 값으로 맨 왼쪽 큐브값 설정
        for i in range(len(left_cube)):
            self.cube[i][0] = left_cube[i]
    def Set_Cube_Right(self,right_cube): # 1-4 right_cube의 값으로 맨 오른쪽 큐브값 설정
        for i in range(len(right_cube)):
            self.cube[i][2] = right_cube[i]

    def Get_Cube_Right(self): # 2-1.현재 맨 오른쪽의 큐브값을 가져온다
          tmp_list=[]
          for i in range(len(self.cube)):tmp_list.append(self.cube[i][2])
          return tmp_list

    def Get_Cube_Left(self): # 2-2. 현재 맨 왼쪽의 큐브값을 가져온다.
        tmp_list = []
        for i in range(len(self.cube)): tmp_list.append(self.cube[i][0])
        return tmp_list

    def Get_Cube_Upper(self): # 2-3. 현재 맨 위쪽의 큐브값을 가져온다.
        return self.cube[0]

    def Get_Cube_Lower(self): # 2-4. 현재 맨 아래의 큐브값을 가져온다.
        return self.cube[2]

    def Print(self): # 3.현재 큐브 상태를 출력하는 함수
        for i in range(3):
            for j in range(3):
                print(self.cube[i][j],end=' ')
            print()
        print()
