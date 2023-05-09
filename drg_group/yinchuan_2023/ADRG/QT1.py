from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCQ_DRG

def group(record):
  adrg_zd=["D65.x00x001","D66.x01","D66.x02","D66.x03+M36.2*","D67.x01","D68.001","D68.205","D68.300","D68.400x002","D68.601","D68.603","D68.801","D68.900x003","D68.900x006","D68.902","D69.000","D69.000x008","D69.001","D69.002","D69.004","D69.006","D69.008","D69.009","D69.100x001","D69.200x005","D69.203","D69.300","D69.301","D69.302","D69.400x002","D69.401","D69.403","D69.406","D69.500","D69.502","D69.504","D69.600","R23.301"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合QT1入组条件，匹配规则：主诊断匹配')
    
    if MDCQ_DRG.QT11_group(record):
      return 'QT11'

    if MDCQ_DRG.QT13_group(record):
      return 'QT13'

    if MDCQ_DRG.QT15_group(record):
      return 'QT15'

    return 'QT1'
  else:
    return ''

