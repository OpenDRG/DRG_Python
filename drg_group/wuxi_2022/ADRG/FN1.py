from drg_group.wuxi_2022.Base import message,intersect,SS_VALID
from drg_group.wuxi_2022.DRG import MDCF_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["00.0102","00.0300","00.5500x009","00.5500x010","00.5500x011","00.5500x012","00.5500x013","00.5500x014","00.5500x015","00.5500x016","00.5500x017","00.5501","00.5502","00.5800","00.6000","00.6300x006","07.4200x002","17.5600x001","38.2300","38.2500","38.7x03","38.7x04","38.9300x901","39.5000x011","39.5000x013","39.5000x014","39.5000x019","39.5000x021","39.5000x024","39.5000x025","39.5000x026","39.5000x029","39.5000x030","39.5000x031","39.5000x041","39.5001","39.5002","39.5003","39.5004","39.5005","39.5006","39.5007","39.5008","39.5009","39.5010","39.5011","39.5012","39.5013","39.5014","39.5015","39.5016","39.5017","39.5900x025","39.5900x026","39.5900x027","39.5900x028","39.5900x029","39.7200x001","39.7200x017","39.7201","39.7300x006","39.7800x005","39.7900x007","39.7900x009","39.7900x013","39.7900x014","39.7900x017","39.7900x019","39.7900x020","39.7900x021","39.7900x022","39.7900x023","39.7900x024","39.7900x025","39.7900x027","39.7900x028","39.7900x029","39.7900x031","39.7900x032","39.7900x033","39.7900x034","39.7900x035","39.7900x036","39.7900x037","39.7900x038","39.7900x039","39.7900x040","39.7900x041","39.7900x042","39.7900x043","39.7900x044","39.7900x045","39.7900x046","39.7900x047","39.7900x049","39.7900x051","39.7900x052","39.7900x053","39.7900x054","39.7900x055","39.7900x056","39.7900x057","39.7900x058","39.7900x059","39.7900x060","39.7900x061","39.7900x062","39.7900x063","39.7900x064","39.7900x065","39.7900x066","39.7900x067","39.7900x068","39.7900x069","39.7900x070","39.7900x071","39.7900x072","39.7900x073","39.7900x074","39.7900x075","39.7900x075","39.7900x402","39.7900x515","39.7900x516","39.7900x518","39.7900x625","39.7900x626","39.7900x703","39.7900x704","39.7900x809","39.7901","39.7902","39.7903","39.7904","39.7905","39.7906","39.7907","39.7910","39.9000x010","39.9000x011","39.9000x012","39.9000x016","39.9000x017","39.9000x019","39.9000x020","39.9000x021","39.9000x023","39.9000x024","39.9000x025","39.9000x026","39.9000x028","39.9000x029","39.9000x030","39.9000x031","39.9000x032","39.9000x033","39.9000x034","39.9000x035","39.9000x036","39.9000x038","39.9000x039","39.9000x040","39.9000x041","39.9001","39.9003","39.9004","39.9005","39.9006","39.9007","39.9008","39.9009","39.9010","39.9011","39.9012","39.9013","39.9014","39.9015","39.9016","39.9100x004","39.9100x005","39.9100x006","39.9100x007","39.9100x008","39.9100x009","39.9100x010","44.4400x001","88.4600","88.6800"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合FN1入组条件，匹配规则：主手术匹配')
    
    if MDCF_DRG.FN19_group(record):
      return 'FN19'

  return ''
