import xml.etree.ElementTree as ET # 输入xml.etree.ElementTree模块，绑定到变量ET。
import os
import shutil

XmlFilePath = r"L:\WD SmartWare.swstor\Engineering Software\Eplan P8 Data Portal\SIEMENS\6ES7516-3FN02-0AB0\manifest.xml" # 需要解析的xml文档路径的常量
FileRoot = os.path.dirname(XmlFilePath) # 取manifest.xml所在目录

DestPathRoot = r"L:\Eplan P8\Data"
DestPathDir = {"partxml": "XML", "document": "Documents", "macro": "Macros", "picture": "Images"}

tree = ET.parse(XmlFilePath)  # 读取路径中xml文件的树结构
root = tree.getroot()   # 读取树结构的根节点

for item in root.iter("item"):  # 遍历manifest.xml文件中根节点下的所有"item"元素
    ItemDir = item.attrib  # 将"item"元素的属性赋值给ItemDir变量
    FileSourcePath = os.path.join(FileRoot, "items", ItemDir["type"], ItemDir["locator"]) # 组合成源文件路径
    FileDestPath = os.path.dirname(os.path.join(DestPathRoot, DestPathDir[ItemDir["type"]], "LUBIN", ItemDir["locator"])) #组合成目标路径
    shutil.move(FileSourcePath, FileDestPath)   #将源文件移动至目标路径