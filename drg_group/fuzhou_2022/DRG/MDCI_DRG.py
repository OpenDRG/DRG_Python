from drg_group.fuzhou_2022.Base import has_mcc,has_cc,intersect
def IB19_group(record):
  return True
def IB29_group(record):
  return True
def IB39_group(record):
  return True
def IC19_group(record):
  return True
def IC29_group(record):
  return True
def IC39_group(record):
  return True
def IC49_group(record):
  return True
def IE19_group(record):
  return True
def IF49_group(record):
  return True
def IF59_group(record):
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
def IF31_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def IT21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def ID13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def IF13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def IF23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def IF33_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def IG13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def IJ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def IT23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def ID15_group(record):
  return True
def IF15_group(record):
  return True
def IF25_group(record):
  return True
def IF35_group(record):
  return True
def IG15_group(record):
  return True
def IJ15_group(record):
  return True
def IT25_group(record):
  return True

