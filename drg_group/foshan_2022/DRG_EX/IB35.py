from drg_group.foshan_2022.Base import message,intersect,SS_VALID

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["03.0900X009","03.0900X022","03.0900X027","03.0908","03.0913","03.0914","03.0915","03.2100X001","03.3101","03.4X07","03.6X01","03.6X02","03.6X03","03.9600","77.2904","77.6905","77.6906","78.4904","80.4900X002","80.5100X026","80.5100X030","80.5100X031","80.5100X032","80.5100X033","80.5100X034","80.5100X037","80.5103","80.5106","80.5110","80.5111","80.5400X001","80.7901","81.6500","81.6600X001","81.6600X002","81.6600X003","81.6601","84.6501","84.8205"]
  adrg_ss1=[]
  adrg_ss2=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合IB35入组条件，匹配规则：主手术匹配、某一手术匹配')
    return True