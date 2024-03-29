import xml.etree.ElementTree as ET 
# 输入xml.etree.ElementTree模块，绑定到变量ET。
import os       
# 输入os模块。
import shutil   
# 输入shutil模块。
import sys 
# 输入sys模块。

XmlFilePath = r"{}".format(sys.argv[1]) 
# 需要解析的xml文档路径的常量。
FileRoot = os.path.dirname(XmlFilePath) 
# 取manifest.xml所在目录。

DestPathRoot = r"{}".format(sys.argv[2])   
# 目标路径的根目录。
DestPathDir = {"partxml":"XML", "document":"Documents", "macro":"Macros",
               "picture":"Images", "gmacro":"Images", "contour":"Macros"} 
# 源路径和目录路径中部分文件夹映射字典。

tree = ET.parse(XmlFilePath)  
# 读取路径中xml文件的树结构。
root = tree.getroot()   
# 读取树结构的根节点。

for item in root.iter("item"):  
# 遍历manifest.xml文件中根节点下的所有"item"元素。
    ItemDir = item.attrib  
    # 将"item"元素的属性赋值给ItemDir变量。
    SourceFile = os.path.join(FileRoot, "items", ItemDir["type"],
                              ItemDir["locator"]) 
    # 组合成源文件路径。
    DestFile = os.path.join(DestPathRoot, DestPathDir[ItemDir["type"]],
                           "LUBIN", ItemDir["locator"])
    FileDestPath = os.path.dirname(DestFile) 
    # 组合成目标路径。
    if os.path.isfile(SourceFile) and os.path.exists(SourceFile):
    # 判断源文件是否是文件和源路径是否存在，if条件为false打印说明继续循环，
    # 如果if条件为true继续下一级判断。
        if not os.path.exists(DestFile): 
        # 判断目标文件路径是否存在，如果if条件为false打印说明继续循环，
        # 如果if条件为true继续下一级判断。
            if not os.path.exists(FileDestPath):
            # 判断目标路径是否存在，如果if条件为false移动文件，
            # 如果if条件为true新建目标路径。
                os.makedirs(FileDestPath)
            else: 
                ReturnResult = shutil.move(SourceFile, FileDestPath)          
                # 将源文件移动至目标路径。
        else:
            print("{}目标目录中存在源文件".format(DestFile))
            continue
    else:
        print("{}源目标不是文件或者是文件但不存在".format(SourceFile))
        continue

shutil.rmtree(FileRoot)     
# 完成源目录移动，删除文件。