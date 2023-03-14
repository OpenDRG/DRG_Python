from drg_group.xian_2020.Base import has_mcc,has_cc,intersect
def GB19_group(record):
  return True
def GB29_group(record):
  return True
def GC19_group(record):
  return True
def GC29_group(record):
  return True
def GD19_group(record):
  return True
def GD29_group(record):
  return True
def GE19_group(record):
  return True
def GF19_group(record):
  return True
def GF29_group(record):
  return True
def GG19_group(record):
  return True
def GK19_group(record):
  return True
def GK29_group(record):
  return True
def GK39_group(record):
  return True
def GS19_group(record):
  return True
def GU19_group(record):
  return True
def GU29_group(record):
  return True
def GW19_group(record):
  return True
def GZ19_group(record):
  return True
def GE21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def GJ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def GR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def GT11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def GV11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def GE23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def GJ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def GR13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def GT13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def GV13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def GE25_group(record):
  return True
def GJ15_group(record):
  return True
def GR15_group(record):
  return True
def GT15_group(record):
  return True
def GV15_group(record):
  return True

