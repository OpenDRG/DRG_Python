from drg_group.changsha_2023.Base import has_mcc,has_cc,intersect
def KB19_group(record):
  return True
def KC19_group(record):
  return True
def KE19_group(record):
  return True
def KR19_group(record):
  return True
def KV19_group(record):
  return True
def KD11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def KD21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def KJ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def KS11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def KT11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def KU11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def KZ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def KS13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def KZ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def KD15_group(record):
  return True
def KD25_group(record):
  return True
def KJ15_group(record):
  return True
def KS15_group(record):
  return True
def KT15_group(record):
  return True
def KU15_group(record):
  return True
def KZ15_group(record):
  return True

