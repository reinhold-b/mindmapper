from configurations import Configs


class Interpreter:

    def leading(self, string: str) -> int:
        """
        Helper function for counting leading "-"s
        """
        leading_amount = 0
        while string[leading_amount] == "-":
            leading_amount += 1
        return leading_amount

    @staticmethod
    def structure(data: list) -> dict:
        """
        Structurize the list of lines into a dict
        by counting the leading "-"s --> as values.
        We also get rid of the "-" and whitespaces afterwards!
        """
        structure = {}
        for i in range(0, len(data)):
            leading_ = Interpreter.leading(Interpreter(), data[i])
            data_ele = data[i].replace("-", "").strip()
            if data_ele in structure:
                structure[data_ele + "%%%"] = leading_
            structure[data_ele] = leading_
        return structure

    @staticmethod
    def interpret(data: list) -> dict:
        """
        Entry point for the interpreter process. 
        """
        return Interpreter.structure(data)
