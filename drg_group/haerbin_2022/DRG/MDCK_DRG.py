from drg_group.haerbin_2022.Base import has_mcc,has_cc,intersect
def KB19_group(record):
  return True
def KC19_group(record):
  return True
def KE19_group(record):
  return True
def KJ19_group(record):
  return True
def KR19_group(record):
  return True
def KS11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def KU11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def KZ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def KD1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def KD2A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def KT1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def KV1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def KS1B_group(record):
  return True
def KU1B_group(record):
  return True
def KZ1B_group(record):
  return True
def KD15_group(record):
  return True
def KD25_group(record):
  return True
def KT15_group(record):
  return True
def KV15_group(record):
  return True

