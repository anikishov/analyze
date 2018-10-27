import os
import sys

path = os.path.join(sys.argv[1])
pars_val = sys.argv[2]
pts_val_lst = []

with open(path, 'r', encoding='UTF-8') as f:
  for line in f:
          if pars_val in line:
                  temp,pts_val = line.split('=')
                  pts_val_lst.append(pts_val.rstrip('\n'))



for x,y in zip(pts_val_lst[0::],pts_val_lst[1::]):
    print(x, y,'-', int(y)-int(x))
