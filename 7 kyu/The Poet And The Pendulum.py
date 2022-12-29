def pendulum(values):
    return (sorted(values)[::2])[::-1] + (sorted(values)[1::])[::2]
