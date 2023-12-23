import uuid
from datetime import datetime, timezone
class expense:
    def __init__(self, title, amount):
        self.id = str(uuid.uuid4())  # Generating a unique identifier
        self.title = title
        self.amount = amount
        self.created_at = datetime.utcnow()  # Timestamp when the expense was created
        self.updated_at = self.created_at  # Initially set to the creation time

    def update(self, title=None, amount=None):
        # Update title, amount and the updated_at timestamp
        if title:
            self.title = title
        if amount:
            self.amount = amount
        self.updated_at = datetime.utcnow()  # Update the timestamp
    
    def to_dict(self):
        # Return a dictionary representation of the expense
        return {
            'id': self.id,
            'title': self.title,
            'amount': self.amount,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
    
class ExpenseDB:
    def __init__(self):
        self.expenses = []  # Initialize the list to store Expense instances
    
    def add_expense(self, expense):
        # Add an expense to the list
        self.expenses.append(expense)
    
    def remove_expense(self, expense_id):
        # Remove an expense by ID if it exists
        for expense in self.expenses:
            if expense.id == expense_id:
                self.expenses.remove(expense)
                break
    
    def get_expense_by_id(self, expense_id):
        # Retrieve an expense by ID
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None  # Return None if expense with the specified ID is not found
    
    def get_expense_by_title(self, title):
        # Retrieve expenses by title
        return [expense for expense in self.expenses if expense.title == title]
    
    def to_dict(self):
        # Return a list of dictionaries representing expenses
        return [expense.to_dict() for expense in self.expenses]
