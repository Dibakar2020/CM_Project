# y0=1.207, vx0=8.113, vy0=4.630, alpha=29.7;   experiment 1

import math
import csv
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Frisbee:
    x = 0.0
    y = 0.0
    vx = 0.0
    vy = 0.0
    g = -9.81
    m = 0.175
    RHO = 1.23
    AREA = 0.0568
    CL0 = 0.1
    CLA = 1.4
    CD0 = 0.08
    CDA = 2.72
    ALPHA0 = -4.0

    @staticmethod
    def simulate(y0, vx0, vy0, alpha, delta_t):
        cl = Frisbee.CL0 + Frisbee.CLA * alpha * math.pi / 180
        cd = Frisbee.CD0 + Frisbee.CDA * (alpha - Frisbee.ALPHA0) * math.pi / 180
        Frisbee.x = 0
        Frisbee.y = y0
        Frisbee.vx = vx0
        Frisbee.vy = vy0

        fig, ax = plt.subplots()
        x_values = []
        y_values = []

        # Set fixed axis limits
        ax.set_xlim(0, 30)
        ax.set_ylim(0, 5)

        def update(frame):
            nonlocal x_values, y_values

            deltavy = (Frisbee.RHO * Frisbee.vx**2 * Frisbee.AREA * cl / (2 * Frisbee.m) + Frisbee.g) * delta_t
            deltavx = -Frisbee.RHO * Frisbee.vx**2 * Frisbee.AREA * cd * delta_t

            Frisbee.vx = Frisbee.vx + deltavx
            Frisbee.vy = Frisbee.vy + deltavy
            Frisbee.x = Frisbee.x + Frisbee.vx * delta_t
            Frisbee.y = Frisbee.y + Frisbee.vy * delta_t

            x_values.append(Frisbee.x)
            y_values.append(Frisbee.y)

            ax.clear()
            ax.plot(x_values, y_values, label='Frisbee Trajectory')
            ax.scatter([Frisbee.x], [Frisbee.y], color='red', marker='o', label='Frisbee Position')
            ax.set_title('Frisbee Trajectory for attacking angle 29.7 degree')
            ax.set_xlabel('Distance (m)')
            ax.set_ylabel('Height (m)')
            ax.legend()

            # Set fixed axis limits
            ax.set_xlim(0, 10)
            ax.set_ylim(-0.1, 5)

            # Add grid
            ax.grid(True)

            # Stop animation when y is negative
            if Frisbee.y < 0:
                anim.event_source.stop()

        anim = FuncAnimation(fig, update, frames=range(1000), interval=10, repeat=False)
        plt.show()

        try:
            with open('frisbee.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['x', 'y', 'vx'])

                k = 0
                while Frisbee.y > 0:
                    deltavy = (Frisbee.RHO * Frisbee.vx**2 * Frisbee.AREA * cl / (2 * Frisbee.m) + Frisbee.g) * delta_t
                    deltavx = -Frisbee.RHO * Frisbee.vx**2 * Frisbee.AREA * cd * delta_t

                    Frisbee.vx = Frisbee.vx + deltavx
                    Frisbee.vy = Frisbee.vy + deltavy
                    Frisbee.x = Frisbee.x + Frisbee.vx * delta_t
                    Frisbee.y = Frisbee.y + Frisbee.vy * delta_t

                    x_values.append(Frisbee.x)
                    y_values.append(Frisbee.y)

                    if k % 10 == 0:
                        writer.writerow([Frisbee.x, Frisbee.y, Frisbee.vx])

                    k += 1

            plt.show()

        except Exception as e:
            print("Error, file frisbee.csv is in use.")

Frisbee.simulate(y0=1.207, vx0=8.113, vy0=4.630, alpha=29.7, delta_t=0.01)
