from drg_group.haerbin_2022.Base import has_mcc,has_cc,intersect
def VB19_group(record):
  return True
def VC19_group(record):
  return True
def VR19_group(record):
  return True
def VS19_group(record):
  return True
def VT19_group(record):
  return True
def VZ19_group(record):
  return True
def VS21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def VJ1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def VS23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def VJ15_group(record):
  return True
def VS25_group(record):
  return True

