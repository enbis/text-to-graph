# text-to-graph

It works over `matplotlib`, with the advantage of making easier reading data from files.
Shows on the screen different charts, passing as input an array of text files (filepath). It reads the files and produce the charts looking at the options setted as input. 

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

The command `texttograph.plotfiles(['./testfiles/tfile0.txt', './testfiles/tfile4.txt', './testfiles/tfile6.txt'], typeg="dot", overlapped=False)` produce:

![Image of chart_bars.png](https://github.com/enbis/text-to-graph/blob/master/images/tfiles.png)

The command `texttograph.plotfiles(['./testfiles/test_one.txt'], 'line')` produce:

![Image of chart_bars.png](https://github.com/enbis/text-to-graph/blob/master/images/test_one.png)




