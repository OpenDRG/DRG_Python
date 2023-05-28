from drg_group.hefei_2023.Base import message,intersect,SS_VALID

def group(record):
  adrg_zd=["A93.802"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合SU1X入组条件，匹配规则：主诊断匹配')
    return True