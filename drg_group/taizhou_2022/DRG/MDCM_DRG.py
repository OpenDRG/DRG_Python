from drg_group.taizhou_2022.Base import messages,has_mcc,has_cc,intersect
def MD19_group(record):
  return True
def MA19_group(record):
  return True
def MB19_group(record):
  return True
def MS19_group(record):
  return True
def MC19_group(record):
  return True
def MJ19_group(record):
  return True
def MZ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def MR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def MZ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def MR13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def MZ15_group(record):
  return True
def MR15_group(record):
  return True

