from typing import List, Any
from basic_node import BasicNode
from func_nodes_layer4 import JudgementStatement,CalculationStatement
from public_area.be_basic_types import BasicTypes

class Layer5Node(BasicNode):
    pass

class JudgementSign(Layer5Node):
    type = 'JudgementSign'
    name:str

    def _check_node_legal(self):
        return isinstance(self.parent_node,JudgementStatement) and (not self.children_nodes)

class CalculationSign(Layer5Node):
    type = 'CalculationSign'
    name:str

    def _check_node_legal(self):
        return isinstance(self.parent_node,CalculationStatement)  and (not self.children_nodes)


class SingleVar(Layer5Node):
    type = 'SingleVar'
    real_var:List[str] | List[float] | str | float | None
    name:str
    vtype:str
    status:int                                      #0未验证，1验证类型成功，2验证变量成功，3类型错误

    def _check_node_legal(self):
        return not self.children_nodes

class CompoundVar(Layer5Node):
    type = 'CompoundVar'
    name:str

    def _check_node_legal(self):
        for c in self.children_nodes:
            if not isinstance(c,SingleVar):
                return False

        return True

    #返回一个bool,List[str]
    def parse_var(self):
        pass
