from func_nodes_layer5 import JudgementSign,CalculationSign,SingleVar,CompoundVar
from basic_node import BasicNode

class Layer4Node(BasicNode):
    pass

class CalculationStatement(Layer4Node):
    type = 'CalculationStatement'

    def _check_node_legal(self):

        if not self.children_nodes:
            return False

        for i,c in enumerate(self.children_nodes):
            if i % 2 == 0:
                if not isinstance(c,CompoundVar):
                    return False
            else:
                if not isinstance(c,CalculationSign):
                    return False

        return True


class JudgementStatement(Layer4Node):
    type = 'JudgementStatement'

    def _check_node_legal(self):
        cn = self.children_nodes
        return (len(cn) == 3) and isinstance(cn[0],CalculationStatement) and isinstance(cn[1],CalculationStatement) and isinstance(cn[2],JudgementSign)