import datetime

class OrGate:
    def __init__(self):

        self.__Input0 = False

        self.__Input1 = False

        self.__Output = False

        self.__Name = "YaOrGate"

    def __get_Input0(self):
        return self.__Input0
    def __set_Input0(self,value):
        isinstance(value,bool)
        self.__Input0 = value
    Input0 = property(__get_Input0,__set_Input0)
    def __get_Input1(self):
        return self.__Input1
    def __set_Input1(self,value):
        isinstance(value,bool)
        self.__Input1 = value
    Input1 = property(__get_Input1,__set_Input1)
    def __get_Output(self):
        return self.__Output
    def __set_Output(self,value):
        isinstance(value,bool)
        self.__Output = value
    Output = property(__get_Output,None)
    def __get_Name(self):
        return self.__Name
    def __set_Name(self,value):
        isinstance(value,str)
        self.__Name = value
    Name = property(__get_Name,__set_Name)

    def execute(self):
        if self.Input0 == True and self.Input1 == True:

            self.__set_Output(True)

        else:

            self.__set_Output(False)

    def show(self):

        print(self.Output)

    def __str__(self):

        temp = """Dies ist das ANDGate: """ + str(self.__Name) + """ um """ + str(datetime.datetime.now().time()) + """\n\
Input0: """ + str(self.Input0) +"""\n\
Input1: """ + str(self.Input1) +"""\n\
Output: """ + str(self.Output)


        return temp


AND = OrGate()

AND.execute()

AND.show()

AND.Input0 = False

AND.Input1 = True

AND.execute()

AND.show()

print(str(AND))