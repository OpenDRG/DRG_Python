from drg_group.yancheng_2023.Base import has_mcc,has_cc,intersect
def ZB19_group(record):
  return True
def ZD19_group(record):
  return True
def ZC11_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def ZJ11_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def ZZ11_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def ZC15_group(record):
  return True
def ZJ15_group(record):
  return True
def ZZ15_group(record):
  return True

