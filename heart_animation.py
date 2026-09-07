import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def animate_heart():

    # Heart equation
    t = np.linspace(0, 2 * np.pi, 1000)

    x = 16 * np.sin(t) ** 3

    y = (
        13 * np.cos(t)
        - 5 * np.cos(2 * t)
        - 2 * np.cos(3 * t)
        - np.cos(4 * t)
    )

    # Create window
    fig, ax = plt.subplots(figsize=(6, 6))

    # Background
    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")

    # Graph limits
    ax.set_xlim(-22, 22)
    ax.set_ylim(-22, 22)

    # Remove axes
    ax.axis("off")

    # Heart line
    heart, = ax.plot(
        [],
        [],
        color="red",
        linewidth=5
    )

    # Text
    text = ax.text(
        0,
        18,
        "❤️ YOU ARE MY HEART BEAT ❤️",
        color="white",
        fontsize=16,
        ha="center",
        fontweight="bold"
    )

    # Animation function
    def animate(frame):

        # Heartbeat effect
        scale = 1 + 0.08 * np.sin(frame * 0.25)

        # Scale heart
        new_x = x * scale
        new_y = y * scale

        # Update heart
        heart.set_data(new_x, new_y)

        return heart, text


    # Create animation
    animation = FuncAnimation(
        fig,
        animate,
        frames=500,
        interval=30,
        blit=True
    )

    # Show animation
    plt.show()