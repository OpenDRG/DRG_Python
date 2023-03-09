import os
import sys
from drg_group.lanzhou_2022.GroupProxy import GroupProxy,replace_csv

if __name__ == "__main__":
  grouper=GroupProxy()
  print(grouper.group_record('22139971,1.0,73.0,27006.0,,13030305.0,8.0,1.0,"G20.x03,R90.803,F41.101,I10.x00x002,N39.000,E77.801,E87.600",,BU21'))
  sys.exit(-1)
  if len(sys.argv)==1:
    path=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    if not os.path.exists(os.path.join(path,'input.txt')):
      print('文件不存在:{}'.format(os.path.join(path,'input.txt')))
      sys.exit(-1)
    grouper.group_txt()
  elif len(sys.argv)==2:
    result=grouper.group_record(sys.argv[1])
    print(result)
  else:
    if not os.path.exists(sys.argv[1]):
      print('文件不存在:{}'.format(sys.argv[1]))
      sys.exit(-1)
    grouper.group_csv(sys.argv[1],sys.argv[2])