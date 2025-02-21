"""
Collection of PyTorch math functions, wrapped to fit Ivy syntax and signature.
"""

# global
import math
import torch as _torch


def tan(x):
    if isinstance(x, float):
        return math.tan(x)
    return _torch.tan(x)


def acos(x):
    if isinstance(x, float):
        return math.acos(x)
    return _torch.acos(x)


def atan(x):
    if isinstance(x, float):
        return math.atan(x)
    return _torch.atan(x)


def atan2(x, y):
    if isinstance(x, float):
        return math.atan2(x, y)
    return _torch.atan2(x, y)


def cosh(x):
    if isinstance(x, float):
        return math.cosh(x)
    return _torch.cosh(x)


def atanh(x):
    if isinstance(x, float):
        return math.atanh(x)
    return _torch.atanh(x)


def log(x):
    if isinstance(x, float):
        return math.log(x)
    return _torch.log(x)


def exp(x):
    if isinstance(x, float):
        return math.exp(x)
    return _torch.exp(x)


def erf(x):
    if isinstance(x, float):
        return math.erf(x)
    return _torch.erf(x)
