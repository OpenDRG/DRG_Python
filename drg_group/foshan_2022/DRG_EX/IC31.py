from drg_group.foshan_2022.Base import message,intersect,SS_VALID

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["78.5700X011","79.3600X020","81.2300X004","81.4501","81.4502","81.4503","81.4504","81.4505","81.8300X007","81.8300X008","81.8300X009"]
  adrg_ss1=[]
  adrg_ss2=[]
  if True and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合IC31入组条件，匹配规则：其他手术匹配、某一手术匹配')
    return True