from drg_group.foshan_2022.Base import message,intersect,SS_VALID

def group(record):
  adrg_zd=["Z51.100X004","Z51.100X004","Z51.101","Z51.102","Z51.103","Z51.104"]
  adrg_zd1=[]
  adrg_ss=["86.0701"]
  adrg_ss1=[]
  adrg_ss2=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合RE16入组条件，匹配规则：主诊断匹配、其他手术匹配、某一手术匹配')
    return True