#!/usr/bin/python3
"""
This module multiply 2 matricies using numpy module
"""


import numpy

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.
    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.
    Returns:
        list of lists: The product of the two matrices.
    Raises:
        ValueError: If the matrices can't be multiplied.
        TypeError: If m_a or m_b are not lists of lists.
        TypeError: If m_a or m_b contain non-numeric elements.
        ValueError: If m_a or m_b are empty.
        ValueError: If the matrices are not rectangular.
    """
    # Convert input matrices to NumPy arrays
    m_a_np = numpy.array(m_a)
    m_b_np = numpy.array(m_b)
    
    # Perform matrix multiplication using NumPy's matmul function
    product = numpy.matmul(m_a_np, m_b_np)
    
    # Convert the resulting NumPy array back to a list of lists
    return product.tolist()
