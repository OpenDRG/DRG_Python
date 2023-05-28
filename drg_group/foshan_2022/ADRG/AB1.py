from drg_group.foshan_2022.Base import message,intersect,SS_VALID
from drg_group.foshan_2022.DRG import MDCA_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["50.5100","50.5100x001","50.5900x001","50.5900x004","50.5900x005","50.5901","50.5902"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合AB1入组条件，匹配规则：主手术匹配、某一手术匹配')
    
    
    if MDCA_DRG.AB19_group(record):
      return 'AB19'

    return ''
  else:
    return ''

