from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCB_DRG

def group(record):
  adrg_zd=["D32.020","D33.007","G40.800x004","G45.002","G45.004","G45.100x002","G45.101","G45.800x004","G45.801","G45.900","G58.002","G93.200","G93.402","G93.600","G93.903","G95.901","H49.000","I60.000x003","I60.000x007","I60.101","I60.300","I60.301","I60.600x006","I60.800x002","I60.801","I60.900x004","I61.000x008","I61.004","I61.100x001","I61.100x005","I61.100x006","I61.100x013","I61.100x014","I61.802","I61.902","I61.903","I62.000","I62.101","I62.900x001","I63.200","I63.201","I63.204","I63.207","I63.208","I63.402","I63.501","I63.502","I63.801","I63.900","I63.901","I63.902","I63.903","I63.904","I63.905","I63.906","I63.907","I65.001","I65.002","I65.102","I65.200x001","I65.200x015","I65.201","I65.203","I65.206","I65.207","I66.001","I66.002","I66.101","I66.400","I67.100x005","I67.100x023","I67.101","I67.103","I67.107","I67.108","I67.200","I67.500","I67.803","I69.300x002","I69.300x003","I72.000x035","I72.500x002","I72.600x002","Q28.200","Q28.300x001","Q28.300x007","R42.x00x004","R51.x00","S06.202","S06.600","S06.800x002"]
  adrg_zd1=[]
  adrg_ss=["88.4101","88.4102","88.4103","88.4401"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合BM1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCB_DRG.BM11_group(record):
      return 'BM11'

    if MDCB_DRG.BM15_group(record):
      return 'BM15'

    return 'BM1'
  else:
    return ''

