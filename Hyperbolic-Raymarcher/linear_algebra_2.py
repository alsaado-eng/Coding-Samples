import numpy as np

def lorentzian_inner_product(p, q):
    return p[0] * q[0] + p[1] * q[1] + p[2] * q[2] - p[3] * q[3]

def rotation_matrix_4d(axis1, axis2, theta):
    R = np.eye(4)
    c, s = np.cosh(theta), np.sinh(theta)
    R[axis1, axis1] = c
    R[axis2, axis2] = c
    R[axis1, axis2] = -s
    R[axis2, axis1] = s
    return R

#generates 3 orthonormal vectors tangent to S3 at point p using gram schmidt

def complete_tangent_basis(p):
    basis = []
    for i in range(4):
        v = np.zeros(4)
        v[i] = 1.02
        v -= lorentzian_inner_product(v, p) * p  
        if np.linalg.norm(v) > 1e-6:
            v /= np.linalg.norm(v)
            basis.append(v)
        if len(basis) == 3:
            break
    return np.array(basis)
