from numpy import arctan, pi, rad2deg, sqrt, square

from configurations import Metrics

# I will use numpy for faster calculation


class Calculator:

    def __init__(self, structure):

        self.struct = structure

        self.swidth, self.sheight = Metrics.get_screen_size()
        self.tnposx, self.tnposy = Metrics.POS_TITLE_NODE()
        self.node_width, self.node_height = Metrics.node_size()
        self.node_distance = Metrics.node_distance()

        self.__bottom = self.sheight / 6

        self.struct_keys = list(self.struct.keys())
        self.struct_values = list(self.struct.values())
        self.amount_prio_one = [index for index,
                                e in enumerate(self.struct_values) if e == 1]
        self.len_amount_prio_one = len(self.amount_prio_one)

        self.coordinates_init = [0 for x in range(len(self.struct_keys))]

    def calculate_mainnodes(self) -> dict:
        """
        Return a dict of the first prio node positions.
        """
        ratio = int(self.len_amount_prio_one / 2)
        nodes_dict = {}

        for i in range(0, self.len_amount_prio_one):
            step = int((self.sheight * (2/3)) / self.len_amount_prio_one)
            if i < ratio:
                pos = (self.tnposx + self.node_distance,
                       self.__bottom + i * step * 2)
            else:
                pos = (self.tnposx - self.node_distance,
                       self.__bottom + (i - ratio) * step * 2)
            nodes_dict[self.struct_keys[self.amount_prio_one[i]]] = pos

        return nodes_dict

    def calculate_lines(self, start_node: tuple, node_positions: list, mode=0) -> list:
        """
        @param start_node: The start node, from which the lines start.
        @param node_positions: A list of the node positions the lines go to.
        @param mode: Are the lines going to the right (0) or to the left (1).

        The function will calculate the proper start coordinates of the line
        depending on the direction, the length and the right angle to
        hit the target nodes at the center.

        @returns: A list of (start_pos(x, y); line_length, rotation_angle) of length len(NODE_POSITIONS)
        """
        pos_lines = []

        # wnode will be 0 if the lines have to go to the left
        wnode = self.node_width if mode == 0 else 0
        hnode = self.node_height

        # this number will be subtracted from the angle to turn the line by 180 degrees
        # otherwise it would go in the wrong direction
        mode_1_substract = 180 if mode == 1 else 0

        for pos in node_positions:
            # calculate the start positions
            start_pos = (start_node[0] + wnode,
                         start_node[1] + hnode/2)
            # calculating DELTA_X and DELTA_Y -> a, b for a^2 + b^2 = c^2
            add = self.node_width if mode == 1 else 0
            diff_x = (pos[0] + add) - start_pos[0]
            diff_y = (pos[1] + hnode / 2) - start_pos[1]
            line_length = round(sqrt(square(diff_x) + square(diff_y)), 2)
            # angle
            rotation_angle = round(
                rad2deg(arctan(diff_y / diff_x)), 2) - mode_1_substract
            # putting everything together
            line_pos = (start_pos, line_length, rotation_angle)
            pos_lines.append(line_pos)

        return pos_lines

    def calculate_title_lines(self, node_positions: list) -> list:
        """
        Basically the same as the calculate_lines function,
        but it will turn the orientation after len(array) / 2 iterations.

        @param start_node: The start node, from which the lines start.
        @param node_positions: A list of the node positions the lines go to.

        @returns: A list of (start_pos(x, y); line_length, rotation_angle) of length len(NODE_POSITIONS)
        """
        START_NODE_POS = Metrics.POS_TITLE_NODE()
        ratio = int(len(node_positions) / 2)
        right_nodes_pos = self.calculate_lines(
            START_NODE_POS, node_positions[:ratio], 0)
        left_node_pos = self.calculate_lines(
            START_NODE_POS, node_positions[ratio:], 1)

        return right_nodes_pos + left_node_pos
