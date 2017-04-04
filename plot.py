from pylab import *
import sys
import json
import inspect

import plotters

"""
Creates a plot based on JSON analysis on stdin
Takes two arguments:
- plotter name (plotters are in plotters.py)
- argument for the plotter (documented in plotters.py)

Example:
python3 plot.py activeTimesPlot "Karel Sedláček" < analysis.json
"""

# Get the plotters from plotters.py
plot_fns = dict(x for x in inspect.getmembers(sys.modules["plotters"], inspect.isfunction) if x[0].endswith("Plot"))

mode = sys.argv[1]
arg = sys.argv[2]

if mode not in plot_fns:
    print("Unknown plotter, stopping...")
    exit(1)

data = json.loads(sys.stdin.read())

plot_fns[mode](data, arg)
