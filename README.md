# text-to-graph

Shows on the screen different charts of data row, passing as input an array of text files (filepath). It reads it and graphed data looking at the options setted. 

## Graph properties

- Type
- Overlapped

**Types**

Five types of charts available.
- `dot`
- `bar`
- `line`
- `linedot`
- `linex`

Uses one of these as an input property, after the list of text files to read.
Default is `dot`.

**Overlapped**

Boolean property, True to show overlapping graphs. In that case only `bar` and `dot` charts are availbale.

### Test 

It exists a `test.py` scipt to show how it works. 

- `python3 test.py`

Some examples in more details.

The command `texttograph.plotfiles(['./testfiles/bars1.txt', './testfiles/bars2.txt'], typeg="bar", overlapped=True)` produce:

![Image of chart_bars.png](https://github.com/enbis/text-to-graph/blob/master/images/chart_bars.png)




