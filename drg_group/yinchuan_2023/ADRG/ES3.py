from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCE_DRG

def group(record):
  adrg_zd=["A01.000x005+J17.0*","A43.000x001+J99.8*","B01.200+J17.1*","B06.801+J17.1*","B25.000+J17.1*","B67.100x001+J99.8*","J10.000","J10.001","J12.100","J12.200","J12.800","J12.900","J13.x00","J14.x00","J15.000","J15.000x002","J15.100","J15.101","J15.200","J15.300","J15.400","J15.402","J15.500","J15.600x002","J15.600x003","J15.600x005","J15.600x006","J15.601","J15.602","J15.700","J15.800x001","J15.900","J15.901","J15.902","J15.903","J16.000","J18.000","J18.000x001","J18.001","J18.002","J18.100","J18.200","J18.800x001","J18.800x002","J18.800x006","J18.802","J18.803","J18.900","J18.901","J18.902","J18.903","J22.x00","J69.000","J69.000x004","J69.001","J85.100","J85.200","J85.300","J86.003","J86.007","J86.009","J86.013","J86.902","J86.903","J95.800x016","J98.414","J98.502","J98.700","J98.802"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合ES3入组条件，匹配规则：主诊断匹配')
    
    if MDCE_DRG.ES31_group(record):
      return 'ES31'

    if MDCE_DRG.ES33_group(record):
      return 'ES33'

    if MDCE_DRG.ES35_group(record):
      return 'ES35'

    return 'ES3'
  else:
    return ''

