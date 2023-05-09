from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=["I20.808","I24.002","I24.800x001","I24.800x007","I24.801","I24.900x001","I24.901","I25.100x003","I25.102","I25.103","I25.400","I25.600x001","I25.800x002","I25.800x003","I25.800x004","I25.800x005","I25.800x010","I25.800x011","I25.900","I25.901","I25.902"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合FR4入组条件，匹配规则：主诊断匹配')
    
    if MDCF_DRG.FR41_group(record):
      return 'FR41'

    if MDCF_DRG.FR43_group(record):
      return 'FR43'

    if MDCF_DRG.FR45_group(record):
      return 'FR45'

    return 'FR4'
  else:
    return ''

