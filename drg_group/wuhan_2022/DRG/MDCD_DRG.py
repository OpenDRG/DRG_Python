from drg_group.wuhan_2022.Base import has_mcc,has_cc,intersect
def DA19_group(record):
  return True
def DB19_group(record):
  return True
def DB29_group(record):
  return True
def DC19_group(record):
  return True
def DC29_group(record):
  return True
def DD19_group(record):
  return True
def DD29_group(record):
  return True
def DE29_group(record):
  return True
def DG19_group(record):
  return True
def DG29_group(record):
  return True
def DG39_group(record):
  return True
def DS19_group(record):
  return True
def DV19_group(record):
  return True
def DW19_group(record):
  return True
def DJ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def DK11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def DR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def DT21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def DU11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def DZ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def DE1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def DT1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def DK13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def DT23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def DU13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def DZ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def DJ1B_group(record):
  return True
def DR1B_group(record):
  return True
def DE15_group(record):
  return True
def DK15_group(record):
  return True
def DT15_group(record):
  return True
def DT25_group(record):
  return True
def DU15_group(record):
  return True
def DZ15_group(record):
  return True

