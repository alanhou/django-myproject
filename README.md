# Django 3.0项目结构样板

* 如需使用 last-modified.txt 来获取静态文件所使用的时间戳，请将scripts/pre-commit拷贝至项目根目录下的.git/hooks/中
* 复制 myproject/settings 内的 sample_secrets.json 为 secrets.json 并进行相应修改
* scripts 目录下文件仅供参考
* 如需使用请对 myproject 进行全局替换


PostgreSQL指定编码

```
createdb --encoding=UTF8 --locale=en_US.UTF-8 --template=template0 myproject
```

手动删除 Python 编译文件(自定义 delpyc 命令)

```
alias delpyc='
find . -name "*.py[co]" -delete
find . -type d -name "__pycache__" -delete'
```

彻底避免编译文件的创建，添加环境变量`PYTHONDONTWRITEBYTECODE=1`


## 参考文档
* [PEP 8](https://www.python.org/dev/peps/pep-0008/)
* [pip 官方文档](https://pip.pypa.io/en/stable/user_guide/)
* [Pipenv](https://github.com/pypa/pipenv)
* [证书生成](https://choosealicense.com/)
* [CodeKit](https://codekitapp.com/)
* [Prepros](https://prepros.io/)