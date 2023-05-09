from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCE_DRG

def group(record):
  adrg_zd=["E32.001","E32.100","E32.801","E85.404","G47.300x034","I88.106","J39.805","J39.806","J43.900","J43.900x001","J43.901","J43.903","J43.904","J70.800","J95.800x012","J98.000x013","J98.001","J98.003","J98.005","J98.009","J98.011","J98.101","J98.102","J98.200","J98.400x001","J98.400x012","J98.400x013","J98.400x016","J98.400x019","J98.402","J98.403","J98.409","J98.410","J98.411","J98.412","J98.413","J98.416","J98.505","J98.507","J98.600x001","J98.602","J98.800x001","J98.901","Q33.002","Q33.200","Q33.600","Q79.000","Q79.102","R59.009","R91.x04","R94.202","T17.400","T17.500","T17.901","T27.300","U07.100x002"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合EZ1入组条件，匹配规则：主诊断匹配')
    
    if MDCE_DRG.EZ11_group(record):
      return 'EZ11'

    if MDCE_DRG.EZ13_group(record):
      return 'EZ13'

    if MDCE_DRG.EZ15_group(record):
      return 'EZ15'

    return 'EZ1'
  else:
    return ''

