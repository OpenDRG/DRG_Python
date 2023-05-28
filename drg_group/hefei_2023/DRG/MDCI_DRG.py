from drg_group.hefei_2023.Base import has_mcc,has_cc,intersect
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
def IS29_group(record):
  return True
def IT19_group(record):
  return True
def IT39_group(record):
  return True
def IU29_group(record):
  return True
def IZ19_group(record):
  return True
def IZ29_group(record):
  return True
def IB11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def IE11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def IF11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def IF21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def IF31_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def IJ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def IS11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def IT21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def IU31_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def IB13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def ID13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def IE13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def IF13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def IF23_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def IF33_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def IG13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def IJ13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def IS13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def IT23_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def IU13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def IU33_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def IV13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def IB15_group(record):
  return True
def ID15_group(record):
  return True
def IE15_group(record):
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
def IS15_group(record):
  return True
def IT25_group(record):
  return True
def IU15_group(record):
  return True
def IU35_group(record):
  return True
def IV15_group(record):
  return True

