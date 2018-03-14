import datetime

class AndGate:
    def __init__(self):

        self.input0 = False

        self.input1 = False

        self.output = False

        self.Name = "YaAndGate"

    def execute(self):

        if self.input0 == True and self.input1 == True:

            self.output = True

        else:

            self.output = False

    def show(self):

        print(self.output)

    def __str__(self):

        temp = """Dies ist das ANDGate: """ + str(self.Name) + """ um """ + str(datetime.datetime.now().time()) + """\n\
Input0: """ + str(self.input0) +"""\n\
Input1: """ + str(self.input1) +"""\n\
Output: """ + str(self.output)


        return temp


AND = AndGate()

AND.execute()

AND.show()

AND.input0 = False

AND.input1 = True

AND.execute()

AND.show()

print(str(AND))