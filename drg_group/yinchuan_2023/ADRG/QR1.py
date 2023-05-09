from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCQ_DRG

def group(record):
  adrg_zd=["C26.100","D18.000x044","D18.100x002","D18.100x006","D18.100x019","D18.104","D21.900x015","D37.703","D70.x00","D70.x00x001","D70.x01","D70.x02","D70.x04","D70.x05","D71.x01","D72.100","D72.102","D72.800x003","D72.802","D72.804","D72.806","D73.100","D73.300","D73.400","D73.500","D73.501","D73.803","D75.100","D75.110","D75.800x003","D75.805","D75.809","D75.902","D76.101","D76.200","D80.101","D81.901","D82.300x002","D84.900","D84.900x002","D86.100","D86.101","I88.100","I88.108","I88.800x001","I88.900x003","I88.900x005","I88.900x006","I88.901","I89.010","I89.802","L03.901","L04.100","L04.200","L04.201","L04.202","L04.300","L04.800","L04.900","L04.900x002","L04.900x007","L04.901","L04.902","M32.111+D77*","Q89.200x601","R16.100x001","R59.000x009","R59.002","R59.004","R59.005","R59.006","R59.007","R59.008","R59.010","R59.011","R59.014","R59.100","S36.000","S36.000x021","S36.001","S36.002"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合QR1入组条件，匹配规则：主诊断匹配')
    
    if MDCQ_DRG.QR11_group(record):
      return 'QR11'

    if MDCQ_DRG.QR13_group(record):
      return 'QR13'

    if MDCQ_DRG.QR15_group(record):
      return 'QR15'

    return 'QR1'
  else:
    return ''

