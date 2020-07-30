from datetime import datetime
class Account:
  #bank="KCB"
  loan={}
  loan_balance=0
  applied_for_loan=False
  _maximum_loan_borrowable=3000000
  loan_interest_rate=.12
  deposits=[]
  withdraws=[]
  repayments=[]
  
  

  
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
    name= "account for {} {} {}".format(self.first_name,self.second_name, self.phone_number)
    return name
  def deposit(self,amount):
    try:
      amount + 1
    except TypeError:
      print("You must enter the amount in figures")
      return
    if amount >0:
      
      self.balance+=amount
      timeDate=self._getCurrentTime()
      transaction_details={"amount":amount,"date":timeDate}
      self.deposits.append(transaction_details)
      print(" Dear {} ,You have deposited {} to your account at {} and your  new balance is {}" .format(self.first_name,amount,timeDate,self.balance))
    else:
      print("Too low ")
  
  
  def withdraw(self, amount):
    try:
      amount + 1
    except TypeError:
      print("You must enter the amount in figures")
      return
    if amount > 0:
      self.balance -= amount
      timeDate=self._getCurrentTime()
      transaction_details={"amount":amount,"date":timeDate}
      self.withdraws.append(transaction_details)
      print(" Dear {} ,You have withdrawed {} to your account at {} and your new balance is {}" .format(self.first_name,amount,timeDate,self.balance))
      #print("You have withdrawed {} from your account".format(amount))
    else:
      print("Amount too low")
  def get_balance(self):
    return "The balance of {} is {} ".format(self.account_name(),self.balance)
  def get_deposit_statement(self):
    for statement in self.deposits:
      print("On",statement['date'],", you deposited KES",statement['amount'])
  def get_withdraw_statement(self):
    for statement in self.withdraws:
      print("On",statement['date'],", you withdrew  KES",statement['amount'])


  def getLoanBalance(self):
    print("Your balance is KES ", self.loan_balance,"for loan KES", self.loan["amount_borrowed"],"borrowed on",self.loan["date"])      
  def requestLoan(self,amount):
    try:
      amount + 1
    except TypeError:
      print("You must enter the amount in figures")
      return
    if not self.loan_balance>0:
      timeDate=self._getCurrentTime()
      self.loan["date"]=timeDate
      self.loan["amount_borrowed"]=amount
      self.loan_balance+=amount
    else:
      print("Error:Loan Request failed Reason:",end="")
      print(self.getLoanBalance())

  def payLoan(self,amount):
    try:
      amount + 1
    except TypeError:
      print("You must enter the amount in figures")
      return
    if self.loan_balance==0:
      print('you have no loan balance')
    elif amount>self.loan_balance:
      self.loan_balance=0
    elif amount<=self.loan_balance:
      self.loan_balance-=amount
      timeDate=self._getCurrentTime()
      transaction_details={"amount":amount,"date":timeDate}
      self.repayments.append(transaction_details)
    return 


  def get_loan_statements(self):
    for statement in self.repayments:
      print("On",statement['date'],", you paid  KES",statement['amount'])


class BankAccount(Account):
  def __init__(self,first_name,second_name,phone_number,bank):
    self.bank=bank
    super().__init__(first_name,second_name,phone_number)


class MobileMoneyAccount(Account):
  def __init__(self,first_name,second_name,phone_number,service_provider):
    self.service_provider=service_provider
    self.airtime=[]
    self.bills=[]
    self.money=[]
    self.received=[]
    super().__init__(first_name,second_name,phone_number)


  def buy_airtime(self,amount):
    try:
      amount + 1
    except TypeError:
      print("You must enter the amount in figures")
      return
    if amount>self.balance:
      print("You dont have enough balance your balance is {}".format(self.balance))
    else:
      self.balance-=amount
      timeDate=self._getCurrentTime()
      transaction_details={"amount":amount,"date":timeDate}
      self.airtime.append(transaction_details)
      print("You have bought airtime worth {} on {}".format(amount,timeDate))


  def pay_bill(self,amount):
    try:
      amount + 1
    except TypeError:
      print("You must enter the amount in figures")
      return
    if amount>self.balance:
      print("You dont have enough balance your balance is {}".format(self.balance))
    else:
      self.balance-=amount
      timeDate=self._getCurrentTime()
      transaction_details={"amount":amount,"date":timeDate}
      self.bills.append(transaction_details)
      print("You have paid  {} on {} and your balance is {}".format(amount,timeDate,self.balance))
  
  def send_money(self,amount):
    try:
      amount + 1
    except TypeError:
      print("You must enter the amount in figures")
      return
    if amount>self.balance:
      print("You dont have enough balance your balance is {}".format(self.balance))
    else:
      self.balance-=amount
      timeDate=self._getCurrentTime()
      transaction_details={"amount":amount,"date":timeDate}
      self.money.append(transaction_details)
      print("You have sent  {} on {} and your balance is {}".format(amount,timeDate,self.balance))
  

  def receive_money(self,amount):
      timeDate=self._getCurrentTime()
      transaction_details={"amount":amount,"date":timeDate}
      self.received.append(transaction_details)
      print("You have received {} from  on {} and your balance is {}".format(amount,timeDate,self.balance))

  

  






acc1=Account("Rachel","Oyugi",25497578566)
acc2=Account("Buyole", "Isacko",254756784789)

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
acc2.get_deposit_statement()
acc2.get_withdraw_statement()
acc1.requestLoan(2000)
acc1.requestLoan(1000)
acc1.payLoan(200)
acc1.getLoanBalance()
acc1.get_loan_statements()



