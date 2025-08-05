class BankAccount():
    def __init__(self, account_id, account_name, balance = 0):
        self._account_name = account_name
        self._account_id = account_id
        self._balance = balance
        self._incomes = []
        self._expenses = []

    def add_expense(self, expense):
        self._expenses.append(expense)
        self._balance -= expense.amount

    def add_income(self, income):
        self._incomes.append(income)
        self._balance += income.amount

    def get_incomes(self): return self._incomes

    def get_expenses(self): return self._expenses

    @property
    def account_id(self): return self._account_id

    @property
    def account_name(self): return self._account_name
    
    @property
    def balance(self): return self._balance

    def to_dict(self):
        return {
            'account_name': self._account_name,
            'account_id': self._account_id,
            'balance': self._balance,
            'incomes': [i.to_dict() for i in self._incomes],
            'expenses': [i.to_dict() for i in self._expenses]
        }
    
    def __str__(self):
        return f'BankAccount(account_name={self._account_name}, account_id={self._account_id}, balance={self._balance}, incomes={len(self._incomes)}, expenses={len(self._expenses)})'
