# global
import numpy as np
from typing import Tuple, Union, Optional


# Array API Standard #
# -------------------#

def min(x: np.ndarray,
        axis: Union[int, Tuple[int]] = None,
        keepdims: bool = False) \
        -> np.ndarray:
    return np.amin(a=x, axis=axis, keepdims=keepdims)


def max(x: np.ndarray,
        axis: Union[int, Tuple[int]] = None,
        keepdims: bool = False) \
        -> np.ndarray:
    return np.amax(a=x, axis=axis, keepdims=keepdims)


def prod(x: np.ndarray,
         axis: Optional[Union[int, Tuple[int]]] = None,
         dtype: Optional[np.dtype] = None,
         keepdims: bool = False)\
        -> np.ndarray:

    if dtype == None and np.issubdtype(x.dtype,np.integer):
        if np.issubdtype(x.dtype,np.signedinteger) and x.dtype in [np.int8,np.int16,np.int32]:
            dtype = np.int32
        elif np.issubdtype(x.dtype,np.unsignedinteger) and x.dtype in [np.uint8,np.uint16,np.uint32]:
            dtype = np.uint32
        elif x.dtype == np.int64: 
            dtype = np.int64
        else:
            dtype = np.uint64

    return np.prod(a=x,axis=axis,dtype=dtype,keepdims=keepdims)


# Extra #
# ------#
