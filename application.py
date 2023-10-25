import random

'''
Class detailing object self and its information from
it's code identification, name, sales cost, manufacturing costs,
stock price, and monthly selfion quantity in order.
'''
class Product:
    def __init__(self):
        #code: int, name: str, sale: float, manufacture: float, stock: int, monthly: int
        self.__code = True                  #int from 100-1000
        self.__name = True                  #string
        self.__sale = True                  #num > 0
        self.__manufacture = True           #num > 0
        self.__stock = True                #stock > 0
        self.__monthly = True            #int >= 0

    #Getters for attributes.
    def getCode(self):
        return self.__code
    def getName(self):
        return self.__name
    def getSale(self):
        return self.__sale
    def getManufacture(self):
        return self.__manufacture
    def getStock(self):
        return self.__stock
    def getMonthly(self):
        return self.__monthly

    #Setters for attributes.
    def setCode(self, code):
        print("set actually works?")
        #Accepts value only if it's an integer from 100 to 1000.
        self.__code = int(code)if code.isdigit() and int(code) in range(100, 1001) else None
        if self.__code == None:
            new_code = input("Invalid product code value inputted, please enter an integer from 100 to 1000.\n")    
            self.setCode(new_code)

    def setName(self, name):
        print("set actually works?")
        self.__name = name if isinstance(name, str) else None
        if self.__sale == None:
            new_name = input("Invalid product value inputted, please enter an actual string.\n")
            self.setName(new_name)
        
    def setSale(self, sale):
        print("set actually works?")
        #Accepts value only if it's a positive number.
        try:
            if float(sale) > 0:
                self.__sale = float(sale)
            else:
                new_sale = input("Invalid manufacture cost value inputted, please enter a positive number.\n")
                self.setSale(new_sale)
                
        except ValueError:
            new_sale = input("Invalid manufacture cost value inputted, please enter a positive number.\n")
            self.setSale(new_sale)



    def setManufacture(self, manufacture):
        print("set actually works?")
        #Accepts value only if it's a positive number.
        try:
            if float(manufacture) > 0:
                self.__manufacture = float(manufacture)
            else:
                new_manufature = input("Invalid manufacture cost value inputted, please enter a positive number.\n")
                self.setManufacture(new_manufature)
        except ValueError:
            print("Invalid manufacture cost value inputted, please enter a positive number.\n")
            new_manufature = input("Invalid manufacture cost value inputted, please enter a positive number.\n")
            self.setManufacture(new_manufature)


    def setStock(self, stock):
        print("set actually works?")
        #Accepts value only if it's an integer larger than 0.
        self.__stock = int(stock) if stock.isdigit() and int(stock) > 0 else None
        if self.__stock == None:
            new_stock = input("Invalid stock level value inputted, please enter a positive integer.\n")
            self.setStock(new_stock)

    def setMonthly(self, monthly):
        print("set actually works?")
        #Accepts value only if it's an integer larger than 0.
        self.__monthly = int(monthly) if monthly.isdigit() and int(monthly) > 0 else None
        if self.__monthly == None:
            new_monthly = input("Invalid monthly unit/s value inputted, please enter a positive integer.\n")
            self.setMonthly(new_monthly)

    def renew_information(self):
        print("welcome to Programming Principles Sample Product Inventory.")
        setters_list = [self.setCode, self.setName, self.setSale, self.setManufacture, self.setStock, self.setMonthly]
        getters_list = [self.getCode(), self.getName(), self.getSale(), self.getManufacture(), self.getStock(), self.getMonthly()]
        stock = self.getStock()


        #Input for attributes.
        code_input = input("Please enter the Product's code: ")
        self.setCode(code_input)
    
        name_input = input("Please enter the Product's name: ")
        self.setName(name_input)

        sale_input = input("Please enter the Product's sale price: ")
        self.setSale(sale_input)
        
        manufacturing_input = input("Please enter the Product's manufacturing cost: ")
        self.setManufacture(manufacturing_input)

        stock_input = input("Please enter the Product's stock amount: ")
        self.setStock(stock_input)

        monthly_input = input("Please enter the Product's monthly manufacturing amount: ")
        self.setMonthly(monthly_input)
        summary_message = f"""

        ******Programming Principles Sample Stock Statement******
        Product Code: {self.getCode()}\n 
        Product Name: {self.getName()}\n 
        \n 
        Sale Price: {self.getSale()}\n 
        Manufacture Cost: {self.getManufacture()}\n 
        Stock Quantity: {self.getStock()}\n 
        Monthly Production {self.getMonthly()}\n 
        """



        for month in range(12):
            monthly_sale = self.getMonthly() + random.randint(-10, 10)
            stock =+ monthly_sale - self.getManufacture()
            #(Total Units Sold * Sale Price) - (Total Units Manufactured * Manufacture Cost).
            performance_message = f"""
            Month: {monthly_sale}\n
            \t  Manufactured: {self.getManufacture}
            \t  Sold: {monthly_sale}
            \t  Stock: {stock - monthly_sale}
            """
            print(performance_message)
        print(f"Net Profit:")
                
            
        


#filler information
product_one = Product()
#predicted stock statement hypothetical implementation

product_one.renew_information()
