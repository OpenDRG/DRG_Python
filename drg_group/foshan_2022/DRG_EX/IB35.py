from drg_group.foshan_2022.Base import message,intersect,has_mcc,has_cc,SS_VALID

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["03.0900x009","03.0900x022","03.0900x027","03.0908","03.0913","03.0914","03.0915","03.2100x001","03.3101","03.4x07","03.6x01","03.6x02","03.6x03","03.9600","77.2904","77.6905","77.6906","78.4904","80.4900x002","80.5100x026","80.5100x030","80.5100x031","80.5100x032","80.5100x033","80.5100x034","80.5100x037","80.5103","80.5106","80.5110","80.5111","80.5400x001","80.7901","81.6500","81.6600x001","81.6600x002","81.6600x003","81.6601","84.6501","84.8205"]
  adrg_ss1=[]
  adrg_ss2=[]
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合IB35入组条件，匹配规则：主手术匹配')
    return True