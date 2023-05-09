from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCI_DRG

def group(record):
  adrg_zd=["C76.500","C76.502","C79.800x817","D36.700x030","D36.700x032","D36.700x036","D36.712","D48.719","D48.720","E55.000x002","E55.001","E64.300","I00.x00x004","I00.x01","M05.200x092","M05.303+G73.7*","M31.702+G63.5*","M47.001+G99.2*","M47.003+G99.2*","M47.101+G99.2*","M50.000+G99.2*","M50.001+G99.2*","M50.100","M50.101+G55.1*","M51.101+G55.1*","M51.103+G55.1*","M96.600x001","S22.200","S22.400","S22.400x011","S22.400x031","S22.400x041","S22.900","T81.800x012","T84.000","T84.000x004","T84.000x005","T84.000x006","T84.000x012","T84.003","T84.100","T84.202","T84.501","T84.502","T84.600","T84.602","T84.603","T84.800","T84.800x003","T84.800x005","T84.803","T84.807","Z44.800x002","Z44.900","Z47.000x002","Z47.001"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合IZ1入组条件，匹配规则：主诊断匹配')
    
    if MDCI_DRG.IZ19_group(record):
      return 'IZ19'

    return 'IZ1'
  else:
    return ''

