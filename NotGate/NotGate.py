# -*- coding: utf8 -*-
__version__ = '1.0'                                         # Versionsinformationen
__author__ = 'Jan Kasper(jan.kasper@students.tbs1.de)'

class NotGate:                                               # Beginn der Klassendefinition
    """
    This class calculates the logical NOT function.
    """
    def __init__(self):                                     # Definition der Attribute
        self.__Input = False
        self.__Output = True
        self.__Name = "YaNotGate"

    def __get_Input(self):                                 # Definition der Getter und Setter
        return self.__Input
    def __set_Input(self,value):
        isinstance(value,bool)
        self.__Input = value
    def __get_Output(self):
        return self.__Output
    def __set_Output(self,value):
        isinstance(value,bool)
        self.__Output = value
    def __get_Name(self):
        return self.__Name
    def __set_Name(self,value):
        isinstance(value,str)
        self.__Name = value

    Input = property(__get_Input,__set_Input)            # Definition der Properties
    Output = property(__get_Output,None)
    Name = property(__get_Name,__set_Name)

    def execute(self):                                      # Berechnung der logischen Verknüpfung
        """
        Negates the input
        :return: None
        """
        self.__set_Output(False)
        if self.Input == False:
            self.__set_Output(True)

    def __str__(self):                                      # Ausformlierung der Stringumwandlung
        """
        Conerts the status of the logical gate to a string.
        :return: string of the gate status
        """
        cwidth = 60
        line = ''.ljust(cwidth, '#')
        format_str = "## {{0:10}}: {{1:{0}}} ##".format(cwidth-18)
        temp = line
        temp += "\n" + format_str.format("Name", self.Name)
        temp += "\n" + format_str.format("Type", type(self).__name__)
        temp += "\n" + format_str.format("Input", str(self.Input))
        temp += "\n" + format_str.format("Output", str(self.Output))
        temp += "\n" + line
        return temp

    def show(self):                                         # Bildschirmausgabe der Stringumwandlung
        """
        Shows the value of each property of the class and the class name
        :return: None
        """
        print(self.__str__())


if __name__ == "__main__":
    AND = NotGate()
    AND.execute()
    AND.show()
    AND.Input=True
    AND.show()
    AND.execute()
    AND.show()
