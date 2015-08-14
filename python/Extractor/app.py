import os
from raexpy import RadarExtractor
import raexpy as rex


trail = 'D:/Document/niplab/LIG'
season = '/july/source/1000'
# source = '/rawdata_oneten'
source = '/rawdata_7980'
output = '/inputdata'
outputtag = '/data_7980'


if __name__ == "__main__": 
    rrelist = []
    for dirname, dirnames, filenames in os.walk(trail + season + source):

        if 'data' in dirname and len(filenames) > 0:
            clsname = os.path.split(dirname)
            rre = RadarExtractor(clsname[-1])
            # print path to all filenames in subdirname.
            for filename in filenames:
                if '.txt' in filename:
                    os.path.join(dirname, filename)
                    # print os.path.join(dirname, filename)
                    dlist = []
                    file = open(dirname + '/' + filename, 'r')
                    file.readline(), file.readline(), file.readline()
                    lines = file.readlines()
                    for line in lines:
                        dlist.append(line)
                    rre.append_data(dlist)
            rre.close()
            # print data
            rrelist.append(rre)
            print('append %s' % rre.name)
    rex.featurescaling(rrelist)  # for feature scaling
    # export Data
    # dirname = os.path.dirname(__file__)
    # dirname = os.path.join(dirname, "export")
    outputpath = trail + season + output + outputtag
    if not os.path.exists(outputpath):
        os.makedirs(outputpath)

    with open(os.path.join(outputpath, 'merge.csv'), 'wb') as fm:
        for c in rrelist: 
            with open(os.path.join(outputpath, c.name + '.csv'), 'wb') as f:
                for data in c.rawdata:
                    dlen = len(data) - 1
                    for i, val in enumerate(data):
                        value = repr(val) + (',' if dlen != i else '\r\n')
                        f.write(value.encode('utf-8'))
                        fm.write(value.encode('utf-8'))

                print('file write: ' + c.name + '.csv')
