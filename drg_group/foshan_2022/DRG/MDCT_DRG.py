from drg_group.foshan_2022.Base import has_mcc,has_cc,intersect
def TR18_group(record):
  return record.inHospitalTime>60
def TS18_group(record):
  return record.inHospitalTime>60
def TU18_group(record):
  return record.inHospitalTime>60
def TW18_group(record):
  return record.inHospitalTime>60
def TR19_group(record):
  return True
def TR29_group(record):
  return True
def TS19_group(record):
  return True
def TT19_group(record):
  return True
def TT29_group(record):
  return True
def TU19_group(record):
  return True
def TV19_group(record):
  return True
def TW19_group(record):
  return True
def TB13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def TS23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def TB15_group(record):
  return True
def TS25_group(record):
  return True

