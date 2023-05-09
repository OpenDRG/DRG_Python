from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCE_DRG

def group(record):
  adrg_zd=["C33.x00","C34.000","C34.000x002","C34.000x003","C34.001","C34.100x003","C34.100x004","C34.101","C34.201","C34.300x003","C34.300x004","C34.301","C34.800","C34.801","C34.802","C34.803","C34.900x001","C34.900x004","C34.900x005","C34.900x006","C34.900x008","C34.901","C37.x00","C38.100","C38.200","C38.300","C38.400","C45.000","C49.300x003","C76.100","C76.100x003","C77.103","C78.000","C78.001","C78.100","C78.200","C78.201","C79.800x809","C79.807","C79.810","D02.200x002","D14.300x001","D15.000","D15.200","D15.200x001","D15.200x002","D17.400x001","D18.100x015","D18.100x025","D36.706","D36.717","D38.100x001","D38.101","D38.201","D38.300x002","D38.301","D38.400x001","D38.401","J98.405","Q85.901"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合ER1入组条件，匹配规则：主诊断匹配')
    
    if MDCE_DRG.ER13_group(record):
      return 'ER13'

    if MDCE_DRG.ER15_group(record):
      return 'ER15'

    return 'ER1'
  else:
    return ''

