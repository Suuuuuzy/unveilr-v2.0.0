import subprocess, os
node = "node"
decompiler_tool = "bin/index.js"

rootpath = "/Users/jianjia/Desktop/tmp/pkg"
def decompile(rootpath):
    for wxapkg in os.listdir(rootpath):
        if wxapkg.endswith(".wxapkg") and not os.path.isdir(os.path.join(rootpath, wxapkg.replace(".wxapkg", ""))):
            try:
                fullpath_wxapkg = os.path.join(rootpath, wxapkg)
                cmdline = [node, decompiler_tool, fullpath_wxapkg, '-f', '--clear-output']
                subprocess.check_output(cmdline)
            except:
                pass

decompile(rootpath)