import os
import sys
# sys.path.append('D:\Repositories\Github\OpenDRG\DRG_Python')
from drg_group.yancheng_2023.GroupProxy import GroupProxy

if __name__ == "__main__":
  grouper=GroupProxy()
  # print(grouper.group_record('22136028,2.0,50.0,18624.0,,13030501.0,16.0,1.0,"D61.900,E03.900,I10.x00x002",00.1801,QJ15'))
  # sys.exit(-1)
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