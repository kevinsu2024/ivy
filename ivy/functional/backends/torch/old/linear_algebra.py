"""
Collection of PyTorch linear algebra functions, wrapped to fit Ivy syntax and signature.
"""

# global
import torch as _torch
from typing import List
import ivy as _ivy
from typing import Union, Tuple




def matrix_norm(x, p=2, axes=None, keepdims=False):
    axes = [-2, -1] if axes is None else axes
    if isinstance(axes, int):
        raise Exception('if specified, axes must be a length-2 sequence of ints,'
                        'but found {} of type {}'.format(axes, type(axes)))
    ret = _torch.linalg.matrix_norm(x, ord=p, dim=axes, keepdim=keepdims)
    if ret.shape == ():
        return _torch.unsqueeze(ret, 0)
    return ret


def inv(x):
    return _torch.inverse(x)


def pinv(x):
    return _torch.pinverse(x)


def cholesky(x):
    return _torch.linalg.cholesky(x)


def vector_to_skew_symmetric_matrix(vector):
    batch_shape = list(vector.shape[:-1])
    # BS x 3 x 1
    vector_expanded = _torch.unsqueeze(vector, -1)
    # BS x 1 x 1
    a1s = vector_expanded[..., 0:1, :]
    a2s = vector_expanded[..., 1:2, :]
    a3s = vector_expanded[..., 2:3, :]
    # BS x 1 x 1
    zs = _torch.zeros(batch_shape + [1, 1], device=vector.device)
    # BS x 1 x 3
    row1 = _torch.cat((zs, -a3s, a2s), -1)
    row2 = _torch.cat((a3s, zs, -a1s), -1)
    row3 = _torch.cat((-a2s, a1s, zs), -1)
    # BS x 3 x 3
    return _torch.cat((row1, row2, row3), -2)

def qr(x, mode):
    return _torch.linalg.qr(x, mode=str(mode)) # str(mode) is required for JIT type inference
