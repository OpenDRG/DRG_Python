from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCC_DRG

def group(record):
  adrg_zd=["B00.501+H19.1*","B49.x04+H19.2*","D17.700x005","D31.000x001","D31.000x002","D31.100","E11.301+H36.0*","H02.000","H02.901","H10.400","H10.401","H11.000","H11.108","H11.201","H11.401","H11.802","H11.805","H11.806","H11.901","H15.900","H16.000","H16.000x001","H16.000x010","H16.001","H16.003","H16.004","H16.006","H16.007","H16.805","H16.900","H17.801","H18.400","H18.404","H18.502","H18.600","H18.701","H18.800x009","H18.808","H18.901","H25.000x003","H25.100","H25.900","H26.900","H33.001","H33.102","H33.200x002","H33.304","H33.502","H33.504","H33.506","H43.100","H44.502","H59.800x003","Q13.400x004","S05.000x002","S05.201","S05.202","S05.206","S05.300x004","S05.301","S05.304","S05.500x002","S05.601","S05.604","T15.000","T26.602","T26.902","T85.300x001","T85.300x004","T85.300x008","T85.300x009","T85.311","T86.801"]
  adrg_zd1=[]
  adrg_ss=["10.0x00x001","10.1x00x001","10.3101","10.4101","10.4400x001","10.4401","10.4403","10.4900x001","10.4900x003","10.4903","10.5x01","10.6x00x001","10.9900x001","10.9901","11.1x01","11.3200","11.3201","11.3202","11.3203","11.3204","11.3900x001","11.3901","11.4100x001","11.4200","11.4903","11.5100","11.5200","11.5300x001","11.5900x001","11.5901","11.6200x002","11.6400x001","11.6400x002","11.6900x003","11.6901","11.7400x001","11.9900x002","12.0200x003","12.8100","12.8400x004","12.8404","12.8700x005","12.8703","12.8801","12.8802","12.8904","12.9201","97.3801","97.3802","98.2200x005"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合CC1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCC_DRG.CC19_group(record):
      return 'CC19'

    return 'CC1'
  else:
    return ''

