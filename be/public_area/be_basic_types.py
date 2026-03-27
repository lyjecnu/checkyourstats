from typing import List,Dict
from pydantic import BaseModel

class BasicTypes(BaseModel):
    var_name:str
    real_var:List | str | float
    type_name:str
    public_func_list:Dict[str,str]            
    public_func_list_input:Dict[str,str]
    public_func_list_output: Dict[str, str]

