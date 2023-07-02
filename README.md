# simple-drf-starter

A simple template or starter for DRF(Django Rest Framework).

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## 项目意图

对于`Django、DRF`初学者，如何设计一个项目的目录结构对随后的健壮性、可维护性是极其重要的，所以这里参考多个知名项目的目录结构以及所使用的库包后，定义一套基本的项目模板，并计划通过`cookiecutter`来进行简单和快速的配置生成基本的项目结构，从容简单的开启一个新项目或重构一个项目。



## 项目开发计划

1. 通过`cookiecutter-django`部署基本的项目结构
2. 根据其余项目的结构进行修改，使其成为更适用于DRF的`restful`风格框架的模板
   - 添加`JWT`校验
   - 更新`user`用户管理方法
   - 添加自定义`middleware`进行全局异常处理
   - 添加`throllting`配置
3. 使用`cookiecutter`进行封装，使其可以自定义部署
4. 加入更多配置项的支持

## 参考：

- [cookiecutter/cookiecutter-django: Cookiecutter Django is a framework for jumpstarting production-ready Django projects quickly. (github.com)](https://github.com/cookiecutter/cookiecutter-django)
- [jazzband/djangorestframework-simplejwt: A JSON Web Token authentication plugin for the Django REST Framework. (github.com)](https://github.com/jazzband/djangorestframework-simplejwt)
- [Cloud-CV/EvalAI: :cloud: :bar_chart: Evaluating state of the art in AI (github.com)](https://github.com/Cloud-CV/EvalAI/tree/master)
