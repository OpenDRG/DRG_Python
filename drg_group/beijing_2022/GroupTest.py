import os
import sys
from drg_group.beijing_2022.GroupProxy import GroupProxy

if __name__ == '__main__':
  grouper=GroupProxy()
  # print(grouper.group_record('22058878,2,88,32460,,13040503,94,1,I62.001|S06.600|S02.102|S22.300|S42.000|S42.100|J94.804|J98.101|S32.000x011|E87.801|E77.801,38.9700x002|31.1x00x005'))
  grouper.group_csv(os.path.join('/mnt/c/yb/yc','ba_group_info_{}.csv'.format('202212')),['BAHM','BRXB','NL','NLT','XSECSTZ','CYKS','ZYTS','LYFS','ICD10_DRGS','ICD9_DRGS'])
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