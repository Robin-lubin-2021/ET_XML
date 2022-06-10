'''
EPLAN部件管理常规和价格/其他选项卡通过录入字典后生成对应的部件XML文件
'''


#输入xml.etree.ElementTree标准库
import xml.etree.ElementTree as ET

#部件属性的字典
PartArguDict = {'P_ARTICLE_PARTTYPE':'1',
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
     'P_ARTICLE_PARTNR':'SIE.3RT2028-2AV041208',
     'P_ARTICLE_DISCONTINUED':'0',
     'P_ARTICLE_ERPNR':'',
     'P_ARTICLE_TYPENR':'3RT2028-2AV041208',
     'P_ARTICLE_UNIQUEID':'',
     'P_ARTICLE_DESCR1':'de_DE@;en_US@;fr_FR@;es_ES@;',
     'P_ARTICLE_DESCR2':'',
     'P_ARTICLE_DESCR3':'',
     'P_ARTICLE_MANUFACTURER':'SIE',
     'P_ARTICLE_SUPPLIER':'',
     'P_ARTICLE_ORDERNR':'3RT2028-2AV041208',
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

#创建标签名为'partmanagement'的根及其默认属性
root = ET.Element('partsmanagement',{'length-unit':'mm', 'type':'EPLAN.PartsManagement', 'build':''})
#创建标签名为'part'的元素，从字典中填充其属性
PartElement = ET.SubElement(root, 'part', PartArguDict)
#生成树结构
PartTree = ET.ElementTree(root)
#获取'part'的'P_ARTICLE_PARTNR'的属性值生成XML文件名
FileName = PartElement.get('P_ARTICLE_PARTNR') + '.xml'
#写入XML文件
PartTree.write(FileName, encoding = 'utf-8', xml_declaration = True, short_empty_elements = True)