from drg_group.chs_drg_10.Base import message,intersect,SS_VALID
from drg_group.chs_drg_10.DRG import MDCR_DRG

def group(record):
  adrg_zd=["Z51.101","Z51.102","Z51.103","Z51.104","Z51.200x008","Z51.800x094","Z51.800x096","Z51.800x922","Z51.800x924","Z51.800x925","Z51.800x927","Z51.800x981","Z51.801","Z51.804","Z51.806","Z51.807","Z51.809","Z51.811"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合RU1入组条件，匹配规则：主诊断匹配')
    
    if MDCR_DRG.RU19_group(record):
      return 'RU19'

    return 'RU1'
  else:
    return ''

