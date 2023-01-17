from drg_group.wuxi_2022.Base import messages,has_mcc,has_cc,intersect
def ZD19_group(record):
  return True
def ZB19_group(record):
  return True
def ZC11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def ZZ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def ZJ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def ZZ15_group(record):
  return True
def ZJ15_group(record):
  return True
def ZC15_group(record):
  return True

