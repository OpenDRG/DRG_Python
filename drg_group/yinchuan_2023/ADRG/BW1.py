from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCB_DRG

def group(record):
  adrg_zd=["H47.203","Q03.102","Q03.800","Q03.900","Q04.000","Q04.303","Q04.306","Q04.902","Q05.700x004","Q05.900x002","Q05.901","Q05.902","Q06.801","Q06.901","Q07.000","Q07.800","Q28.103","Q28.200","Q28.201","Q28.202","Q28.300x001","Q28.300x007","Q28.301","Q28.305","Q76.000","Q85.805"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合BW1入组条件，匹配规则：主诊断匹配')
    
    if MDCB_DRG.BW19_group(record):
      return 'BW19'

    return 'BW1'
  else:
    return ''

