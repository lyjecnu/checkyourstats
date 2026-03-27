from basic_node import BasicNode
from func_nodes_layer3 import IfStruct,ElseStruct,ElseIfStruct
from func_nodes_layer4 import CalculationStatement
from func_nodes_layer5 import SingleVar


class Layer2Node(BasicNode):
    pass

class IfElseStruct(Layer2Node):
    type = 'IfElseStruct'

    def _check_node_legal(self):

        if len(self.children_nodes) < 2:
            return False

        for i,c in enumerate(self.children_nodes):
            if i == 0:
                if not isinstance(c,IfStruct):
                    return False

            if i >= 1 and i < len(self.children_nodes) - 1:
                if not isinstance(c,ElseIfStruct):
                    return False

            if i == len(self.children_nodes) - 1:
                if not isinstance(c,ElseStruct):
                    return False

        return True


class AssignmentStruct(Layer2Node):
    type = 'AssignmentStruct'

    def _check_node_legal(self):
        return (len(self.children_nodes) == 2) and isinstance(self.children_nodes[0],CalculationStatement) and isinstance(self.children_nodes[1],SingleVar)



class CreateVarStruct(Layer2Node):
    type = 'CreateVarStruct'

    def _check_node_legal(self):
        return (len(self.children_nodes) == 2) and isinstance(self.children_nodes[0],CalculationStatement) and isinstance(self.children_nodes[1],SingleVar)

