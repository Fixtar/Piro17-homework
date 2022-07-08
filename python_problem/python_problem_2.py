#함수 이름은 변경 가능합니다.

##############  menu 1
from posixpath import split
from re import T

students = [];

class student:
    def __init__(self, name, mid, final, grade):
        self.name = name;
        self.mid = mid;
        self.final = final;
        self.grade = grade;
    
    def setgrade(self):
        grade = (self.mid  + self.final)/2;
        if grade >= 90:
            self.grade = 'A';
        elif grade >= 80:
            self.grade = 'B';
        elif grade >= 70:
            self.grade = 'C';
        else:
            self.grade = 'D';

def Menu1(a,b,c) :
    students.append(student(a,b,c,0));
    #사전에 학생 정보 저장하는 코딩 

##############  menu 2
def Menu2() :
    for i in range(len(students)):
        if students[i].grade == 0:
            students[i].setgrade();
    #학점 부여 하는 코딩

##############  menu 3
def Menu3() :
    print("--------------------")
    print("name  mid  final grade")
    print("--------------------")
    for i in range(len(students)):
        print(students[i].name, students[i].mid, students[i].final, students[i].grade);
    #출력 코딩

##############  menu 4
def Menu4(i):
    del students[i];
    #학생 정보 삭제하는 코딩

#학생 정보를 저장할 변수 초기화
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        try:
            a,b,c = input('Enter name mid-score final-score :').split();
        except ValueError:
            print('Num of data is not 3!');
        else:
            flag = 0;
            for i in range(len(students)):
                if students[i].name == a:
                    flag = 1;
                    break;
            if flag == 1:
                print('Already exist name!');
            else:
                try:
                    mid = int(b);
                    final = int(c);
                except ValueError:
                    print('Score is not positive integer!');
                else:
                    if mid < 0 or final < 0:
                        print('Score is not positive integer!');
                    else:
                        Menu1(a,mid,final);

        #학생 정보 입력받기
        #예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
        #예외사항이 아닌 입력인 경우 1번 함수 호출 

    elif choice == "2" :
        if len(students) == 0 :
            print('No student data!');
        else:
            Menu2();
            print('Grading to all students.');
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우 2번 함수 호출
        #"Grading to all students." 출력

    elif choice == "3" :
        if len(students) == 0 :
            print('No student data!');
        else :
            for i in range(len(students)):
                if students[i].grade == 0:
                    print("There is a student who didn't get grade.")
                    break;
                if i == len(students)-1:
                    Menu3();
           
        #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        #예외사항이 아닌 경우 3번 함수 호출

    elif choice == "4" :
        if len(students) == 0 :
            print('No student data!');
        else:
            delname = input('Enter the name to delete : ');
            for i in range(len(students)):
                if students[i].name == delname:
                    Menu4(i);
                    print(delname,'student information is deleted.');
                    break;
                if i == len(students)-1:
                    print('Not exist name!');
        
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력

    elif choice == "5" :
        print("Exit Program!");
        exit();
        #프로그램 종료 메세지 출력
        #반복문 종료

    else :
        print("Wrong number. Choose again.");
        #"Wrong number. Choose again." 출력d