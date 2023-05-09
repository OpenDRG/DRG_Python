from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCL_DRG

def group(record):
  adrg_zd=["C65.x00","C66.x00","C67.200","C67.500","C67.900","C79.102","D69.005+N08.2*","E11.200x213+N08.3*","E11.200x214+N08.3*","E11.201+N08.3*","I12.900x003","N02.002","N02.101","N02.201","N02.801","N03.900","N04.101","N04.300x001","N04.900","N10.x02","N13.000","N13.201","N13.202","N13.203","N13.301","N13.400","N13.504","N13.602","N13.603","N15.101","N18.500","N20.000","N20.100","N20.200x001","N20.900","N21.000","N21.100","N28.100","N28.101","N28.805","N28.833","N28.834","N30.000","N30.100","N30.201","N30.800x004","N30.809","N35.800","N35.900","N39.000","Q61.300","Q62.101","R33.x00","T83.002","Z46.601"]
  adrg_zd1=[]
  adrg_ss=["55.9200x002","55.9200x006","55.9201","55.9202","55.9203","55.9206","55.9300","55.9400","55.9500","55.9601","56.3300x001","57.1101","57.1701","57.1800x001","57.3300","57.9500","59.9501","97.6201","98.5101","98.5102","98.5103"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合LJ1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCL_DRG.LJ11_group(record):
      return 'LJ11'

    if MDCL_DRG.LJ13_group(record):
      return 'LJ13'

    if MDCL_DRG.LJ15_group(record):
      return 'LJ15'

    return 'LJ1'
  else:
    return ''

