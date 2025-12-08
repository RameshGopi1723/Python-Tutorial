# ================================================================================================
# PUBLIC VARIABLES
# ================================================================================================

class PublicVariableExample:
    """Demonstrates public variables - accessible anywhere."""
    def __init__(self):
        self.public_variable = "I am Public"


def demo_public():
    obj = PublicVariableExample()
    print(f"✓ Public: {obj.public_variable}")


# ================================================================================================
# PROTECTED VARIABLES
# ================================================================================================

class ProtectedVariableExample:
    """Demonstrates protected variables - accessible in class and subclasses."""
    def __init__(self):
        self._protected_variable = "I am Protected"

    def show_protected(self):
        return self._protected_variable


def demo_protected():
    obj = ProtectedVariableExample()
    print(f"✓ Protected (via method): {obj.show_protected()}")
    print(f"✓ Protected (direct access): {obj._protected_variable}  [Not recommended]")


# ================================================================================================
# PRIVATE VARIABLES
# ================================================================================================

class PrivateVariableExample:
    """Demonstrates private variables - accessible only within the class."""
    def __init__(self):
        self.__private_var = "I am Private"

    def show_private(self):
        return self.__private_var
    
    def __private_method(self):
        """Private method - only accessible within class."""
        return "This is a private method"
    
    def access_private_method(self):
        """Public method to access private method."""
        return self.__private_var + " and " + self.__private_method()


def demo_private():
    obj = PrivateVariableExample()
    print(f"✓ Private (via method): {obj.show_private()}")
    print(f"✓ Private method (via public method): {obj.access_private_method()}")
    # print(obj.__private_var)  # ✗ AttributeError


# ================================================================================================
# REAL-WORLD EXAMPLE: BANK ACCOUNT
# ================================================================================================

class BankAccount:
    """Real-world example using private variables for security."""
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        return self.__balance
    
    def get_account_number(self):
        return self.__account_number


def demo_bank_account():
    account = BankAccount("12345", 1000)
    print(f"✓ Initial balance: ${account.get_balance()}")
    
    account.deposit(500)
    print(f"✓ After deposit: ${account.get_balance()}")
    
    account.withdraw(200)
    print(f"✓ After withdrawal: ${account.get_balance()}")
    
    # Try direct access (will fail silently)
    try:
        account.__balance += 500  # ✗ AttributeError
    except AttributeError:
        print("✗ Direct access to private variable blocked!")


# ================================================================================================
# RUN ALL DEMOS
# ================================================================================================

if __name__ == "__main__":
    print("\n\n🔓 PUBLIC VARIABLES")
    demo_public()
    
    print("\n\n🔒 PROTECTED VARIABLES")
    demo_protected()
    
    print("\n\n🔐 PRIVATE VARIABLES")
    demo_private()
    
    print("\n\n💰 BANK ACCOUNT EXAMPLE")
    demo_bank_account()