from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCK_DRG

def group(record):
  adrg_zd=["E10.002","E10.003","E10.100","E10.100x012","E10.100x031","E10.100x061","E10.101","E10.103","E10.600x051","E10.700","E10.800","E10.900","E10.901","E11.000","E11.000x001","E11.000x006","E11.001","E11.002","E11.003","E11.100x051","E11.101","E11.102","E11.103","E11.600x043","E11.600x051","E11.700x011","E11.700x025","E11.700x033","E11.800","E11.900","E13.000","E13.101","E13.102","E13.800","E13.900x006","E13.903","E13.907","E14.000x001","E14.000x003","E14.000x004","E14.100","E14.100x012","E14.600x043","E14.700","E14.800","E14.900x001","R73.000","R73.002","R81.x00x001"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合KS1入组条件，匹配规则：主诊断匹配')
    
    if MDCK_DRG.KS11_group(record):
      return 'KS11'

    if MDCK_DRG.KS13_group(record):
      return 'KS13'

    if MDCK_DRG.KS15_group(record):
      return 'KS15'

    return 'KS1'
  else:
    return ''

