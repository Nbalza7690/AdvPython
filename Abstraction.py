from abc import ABC, abstractmethod


class house(ABC):

    def ReqPmnt(self, amount):
        print("Total payment amount: ", amount)

    @abstractmethod
    def payment(self, amount):
        pass


class PaymentMethod(house):

    def payment(self, amount):
        print("Your payment amount of '{}' has been confirmed.".format(amount))


obj = PaymentMethod()
obj.ReqPmnt("$1,200")
obj.payment("$1,200")
