from datetime import datetime
class BankAccount:
  bank="KCB"
  loan={}
  loan_balance=0
  applied_for_loan=False
  _maximum_loan_borrowable=3000000
  loan_interest_rate=.12
  deposits=[]
  withdraws=[]

  
  def __init__(self, first_name, second_name,phone_number):
    self.first_name=first_name
    self.second_name=second_name
    self.balance=0
    self.phone_number=phone_number
    

  def _getCurrentTime(self):
    now=datetime.now()
    now_formatted=now.strftime("%b %d %Y, %H:%M:%S")
    return now_formatted

  def account_name(self):
    name= "{} account for {} {} {}".format(self.bank, self.first_name,self.second_name, self.phone_number)
    return name
  def deposit(self,amount):
    if amount >0:
      
      self.balance+=amount
      timeDate=self._getCurrentTime()
      transaction_details={"amount":amount,"date":timeDate}
      self.deposits.append(transaction_details)
      print("You have deposited {} to your account at {}".format(amount,timeDate))
    else:
      print("Too low ")
  
  
  def withdraw(self, amount):
    if amount > 0:
      self.balance -= amount
      timeDate=self._getCurrentTime()
      transaction_details={"amount":amount,"date":timeDate}
      self.withdraws.append(transaction_details)
      print("You have withdrawed {} to your account at {}".format(amount,timeDate))
      #print("You have withdrawed {} from your account".format(amount))
    else:
      print("Amount too low")
  def get_balance(self):
    return "The balance of {} is {} ".format(self.account_name(),self.balance)
  def get_statement(self):
    for statement in self.deposits:
      print("On",statement['date'],", you deposited KES",statement['amount'])

  def getLoanBalance(self):
    print("Your balance is KES ", self.loan_balance,"for loan KES", self.loan["amount_borrowed"],"borrowed on",self.loan["date"])      
  def requestLoan(self,amount):
    if not self.loan_balance>0:
      timeDate=self._getCurrentTime()
      self.loan["date"]=timeDate
      self.loan["amount_borrowed"]=amount
      self.loan_balance+=amount
    else:
      print("Error:Loan Request failed Reason:",end="")
      print(self.getLoanBalance())

  def payLoan(self,amount):
    if self.loan_balance==0:
      print('you have no loan balance')
    elif amount>self.loan_balance:
      self.loan_balance=0
    elif amount<=self.loan_balance:
      self.loan_balance-=amount
    return       
acc1=BankAccount("Rachel","Oyugi",25497578566)
acc2=BankAccount("Buyole", "Isacko",254756784789)

acc1.deposit(-1000)
acc2.deposit(5000)
acc1.deposit(100)
acc2.deposit(30)
acc1.withdraw(10)
acc2.withdraw(30)
acc1.withdraw(20)
acc2.withdraw(10)
print(acc1.get_balance())
print(acc2.get_balance())
acc2.get_statement()
acc1.requestLoan(2000)
acc1.requestLoan(1000)
acc1.payLoan(200)
acc1.getLoanBalance()


print(acc1.account_name())
print(acc2.account_name())
