# Base class for Member
class Member:
    def __init__(self, customerId, customerName, emailId):
        self.customerId = customerId
        self.customerName = customerName
        self.emailId = emailId

# Derived class for GoldMember
class GoldMember(Member):
    def __init__(self, customerId, customerName, emailId, discountAmount=0):
        # Initialize the base class
        super().__init__(customerId, customerName, emailId)
        self.discountAmount = discountAmount

    def calculateDiscount(self, purchaseAmount):
        # Calculate 10% discount for Gold Members
        self.discountAmount = purchaseAmount - (purchaseAmount * 0.10)

# Derived class for DiamondMember
class DiamondMember(Member):
    def __init__(self, customerId, customerName, emailId, discountAmount=0):
        # Initialize the base class
        super().__init__(customerId, customerName, emailId)
        self.discountAmount = discountAmount

    def calculateBalance(self, purchaseAmount):
        # Calculate 20% discount for Diamond Members
        self.discountAmount = purchaseAmount - (purchaseAmount * 0.20)

# Main code to get input and display member details
def main():
    # Display membership options
    print("1.GoldMembership\n2.DiamondMembership")
    
    # Get the user's choice
    choice = int(input("Enter the choice\n"))
    
    # Get member details from the user
    customerId = input("Enter the Details:\nCustomer Id\n")
    customerName = input("Customer Name\n")
    emailId = input("EmailId\n")
    purchaseAmount = float(input("Enter the Purchase Amount\n"))
    
    if choice == 1:
        # Gold Membership
        g_account_obj = GoldMember(customerId, customerName, emailId)
        g_account_obj.calculateDiscount(purchaseAmount)
        print(f"Member Details\n{g_account_obj.customerId} {g_account_obj.customerName} {g_account_obj.emailId} {g_account_obj.discountAmount}")
    
    elif choice == 2:
        # Diamond Membership
        d_account_obj = DiamondMember(customerId, customerName, emailId)
        d_account_obj.calculateBalance(purchaseAmount)
        print(f"Member Details\n{d_account_obj.customerId} {d_account_obj.customerName} {d_account_obj.emailId} {d_account_obj.discountAmount}")
    
if __name__ == "__main__":
    main()
