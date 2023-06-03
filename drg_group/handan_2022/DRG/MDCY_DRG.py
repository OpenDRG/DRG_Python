from drg_group.handan_2022.Base import has_mcc,has_cc,intersect
def YR19_group(record):
  return True
def YR29_group(record):
  return True
def YC11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def YC13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def YC15_group(record):
  return True

