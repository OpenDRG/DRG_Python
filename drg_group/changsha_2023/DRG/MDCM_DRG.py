from drg_group.changsha_2023.Base import has_mcc,has_cc,intersect
def MA19_group(record):
  return True
def MC19_group(record):
  return True
def MR19_group(record):
  return True
def MD1A_CS_group(record):
  return int(record.age)<=6
def MJ1A_CS_group(record):
  return int(record.age)<=6
def MD1B_CS_group(record):
  return True
def MJ1B_CS_group(record):
  return True
def MB11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def MS11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def MZ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def MS13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def MB15_group(record):
  return True
def MS15_group(record):
  return True
def MZ15_group(record):
  return True

