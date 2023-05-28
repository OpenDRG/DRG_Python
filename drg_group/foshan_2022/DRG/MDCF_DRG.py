from drg_group.foshan_2022.Base import has_mcc,has_cc,intersect
def FM20_group(record):
    return record.icuHours>120
def FR10_group(record):
    return record.icuHours>120
def FR20_group(record):
    return record.icuHours>120
def FR30_group(record):
    return record.icuHours>120
def FR22_group(record):
  return 1<=record.icuHours<=120
def FR32_group(record):
  return 1<=record.icuHours<=120
def FB19_group(record):
  return True
def FB29_group(record):
  return True
def FC19_group(record):
  return True
def FD19_group(record):
  return True
def FD29_group(record):
  return True
def FD39_group(record):
  return True
def FE19_group(record):
  return True
def FE29_group(record):
  return True
def FF19_group(record):
  return True
def FF29_group(record):
  return True
def FJ19_group(record):
  return True
def FK19_group(record):
  return True
def FK29_group(record):
  return True
def FL19_group(record):
  return True
def FL39_group(record):
  return True
def FM19_group(record):
  return True
def FN19_group(record):
  return True
def FN29_group(record):
  return True
def FR39_group(record):
  return True
def FT29_group(record):
  return True
def FT49_group(record):
  return True
def FK31_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FL21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FM31_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FM41_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FP11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FR21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FR41_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FT11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FT31_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FU11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FV11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FW11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FW21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FZ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FF33_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FM23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FU23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FV23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FV33_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FL23_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def FM33_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def FR23_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def FT13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def FU13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def FZ13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def FK33_group(record):
  return True
def FM43_group(record):
  return True
def FP13_group(record):
  return True
def FR13_group(record):
  return True
def FR43_group(record):
  return True
def FT33_group(record):
  return True
def FV13_group(record):
  return True
def FW13_group(record):
  return True
def FW23_group(record):
  return True
def FF35_group(record):
  return True
def FL25_group(record):
  return True
def FM25_group(record):
  return True
def FM35_group(record):
  return True
def FR25_group(record):
  return True
def FT15_group(record):
  return True
def FU15_group(record):
  return True
def FU25_group(record):
  return True
def FV25_group(record):
  return True
def FV35_group(record):
  return True
def FZ15_group(record):
  return True

