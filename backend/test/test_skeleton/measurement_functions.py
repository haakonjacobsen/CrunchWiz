import numpy as np
import sympy as sym


import backend.crunch.skeleton.measurement_functions as mf

tol = 1e-5
t = sym.symbols("t")


def test_get_joint_by_index():
    assert len(mf.get_joint_by_index(1, "all")) == 25
    assert len(mf.get_joint_by_index(1, 2)) == 3


def test_norm_by_array():
    a = [1, 2, 3]
    b = [3, 2, 1]
    estimate = mf.norm_by_array(a, b)
    exact = 2.8284
    assert np.abs(round(estimate, 4) - exact) < tol


def test_func():
    a = [2, 4, 6]
    b = [1, 3, 5]
    x, y, z = mf.func(a, b)
    # t = 2 gives 0
    x_exact = 0
    # t = 4 gives 0
    y_exact = 0
    # t = 6 gives 0
    z_exact = 0

    assert np.abs(x.subs(t, 2) - x_exact) < tol
    assert np.abs(y.subs(t, 4) - y_exact) < tol
    assert np.abs(z.subs(t, 6) - z_exact) < tol


def test_finiteDiff():
    eq = t + 1
    assert mf.finiteDiff(eq, 1, 2) - 0 < tol


def test_fatigue():
    estimated = mf.fatigue(1, 12)
    exact = 78.9378
    assert np.abs(round(estimated, 4) - exact) < tol


def test_amount_of_motion():
    estimated = mf.amount_of_motion(1, 20)
    exact = 0.1544
    assert np.abs(round(estimated, 4) - exact) < tol


def test_most_used_joints():
    estimated = [0] * 25
    mf.most_used_joints(1, 50, estimated)
    min_estimated = round(min(estimated), 4)
    max_estimated = round(max(estimated), 4)
    min_exact = 0.0675
    max_exact = 0.4716
    assert np.abs(min_estimated - min_exact) < tol
    assert np.abs(max_estimated - max_exact) < tol


def test_stability_of_motion():
    estimated = round(mf.stability_of_motion(1, 20), 4)
    exact = 21.8083
    assert np.abs(estimated - exact) < tol

""" 
t = sym.symbols("t")
f = equation([4,-3],[3,-6])
#exect m= 3
# f(t) = 3t-15
print(f)
 """
