from drg_group.zhejiang_2022.Base import has_mcc,has_cc,intersect
def ZB11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def ZC11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def ZD11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def ZJ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def ZZ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def ZB1B_group(record):
  return True
def ZC1B_group(record):
  return True
def ZD1B_group(record):
  return True
def ZJ1B_group(record):
  return True
def ZZ1B_group(record):
  return True

