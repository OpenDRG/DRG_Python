from drg_group.wuhan_2022.Base import has_mcc,has_cc,intersect
def FB19_group(record):
  return True
def FB29_group(record):
  return True
def FC19_group(record):
  return True
def FC29_group(record):
  return True
def FC39_group(record):
  return True
def FD19_group(record):
  return True
def FD39_group(record):
  return True
def FF19_group(record):
  return True
def FK19_group(record):
  return True
def FK29_group(record):
  return True
def FK39_group(record):
  return True
def FL19_group(record):
  return True
def FM19_group(record):
  return True
def FM29_group(record):
  return True
def FN19_group(record):
  return True
def FR29_group(record):
  return True
def FR39_group(record):
  return True
def FS19_group(record):
  return True
def FT29_group(record):
  return True
def FT39_group(record):
  return True
def FU19_group(record):
  return True
def FV29_group(record):
  return True
def FV49_group(record):
  return True
def FW19_group(record):
  return True
def FB31_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FE11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FF31_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FN21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FR41_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FT11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FU21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FV11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FW21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FZ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FD2A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FF2A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FF4A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FJ1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FL2A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FM3A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FV3A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FB33_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FF33_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FU23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FZ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FE1B_group(record):
  return True
def FN2B_group(record):
  return True
def FR1B_group(record):
  return True
def FR4B_group(record):
  return True
def FT1B_group(record):
  return True
def FV1B_group(record):
  return True
def FW2B_group(record):
  return True
def FB35_group(record):
  return True
def FD25_group(record):
  return True
def FF25_group(record):
  return True
def FF35_group(record):
  return True
def FF45_group(record):
  return True
def FJ15_group(record):
  return True
def FL25_group(record):
  return True
def FM35_group(record):
  return True
def FU25_group(record):
  return True
def FV35_group(record):
  return True
def FZ15_group(record):
  return True

