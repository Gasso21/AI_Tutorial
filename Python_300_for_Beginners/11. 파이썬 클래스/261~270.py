#261
class stock:
    pass

#262
class Stock:
    def __init__(self, a, b):
        self.name = a
        self.code = b

삼성 = Stock("삼성전자", "005930")
print(삼성.name)
print(삼성.code)

#263
class Stock:
    def __init__(self, a, b):
        self.name = a
        self.code = b
    def set_name(self, set_name):
        self.set_name = set_name

a = Stock(None, None)
a.set_name("삼성전자")

#264
class Stock:
    def __init__(self, a, b):
        self.name = a
        self.code = b
    def set_name(self, set_name):
        self.set_name = set_name

    def set_code(self, code):
        self.set_code = code

a = Stock(None, None)
a.set_code("005930")

#265
class Stock:
    def __init__(self, a, b):
        self.name = a
        self.code = b
    def set_name(self, set_name):
        self.set_name = set_name

    def set_code(self, code):
        self.set_code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

삼성 = Stock("삼성전자", "005930")
print(삼성.name)
print(삼성.code)
print(삼성.get_name())
print(삼성.get_code())

#266
class Stock:
    def __init__(self, name, code, per, pbr, 배당수익률):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.배당수익률 = 배당수익률

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

#267
삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
print(삼성.배당수익률)

#268
class Stock:
    def __init__(self, name, code, per, pbr, dividend):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend = dividend

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, dividend):
        self.dividend = dividend

#269
삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
삼성.set_per(12.75)
print(삼성.per)

#270
class Stock:
    def __init__(self, name, code, per, pbr, dividend):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend = dividend

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, dividend):
        self.dividend = dividend

Samsung = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
Hyendai = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

for i in [Samsung, Hyendai, LG]:
    print(i.code, i.per)