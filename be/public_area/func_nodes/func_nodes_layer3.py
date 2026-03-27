from basic_node import BasicNode
from func_nodes_layer4 import JudgementStatement
from func_nodes_layer2 import Layer2Node
from func_nodes_layer1 import BlockStruct


class Layer3Node(BasicNode):
    pass

class IfStruct(Layer3Node):
    type = 'IfStruct'

    def _check_node_legal(self):
        if len(self.children_nodes) != 2:
            return False

        return isinstance(self.children_nodes[0],JudgementStatement) and isinstance(self.children_nodes[1],BlockStruct)


class ElseIfStruct(Layer3Node):
    type = 'ElseIfStruct'

    def _check_node_legal(self):
        if len(self.children_nodes) != 2:
            return False

        return isinstance(self.children_nodes[0],JudgementStatement) and isinstance(self.children_nodes[1],BlockStruct)




class ElseStruct(Layer3Node):
    type = 'ElseStruct'

    def _check_node_legal(self):
        return len(self.children_nodes) == 1 and isinstance(self.children_nodes[0],BlockStruct)