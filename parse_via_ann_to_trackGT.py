import sys, os, json, string
import argparse

def parse_args():
    #parse input arguments
    parser = argparse.ArgumentParser(description='parse via annotation file into json files')
    parser.add_argument('--outfile', dest='outfile', help="output dir", type=str)
    parser.add_argument('--viafile', dest='viafile', help="via annotation file", type=str)
    args = parser.parse_args()
    return args

args = parse_args()
outfile = args.outfile
viafile = args.viafile
with open(viafile, 'r') as f:
    anns = json.load(f)

ann_dict = dict()
for _, cur_ann in anns.iteritems():
    imname = cur_ann['filename']
    if imname > "test_two_faces_0210":
        #print imname
        continue
    print "\n"
    print cur_ann
    bbs = cur_ann['regions']
    all_boxes = []
    cur_dict = dict()
    for tbb in bbs:
        ids = tbb['region_attributes']['id']
        tbb = tbb['shape_attributes']
        left    = tbb['x']
        top     = tbb['y']
        width   = tbb['width']
        height  = tbb['height']
        right   = left + width - 1
        bottom  = top + height - 1
        #print(left, top, right, bottom)
        cur_dict[ids] = [left, top, right, bottom]
    ann_dict[imname] = cur_dict

with open(outfile, 'w') as f:
    json.dump(ann_dict, f, indent=2)
#with open(outfile, 'w') as f:
#    for idx in range(0,256, 2):
#        imname = "%s_%d.jpg"%("test_jiaxin_face", idx)
#        loc = ann_dict[imname]
#        print imname
#        print loc
#        f.write("%d,%d,%d,%d,%d,%d,%d,%d\n"%(loc[0],loc[1],loc[2],loc[3],loc[4],loc[5],loc[6],loc[7]))

