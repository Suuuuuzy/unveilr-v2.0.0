# suzy: I tried using this to unpack the top 50 miniapps,
# but they either require authorization from plugin,
# or what ....


import subprocess, os
import shutil
node = "node"
decompiler_tool = "bin/index.js"
# 腾讯手机充值
# rootpath = "/Users/jianjia/Library/Containers/com.tencent.xinWeChat/Data/.wxapplet/packages/wxad3150031786d672/399/"
# rootpath = "/Users/jianjia/Library/Containers/com.tencent.xinWeChat/Data/.wxapplet/packages/wx8c0e5ec1168dd3e0/18"
# 生活缴费
# rootpath = "/Users/jianjia/Library/Containers/com.tencent.xinWeChat/Data/.wxapplet/packages/wxd2ade0f25a874ee2/424"
# rootpath = "/Users/jianjia/Library/Containers/com.tencent.xinWeChat/Data/.wxapplet/packages/wx77af30c90654b3f6/9"
# 微信同声传译
# Plugin wx069ba97219f66d99 is not authorized to use
# the plugin is at: https://mp.weixin.qq.com/wxopen/plugindevdoc?appid=wx069ba97219f66d99&token=&lang=zh_CN
# 中国移动10086
# rootpath = "/Users/jianjia/Library/Containers/com.tencent.xinWeChat/Data/.wxapplet/packages/wx43aab19a93a3a6f2/448"
# Plugin wx8d5022c70b288b21 is not authorized to use.
# https://mp.weixin.qq.com/wxopen/plugindevdoc?appid=wx8d5022c70b288b21&token=&lang=zh_CN
# the plugin: 
# rootpath = "/Users/jianjia/Library/Containers/com.tencent.xinWeChat/Data/.wxapplet/packages/__plugin__/wx8d5022c70b288b21/5"
# live-player-plugin
# rootpath = "/Users/jianjia/Library/Containers/com.tencent.xinWeChat/Data/.wxapplet/packages/__plugin__/wx2b03c6e691cd7370/82"
# wechat-SI
# rootpath = "/Users/jianjia/Library/Containers/com.tencent.xinWeChat/Data/.wxapplet/packages/__plugin__/wx069ba97219f66d99/16"
# plugin in 腾讯手机充值
# rootpath = "/Users/jianjia/Library/Containers/com.tencent.xinWeChat/Data/.wxapplet/packages/__plugin__/wxa180307169cfd6e6/18"
# 金山文档
# rootpath = "/Users/jianjia/Library/Containers/com.tencent.xinWeChat/Data/.wxapplet/packages/wx5b97b0686831c076/592"
rootpath = "/Users/jianjia/Desktop/tmp/wx26"
# 中国电信
# rootpath = "/Users/jianjia/Library/Containers/com.tencent.xinWeChat/Data/.wxapplet/packages/wxd4daf5a66b681275/410"
# 美图
rootpath = "/Users/jianjia/Library/Containers/com.tencent.xinWeChat/Data/.wxapplet/packages/wxde8ac0a21135c07d/1330"

def decompile(rootpath):
    for wxapkg in os.listdir(rootpath):
        if wxapkg.endswith(".wxapkg"):
            fullpath_wxapkg = os.path.join(rootpath, wxapkg)
            cmdline = [node, decompiler_tool, fullpath_wxapkg, '-f', '--clear-output']
            subprocess.check_output(cmdline)


def combine_pkgs(rootpath):
    mainpkg_path = os.path.join(rootpath, "__APP__")
    if not os.path.isdir(mainpkg_path):
        return
    subpkgs = os.listdir(rootpath)
    subpkgs = [i for i in subpkgs if os.path.isdir(os.path.join(rootpath, i))]
    if "__APP__" in subpkgs:
        subpkgs.remove("__APP__")
    print(subpkgs)
    files_under_main_pkg = os.listdir(mainpkg_path)
    for subpkg in subpkgs:
        subpkg_name = subpkg[1:-1]
        if os.path.isdir(os.path.join(rootpath, subpkg, subpkg_name)):
            if subpkg_name in files_under_main_pkg:
                print(os.path.join(rootpath, subpkg, subpkg_name), os.path.join(mainpkg_path, subpkg_name))
                if os.path.exists(os.path.join(mainpkg_path, subpkg_name)):
                    shutil.rmtree(os.path.join(mainpkg_path, subpkg_name))
                shutil.move(os.path.join(rootpath, subpkg, subpkg_name), mainpkg_path)
    if "___wx___" in subpkgs:
        print(os.path.join(rootpath, "___wx___", "__wx__"), os.path.join(mainpkg_path, "__wx__"))
        if os.path.exists(os.path.join(rootpath, "___wx___", "__wx__")):
            if os.path.exists(os.path.join(mainpkg_path, "__wx__")):
                shutil.rmtree(os.path.join(mainpkg_path, "__wx__"))
            shutil.move(os.path.join(rootpath, "___wx___", "__wx__"), os.path.join(mainpkg_path))

decompile(rootpath)
combine_pkgs(rootpath)

def single_decompile(fullpath_wxapkg):
    cmdline = [node, decompiler_tool, fullpath_wxapkg, '-f', '--clear-output']
    subprocess.check_output(cmdline)

# fullpath_wxapkg = "/Users/jianjia/Desktop/tmp/pkg/_930991203_1341.wxapkg"
# single_decompile(fullpath_wxapkg)