from drg_group.handan_2022.Base import has_mcc,has_cc,intersect
def HC19_group(record):
  return True
def HC29_group(record):
  return True
def HC39_group(record):
  return True
def HR19_group(record):
  return True
def HS19_group(record):
  return True
def HS29_group(record):
  return True
def HS39_group(record):
  return True
def HT19_group(record):
  return True
def HT29_group(record):
  return True
def HZ39_group(record):
  return True
def HB11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def HJ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def HK11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def HL11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def HU11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def HZ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def HZ21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def HK13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def HL23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def HB15_group(record):
  return True
def HJ15_group(record):
  return True
def HK15_group(record):
  return True
def HL15_group(record):
  return True
def HL25_group(record):
  return True
def HU15_group(record):
  return True
def HZ15_group(record):
  return True
def HZ25_group(record):
  return True

