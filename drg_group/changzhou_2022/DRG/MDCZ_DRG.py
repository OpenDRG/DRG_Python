from drg_group.changzhou_2022.Base import has_mcc,has_cc,intersect
def ZB19_group(record):
  return True
def ZD19_group(record):
  return True
def ZZ17_group(record):
  return record.inHospitalTime<5 and record.leavingType in ['2','5']
def ZJ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def ZZ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def ZJ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def ZZ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def ZJ15_group(record):
  return True
def ZZ15_group(record):
  return True
def ZC14_group(record):
  return len(record.ssList)>1 and intersect(record.ssList[1:],['31.1x00x005','31.2100x001','31.2900x001','31.7400','31.7400x001','96.0400'])
def ZC18_group(record):
  return True

