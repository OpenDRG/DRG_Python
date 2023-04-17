from drg_group.changzhou_2022.Base import has_mcc,has_cc,intersect
def FT10_group(record):
    return record.age<=17
def FT30_group(record):
    return record.age<=17
def FB19_group(record):
  return True
def FB29_group(record):
  return True
def FB39_group(record):
  return True
def FC19_group(record):
  return True
def FC29_group(record):
  return True
def FC39_group(record):
  return True
def FD19_group(record):
  return True
def FD29_group(record):
  return True
def FD39_group(record):
  return True
def FE19_group(record):
  return True
def FF19_group(record):
  return True
def FF49_group(record):
  return True
def FJ19_group(record):
  return True
def FK19_group(record):
  return True
def FK29_group(record):
  return True
def FK39_group(record):
  return True
def FL19_group(record):
  return True
def FL29_group(record):
  return True
def FM19_group(record):
  return True
def FM29_group(record):
  return True
def FM39_group(record):
  return True
def FN29_group(record):
  return True
def FS19_group(record):
  return True
def FV29_group(record):
  return True
def FV49_group(record):
  return True
def FR17_group(record):
  return record.inHospitalTime<5 and record.leavingType in ['2','5']
def FR37_group(record):
  return record.inHospitalTime<5 and record.leavingType in ['2','5']
def FR47_group(record):
  return record.inHospitalTime<5 and record.leavingType in ['2','5']
def FU17_group(record):
  return record.inHospitalTime<5 and record.leavingType in ['2','5']
def FU27_group(record):
  return record.inHospitalTime<5 and record.leavingType in ['2','5']
def FW17_group(record):
  return record.inHospitalTime<5 and record.leavingType in ['2','5']
def FW27_group(record):
  return record.inHospitalTime<5 and record.leavingType in ['2','5']
def FZ17_group(record):
  return record.inHospitalTime<5 and record.leavingType in ['2','5']
def FF21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FF31_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FN11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FR21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FR31_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FR41_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FT11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FT21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FT31_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FU11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FU21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FV11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FW11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FW21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FZ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FF23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FF33_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FN13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FR13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FR23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FR33_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FR43_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FT13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FT23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FT33_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FU13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FU23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FV13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FV33_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FW13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FW23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FZ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FF25_group(record):
  return True
def FF35_group(record):
  return True
def FN15_group(record):
  return True
def FR15_group(record):
  return True
def FR25_group(record):
  return True
def FR35_group(record):
  return True
def FR45_group(record):
  return True
def FT15_group(record):
  return True
def FT25_group(record):
  return True
def FT35_group(record):
  return True
def FU15_group(record):
  return True
def FU25_group(record):
  return True
def FV15_group(record):
  return True
def FV35_group(record):
  return True
def FW15_group(record):
  return True
def FW25_group(record):
  return True
def FZ15_group(record):
  return True

