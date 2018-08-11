import sys
import os
from PIL import Image
from multiprocessing import Pool
import multiprocessing as multi

argc = len(sys.argv)

if argc != 2:
  print('Usage:  python augment.py (directory path)')
  sys.exit()

path = os.path.join(os.getcwd(),sys.argv[1])
print(path)

def augment(file_path, new_width=1000, new_height=1000):
  root, ext = os.path.splitext(file_path)
  filename = root.split('/')[-1]
  #print(file_path)
  if '_r' in filename:
    return	
  if os.path.isfile(file_path):
    im = Image.open(file_path)
    width, height = im.size
    left = (width - new_width)/2
    top = (height - new_height)/2
    right = (width + new_width)/2
    bottom = (height + new_height)/2
    im = im.crop((left,top,right,bottom))
    im.save(file_path, 'JPEG')

for p in os.listdir(path):
  if os.path.isdir(os.path.join(path, p)):
    print("reading files in {}".format(os.path.join(path, p)))
    file_path_list = [os.path.join(path, p, f) for f in os.listdir(os.path.join(path, p))]
    p = Pool(multi.cpu_count())
    p.map(augment, file_path_list)
    p.close()
