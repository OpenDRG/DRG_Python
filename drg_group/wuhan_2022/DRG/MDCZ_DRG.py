from drg_group.wuhan_2022.Base import has_mcc,has_cc,intersect
def ZB19_group(record):
  return True
def ZC19_group(record):
  return True
def ZD19_group(record):
  return True
def ZJ19_group(record):
  return True
def ZZ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def ZZ1B_group(record):
  return True

