from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCB_DRG

def group(record):
  adrg_zd=["E53.801+G32.0*","G37.301","G82.100","G82.200","G82.201","G82.204","G82.400","G82.500","G83.300x003","G83.900x001","G83.900x002","G83.900x004","G95.002+M49.4*","G95.003","G95.100x008","G95.101","G95.102","G95.103","G95.200","G95.800x010","G95.807","G95.900","G95.900x003","G95.900x004","G95.901","I77.002","M51.003+G99.2*","Q28.800x003","S14.001","S14.002","S14.100x021","S14.100x022","S14.101","S24.100x023","S24.101","S34.100x001","S34.300","S34.800x001","T09.300","T09.300x004","T09.300x006","T91.300","T91.300x004","T91.301"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合BY2入组条件，匹配规则：主诊断匹配')
    
    if MDCB_DRG.BY21_group(record):
      return 'BY21'

    if MDCB_DRG.BY23_group(record):
      return 'BY23'

    if MDCB_DRG.BY25_group(record):
      return 'BY25'

    return 'BY2'
  else:
    return ''

