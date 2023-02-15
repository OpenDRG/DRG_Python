from drg_group.wuhan_2022.Base import has_mcc,has_cc,intersect
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
def IE19_group(record):
  return True
def IF29_group(record):
  return True
def IF49_group(record):
  return True
def IR19_group(record):
  return True
def IR39_group(record):
  return True
def IU19_group(record):
  return True
def IU29_group(record):
  return True
def IV19_group(record):
  return True
def IZ29_group(record):
  return True
def IB31_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def IF51_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def IG11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def IH11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def IJ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def IR21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def IT11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def IT21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def IU31_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def IZ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def ID1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def IF1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def IF3A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def IS1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def IS2A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def IT3A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def IB33_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def IG13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def IF5B_group(record):
  return True
def IH1B_group(record):
  return True
def IJ1B_group(record):
  return True
def IR2B_group(record):
  return True
def IT1B_group(record):
  return True
def IT2B_group(record):
  return True
def IU3B_group(record):
  return True
def IZ1B_group(record):
  return True
def IB35_group(record):
  return True
def ID15_group(record):
  return True
def IF15_group(record):
  return True
def IF35_group(record):
  return True
def IG15_group(record):
  return True
def IS15_group(record):
  return True
def IS25_group(record):
  return True
def IT35_group(record):
  return True

