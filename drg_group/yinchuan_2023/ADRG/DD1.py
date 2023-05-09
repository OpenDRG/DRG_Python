from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCD_DRG

def group(record):
  adrg_zd=["B49.x05","B49.x08","C44.300x006","C44.304","D04.300x001","D10.100","D36.700x007","G47.300x001","G47.300x037","J30.400","J31.000","J32.400","J32.803","J32.900","J33.000","J33.900","J34.001","J34.200","J34.800x019","J34.813","K13.004","M95.005","Q85.905","R04.000","S01.200x092","S02.200","Z42.006"]
  adrg_zd1=[]
  adrg_ss=["21.3200x011","21.3201","21.8301","21.8400x002","21.8400x003","21.8400x006","21.8401","21.8600x004","21.8602","21.8700x004","21.8700x008","21.8702","21.8801","21.8802","21.8900x002"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合DD1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCD_DRG.DD19_group(record):
      return 'DD19'

    return 'DD1'
  else:
    return ''

