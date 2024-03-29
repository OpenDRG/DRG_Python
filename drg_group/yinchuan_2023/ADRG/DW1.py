from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCD_DRG

def group(record):
  adrg_zd=["A18.804+K93.8*","B00.200x001","B00.201","B00.203","B37.003","K02.100","K03.400","K04.001","K04.401","K04.500","K04.702","K04.800","K05.000","K05.101","K05.202","K05.300","K06.804","K07.006","K07.008","K07.301","K07.500x002","K07.604","K07.800x001","K08.103","K08.104","K08.802","K08.803","K08.805","K10.204","K10.804","K10.900x002","K12.000","K12.002","K12.003","K12.101","K12.102","K12.107","K12.109","K12.112","K12.200x011","K12.200x018","K12.203","K12.215","K12.216","K13.000x018","K13.010","K13.011","K13.013","K13.700x009","K13.705","M31.300","Q35.100","Q35.300","Q35.500","Q35.901","Q35.902","Q35.907","Q36.000","Q36.006","Q36.901","Q36.903","Q36.904","Q38.100","Q38.600x006"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合DW1入组条件，匹配规则：主诊断匹配')
    
    if MDCD_DRG.DW19_group(record):
      return 'DW19'

    return 'DW1'
  else:
    return ''

