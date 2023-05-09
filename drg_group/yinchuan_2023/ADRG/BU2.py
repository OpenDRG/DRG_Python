from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCB_DRG

def group(record):
  adrg_zd=["E75.201","E75.202","E83.001","G11.100x002","G11.300x001","G11.400","G11.900","G11.900x001","G11.901","G12.100x008","G12.200","G12.200x008","G12.200x010","G12.200x011","G12.200x013","G12.201","G12.204","G12.205","G12.206","G20.x00","G20.x01","G20.x02+F02.3*","G20.x03","G21.001","G21.100","G21.900","G23.101","G23.200","G23.300","G23.800x005","G23.801","G23.900","G24.101","G24.105","G24.201","G24.500","G24.501","G24.804","G24.900x003","G24.901","G24.902","G25.000","G25.000x009","G25.100","G25.201","G25.500","G25.501","G25.600x001","G25.800x001","G25.901","G31.200x001","G31.200x005","G31.202","G31.203","G31.802","G31.900","G31.900x003","G31.903","G31.904","Q85.000","Q85.100","R27.000"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合BU2入组条件，匹配规则：主诊断匹配')
    
    if MDCB_DRG.BU21_group(record):
      return 'BU21'

    if MDCB_DRG.BU25_group(record):
      return 'BU25'

    return 'BU2'
  else:
    return ''

