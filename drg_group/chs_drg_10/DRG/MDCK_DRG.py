from drg_group.chs_drg_10.Base import has_mcc,has_cc,intersect
def KB19_group(record):
  return True
def KC19_group(record):
  return True
def KD19_group(record):
  return True
def KD29_group(record):
  return True
def KE19_group(record):
  return True
def KF19_group(record):
  return True
def KR19_group(record):
  return True
def KS19_group(record):
  return True
def KV19_group(record):
  return True
def KZ19_group(record):
  return True
def KJ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def KT11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def KU11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def KJ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def KT13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def KU13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def KJ15_group(record):
  return True
def KT15_group(record):
  return True
def KU15_group(record):
  return True

