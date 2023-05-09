from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCG_DRG

def group(record):
  adrg_zd=["K22.200","K22.201","K22.202","K22.205","K22.208","K22.901","K31.100x002","K31.102","K31.500","K31.501","K31.502","K31.808","K40.303","K40.304","K40.305","K40.306","K40.307","K40.309","K40.312","K40.313","K40.314","K40.315","K40.402","K41.302","K43.001","K43.200","K43.603","K45.002","K46.000x002","K46.100x001","K56.000","K56.100","K56.101","K56.200","K56.200x003","K56.203","K56.400x001","K56.401","K56.500x003","K56.600x008","K56.602","K56.603","K56.604","K56.700","K56.700x003","K56.701","K62.402","K91.300","K91.404","K91.809","K91.812","K91.819","K91.839","R10.101","R10.301","R10.400x002","R10.402"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合GV1入组条件，匹配规则：主诊断匹配')
    
    if MDCG_DRG.GV11_group(record):
      return 'GV11'

    if MDCG_DRG.GV13_group(record):
      return 'GV13'

    if MDCG_DRG.GV15_group(record):
      return 'GV15'

    return 'GV1'
  else:
    return ''

