import random

'''
Class detailing object self and its information from
it's code identification, name, sales cost, manufacturing costs,
stock price, and monthly selfion quantity in order.
'''
class Product:
    def __init__(self):
        #code: int, name: str, sale: float, manufacture: float, stock: int, monthly: int
        self.__code = None                  #int from 100-1000
        self.__name = None                  #string
        self.__sale = None                  #num > 0
        self.__manufacture = None           #num > 0
        self.__stock = None                #stock > 0
        self.__quantity = None            #int >= 0

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
    def getQuantity(self):
        return self.__quantity

    #Setters for attributes.
    def setCode(self, code):
        #Accepts value only if it's an integer from 100 to 1000.
        self.__code = int(code)if code.isdigit() and int(code) in range(100, 1001) else None
        if self.__code == None:
            new_code = input("Invalid product code value inputted, please enter an integer from 100 to 1000.\n")    
            self.setCode(new_code)

    def setName(self, name):
        self.__name = name if isinstance(name, str) else None
        if self.__name == None:
            new_name = input("Invalid product value inputted, please enter an actual string.\n")
            self.setName(new_name)
        
    def setSale(self, sale):
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
        #Accepts value only if it's an integer larger than 0.
        self.__stock = int(stock) if stock.isdigit() and int(stock) > 0 else None
        if self.__stock == None:
            new_stock = input("Invalid stock level value inputted, please enter a positive integer.\n")
            self.setStock(new_stock)

    def setQuantity(self, quantity):
        #Accepts value only if it's an integer larger than 0.
        self.__quantity = int(quantity) if quantity.isdigit() and int(quantity) > 0 else None
        if self.__quantity == None:
            new_quantity = input("Invalid quantity unit/s value inputted, please enter a positive integer.\n")
            self.setQuantity(new_quantity)

    def register_information(self):
        print("welcome to Programming Principles Sample Product Inventory.")

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

        quantity_input = input("Please enter the Product's monthly quantity amount: ")
        self.setQuantity(quantity_input)
        summary_message = f"""

        ******Programming Principles Sample Stock Statement******
        Product Code: {self.getCode()}\n 
        Product Name: {self.getName()}\n 
        \n 
        Sale Price: {self.getSale()}\n 
        Manufacture Cost: {self.getManufacture()}\n 
        Stock Quantity: {self.getStock()}\n 
        Monthly quantity {self.getQuantity()}\n 
        """
        print(summary_message)
        stock = self.getStock()
        total_units_sold = 0

        for month in range(12):
            monthly_units_sold = self.getQuantity() + random.randint(-10, 10)
            #safety net so that items can not be sold more than what is in supply
            total_units_sold += monthly_units_sold if stock >= total_units_sold and stock > 0 else stock

            stock += self.getQuantity() - monthly_units_sold
            total_units_sold += monthly_units_sold

            #(Total Units Sold * Sale Price) - (Total Units Manufactured * Manufacture Cost).
            performance_message = f"""
            Month: {month+1}\n
            \t  Manufactured: {self.getQuantity()}
            \t  Sold: {monthly_units_sold}
            \t  Stock: {stock}
            """
            print(performance_message)
        
        net_profit = (total_units_sold + self.getSale()) - (self.getQuantity() * self.getManufacture())
        print(f"Net Profit: ${net_profit}")
                

#filler information
product_one = Product()
#predicted stock statement hypothetical implementation

product_one.register_information()
