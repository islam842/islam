class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance



    def __str__(self):
        return f"name is:{self._name}\n" \
               f"balance:{self._balance}\n" \
               f""

    def moneyX(self):
        money_add = int(input("Enter money add: "))
        self._balance += money_add
        print("\n"
              "Replenishment in your balace by:", money_add)


    def _kill(self):
        self._balance = 0
        print("\n"
              "Your balance has been reset.")

    def __jackpot(self):
        self._balance *= 10
        print(f"\n"
              f"Your balance has multiplied by 10: {self._balance}")

    def _merge_balance(self, other):
        self._balance += other._balance
        other._balance = 0
        print("\nThe balance of", other._name, "has been transferred to", self._name)
        print("The new balance of", self._name, "is", self._balance)

islam = Bank("Islam", 100)
islam.moneyX()
print(islam)

aidar = Bank("Aidar", 100)
aidar._kill()
print(aidar)


sultan = Bank("Sultan", 100)
sultan._Bank__jackpot()
print(sultan)


bekbolot = Bank("Bekbolot", 100)
turat = Bank("Turat", 100)
print(turat)


bekbolot._merge_balance(turat)
print(bekbolot)
