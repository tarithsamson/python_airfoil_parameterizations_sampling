from scipy.interpolate import BSpline
import numpy as np

def b_spline_coords(points):
    """
    Calculates x and z coordinates of a B-spline curve from a set of control points.

    Args:
        points: list of tuples of x, y, z coordinates of control points

    Returns:
        x: numpy array of x coordinates of the B-spline curve
        z: numpy array of z coordinates of the B-spline curve
    """
    # Extract the x and z coordinates from the control points
    x = np.array([p[0] for p in points])
    z = np.array([p[1] for p in points])

    # Calculate the knot vector and degree of the B-spline curve
    n = len(points)
    k = min(n - 1, 3)
    t = np.linspace(0, 1, n - k, endpoint=True)

    # Create the B-spline object and evaluate the curve
    spline = BSpline(t, x, k)
    x_vals = np.linspace(0, 1, 100)
    x_curve = spline(x_vals)
    
    spline = BSpline(t, z, k)
    z_vals = np.linspace(0, 1, 100)
    z_curve = spline(z_vals)

    return x_curve, z_curve