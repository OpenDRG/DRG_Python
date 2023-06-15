from drg_group.yunnan_2023.Base import message,intersect,SS_VALID
from drg_group.yunnan_2023.DRG import MDCW_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=["T31.300","T31.400","T31.500","T31.600","T31.700","T31.800","T31.900","T32.300","T32.400","T32.500","T32.600","T32.700","T32.800","T32.900"]
  adrg_ss=["85.8200","85.8300","85.8400","85.8500","86.6101","86.6200x002","86.6201","86.6202","86.6300x001","86.6301","86.6302","86.6303","86.6304","86.6501","86.6601","86.6701","86.6702","86.6901","86.6903","86.6904","86.6905","86.6906","86.7100x009","86.7101","86.7102","86.7103","86.7104","86.7105","86.7200x001","86.7300x003","86.7300x004","86.7301","86.7302","86.7303","86.7400x026","86.7400x031","86.7400x032","86.7400x033","86.7400x034","86.7400x035","86.7400x036","86.7400x037","86.7400x038","86.7400x039","86.7400x040","86.7400x041","86.7400x042","86.7401","86.7402","86.7403","86.7404","86.7500x001","86.7501","86.7502","86.7503","86.7504","86.9301","86.9302","86.9303","86.9305","86.9306"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and intersect(record.zdList[1:],adrg_zd1) and record.ssList and record.ssList[0] in adrg_ss:
    message('符合WB1_2入组条件，匹配规则：其他诊断匹配、主手术匹配')
    
    
    if MDCW_DRG.WB19_group(record):
      return 'WB19'

    return ''
  else:
    return ''
