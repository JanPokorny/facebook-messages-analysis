# coding=utf-8

import json
import sys
import inspect
import itertools

import analysers


"""
Analyses the clean messages JSON and creates all sorts of statistics (also JSON) that can be plotted.
Global statistics save under the special name _GLOBAL.
Usage: python3 analyse.py < messages-clean.json > analysis.json
"""


def get_fns(s):  # returns array of functions from analysers.py that match given prefix
    return [x[1] for x in inspect.getmembers(sys.modules["analysers"], inspect.isfunction) if x[0].startswith(s)]

agg_fns = get_fns("aggregator_")
dagg_fns = get_fns("dual_aggregator_")
post_fns = get_fns("postprocessor_")


def aggregate(msgs, glob=False):
    """
    Uses the appropriate analysis functions on the message list
    """

    # First, simple aggregation (word count etc.)
    msgs_me = [msg for msg in msgs if msg['by_me']]
    msgs_other = [msg for msg in msgs if not msg['by_me']]
    res = {}
    for agg_fn in agg_fns:
        res.update({k + "_me":    v for k, v in agg_fn(msgs_me).items()})
        res.update({k + "_other": v for k, v in agg_fn(msgs_other).items()})

    # For non-global analysis, dual aggregation (conversations etc.)
    if not glob:
        for dagg_fn in dagg_fns:
            res.update(dagg_fn(msgs))

    return res


data = json.loads(sys.stdin.read())

new_data = {name: aggregate(msgs) for name, msgs in data.items()}

# This gizmo concats the list of lists and sorts all messages by their date
all_msgs = sorted(itertools.chain.from_iterable(data.values()), key=lambda x: x['date'])
# ... so they can be analysed all together
new_data["_GLOBAL"] = aggregate(all_msgs, True)

# Post-processors
for post_fn in post_fns:
    post_fn(new_data)

sys.stdout.write(json.dumps(new_data, indent=2, ensure_ascii=False, sort_keys=True))
