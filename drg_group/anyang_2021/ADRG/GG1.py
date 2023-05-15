from drg_group.anyang_2021.Base import message,intersect,SS_VALID
from drg_group.anyang_2021.DRG import MDCG_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["54.5100","54.5100x005","54.5100x009","54.5101","54.5102","54.5103","54.5900x007","54.5901","54.5902","54.5903","54.5904","54.5905","54.5906"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合GG1入组条件，匹配规则：主手术匹配、某一手术匹配')
    
    if MDCG_DRG.GG11A_group(record):
      return 'GG11A'

    if MDCG_DRG.GG11B_group(record):
      return 'GG11B'

    if MDCG_DRG.GG13A_group(record):
      return 'GG13A'

    if MDCG_DRG.GG13B_group(record):
      return 'GG13B'

    if MDCG_DRG.GG15A_group(record):
      return 'GG15A'

    if MDCG_DRG.GG15B_group(record):
      return 'GG15B'

    return ''
  else:
    return ''

