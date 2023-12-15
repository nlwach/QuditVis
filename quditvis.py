import qutip as q
from qutip import spin_q_function
from qutip import Qobj

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm, colors
import matplotlib.pyplot as plt

import numpy as np

def plot_qudit_wigner(state, qudit_dim=None, azim=None, elev=None, resolution=500, cmap=None):
    """
    Plot Qudit state from Wigner
    This function takes a state and maps the Husimi Q function of saif state onto a sphere.
    This helps to visualize the quantum state.
    
    Paramerters:
        state: numpy array of the state vector
        qudit_num: Dimensionality of the qudit, used for plotting only
        azim: azimuthal angle of the plotting view
        elev: elevation angle of the plotting view
        resolution: define resolution of plottted qudit sphere
        cmap: used colormap
    Returns:
        figure
    """
    if cmap == None:
        cmap = cm.coolwarm
    
    thetas = np.linspace(0, np.pi, resolution)
    phis = np.linspace(0, 2*np.pi, resolution)
    
    density, _, _  = spin_q_function(Qobj(state), thetas, phis)

    thetam, phim = np.meshgrid(thetas,phis)

    x = np.sin(thetam) * np.cos(phim)
    y = np.sin(thetam) * np.sin(phim)
    z = np.cos(thetam)


    fig = plt.figure(figsize=(15, 11))
    ax = fig.add_subplot(111, projection='3d')


    norm=colors.Normalize(vmin = np.min(density),
                          vmax = np.max(density), clip = False)

    ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False,
                           facecolors=cmap(norm(density)))
    if qudit_dim:
        ax.text(0, 0, -1.3, rf"$|{0}\rangle$")
        ax.text(0, 0, 1.2, rf"$|{qudit_num}\rangle$")
        
    ax.view_init(azim, elev)
    
    return fig
    
