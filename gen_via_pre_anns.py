import sys, os, json, string
import argparse

def parse_args():
    #parse input arguments
    parser = argparse.ArgumentParser(description='trans detect res to via label format')
    parser.add_argument('--anndir', dest='anndir', help="annotation dir", type=str)
    parser.add_argument('--imgdir', dest='imgdir', help="image dir", type=str)
    parser.add_argument('--outfile', dest='outfile', help="out file path", type=str)
    parser.add_argument('--listfile', dest='listfile', help="namelist file to be annotated", type=str)
    parser.add_argument('--minarea', dest='minarea', help="minimum box area", type=int)
    args = parser.parse_args()
    return args
args = parse_args()
ann_dir = args.anndir
img_dir = args.imgdir
out_file = args.outfile
if args.listfile is None:
    namelist = os.listdir(ann_dir)
else:
    with open(args.listfile, 'r') as f:
        namelist = [x.strip() for x in f.readlines()]

out = dict()
for name in namelist:
    prefix = os.path.splitext(name)[0]
    imname = prefix+".jpg"
    cur_ann = dict()
    filesize = os.path.getsize(os.path.join(img_dir, imname))
    cur_ann['filename']=imname
    cur_ann['size'] = filesize
    cur_ann['file_attributes'] = {}
    ann_path = os.path.join(ann_dir, name)
    with open(ann_path, 'r') as f:
        bbs = json.load(f)
    regions = []
    for bb in bbs:
        wid = bb[2] - bb[0]
        hei = bb[3] - bb[1]
        if (wid * hei) < args.minarea:
            continue
        regions.append({'shape_attributes':{'x':bb[0], 'y':bb[1],'width':wid, 'height':hei, 'name':'rect'}, 'region_attributes':{}})
    cur_ann['regions'] = regions
    out_key = "%s%d"%(imname,filesize)
    out[out_key]=cur_ann
with  open(out_file, 'w') as f:
    json.dump(out, f)
