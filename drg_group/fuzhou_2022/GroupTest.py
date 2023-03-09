import os
import sys
from drg_group.fuzhou_2022.GroupProxy import GroupProxy

if __name__ == "__main__":
  grouper=GroupProxy()
  # print(grouper.group_record("22058878,2,88,32460,,13040503,94,1,K80.302|K80.305|K83.109|K72.905|Z90.408|E14.900x001,51.8803|51.8701|54.5100x005|45.1301"))
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