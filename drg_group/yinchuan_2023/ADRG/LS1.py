from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCL_DRG

def group(record):
  adrg_zd=["C90.004+N16.1*","D69.005+N08.2*","E66.902+N08.4*","E85.411+N29.8*","I12.900x003","M31.305+N08.5*","M31.701+N08.5*","M31.703+N08.5*","M32.101+N08.5*","M32.102+N16.4*","M35.006+N16.4*","N02.001","N02.002","N02.101","N02.201","N02.302","N02.801","N03.000","N03.100","N03.200x001","N03.300x001","N03.800x003","N03.800x004","N03.900","N03.900x002","N03.900x003","N03.900x004","N03.900x006","N03.900x007","N03.901","N04.001","N04.101","N04.102","N04.200x001","N04.300x001","N04.300x003","N04.501","N04.502","N04.601","N04.800x002","N04.801","N04.900","N04.903","N05.000x001","N05.000x004","N05.201","N05.301","N05.701","N05.803","N05.900","N05.900x002","N05.900x003","N06.001","N10.x00","N10.x01","N11.900","N11.901","N12.x01","N13.801","N14.000","N14.101","N14.201","N25.802","N25.803","N26.x01","N28.900x013","N28.900x017","N28.901","Q61.400","Q61.401"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合LS1入组条件，匹配规则：主诊断匹配')
    
    if MDCL_DRG.LS11_group(record):
      return 'LS11'

    if MDCL_DRG.LS13_group(record):
      return 'LS13'

    if MDCL_DRG.LS15_group(record):
      return 'LS15'

    return 'LS1'
  else:
    return ''

