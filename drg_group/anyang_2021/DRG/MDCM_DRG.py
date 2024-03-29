from drg_group.anyang_2021.Base import has_mcc,has_cc,intersect
def MA19_group(record):
  return True
def MB19_group(record):
  return True
def MC19_group(record):
  return True
def MR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def MD1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def MJ1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def MS1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def MZ1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def MR1B_group(record):
  return True
def MD15_group(record):
  return True
def MJ15_group(record):
  return True
def MS15_group(record):
  return True
def MZ15_group(record):
  return True

