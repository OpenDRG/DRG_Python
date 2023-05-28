from drg_group.foshan_2022.Base import message,intersect,SS_VALID

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["99.1000"]
  adrg_ss1=[]
  adrg_ss2=[]
  if True and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合BR27入组条件，匹配规则：其他手术匹配、某一手术匹配')
    return True