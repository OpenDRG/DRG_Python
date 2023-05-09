from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCC_DRG

def group(record):
  adrg_zd=["H34.100","H34.200","H34.201","H34.202","H34.204","H34.801","H34.802","H34.803","H34.900","H35.000","H35.000x017","H35.008","H46.x00","H46.x01","H46.x02","H47.000x009","H47.003","H47.004","H47.200","H47.300x005","H47.303","H49.400","H49.400x001","H49.800","H49.800x002","H49.800x007","H49.804","H49.805","H49.808","H49.810","H49.900","H49.901","H50.000x002","H50.000x004","H50.005","H50.006","H50.007","H50.100","H50.100x002","H50.100x004","H50.101","H50.103","H50.105","H50.106","H50.200x004","H50.201","H50.301","H50.400","H50.402","H50.405","H50.801","H50.803","H50.900","H53.200","H53.400","H55.x00x002","I70.800x003","S04.000x001","S04.100"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合CS1入组条件，匹配规则：主诊断匹配')
    
    if MDCC_DRG.CS19_group(record):
      return 'CS19'

    return 'CS1'
  else:
    return ''

