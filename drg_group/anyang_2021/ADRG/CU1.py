from drg_group.anyang_2021.Base import message,intersect,SS_VALID
from drg_group.anyang_2021.DRG import MDCC_DRG

def group(record):
  adrg_zd=["A06.801","A18.500x002","A18.500x005+H32.0*","A18.500x008+H13.1*","A18.500x010+H32.0*","A18.500x013+H22.0*","A18.501+H32.0*","A18.502+H32.0*","A18.503+H48.8*","A18.504+H22.0*","A18.506+H19.2*","A18.507+H19.0*","A30.900x006+H19.2*","A30.900x007+H32.0*","A36.800x006+H22.8*","A36.801+H13.1*","A39.801+H13.1*","A50.000x001+H32.0*","A50.001+H58.8*","A50.300+H58.8*","A50.300x002+H19.2*","A50.300x003+H32.0*","A50.301+H19.2*","A51.400x005+H22.0*","A51.402+H22.0*","A51.403+H32.0*","A51.404+H58.8*","A51.405+H58.8*","A52.100x012+H48.1*","A52.102+H58.0*","A52.700x015+H58.8*","A52.701+H22.0*","A52.702+H32.0*","A52.708+H58.8*","A54.300x002+H19.2*","A54.302+H13.1*","A54.303+H22.0*","A71.000","A71.100","A71.100x002","A71.100x003","A71.101","A71.900","A74.000+H13.1*","B00.500x002+H58.8*","B00.500x005+H19.1*","B00.500x007+H22.0*","B00.500x009+H22.0*","B00.501+H19.1*","B00.502+H13.1*","B00.503+H58.8*","B00.504+H03.1*","B00.504+H03.1*","B00.505+H22.0*","B00.506+H22.0*","B00.506+H22.0*","B00.507+H19.1*","B00.507+H19.1*","B00.508+H22.0*","B00.509+H03.1*","B02.301+H58.8*","B02.302+H19.2*","B02.303+H03.1*","B02.304+H13.1*","B02.305+H22.0*","B02.306+H22.0*","B02.307+H19.2*","B02.308+H19.0*","B05.800x001+H19.2*","B07.x02","B25.800x002+H19.2*","B25.802+H32.0*","B26.801+H13.1*","B30.000+H19.2*","B30.001+H19.2*","B30.100+H13.1*","B30.200+H13.1*","B30.201+H13.1*","B30.300+H13.1*","B30.301+H13.1*","B30.800+H13.1*","B30.900","B37.807+H48.8*","B49.x03+H19.2*","B49.x04+H19.2*","B58.000","B58.001+H32.0*","B60.100x002+H13.1*","B60.100x003+H19.2*","B60.100x004+H19.2*","B87.200x001+H58.8*","B89.x02+H06.1*","D86.800x003+H22.1*","H00.003","H05.000","H05.000x002","H05.000x006","H05.001","H05.002","H05.004","H05.005","H05.100","H05.100x003","H05.100x005","H05.101","H05.102","H05.103","H05.104","H05.205","H10.300","H16.000","H16.000x001","H16.000x006","H16.000x010","H16.001","H16.002","H16.003","H16.004","H16.005","H16.006","H16.007","H16.101","H16.102","H16.103","H16.200","H16.200x001","H16.200x006","H16.201","H16.203","H16.204","H16.205","H16.300x004","H16.300x005","H16.301","H16.302","H16.303","H16.800x003","H16.800x005","H16.800x006","H16.800x010","H16.800x014","H16.801","H16.802","H16.803","H16.804","H16.805","H16.900","H20.101","H20.102","H20.200","H20.800","H20.801","H20.804","H20.900","H20.901","H44.000","H44.000x002","H44.000x005","H44.000x007","H44.001","H44.002","H44.003","H44.100","H44.100x003","H44.101","H44.102","H44.103","H44.104","H59.810","H59.811","H59.812","M35.005+H19.3*"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合CU1入组条件，匹配规则：主诊断匹配')
    
    if MDCC_DRG.CU1A_group(record):
      return 'CU12'

    if MDCC_DRG.CU15_group(record):
      return 'CU15'

    return ''
  else:
    return ''

