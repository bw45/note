#####part_01
# git init 将目录变成仓库
# ls -ah 显示隐藏文件夹

#####part_02
# git add file_name 添加文件到暂存区
# git commit -m 'a comment' 提交文件到分支
# git status 查看操作结果,显示仓库当前的状态
# git diff file_name 查看文件修改内容,条件是未提交到暂存区,只在工作区修改了
# git log 查看该仓库提交日志
# git log --pretty=oneline 提交日志一行显示

#####part_03
# git reset --hard HEAD^ 回退到上一个版本
# git reset --hard number 回退到指定版本,包括最新版本
# git reflog 记录每一次提交的命令及编码号,方便回退

#####part_04
# git checkout -- file_name 将工作区已保存的内容回退至上一次
# git reset HEAD new.txt 将暂存区的内容回退值工作区

#####part_05
# rm file_name 只是删除工作区文件，并没有删除版本库中的文件
# git checkout -- file_name 将工作区已删除的文件恢复
# git rm file_name 删除版本库和工作区文件,同样可以用 git reset的方法恢复；删除文件后，记得commit

#####part_06
# ssh-keygen -t rsa -C "u email adrress" 创建自己电脑的SSH-KEY,导入github,才可以链接GITHUB,克隆,push,pull
# git remote add origin github_ip_address.git 与github上的仓库相关联
# git push -u origin master 将本地库的所有内容推送到远程库上
# git push origin master 只要第一此推送和关联后,就可以使用此命令