from drg_group.yunnan_2022.Base import message,intersect,SS_VALID
from drg_group.yunnan_2022.DRG import MDCJ_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["21.9900x002","21.9901","21.9902","86.2800x012"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合JD2入组条件，匹配规则：主手术匹配、某一手术匹配')
    
    if MDCJ_DRG.JD21_group(record):
      return 'JD21'

    if MDCJ_DRG.JD23_group(record):
      return 'JD23'

    if MDCJ_DRG.JD25_group(record):
      return 'JD25'

    return 'JD2'
  else:
    return ''

