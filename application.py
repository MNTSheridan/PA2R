import random

'''
Class detailing object self and its information from
it's code identification, name, sales cost, manufacturing costs,
stock price, and monthly selfion quantity in order.
'''
class Product:
    def __init__(self, code: int, name: str, sale: float, manufacture: float, stock: int, monthly: int):
        self.__code = code                  #int from 100-1000
        self.__name = name                  #string
        self.__sale = sale                  #num > 0
        self.__manufacture = manufacture    #num > 0
        self.__stock = stock                #stock > 0
        self.__monthly = monthly            #int >= 0

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
        #Accepts value only if it's an integer from 100 to 1000.
        self.__code = int(code) if code.isdigit() and int(code) in range(100, 1001) else None
        if self.__code == None:
            new_code = input("Invalid product code value inputted, please enter an integer from 100 to 1000.\n")    
            self.setCode(new_code)

    def setName(self, name):
        self.__name = name if isinstance(name, str) else None
        if self.__sale == None:
            new_name = input("Invalid product value inputted, please enter an actual string.\n")
            self.setName(new_name)
        
    def setSale(self, sale):
        #Accepts value only if it's a positive number.
        try:
            if float(sale) > 0:
                self.__sale = float(sale)
            else:
                print("Invalid manufacture cost value inputted, please enter a positive number.\n")
        except ValueError:
            print("Invalid manufacture cost value inputted, please enter a positive number.\n")

    def setManufacture(self, manufacture):
        #Accepts value only if it's a positive number.
        try:
            if float(manufacture) > 0:
                self.__manufacture = float(manufacture)
            else:
                print("Invalid manufacture cost value inputted, please enter a positive number.\n")
        except ValueError:
            print("Invalid manufacture cost value inputted, please enter a positive number.\n")


    def setStock(self, stock):
        #Accepts value only if it's an integer larger than 0.
        self.__stock = int(stock) if stock.isdigit() and int(stock) > 0 else None
        if self.__stock == None:
            new_stock = input("Invalid stock level value inputted, please enter a positive integer.\n")
            self.setStock(new_stock)

    def setMonthly(self, monthly):
        #Accepts value only if it's an integer larger than 0.
        self.__monthly = int(monthly) if monthly.isdigit() and int(monthly) > 0 else None
        if self.__monthly == None:
            new_monthly = input("Invalid monthly unit/s value inputted, please enter a positive integer.\n")
            self.setMonthly(new_monthly)

    def renew_information(self):
        print("welcome to Programming Principles Sample Product Inventory.")
        setters_list = [self.setCode, self.setName, self.setSale, self.setManufacture, self.setStock, self.setMonthly]
        getters_list = [self.getCode, self.getName, self.getSale, self.getManufacture, self.getStock, self.getMonthly]
        information = ["Code", "Name", "Sale Price", "Manufacture Cost", "Stock Level", "Estimated Monthly Units Manufactured"]
        stock = self.getStock()


        #Input for attributes.
        for current_info in range(6):
            information_input = input(f"Please enter the Product's {information[current_info]}: ")
            setters_list[current_info](information_input)
        print("******Programming Principles Sample Stock Statement******")
        #Summary of attributes.
        for current_info in range(6):
            print(f"Product {information[current_info]}: {getters_list[current_info]}")
        for month in range(12):
            monthly_sale = random.randint(range(self.getMonthly()-10, self.getMonthly()+10))
            stock =+ monthly_sale - self.getManufacture
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
product_one = Product(100,"Coke",12.00,10.00,1,1)
#predicted stock statement hypothetical implementation

product_one.renew_information()
