import sublime
import sublime_plugin,time
import os
import subprocess


class rushCommand(sublime_plugin.TextCommand):
    def is_visible(self):
        file_name = self.view.file_name()
        if file_name.endswith(".rush"):
            return True
        else:
            return False    



    def run(self,edit):
        file_name = self.view.file_name()
        # file_path = os.path.dirname(file_name)
        #完整的文件路径
        # complete_path = file_path + file_name
        # print("complete_path is *********************")
        # print(file_name)
        #next-->执行命令行
        command_rushc = '/AppleInternal/Library/Frameworks/Rush.framework/bin/rushc ' + file_name
        if command_rushc.endswith('.rush'):
            out1 = subprocess.getstatusoutput(command_rushc)
            status = out1[0]
            result = out1[1]
            if status == 1:
                print(result)
            #print(str(out,encoding='utf-8'))    
        else:
            return
        command_path = '/AppleInternal/Library/Frameworks/Rush.framework/bin/rush ' + file_name
        if command_path.endswith('.rush'):
            #这里可以执行下 rush ~/..../file.rush
            out = subprocess.getstatusoutput(command_path)
            #print(out)
            status1 = out[0]
            result1 = out[1]
            if status1 == 0:
                print(result1)
            else:
                out2 = subprocess.check_output(command_path, shell=True)
                print(str(out2, encoding='utf-8'))
                    


            