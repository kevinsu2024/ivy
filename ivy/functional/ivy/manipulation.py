# global
from typing import Union, Optional, Tuple, List

# local
import ivy
from ivy.framework_handler import current_framework as _cur_framework


# Array API Standard #
# -------------------#

def flip(x: Union[ivy.Array, ivy.NativeArray],
        axis: Optional[Union[int, Tuple[int], List[int]]] = None)\
        -> ivy.Array:
    """
    Reverses the order of elements in an array along the given axis. The shape of the array must be preserved.

    Parameters
    ----------
    x:
        input array.
    axis:
        axis (or axes) along which to flip. If ``axis`` is ``None``, the function must flip all input array axes. If ``axis`` is negative, the function must count from the last dimension. If provided more than one axis, the function must flip only the specified axes. Default: ``None``.

    Returns
    -------
    out:
        an output array having the same data type and shape as ``x`` and whose elements, relative to ``x``, are reordered.
    """

    return _cur_framework(x).flip(x, axis)


def expand_dims(x: Union[ivy.Array, ivy.NativeArray],
                axis: Optional[Union[int, Tuple[int], List[int]]] = None) \
        -> ivy.Array:
    """
    Expands the shape of an array.
    Inserts a new axis that will appear at the axis position in the expanded array shape.

    :param x: Input array.
    :type x: array
    :param axis: Position in the expanded axes where the new axis is placed.
    :type axis: int
    :return: array with the number of dimensions increased by onearray
    """
    return _cur_framework(x).expand_dims(x, axis)


# Extra #
# ------#
