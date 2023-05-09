from drg_group.yunnan_2022.Base import has_mcc,has_cc,intersect
def YC19_group(record):
  return True
def YR29_group(record):
  return True
def YR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def YR13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def YR15_group(record):
  return True

