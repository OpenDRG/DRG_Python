from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCC_DRG

def group(record):
  adrg_zd=["E11.300x051+H42.0*","H16.000","H21.000","H21.503","H25.900","H35.305","H40.000x004","H40.100","H40.100x001","H40.101","H40.102","H40.200","H40.200x007","H40.202","H40.203","H40.300","H40.500","H40.500x002","H40.500x009","H40.501","H40.801","H40.900","H43.100","H44.501","H59.808","Q15.000","Q15.005","S05.100x004","S05.200x007","S05.601","S05.802","T26.603","T85.300x001","Z48.801"]
  adrg_zd1=[]
  adrg_ss=["12.5100x001","12.5400","12.5900x001","12.5900x003","12.5901","12.6400x001","12.6400x003","12.6402","12.6405","12.6408","12.6701","12.6702","12.6704","12.7100","12.7200","12.7300","12.9100x004","12.9100x006","12.9101","12.9102","12.9803","12.9900x008","12.9900x009","12.9903"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合CB4入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCC_DRG.CB49_group(record):
      return 'CB49'

    return 'CB4'
  else:
    return ''

