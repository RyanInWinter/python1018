# BankAccount.py

#파이썬은 개인적으로 사용 : AI, 데이터 사이언스, 분석
#팀단위로 작업할 경우 : 멤버를 숨김
#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        #모든 멤버 변수가 public -> 이름을 숨겨야 보안이 좋아짐
        #이름을 어떻게 숨기냐? -> '__'
        
        #self.id = id
        #self.name = name 
        #self.balance = balance 
        
        self.__id = id
        self.__name = name 
        self.__balance = balance         
    def deposit(self, amount):
        #self.balance += amount 
        self.__balance += amount 
    def withdraw(self, amount):
        #self.balance -= amount
        self.__balance -= amount
    
    # 문자열로 결과를 출력
    def __str__(self):
#        return "{0} , {1} , {2}".format(self.id, \
#            self.name, self.balance)
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.withdraw(3000)
print(account1)

# print(account1.__balance) # 실행되지 않음
print(account1._BankAccount__balance) # 백도어용 이름으로 변경
