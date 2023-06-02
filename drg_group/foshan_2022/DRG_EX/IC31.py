from drg_group.foshan_2022.Base import message,intersect,has_mcc,has_cc,SS_VALID

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["78.5700x011","79.3600x020","81.2300x004","81.4501","81.4502","81.4503","81.4504","81.4505","81.8300x007","81.8300x008","81.8300x009"]
  adrg_ss1=[]
  adrg_ss2=[]
  if True and record.ssList and intersect(record.ssList[1:],adrg_ss):
    message('符合IC31入组条件，匹配规则：其他手术匹配')
    return True