from drg_group.handan_2022.Base import has_mcc,has_cc,intersect
def IB19_group(record):
  return True
def IB29_group(record):
  return True
def IC19_group(record):
  return True
def IC29_group(record):
  return True
def IC39_group(record):
  return True
def ID19_group(record):
  return True
def IE19_group(record):
  return True
def IF19_group(record):
  return True
def IF29_group(record):
  return True
def IF39_group(record):
  return True
def IF49_group(record):
  return True
def IF59_group(record):
  return True
def IG19_group(record):
  return True
def IH19_group(record):
  return True
def IR19_group(record):
  return True
def IR29_group(record):
  return True
def IS19_group(record):
  return True
def IS29_group(record):
  return True
def IT19_group(record):
  return True
def IT39_group(record):
  return True
def IV19_group(record):
  return True
def IZ19_group(record):
  return True
def IZ29_group(record):
  return True
def IC41_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def IT21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def IU31_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def IB33_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def IC43_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def IJ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def IT23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def IU13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def IU23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def IB35_group(record):
  return True
def IC45_group(record):
  return True
def IJ15_group(record):
  return True
def IT25_group(record):
  return True
def IU15_group(record):
  return True
def IU25_group(record):
  return True
def IU35_group(record):
  return True

