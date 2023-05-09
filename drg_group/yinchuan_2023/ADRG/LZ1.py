from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCL_DRG

def group(record):
  adrg_zd=["D17.700x016","N18.100","N18.200","N27.000","N28.001","N28.003","N28.004","N28.100","N28.101","N28.804","N28.805","N28.806","N28.807","N28.815","N28.816","N28.819","N28.821","N28.823","N28.826","N28.828","N28.833","N28.902","N30.100","N30.400","N30.805","N30.806","N30.809","N30.900","N30.902","N31.901","N32.104","N32.300","N32.301","N32.805","N32.808","N32.900x002","N32.901","N36.000","N36.200","N36.805","N36.806","N36.901","N39.900","N99.800x006","N99.800x011","Q60.000","Q61.300","Q62.000","Q62.500","Q62.800","Q63.001","Q63.102","Q63.200","Q63.800x902","Q63.900","Q64.303","Q64.401","Q64.402","Q64.403","S37.000","S37.001","S37.002","S37.200","S37.200x022","S37.300","S37.302","T19.100","T81.800x011","T83.000x001","T83.100x001","T83.101","T83.102","T83.800x001","T83.802","Z46.600x001","Z46.601","Z46.603","Z49.000x004","Z49.101"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合LZ1入组条件，匹配规则：主诊断匹配')
    
    if MDCL_DRG.LZ11_group(record):
      return 'LZ11'

    if MDCL_DRG.LZ13_group(record):
      return 'LZ13'

    if MDCL_DRG.LZ15_group(record):
      return 'LZ15'

    return 'LZ1'
  else:
    return ''

