from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCC_DRG

def group(record):
  adrg_zd=["B00.500x005+H19.1*","B00.501+H19.1*","B00.502+H13.1*","B00.504+H03.1*","B00.507+H19.1*","B00.509+H03.1*","B02.301+H58.8*","B02.302+H19.2*","B02.303+H03.1*","B02.304+H13.1*","B02.307+H19.2*","B30.900","B49.x03+H19.2*","B49.x04+H19.2*","B60.100x004+H19.2*","H00.003","H05.000x006","H05.001","H05.103","H05.205","H10.300","H16.000","H16.000x001","H16.001","H16.003","H16.004","H16.005","H16.006","H16.103","H16.200","H16.205","H16.300x005","H16.800x010","H16.801","H16.805","H16.900","H20.101","H20.900","H20.901","H44.000x005","H44.100","H44.101","H44.102","H44.103"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合CU1入组条件，匹配规则：主诊断匹配')
    
    if MDCC_DRG.CU19_group(record):
      return 'CU19'

    return 'CU1'
  else:
    return ''

