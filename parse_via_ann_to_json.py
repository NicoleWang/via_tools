import sys, os, json, string
import argparse

def parse_args():
    #parse input arguments
    parser = argparse.ArgumentParser(description='parse via annotation file into json files')
    parser.add_argument('--outdir', dest='outdir', help="output dir", type=str)
    parser.add_argument('--viafile', dest='viafile', help="via annotation file", type=str)
    args = parser.parse_args()
    return args

args = parse_args()
outdir = args.outdir
viafile = args.viafile
with open(viafile, 'r') as f:
    anns = json.load(f)

for _, cur_ann in anns.iteritems():
    imname = cur_ann['filename']
    prefix = os.path.splitext(imname)[0]
    bbs = cur_ann['regions']
    all_boxes = []
    for tbb in bbs:
	left    = tbb['x']
	top     = tbb['y']
	width   = tbb['width']
	height  = tbb['height']
	right   = left + width - 1
	bottom  = top + height - 1
	all_boxes.append([left, top, right, bottom])
    out_path = os.path.join(outdir, prefix+".json")
    with open(out_path, 'w') as f:
        json.dump(all_boxes, f)
