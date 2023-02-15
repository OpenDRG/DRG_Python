from drg_group.beijing_2022.Base import has_mcc,has_cc,intersect
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
def DE29_group(record):
  return True
def DG19_group(record):
  return True
def DT29_group(record):
  return True
def DW19_group(record):
  return True
def DZ19_group(record):
  return True
def DR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def DT11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def DU11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def DA13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def DB33_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def DE13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def DG23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def DJ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def DK13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def DR13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def DS13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def DU13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def DV13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def DA15_group(record):
  return True
def DB35_group(record):
  return True
def DE15_group(record):
  return True
def DG25_group(record):
  return True
def DJ15_group(record):
  return True
def DK15_group(record):
  return True
def DR15_group(record):
  return True
def DS15_group(record):
  return True
def DT15_group(record):
  return True
def DU15_group(record):
  return True
def DV15_group(record):
  return True
def DC2D_group(record):
  return record.age<=6
def DC29_group(record):
  return True

