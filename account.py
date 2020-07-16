class BankAccount:
  bank="KCB"
  
  def __init__(self, first_name, second_name):
    self.first_name=first_name
    self.second_name=second_name
    self.balance=0
    
  def account_name(self):
    name= "{} account for {} {} ".format(self.bank, self.first_name,self.second_name)
    return name
  def deposit(self,amount):
    if amount >0:
      
      self.balance+=amount
      print("You have deposited {} to your account".format(amount))
    else:
      print("Too low ")
  
  
  def withdraw(self, amount):
    if amount > 0:
      self.balance -= amount
      print("You have withdrawed {} from your account".format(amount))
    else:
      print("Amount too low")
  def get_balance(self):
    return "The balance of {} is {} ".format(self.account_name(),self.balance)
    
    
acc1=BankAccount("Rachel","Oyugi")
acc2=BankAccount("Buyole", "Isacko")

acc1.deposit(-1000)
acc2.deposit(50)
acc1.deposit(100)
acc2.deposit(30)
acc1.withdraw(10)
acc2.withdraw(30)
acc1.withdraw(20)
acc2.withdraw(10)
print(acc1.get_balance())
print(acc2.get_balance())

print(acc1.account_name())
print(acc2.account_name())
