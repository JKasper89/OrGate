import datetime

class OrGate:
    def __init__(self):

        self.input0 = False

        self.input1 = False

        self.output = False

        self.Name = "YaOrGate"

    def execute(self):

        if self.input0 == True:
            self.output = True
        elif self.input1 == True:
            self.output = True
        else:

            self.output = False

    def show(self):

        print(self.output)

    def __str__(self):

        temp = """Dies ist das ORGate: """ + str(self.Name) + """ um """ + str(datetime.datetime.now().time()) + """\n\
Input0: """ + str(self.input0) +"""\n\
Input1: """ + str(self.input1) +"""\n\
Output: """ + str(self.output)


        return temp


OR = OrGate()

OR.execute()

OR.show()

OR.input0 = False

OR.input1 = True

OR.execute()

OR.show()

print(str(OR))