from func_nodes_layer5 import SingleVar
from func_nodes_layer2 import Layer2Node
from basic_node import BasicNode
from typing import Dict,List,Any
from pydantic import BaseModel


class ParamDictChange:
    method:int          #0表示assignment,1表示add
    name:str
    real_var:List[str] | List[float] | str | float
    vtype:str


"""
返回值都是bool,str
"""
class ParamDict(BaseModel):
    param_dict:Dict[str,SingleVar] = {}

    def _check_change_dict_legal(self,change_dict:ParamDictChange)->(bool,str):
        return True,"ok"

    def parse_change_dict(self,change_dict:ParamDictChange)->(bool,str):
        status,description =self._check_change_dict_legal(change_dict)
        if not status:
            return status,description

        if change_dict.method == 0:
            status,description = self._assign_dict(change_dict)
        elif change_dict.method == 1:
            status,description = self._add_dict(change_dict)

        return status,description



    def _assign_dict(self,change_dict:ParamDictChange)->(bool,str):
        pname = change_dict.name
        if pname not in self.param_dict.keys():
            return False,f"{pname}未被定义"

        supposed_vtype = self.param_dict[pname].vtype
        changed_vtype = self.param_dict[pname].vtype

        if supposed_vtype != changed_vtype:
            return False,f"类型错误，{pname}的类型应该是{supposed_vtype},更改的类型是{changed_vtype}"

        self.param_dict[pname].real_var = change_dict.real_var
        return True,'ok'

    def _add_dict(self,change_dict:ParamDictChange)->(bool,str):
        pname = change_dict.name
        if pname in self.param_dict.keys():
            return False,f"{pname}已经被定义"

        sv = SingleVar()
        sv.name = change_dict.name
        sv.real_var = change_dict.real_var
        sv.vtype = change_dict.vtype

        self.param_dict[pname] = sv

        return True,'ok'


class BlockStruct(BasicNode):
    type = 'BlockStruct'

    def _check_node_legal(self):
        for c in self.children_nodes:
            if not isinstance(c,Layer2Node):
                return False

        return True




class FunctionStruct(BasicNode):
    type = 'FunctionStruct'
    func_name:str
    input_type:str
    output_type:str
    param_dict:ParamDict


    def _check_node_legal(self):

        if len(self.children_nodes) != 3:
            return False

        ch = self.children_nodes
        return isinstance(ch[0],SingleVar) and isinstance(ch[1],BlockStruct) and isinstance(ch[2],SingleVar)