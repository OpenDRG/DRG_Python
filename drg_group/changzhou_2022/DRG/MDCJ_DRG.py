from drg_group.changzhou_2022.Base import has_mcc,has_cc,intersect
def JJ10_group(record):
    return record.age<=17
def JU10_group(record):
    return record.age<=17
def JZ10_group(record):
    return record.age<=17
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
def JD29_group(record):
  return True
def JR19_group(record):
  return True
def JR29_group(record):
  return True
def JS29_group(record):
  return True
def JU19_group(record):
  return True
def JV29_group(record):
  return True
def JZ19_group(record):
  return True
def JC11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def JD11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def JJ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def JS11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def JT11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def JV11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def JD13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def JJ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def JS13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def JT13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def JV13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def JC15_group(record):
  return True
def JD15_group(record):
  return True
def JJ15_group(record):
  return True
def JS15_group(record):
  return True
def JT15_group(record):
  return True
def JV15_group(record):
  return True

