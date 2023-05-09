from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCI_DRG

def group(record):
  adrg_zd=["M86.100","M86.400","M86.602","M86.604","M86.607","M86.608","M86.808","M86.809","M86.900","M86.900x073","M86.903","M86.904","M86.905","M86.907","M86.908","M86.910","M86.911","M86.912","M86.913","M86.914","M86.915","M86.916","M86.917","M86.920","M86.921","M86.923","M87.000","M87.001","M87.002","M87.102","M87.200x042","M87.200x072","M87.203","M87.204","M87.800x021","M87.800x041","M87.800x051","M87.800x091","M87.800x101","M87.900","M87.900x071","M87.901"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合IT1入组条件，匹配规则：主诊断匹配')
    
    if MDCI_DRG.IT19_group(record):
      return 'IT19'

    return 'IT1'
  else:
    return ''

