from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCL_DRG

def group(record):
  adrg_zd=["C64.x00x001","C66.x00","C67.900","D09.103","D17.700x016","D18.000x811","D30.000","D41.001","N13.000","N13.100x001","N13.201","N13.202","N13.203","N13.300x005","N13.301","N13.501","N13.600x002","N13.602","N13.603","N13.605","N15.102","N17.900","N18.300","N19.x02","N26.x00","N28.100","N28.101","N28.813","N28.814","N28.815","N28.819","N28.827","N28.833","Q61.300","Q62.101","Q63.001","Q63.102","R31.x00","R93.403","S37.001","T83.002"]
  adrg_zd1=[]
  adrg_ss=["55.0105","55.0106","55.0200","55.0300x005","55.1100x001","55.1100x002","55.1108","55.1200","55.3900x001","55.3900x003","55.3900x004","55.3902","55.4x00","55.4x03","55.5100","55.5101","55.5103","55.5104","55.8501","55.8701","55.8702","55.8703","55.8704","59.0903"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合LB2入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCL_DRG.LB21_group(record):
      return 'LB21'

    if MDCL_DRG.LB23_group(record):
      return 'LB23'

    if MDCL_DRG.LB25_group(record):
      return 'LB25'

    return 'LB2'
  else:
    return ''

