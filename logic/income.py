from datetime import datetime

class Income():
    def __init__(self, amount, date = 'None', category = 'None', description = 'None'):
        if amount <= 0:
            raise ValueError('Amount must be greater than 0')
        self._amount = amount
        self._date = date
        self._category = category
        self._description = description

    def _parse_date(self, date):
        if isinstance(date, str) and date != 'None':
            return datetime.strptime(date, '%Y-%m-%d').date()
        else:
            return datetime.today().date()
    
    @property
    def amount(self): return self._amount
    
    @property
    def date(self): return self._date
    
    @property
    def category(self): return self._category

    @property
    def description(self): return self._description
    
    @amount.setter
    def amount(self, new_amount): 
        if new_amount <= 0:
            raise ValueError('Amount must be greater than 0')
        self._amount = new_amount

    @date.setter
    def date(self, new_date): self._date = self._parse_date(new_date)

    @category.setter
    def category(self, new_category): self._category = new_category

    @description.setter
    def description(self, new_description): self._description = new_description

    def to_dict(self):
        return {
            'amount': self._amount,
            'date': self._date,
            'category': self._category,
            'description': self._description
        }

    def __str__(self):
        return f'Income(amount={self._amount}, date={self._date}, category={self._category}, description={self._description})'