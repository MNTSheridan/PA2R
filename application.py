
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
        self.__code = code if code.isdigit() and code in range(100, 1001) else None
        if self.__code == None:
            code = input("Invalid product code value inputted, please enter an integer from 100 to 1000.")    
            self.setCode(code)

    def setName(self, name):
        self.__name = name
        
    def setSale(self, sale):
        #Accepts value only if it's a positive number.
        self.__sale = sale if isinstance(sale, (float, int)) and sale > 0 else None
        if self.__sale == None:
            p("Invalid sale price value inputted, please enter a positive value.")

    def setManufacture(self, manufacture):
        #Accepts value only if it's a positive number.
        self.__manufacture = manufacture if isinstance(manufacture, (float, int)) and manufacture > 0 else None
        print("Invalid manufacture cost value inputted.") if self.__manufacture == None else None
    def setStock(self, stock):
        #Accepts value only if it's an integer larger than 0.
        self.__stock = stock if isinstance(stock, int) and stock > 0 else None
        print("Invalid stock level value inputted.") if self.__stock == None else None
    def setMonthly(self, monthly):
        #Accepts value only if it's an integer larger than 0.
        self.__monthly = monthly if isinstance(monthly, int) and monthly > 0 else None
        print("Invalid monthly unit/s value inputted.") if self.__monthly == None else None

    

product_one = Product(1,"Coca Cola",0.50,0.20,100,12000000)
#predicted stock statement hypothetical implementation
PSS = product_one.
print("hello world", product_one.getMonthly())
