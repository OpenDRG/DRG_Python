from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCE_DRG

def group(record):
  adrg_zd=["A15.000x001","A15.000x002","A15.000x003","A15.000x010","A15.000x012","A15.000x014","A15.000x016","A15.000x018","A15.000x020","A15.000x022","A15.000x024","A15.000x026","A15.000x028","A15.001","A15.002","A15.007","A15.100x001","A15.100x002","A15.100x003","A15.100x005","A15.100x007","A15.100x008","A15.100x009","A15.100x010","A15.107","A15.200x001","A15.201","A15.204","A15.207","A15.301","A15.307","A15.500x003","A15.501","A15.508","A15.509","A15.601","A15.603","A15.806","A15.810","A16.007","A16.008","A16.009","A16.010","A16.017","A16.018","A16.020","A16.036","A16.037","A16.038","A16.107","A16.108","A16.200x002","A16.200x013","A16.200x014","A16.200x015","A16.207","A16.300x002","A16.400x011","A16.402","A16.500x004","A16.500x008","A16.500x009","A16.500x010","A16.501","A16.503","A16.504","A16.700x002","A16.807","A16.900x002","A19.000x008","A19.000x010","A19.000x011","A19.000x015","A19.001","A19.801"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合ES1入组条件，匹配规则：主诊断匹配')
    
    if MDCE_DRG.ES11_group(record):
      return 'ES11'

    if MDCE_DRG.ES13_group(record):
      return 'ES13'

    if MDCE_DRG.ES15_group(record):
      return 'ES15'

    return 'ES1'
  else:
    return ''

