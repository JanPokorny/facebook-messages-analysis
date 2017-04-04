# Facebook message analysis

This project helps you with analyzing your Facebook messages data: how often do you chat with people, how many messages have you send and much more.

Incorporates https://github.com/hey-johnnypark/convert-facebook-messages

## How-to:

- [order the take-out data from Facebook](https://www.facebook.com/settings)
- install node.js, npm, Python 3
- run `npm i` to install dependencies
- (optional -- for plotting) run `pip install matplotlib`
- convert messages.htm from the FB data to JSON: `node convert.js < messages.html > messages.json`
- feed the resulting dirty JSON into data_clean.py (documentation in the file header)
- feed the resulting clean JSON into analysis.py (documentation in the file header)
- feed the resulting analysis JSON into plot.py and make some cool bar graphs! (documentation in the file header)

More info in individual files.

### Example:

```
    node convert.js < messages.htm | python3 data_clean.py "John Doe" 1000 | python3 analyse.py > analysis.json
    python3 plot.py activeTimesPlot _GLOBAL < analysis.json
```