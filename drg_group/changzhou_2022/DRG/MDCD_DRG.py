from drg_group.changzhou_2022.Base import has_mcc,has_cc,intersect
def DJ10_group(record):
    return record.age<=17
def DU10_group(record):
    return record.age<=17
def DZ10_group(record):
    return record.age<=17
def DA19_group(record):
  return True
def DB19_group(record):
  return True
def DB29_group(record):
  return True
def DC19_group(record):
  return True
def DD19_group(record):
  return True
def DD29_group(record):
  return True
def DE19_group(record):
  return True
def DE29_group(record):
  return True
def DG19_group(record):
  return True
def DG39_group(record):
  return True
def DK19_group(record):
  return True
def DS19_group(record):
  return True
def DT19_group(record):
  return True
def DT29_group(record):
  return True
def DV19_group(record):
  return True
def DR17_group(record):
  return record.inHospitalTime<5 and record.leavingType in ['2','5']
def DC21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def DG21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def DJ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def DR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def DU11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def DW11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def DZ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def DC23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def DG23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def DJ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def DR13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def DU13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def DW13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def DZ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def DC25_group(record):
  return True
def DG25_group(record):
  return True
def DJ15_group(record):
  return True
def DR15_group(record):
  return True
def DU15_group(record):
  return True
def DW15_group(record):
  return True
def DZ15_group(record):
  return True

