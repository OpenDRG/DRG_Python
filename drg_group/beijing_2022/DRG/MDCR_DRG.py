from drg_group.beijing_2022.Base import messages,has_mcc,has_cc,intersect
def RA49_group(record):
  return True
def RT29_group(record):
  return True
def RA39_group(record):
  return True
def RG19_group(record):
  return True
def RW11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def RA11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def RW21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def RR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def RS11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def RU11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def RB11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def RD11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def RT11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def RA21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def RB21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def RA23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def RS23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def RR13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def RS13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def RA25_group(record):
  return True
def RT15_group(record):
  return True
def RB25_group(record):
  return True
def RA15_group(record):
  return True
def RU15_group(record):
  return True
def RB15_group(record):
  return True
def RW15_group(record):
  return True
def RW25_group(record):
  return True
def RD15_group(record):
  return True
def RS25_group(record):
  return True
def RR15_group(record):
  return True
def RS15_group(record):
  return True
def RC12_group(record):
  return record.inHospitalTime>=13
def RC14_group(record):
  return 6<=record.inHospitalTime<13
def RC16_group(record):
  return 2<=record.inHospitalTime<6
def RC18_group(record):
  return record.inHospitalTime==1
def RC22_group(record):
  return record.inHospitalTime>=14
def RC24_group(record):
  return 7<=record.inHospitalTime<14
def RC26_group(record):
  return 3<=record.inHospitalTime<7
def RC28_group(record):
  return 1<=record.inHospitalTime<3
def RE12_group(record):
  return record.inHospitalTime>=14
def RE14_group(record):
  return 7<=record.inHospitalTime<14
def RE16_group(record):
  return 1<=record.inHospitalTime<7

