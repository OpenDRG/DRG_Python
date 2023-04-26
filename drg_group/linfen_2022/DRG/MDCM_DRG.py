from drg_group.linfen_2022.Base import has_mcc,has_cc,intersect
def MA19_group(record):
  return True
def MB19_group(record):
  return True
def MC19_group(record):
  return True
def MD19_group(record):
  return True
def MZ19_group(record):
  return True
def MR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def MS11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def MJ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def MS13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def MJ15_group(record):
  return True
def MR15_group(record):
  return True
def MS15_group(record):
  return True

