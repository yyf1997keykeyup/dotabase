# Dotabase backend

## 安装配置
```
# 建立自己的python3虚拟环境（你要想用全局环境我也没有意见）不同平台不同
pip install -r requirements.txt
```
安装了相关的包之后，记得更新requirement.txt，例如可以这样:
```
pip freeze > requirements.txt
```

## 结构
* top为project顶层目录，相关配置清修改setting.py，路由则修改urls.py
* dotabase为主要应用，models.py对应的即为表相关配置，如有遗漏或错误烦请补充。urls.py配置相关api

## API
获取所有英雄数据:
```
api: api/dotabase/hero
```
获取、删除、更新特定英雄：
```
api: api/dotabase/hero/<heroid>
```
将用户名和密码post到下面的api获取token:
```
api: api/dotabase/user/get_token
```
默认账户：

username:admin1

password:dotabase

token使用：在header中添加Authorization: JWT <your_token>即可。

Hero Log的api:
```
api: api/dotabase/hero_log
```

## 相关资料
* [Django官方文档](https://docs.djangoproject.com/en/3.0/)，有中文但翻译不完全
* [RestFramework中文文档](https://q1mi.github.io/Django-REST-framework-documentation/tutorial/1-serialization_zh/)