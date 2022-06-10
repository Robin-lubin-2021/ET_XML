'''
将读取的包含‘P_ARTICLE_PARTNR’、‘P_ARTICLE_TYPENR’、‘P_ARTICLE_ORDERNR’的sourcedata.json
转换生成包含字典模板并更新P_ARTICLE_PARTNR’、‘P_ARTICLE_TYPENR’、‘P_ARTICLE_ORDERNR’值的data.json文件。
'''
#输入json模块
import json

#字典模板常量
LibTemplate = {'P_ARTICLE_PARTTYPE':'1',
     'P_ARTICLE_PRODUCTTOPGROUP':'1',
     'P_ARTICLE_PRODUCTGROUP':'0',
     'P_ARTICLE_PRODUCTSUBGROUP':'0',
     'P_ARTICLE_CRAFT_ELECTRICAL':'1',
     'P_ARTICLE_CRAFT_FLUID':'0',
     'P_ARTICLE_CRAFT_MECHANICS':'0',
     'P_ARTICLE_CRAFT_PROCESS':'0',
     'P_ARTICLE_CRAFT_HYDRAULICS':'0',
     'P_ARTICLE_CRAFT_PNEUMATICS':'0',
     'P_ARTICLE_CRAFT_LUBRICATION':'0',
     'P_ARTICLE_CRAFT_COOLING':'0',
     'P_ARTICLE_CRAFT_COOLINGLUBRICANT':'0',
     'P_ARTICLE_CRAFT_GASTECHNOLOGY':'0',
     'P_ARTICLE_CRAFT_FLUID_UNDEFINED':'0',
     'P_ARTICLE_PARTNR':'',
     'P_ARTICLE_DISCONTINUED':'0',
     'P_ARTICLE_ERPNR':'',
     'P_ARTICLE_TYPENR':'',
     'P_ARTICLE_UNIQUEID':'',
     'P_ARTICLE_DESCR1':'de_DE@;en_US@;fr_FR@;es_ES@;',
     'P_ARTICLE_DESCR2':'',
     'P_ARTICLE_DESCR3':'',
     'P_ARTICLE_MANUFACTURER':'',
     'P_ARTICLE_SUPPLIER':'',
     'P_ARTICLE_ORDERNR':'',
     'P_ARTICLE_NOTE':'de_DE@;en_US@;fr_FR@;es_ES@;',
     'P_ARTICLE_PRICEUNIT':'',
     'P_ARTICLE_QUANTITYUNIT':'',
     'P_ARTICLE_PACKAGINGQUANTITY':'',
     'P_ARTICLE_DISCOUNT':'',
     'P_ARTICLE_PURCHASEPRICE_1':'',
     'P_ARTICLE_PURCHASEPRICE_2':'',
     'P_ARTICLE_PACKAGINGPRICE_1':'',
     'P_ARTICLE_PACKAGINGPRICE_2':'',
     'P_ARTICLE_SALESPRICE_1':'',
     'P_ARTICLE_SALESPRICE_2':'',
     'P_ARTICLE_IDENTCODE':'',
     'P_ARTICLE_IDENTTYPE':'',
     'P_ARTICLE_CERTIFICATE':'',
     'P_ARTICLE_CERTIFICATE_UL':'',
     'P_ARTICLE_CERTIFICATE_VDE':'',
     'P_ARTICLE_CERTIFICATE_CE':''}

