class Configs:

    @staticmethod
    def VAL_FILES():
        VAL_FILES = [
            ".txt"
        ]
        return VAL_FILES


class Metrics:

    @staticmethod
    def POS_TITLE_NODE() -> tuple:
        """
        Title Node Position (width, height)
        """
        swidth, sheight = Metrics.get_screen_size()
        tn_width, tn_height = Metrics.node_size()
        position_title_node = ((swidth - tn_width) / 2,
                               (sheight - tn_height - (264.5 * (5/10))) / 2)
        return position_title_node

    @ staticmethod
    def MAP_GEOMETRY(structure):
        from calculator import Calculator
        calc = Calculator(structure)
        main_nodes_dict = calc.calculate_mainnodes()
        lines_pos = calc.calculate_title_lines(list(main_nodes_dict.values()))
        return main_nodes_dict, lines_pos

    @ staticmethod
    def get_screen_size() -> tuple:
        """
        (width, height)
        """
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()
        screen = (root.winfo_screenwidth(), root.winfo_screenheight())
        root.destroy()
        return screen

    @ staticmethod
    def node_size() -> tuple:
        """
        return node_size (width, height)
        """
        return (90, 40)

    @ staticmethod
    def node_distance() -> int:
        return 190
