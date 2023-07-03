<p align="center">
  <h1 align="center">Simple-DRF-Starter</h1>
  <p align="center">一个全面的Django Rest框架（DRF）项目模板。</p>
</p>

[![English badge](https://img.shields.io/badge/%E8%8B%B1%E6%96%87-English-blue)](./README.md)
[![简体中文 badge](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-Simplified%20Chinese-blue)](./README-ZH_CN.md)\
[![使用Cookiecutter Django构建](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black代码风格](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

许可证：MIT

## 目的

该项目旨在为Django和DRF的初学者提供一个健壮且可维护的项目结构。它是根据多个知名项目的目录结构和所使用的库来设计的，并计划使用`cookiecutter`进行简单和快速的配置，生成基本的项目结构。这个模板可以用来舒适地启动一个新项目或重构一个现有的项目。

## 开发计划

1. [x] 使用`cookiecutter-django`部署基本的项目结构
2. [x] 根据其他项目修改结构，使其更适合DRF的`restful`风格框架
   - [x] 添加`JWT`验证
   - [x] 更新`user`管理方法
   - [x] 添加自定义`middleware`进行全局异常处理
   - [x] 添加`throttling`配置
3. 使用`cookiecutter`进行自定义部署
4. 支持更多配置项

## 参考

- [Cookiecutter Django](https://github.com/cookiecutter/cookiecutter-django)
- [Django REST Framework Simple JWT](https://github.com/jazzband/djangorestframework-simplejwt)
- [EvalAI](https://github.com/Cloud-CV/EvalAI/tree/master)
