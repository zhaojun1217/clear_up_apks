# -*- coding: utf-8 -*-
'''
用途：
    遍历某目录的下级目录，并查找指定名称文件，复制到指定文件夹

需求的目录结构为
android_apk
          hlpq  // 一级目录
              release // 二级目录
                     xxx-xxx-xxx.apk // 三级目录
          zhpq
              release
                     xxx-xxx-xxx.apk
          zlpq
              release
                     xxx-xxx-xxx.apk
          typq
              release
                     xxx-xxx-xxx.apk
          wbpq
              release
                     xxx-xxx-xxx.apk
'''
import shutil, os


def get_dir(path, fileType):
    '''
    :param path: 路径
    :param fileType: 需要复制的文件类型（.mkv或.avi等，前面需要加.）
    :return:null
    '''
    # 查看当前目录文件列表（包含文件夹）
    allfilelist = os.listdir(path)

    for file in allfilelist:
        print('第一级目录 ： ' + file, '\n')
        filepath = os.path.join(path, file)
        # 判断是否是文件夹，如果是则继续遍历，否则打印信息
        if os.path.isdir(filepath):
            # 一级目录下的文件（）
            allfilelist2 = os.listdir(filepath)
            for file2 in allfilelist2:
                print('          第二级目录 ： ' + file2, '\n')
                filepath2 = os.path.join(filepath, file2)
                # 判断是否是文件夹，如果是则继续遍历，否则打印信息
                if os.path.isdir(filepath2):
                    # 二级目录下的文件（）
                    allfilelist3 = os.listdir(filepath2)
                    for file3 in allfilelist3:
                        print('                    第三级目录 ： ' + file3, '\n')
                        filepath3 = os.path.join(filepath2, file3)
                        # 判断文件是否以.apk结尾
                        if filepath3.endswith(fileType):
                            print('--------------------------------------------找到文件--------------------------------------------\n：' + filepath3+'\n--------------------------------------------------------------------------------------------')
                            # 复制filepath3找到的文件到distPath目录
                            shutil.copy(filepath3, distPath)
                else:
                    print('不是文件夹，继续查找...')

        else:
            print('不是文件夹，继续查找...')

# 可以直接运行，厉害了
if __name__ == '__main__':
    path = '/Users/zhaojun/Documents/androidworkspace/android_apk'
    # 复制到distPath目录，目录需先创建
    distPath = '/Users/zhaojun/Documents/androidworkspace/android_apk/clear_up_apk'
    get_dir(path, 'pq_1.0.5_production.apk')
    get_dir(path, 'zp_1.0.4_production.apk')
