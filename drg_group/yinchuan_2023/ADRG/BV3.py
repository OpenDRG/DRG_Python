from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCB_DRG

def group(record):
  adrg_zd=["G43.000","G43.100","G43.100x006","G43.100x011","G43.102","G43.106","G43.200","G43.800x002","G43.900","G44.000","G44.000x002","G44.000x004","G44.001","G44.003","G44.004","G44.005","G44.100","G44.100x004","G44.200","G44.200x003","G44.207","G44.300","G44.800","G44.800x002","R51.x00","R51.x00x002"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合BV3入组条件，匹配规则：主诊断匹配')
    
    if MDCB_DRG.BV39_group(record):
      return 'BV39'

    return 'BV3'
  else:
    return ''

