
'''
Class detailing object self and its information from
it's code identification, name, sales cost, manufacturing costs,
stock price, and monthly selfion quantity in order.
'''
class Product:
    def __init__(self, code, name, sale, manufacture, stock, monthly):
        self.__code = code
        self.__name = name
        self.__sale = sale
        self.__manufacture = manufacture
        self.__stock = stock
        self.__monthly = monthly

    #getters for attributes
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

    #setters for attributes
    def setCode(self, code):
        self.__code = code
    def setName(self, name):
        self.__name = name
    def setSale(self, sale):
        self.__sale = sale
    def setManufacture(self, manufacture):
        self.__manufacture = manufacture
    def setStock(self, stock):
        self.__stock = stock
    def setMonthly(self, monthly):
        self.__monthly = monthly

    

coca_cola = Product(12,12,12,12,12,12)
print("hello world", coca_cola.getMonthly())
