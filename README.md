### 1.软件的安装

1. VSCode下载（安装python，chinese，path intellisence，npm，npm intellisence，Vetur，VUE3 Snipper，vscode-icons，live-server）

2. 配置终端

   切换到cmd

3. 安装前端开发工具HbuilderX   https://www.dcloud.io/hbuilderx.html

4. 安装小程序开发工具   https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html

### 二.git仓库:  https://git-scm.com/；

1. 安装git
2. 创建远程仓库myBlog
3. 初始化本地仓库,也就是再本地的myBlog文件夹下执行:`git init`,执行后会创建一个.git隐藏文件
4. 远程仓库和本地仓库进行关联:`git remote add origin '你的远程仓库地址'`
5. 如果出现错误,ssh没有创建
6. 先去创建密钥:`ssh keygen`, 一路enter,生成密钥
7. 查看生成的密钥 `cat~/.ssh/id_rsa.pub`,将生成的密钥写入github上的settings下的SSH and GPG keys下。
8. 推送四步骤
   - git status     查看发生变化的文件
   - git add .     追踪所有发生变化的文件
   - git commit -m '备注'  提交到本地仓库
   - git push -u origin master 首次提交到远程仓库
   - git push  之后的提交

### 三.创建myBlog项目

1. 空文件夹下,执行`django-admin startproject myBlog `
2. 给myBlog创建虚拟环境,使用:`python -m venv env `
3. 进入虚拟环境,windows:`.\\env\\Scripts\\activate`
4. 退出虚拟环境,windows下:`deactivate`
5. 使用VScode打开myBlog,执行:`python manage.py startapp article `  
   - 创建的所有app记得在settings里面注册一下。
6. 创建超级管理员账户: `python manage.py createsuperuser`

### 四.创建articles的models

- pip install pillow 处理图片需要的库

1. ##### 创建model

   ![1609720280555](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\1609720280555.png)

   - 注册进admin.py中

   <img src="C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\1609720421112.png" alt="1609720421112" style="zoom:80%;" />

   - apps.py中可更改一些页面的展示，以及主url中修改的

     ![1609723834697](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\1609723834697.png)

   ![1609720735815](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\1609720735815.png)

   ![1609720781277](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\1609720781277.png)

2. ##### 数据库同步

   '进行迁移'：
    - python manage.py makemigrations
    - python manage.py migrate

3. ##### 再次推送到远程

   - git status查看发生变化的文件
   - git add .追踪所有发生变化的文件
   - git commit -m '备注'′提交到本地仓库
   - git push -u origin master首次提交到远程仓库
   - git push 之后的提交



## 五、业务逻辑(前端分析)

1. 文章列表页，分页
2. 文章详情页，评论
3. 全局搜索功能 ，用Q对象
4. 最新文章，最新评论的排行
5. 按照分类，标签的一个聚类操作
6. 练习我页面，发送邮件



## 六、添加静态页面

​	1.创建static、templates两个空文件夹

​	2.在settings.py中配置路径

![1609721426697](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\1609721426697.png)

![1609721501754](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\1609721501754.png)

![1609721523406](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\1609721523406.png)

​	3.将提前准备好的前端页面和文件分别放进static和templates文件夹中

- 分析一下页面

  渲染列表，可以点击详情页，

  通篇都有搜索功能，首页订阅是rss功能

  ![1609721827895](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\1609721827895.png)

​	

​	4.view

![1609722451776](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\1609722451776.png)

5. 创建一个分urls，总路由进行分发，

   ![1609722617746](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\1609722617746.png)

   ![1609722827592](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\1609722827592.png)

6. 继承静态资源，把static的样式  继承到 模板，每个页面都要改成这样

![1609723188380](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\1609723188380.png)

