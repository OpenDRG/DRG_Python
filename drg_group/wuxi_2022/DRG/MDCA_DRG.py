from drg_group.wuxi_2022.Base import messages,has_mcc,has_cc,intersect
def AG19_group(record):
  return True
def AF19_group(record):
  return True
def AG29_group(record):
  return True
def AH11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])

