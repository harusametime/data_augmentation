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

def augment(file_path):
  root, ext = os.path.splitext(file_path)
  filename = root.split('/')[-1]
  if '_r' in filename:
    return	
  if os.path.isfile(file_path):
    im = Image.open(file_path)
      for i in range(1,8):
        im_rotate = im.rotate(45*i)
	      root, ext = os.path.splitext(file_path)
	      new_file_name = root + '_r'+ str(45*i) + ext
	      im_rotate.save(new_file_name, 'JPEG')

for p in os.listdir(path):
  if os.path.isdir(os.path.join(path, p)):
	  print("reading files in {}".format(os.path.join(path, p)))
    file_path_list = [os.path.join(path, p, f) for f in os.listdir(os.path.join(path, p))]
    p = Pool(multi.cpu_count())
    p.map(augment, file_path_list)
    p.close()            
