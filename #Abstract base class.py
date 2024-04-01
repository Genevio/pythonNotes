#Abstract base class

from abc import ABC, abstractmethod

class Bank(ABC):
    
    @abstractmethod
    def loan(self):pass
    
    @abstractmethod
    def credit(self):pass

    @abstractmethod
    def debit(self):pass

class SBi(Bank):
    def loan(self):
        print("we provide 8.5% as Loan Intest")

o=SBi()
o.loan()

