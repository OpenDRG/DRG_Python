from drg_group.foshan_2022.Base import message,intersect,SS_VALID

def group(record):
  adrg_zd=["Z51.000x003","Z51.000x008","Z51.000x012","Z51.001","Z51.002","Z51.003"]
  adrg_zd1=[]
  adrg_ss=["92.2400"]
  adrg_ss1=[]
  adrg_ss2=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合RC14入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    return True