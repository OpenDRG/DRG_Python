from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=["C49.900x001","C79.800x807","C79.808","D15.100","D15.101","D15.103","D18.000x001","D18.000x836","D18.000x840","D18.010","D44.601","E03.900x004+I43.8*","E05.903+I43.8*","I09.900","I25.300x009","I26.001","I27.900","I27.900x002","I51.302","I51.700","I51.700x009","I51.700x014","I51.703","I51.704","I51.707","I51.708","I51.800x006","I51.900","I51.900x002","I51.903","I78.801","I89.001","I95.000","I95.200","I95.800x001","I95.900","I97.800x013","M05.304+I52.8*","N18.505+I68.8*","Q27.809","Q28.801","Q85.900x048","R07.301","R07.400","R94.301","R94.303","S35.700x004","S85.900x001","S95.800","T81.700x002","T82.002","T82.103","T82.301","T82.303","T82.400","T82.500x003","T82.503","T82.800x009","T82.800x105","T82.814","Z03.500x001","Z03.501"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合FZ1入组条件，匹配规则：主诊断匹配')
    
    if MDCF_DRG.FZ11_group(record):
      return 'FZ11'

    if MDCF_DRG.FZ13_group(record):
      return 'FZ13'

    if MDCF_DRG.FZ15_group(record):
      return 'FZ15'

    return 'FZ1'
  else:
    return ''

