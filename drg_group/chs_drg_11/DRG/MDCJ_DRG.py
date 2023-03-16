from drg_group.chs_drg_11.Base import has_mcc,has_cc,intersect
def JA19_group(record):
  return True
def JA29_group(record):
  return True
def JB19_group(record):
  return True
def JB29_group(record):
  return True
def JB39_group(record):
  return True
def JC19_group(record):
  return True
def JD29_group(record):
  return True
def JR19_group(record):
  return True
def JS29_group(record):
  return True
def JT19_group(record):
  return True
def JV19_group(record):
  return True
def JV29_group(record):
  return True
def JZ19_group(record):
  return True
def JS11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def JU11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def JD13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def JJ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def JR23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def JS13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def JU13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def JD15_group(record):
  return True
def JJ15_group(record):
  return True
def JR25_group(record):
  return True
def JS15_group(record):
  return True
def JU15_group(record):
  return True

