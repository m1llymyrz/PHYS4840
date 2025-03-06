#!/usr/bin/python3.8
#####################################
#
# Class 14: Matrices and Linear algebra 
# Author: M Joyce; A "Mila" Myers
#
#####################################
import numpy as np 
import Myers_function_lab as mfl 

'''
by importing and using the QR decomposition 
algorithm in my_functions_lib.py:
1) Find Q and R
2) Confirm that Q is orthogonal
3) Confirm that R is upper triangular
4) Confirm that the matrix A introduced in eigenvalues.py
can indeed be reconstructed by the dot product 
of matrices Q and R

Note that the function qr_decomposition is a function written by M Joyce
'''

A = np.array([ [2, -1, 3,],\
			   [-1, 4, 5], 
			   [3,  5, 6] ],float)

Q = mfl.qr_decomposition(A)[0]
R = mfl.qr_decomposition(A)[1]

# Test of orthonormality:
Qt = np.transpose(Q)
print(Qt * Q)

# Test of R being upper traingular:
print(R) # it is

# Constructing A from the dot product of Q and R:
Anew = np.dot(Q, R)
print(f'Dot product of Q and R:\n{Anew} \n\nOriginal matrix A:\n{A}')