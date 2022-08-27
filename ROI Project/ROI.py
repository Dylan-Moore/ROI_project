class ROI_investment():
    def __init__(self):
        self.income = 0
        self.expense = 0
        self.cash_flow = 0
        self.ROI = 0
        self.total_invest = 0

    def find_income(self, rent_q = 0, laundry_q = 0, storage_q = 0):
        while True:
            income_question = input("What are your methods of income for this property? \n [1]Rent \n [2]Laundry \n [3]Storage \n [q]to quit ")
            if income_question == "1":
                rent_q = input("How much do you plan on making monthly from this property? ")
                self.income = int(rent_q)
            elif income_question == "2":
                laundry_q = input("How much do you plan to make monthly from laundry? ")
                self.income = int(rent_q) + int(laundry_q)
            elif income_question == "3":
                storage_q = input("How much do you plan to make monthly from storage? ")
                self.income = int(rent_q) + int(laundry_q) + int(storage_q)
            elif income_question == "q":
                print(self.income)
                self.find_expenses()
                
    def find_expenses(self, taxes = 0, insurance = 0, utilities = 0, Home_A = 0, vacancy = 0, repairs = 0, mortgage = 0):
        while True:
            expense_question = input("What are your monthly expenses? [1]Taxes \n [2]Insurance \n [3]Utilities \n [4]HOA \n [5]Vacancy \n [6]repairs \n [7]mortgage ")
            if expense_question == "1":
                taxes = input("How much are your monthly taxes? ")
                self.expense = int(taxes)
            elif expense_question == "2":
                insurance = input("How much is your monthly insurance? ")
                self.expense = int(taxes) + int(insurance)
            elif expense_question == "3":
                utilities = input("How much are your monthly utilities? ")
                self.expense = int(taxes) + int(insurance) + int(utilities)
            elif expense_question == "4":
                Home_A = input("What is your monthly HOA payment? ")
                self.expense = int(taxes) + int(insurance) + int(utilities) + int(Home_A)
            elif expense_question == "5":
                vacancy = input("How much would you like to put aside for vacancy? ")
                self.expense = int(taxes) + int(insurance) + int(utilities) + int(Home_A) + int(vacancy)
            elif expense_question == "6":
                repairs = input("How much are your monthly repairs? ")
                self.expense = int(taxes) + int(insurance) + int(utilities) + int(Home_A) + int(vacancy) + int(repairs)
            elif expense_question == "7":
                mortgage = input("How much is your monthly mortgage?")
                self.expense = int(taxes) + int(insurance) + int(utilities) + int(Home_A) + int(vacancy) + int(repairs) + int(mortgage)
            elif expense_question == "q":
                print(self.expense)
                self.cash_flw()
    def cash_flw(self):
        self.cash_flow = self.income - self.expense
        print(self.cash_flow)
        self.Return_invest()
    def Return_invest(self, downpayment = 0, closing_cost = 0, repair = 0):
        Annual_c_f = self.cash_flow * 12
        print(Annual_c_f)
        while True:
            investment_q = input("What have you invested into this property? [1]Down Payment [2]Closing Costs [3]Initial Repair/Rehab [q]")
            if investment_q == "1":
                downpayment = input("What was your downpayment? ")
                self.total_invest = int(downpayment)
            elif investment_q == "2":
                closing_cost = input("How much was your closing costs? ")
                self.total_invest = int(downpayment) + int(closing_cost)
            elif investment_q == "3":
                repair = input("How much did it cost to repair? ")
                self.total_invest = int(downpayment) + int(closing_cost) + int(repair)
            elif investment_q == "q":
                self.ROI = (Annual_c_f / self.total_invest) * 100
                check_data = input(f"Your income is: {self.income} \nYour expenses are: {self.expense} \nYour cash flow is: {self.cash_flow} \nYour investment is: {self.total_invest}, is this correct? ")
                if check_data == "yes":
                    print(f"Your ROI is {self.ROI}%")
                    run()
                elif check_data == "no":
                    wrong_data = input("Which number seems incorrect? ")
                    if wrong_data.title() == "Income":
                        self.find_income()
                    elif wrong_data.title() == "Expenses":
                        self.find_expenses()
                    elif wrong_data.title() == "Investment":
                        self.Return_invest()

prop = ROI_investment()
def run():
    property_q = input("Do you have a property you would like to get the ROI on? ")
    if property_q == "yes":
        prop.find_income()
    elif property_q == "2":
        print("Have a nice day!")
        run()
    #     prop.find_expenses()
    # elif property_q == "3":
    #     prop.cash_flw()
    # elif property_q == "4":
    #     prop.ROI()
    else:
        print("Please enter a valid option")
        run()

run()
            