from drg_group.lanzhou_2023.Base import message,intersect,SS_VALID
from drg_group.lanzhou_2023.DRG import MDCB_DRG

def group(record):
  adrg_zd=["G43.000","G43.100","G43.100x002","G43.100x005","G43.100x006","G43.100x011","G43.102","G43.103","G43.105","G43.106","G43.200","G43.300","G43.800x002","G43.801","G43.802","G43.803","G43.804","G43.900","G44.000","G44.000x002","G44.000x004","G44.001","G44.002","G44.003","G44.004","G44.005","G44.100","G44.100x004","G44.200","G44.200x003","G44.200x005","G44.201","G44.202","G44.204","G44.205","G44.207","G44.208","G44.300","G44.400","G44.800","G44.800x001","G44.800x002","G44.800x006","G97.101","R51.x00","R51.x00x002","R51.x00x003"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合BV3入组条件，匹配规则：主诊断匹配')
    
    if MDCB_DRG.BV3A_group(record):
      return 'BV32'

    if MDCB_DRG.BV35_group(record):
      return 'BV35'

    return 'BV3'
  else:
    return ''

