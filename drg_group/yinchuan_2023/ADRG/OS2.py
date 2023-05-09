from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCO_DRG

def group(record):
  adrg_zd=["O01.001","O01.101","O01.102","O01.901","O02.000x001","O02.001","O02.100","O03.001","O03.101","O03.400x001","O03.502","O03.601","O03.603","O03.802","O03.900x002","O03.901","O03.903","O03.904","O04.001","O04.100x002","O04.101","O04.401","O04.402","O04.602","O04.801","O04.900x001","O04.901","O04.902","O04.905","O05.100","O05.400","O05.900","O06.000","O06.100","O06.301","O06.400","O06.900","O07.402","O08.004","O08.005","O08.100x002","O08.102","O08.301","O08.802","O08.803","O20.000"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合OS2入组条件，匹配规则：主诊断匹配')
    
    if MDCO_DRG.OS29_group(record):
      return 'OS29'

    return 'OS2'
  else:
    return ''

