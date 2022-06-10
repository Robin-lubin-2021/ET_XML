'''
从保存了词典列表的JSON文件中读取部件属性，批量创建XML文件
'''


#输入json和xml.etree.ElementTree标准库
import json
import xml.etree.ElementTree as ET

#with语句打开json文件，加装字典列表数据
with open('data.json', 'r', encoding = 'utf-8') as f:
    data = json.load(f)
    
#从字典列表循环读取part的属性字典并创建XML文件
for PartArguDict in data:
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