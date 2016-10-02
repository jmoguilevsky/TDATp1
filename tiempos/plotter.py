import matplotlib.pyplot as plt

# results: tuple (k, time)
def plotResults(results):
    plt.xlabel('k')
    plt.ylabel('Time [seconds]')
    xValues = map(lambda r: r[0], results)
    yValues = map(lambda r: r[1], results)
    plt.plot(xValues, yValues)

def saveResults(filepath):
    plt.savefig(filepath)

def showResults():
    plt.show()
