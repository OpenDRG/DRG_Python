from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCB_DRG

def group(record):
  adrg_zd=["C71.003","G91.000","G91.100","G91.200","G91.900","I60.802","I61.004","I61.300x004","I61.400x001","I61.802","R90.000","Z42.001"]
  adrg_zd1=[]
  adrg_ss=["02.2101","02.2208","02.3400x002","02.3401","02.3404","02.3405","02.4203"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合BC2入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCB_DRG.BC21_group(record):
      return 'BC21'

    if MDCB_DRG.BC23_group(record):
      return 'BC23'

    if MDCB_DRG.BC25_group(record):
      return 'BC25'

    return 'BC2'
  else:
    return ''

