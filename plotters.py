from pylab import *


def access(data, path):
    """
    Utility function that accesses a path in a nested dict
    """
    d = data
    for p in path:
        d = d[p]
    return d


def activeTimesPlot(data, name):
    """
    Plots the sum of all messages exchanged based on time window
    Argument: name of person analysed
    """
    left = np.arange(24)
    height = np.add(data[name]["active_hours_other"], data[name]["active_hours_me"])
    labels = [str(i) for i in range(24)]
    figure(1)
    title(("Messages with "+name+" based on time of day") if name != "_GLOBAL" else "Global messages based on time of day")
    bar(left, height, tick_label=labels)
    xlabel("Time of day")
    ylabel("Messages exchanged")
    tight_layout()
    show()


def comparePropertyPlot(data, prop):
    """
    Plots and compares people based on property
    Property can be nested, divider is #, for example: smiley_count_other#:)
    Argument: (nested) property to compare and plot users by
    """
    path = prop.split('#')
    sortedList = sorted([x for x in data.items() if x[0][0] != '_'], key=lambda x: access(x[1], path))
    labels, widths = zip(*[(k, access(v, path)) for (k, v) in sortedList])
    l = len(labels)
    bottom = np.arange(l) + 0.5  # for centered bars
    figure(1)
    title(prop)
    barh(bottom, widths, tick_label=labels, align='center')
    xlabel(prop)
    tight_layout()
    show()


def compoundPropertyPlot(data, prop):
    """
    Prints analysis of a single compound property (smiley count, for example)
    Argument: compound property path incl. person, separator is #, for example: Arrora Arrra#smiley_count_other
    """
    path = prop.split('#')
    labels, widths = zip(*sorted(access(data, path).items(), key=lambda x: x[1]))
    l = len(labels)
    bottom = np.arange(l) + 0.5  # for centered bars
    figure(1)
    title(prop)
    barh(bottom, widths, tick_label=labels, align='center')
    xlabel(prop)
    tight_layout()
    show()
