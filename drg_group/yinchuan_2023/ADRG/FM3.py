from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=["I07.100","I10.x05","I20.000","I20.002","I20.101","I20.800x007","I20.801","I20.900","I21.001","I21.004","I21.103","I21.300x004","I21.401","I21.900","I24.000x003","I24.901","I25.100x003","I25.102","I25.103","I25.400x005","I25.500","I27.200x002","I27.200x012","I27.201","I27.202","I27.801","I28.801","I45.102","I45.600","I45.600x003","I45.600x004","I45.600x005","I47.100x004","I47.100x005","I47.101","I47.102","I47.104","I47.109","I47.203","I48.000","I48.100","I49.100x001","I49.300x002","I49.301","I50.001","I50.908","I71.203","Q21.000","Q21.101","R00.001","R07.400","R94.300x011","T82.504"]
  adrg_zd1=[]
  adrg_ss=["00.2400x001","00.5902","37.2100","37.2600x001","37.2700","88.5000","88.5201","88.5202","88.5302","88.5500x002","88.5701"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合FM3入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCF_DRG.FM39_group(record):
      return 'FM39'

    return 'FM3'
  else:
    return ''

