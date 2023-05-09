from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCD_DRG

def group(record):
  adrg_zd=["C13.900","C32.101","C32.900","D14.102","H60.300x002","H65.900x001","H81.303","H81.901","H90.300","H90.500","J02.900","J03.901","J04.000","J04.002","J04.100","J05.100","J06.000","J06.900","J36.x00","J36.x00x001","J36.x00x003","J37.000","J37.001","J38.002","J38.102","J38.304","J38.705","J38.710","J38.715","J39.220","K04.401","K12.200x011","K12.202","K12.204","Q18.003","R04.000","S01.500x001","T16.x00","T16.x00x001","T17.101","T17.200","T18.000"]
  adrg_zd1=[]
  adrg_ss=["21.0100","21.0200","21.0300x003","21.0300x004","21.0301","21.0302","27.9201","31.4200x001","31.4200x003","31.4201","31.4300x002","31.4301","98.0101","98.1100x001","98.1201","98.1300x001"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合DK1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCD_DRG.DK19_group(record):
      return 'DK19'

    return 'DK1'
  else:
    return ''