#长制造商名与简称映射字典常量
ManufMapping = {
               'Allen-Bradley':'A-B',
               'ABB Automation GmbH':'ABB',
               'Atlas Copco IAS GmbH':'ATCO',
               'Balluff':'BAL',
               'BANNER':'BAN',
               'Beckhoff Automation GmbH & Co. KG':'BEC',
               'Becker GmbH':'BECK',
               'Bender GmbH & Co. KG':'BEN',
               'Bernstein AG':'BERN',
               'Binzel-Abicor':'BINZ',
               'Bosch Rexroth':'BOS',
               'Bräuer Systemtechnik GmbH':'BRAU',
               'DANFOSS':'DAN',
               'Doepke Schaltgeräte GmbH':'DOEP',
               'Eckold GmbH & Co. KG':'ECKO',
               'EJOT GmbH & Co. KG':'EJOT',
               'E-T-A':'ETA',
               'Eaton':'ETN',
               'Euchner':'EUC',
               'EXPERT Transformatorenbau GmbH':'EXPE',
               'FANUC Deutschland GmbH':'FANU',
               'FerRobotics GmbH':'FERO',
               'Festo':'FES',
               'FINDER GmbH':'FIN',
               'FRONIUS Deutschland GmbH':'FRON',
               'GESS':'GESS',
               'GOM GmbH':'GOM',
               'Hager':'HAG',
               'Harting':'HAR',
               'HEBOTEC GmbH':'HEBO',
               'Helukabel GmbH':'HELU',
               'Hirschmann':'HIR',
               'HIGHYAG Lasertechnologie GmbH':'HIYA',
               'HTI Gienger KG':'HTI',
               'Harms & Wende':'HWH',
               'Icotek GmbH':'ICO',
               'ifm electronic':'IFM',
               'INOVANCE':'INO',
               'Eisenmann intec GmbH & Co. KG':'INT',
               'JVL Deutschland':'JVL',
               'Kraus & Naimer GmbH':'K&N',
               'Keyence':'KEY',
               'KnorrTec':'KNOR',
               'KUKA Roboter GmbH':'KUKA',
               'Laserline GmbH':'LALI',
               'Lapp':'LAPP',
               'LEONI AG':'LEON',
               'LEUZE Electronic':'LEU',
               'Lütze':'LUE',
               'Lutz Precision k.s.':'LUTZ',
               'MARKATOR':'MARK',
               'MBS Sulzbach':'MBS',
               'MENNEKES GmbH & Co. KG':'MENN',
               'Mersen Deutschland GmbH':'MER',
               'microSYST Systemelectronic GmbH':'MISY',
               'Mitsubishi':'MIT',
               'Murrplastik Systemtechnik':'MPS',
               'MULTI-BOX GmbH':'MUBO',
               'Murrelektronik GmbH':'MURR',
               'OBO Bettermann GmbH':'OBO',
               'OMRON Corporation':'OMR',
               'Pepperl+Fuchs':'P+F',
               'Perceptron GmbH':'PERC',
               'perma-tec GmbH & Co. KG':'PERM',
               'PFLITSCH':'PFL',
               'Piab Vakuum GmbH':'PIAB',
               'Pilz':'PILZ',
               'Plasmo Industrietechnik GmbH':'PLAS',
               'Precitec GmbH & Co. KG':'PREC',
               'PRIMES':'PRIM',
               'Phoenix Contact':'PXC',
               'Morgan Rekofa GmbH':'REKO',
               'Rittal':'RIT',
               'ROSE Systemtechnik GmbH':'ROSE',
               'Sälzer Holding GmbH':'SAE',
               'Scansonic GmbH':'SCAN',
               'Schlemmer GmbH':'SCHL',
               'Schmersal':'SCHM',
               'Schneider Electric':'SE',
               'SEW-EURODRIVE':'SEW',
               'SICK AG':'SICK',
               'Siemens AG':'SIE',
               'Sinterleghe S.r.l.':'SINT',
               'SKS Welding Systems GmbH':'SKS',
               'Schmalz':'SLZ',
               'SMC Pneumatik':'SMC',
               'SmartRay GmbH':'SMRA',
               'Stäubli Electrical Connectors GmbH':'STÄU',
               'SVS-Schweisstechnik':'SVS',
               'TBi Industries GmbH':'TBI',
               'TE Connectivity':'TE',
               'TR electronic':'TR',
               'J. Thielmann':'THIE',
               'TOX Pressotechnik GmbH & Co.KG':'TOX',
               'TRUMPF GmbH':'TRUM',
               'TUCKER GmbH':'TUCK',
               'Vulkan Technic GmbH':'VULK',
               'Walther-Präzision':'WALT',
               'Weber Schraubautomaten GmbH':'WEBE',
               'Weidmueller':'WEI',
               'WERMA Signaltechnik GmbH + Co. KG':'WER',
               'WETRON automation technology GmbH':'WET',
               'Woehner GmbH':'WOE',
               'EUGEN WOERNER GmbH & Co. KG':'WOER',
               'Carl Zeiss Automated GmbH':'ZEIS'
               }

#with语句打开json文件，加装字典列表数据
with open('source.json', 'r', encoding = 'utf-8') as f:
    SourceData = json.load(f)

#初始化存储字典数据类型的列表
ListData = []

#循环读取字典列表数据
for x in SourceData:
    #初始化临时变量和临时字典
    TempLib = LibTemplate.copy()
    TempManuf = ''
    TempPartNr = ''
    #赋值临时变量
    TempManuf = ManufMapping[x['P_PART_ADDRESS_LONGNAME']]
    TempPartNr = TempManuf + '.' + x['P_ARTICLE_ORDERNR']
    #更新临时字典的对应键值
    TempLib['P_ARTICLE_PARTNR'] = TempPartNr.replace('\n', '')
    TempLib['P_ARTICLE_TYPENR'] = x['P_ARTICLE_TYPENR'].replace('\n', '') 
    TempLib['P_ARTICLE_MANUFACTURER'] = TempManuf.replace('\n', '') 
    TempLib['P_ARTICLE_ORDERNR'] = x['P_ARTICLE_ORDERNR'].replace('\n', '')
    #ListData列表添加更新的字典进行迭代存储
    ListData.append(TempLib)

#dump将ListData列表保存至data.json模板文件
with open('data.json', 'w', encoding = 'utf-8') as f:
    json.dump(ListData, f, indent = 4)
