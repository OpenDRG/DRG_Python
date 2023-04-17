from drg_group.changzhou_2022.Base import has_mcc,has_cc,intersect
def KT10_group(record):
    return record.age<=17
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
def KV19_group(record):
  return True
def KS17_group(record):
  return record.inHospitalTime<5 and record.leavingType in ['2','5']
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
def KJ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def KS13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def KT13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def KU13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def KZ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
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

