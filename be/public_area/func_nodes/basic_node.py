from typing import List,Optional
from pydantic import BaseModel,PrivateAttr

class BasicNode(BaseModel):
    type:str
    uid:str
    children_nodes:List['BasicNode']
    parent_node: Optional['BasicNode'] = PrivateAttr(default=None)

    def _check_node_legal(self):
        return True

    def run_node(self):
        pass

    def test_node(self):
        pass

    def get_param_dict(self):
        current = self
        while current.parent_node.type != 'FunctionStruct':
            current = current.parent
        return current.param_dict

