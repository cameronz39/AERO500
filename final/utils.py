import numpy as np

def plotBounds(ax,CUBE_SIZE,col='blue',thickness=0.1,scale=1.5):
    X_LIM = CUBE_SIZE
    Y_LIM = CUBE_SIZE
    Z_LIM = CUBE_SIZE
    ax.plot([X_LIM,-X_LIM],[Y_LIM,Y_LIM],[Z_LIM,Z_LIM],color=col,linewidth=thickness)
    ax.plot([X_LIM,-X_LIM],[Y_LIM,Y_LIM],[-Z_LIM,-Z_LIM],color=col,linewidth=thickness)
    ax.plot([X_LIM,-X_LIM],[-Y_LIM,-Y_LIM],[Z_LIM,Z_LIM],color=col,linewidth=thickness)
    ax.plot([X_LIM,-X_LIM],[-Y_LIM,-Y_LIM],[-Z_LIM,-Z_LIM],color=col,linewidth=thickness)

    ax.plot([X_LIM,X_LIM],[Y_LIM,-Y_LIM],[Z_LIM,Z_LIM],color=col,linewidth=thickness)
    ax.plot([X_LIM,X_LIM],[Y_LIM,-Y_LIM],[-Z_LIM,-Z_LIM],color=col,linewidth=thickness)
    ax.plot([-X_LIM,-X_LIM],[Y_LIM,-Y_LIM],[Z_LIM,Z_LIM],color=col,linewidth=thickness)
    ax.plot([-X_LIM,-X_LIM],[Y_LIM,-Y_LIM],[-Z_LIM,-Z_LIM],color=col,linewidth=thickness)

    ax.plot([X_LIM,X_LIM],[Y_LIM,Y_LIM],[-Z_LIM,Z_LIM],color=col,linewidth=thickness)
    ax.plot([X_LIM,X_LIM],[-Y_LIM,-Y_LIM],[-Z_LIM,Z_LIM],color=col,linewidth=thickness)
    ax.plot([-X_LIM,-X_LIM],[Y_LIM,Y_LIM],[-Z_LIM,Z_LIM],color=col,linewidth=thickness)
    ax.plot([-X_LIM,-X_LIM],[-Y_LIM,-Y_LIM],[-Z_LIM,Z_LIM],color=col,linewidth=thickness)

    ax.set_xlim([-X_LIM*scale, X_LIM*scale]); ax.set_ylim([-Y_LIM*scale, Y_LIM*scale]); ax.set_zlim([-Z_LIM*scale, Z_LIM*scale])
    ax.set_box_aspect([1, 1, 1])                    # equal aspect ratio
    ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')


def projectSphere(num_pts):
    indices = np.arange(0, num_pts, dtype=float) + 0.5

    phi = np.arccos(1 - 2*indices/num_pts)
    theta = np.pi * (1 + 5**0.5) * indices

    x, y, z = np.cos(theta) * np.sin(phi), np.sin(theta) * np.sin(phi), np.cos(phi)

    return x, y, z
    # plt.figure().add_subplot(111, projection='3d').scatter(x, y, z)
    # plt.show()