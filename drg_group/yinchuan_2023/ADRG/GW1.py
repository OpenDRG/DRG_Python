from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCG_DRG

def group(record):
  adrg_zd=["A04.401","A04.700x002","A04.900","A04.902","A05.900","A08.000","A08.200","A08.402","A09.000x001","A09.000x006","A09.001","A09.004","A09.006","A09.007","A09.900x003","A09.900x004","A09.900x006","A09.900x007","A09.901","A09.902","A09.903","A09.904","A49.809","B37.804","B49.x12","K20.x00","K20.x00x001","K20.x00x003","K20.x01","K20.x02","K21.001","K29.000","K29.001","K29.100x001","K29.101","K29.300","K29.400","K29.500","K29.501","K29.600","K29.600x006","K29.603","K29.700","K29.701","K29.800","K29.801","K51.500","K52.902","K52.903","K52.904","K52.907","K52.908","K52.909","K52.910","K52.911","K52.912","K52.917","K57.003","K57.100x005","K57.102","K57.104","K57.106","K57.107","K57.108","K57.200x001","K57.202","K57.303","K57.304","K57.305","K58.100","K58.200","K58.800","K58.801"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合GW1入组条件，匹配规则：主诊断匹配')
    
    if MDCG_DRG.GW19_group(record):
      return 'GW19'

    return 'GW1'
  else:
    return ''

