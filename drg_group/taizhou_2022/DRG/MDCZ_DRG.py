from drg_group.taizhou_2022.Base import has_mcc,has_cc,intersect
def ZC19_group(record):
  return True
def ZD19_group(record):
  return True
def ZJ19_group(record):
  return True
def ZB11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def ZZ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def ZB13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def ZZ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def ZB15_group(record):
  return True
def ZZ15_group(record):
  return True

