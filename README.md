<p align="center">
  <h1 align="center">Simple-DRF-Starter</h1>
  <p align="center">A comprehensive template for Django Rest Framework (DRF) projects.</p>
</p>

[![English badge](https://img.shields.io/badge/%E8%8B%B1%E6%96%87-English-blue)](./README.md)
[![简体中文 badge](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-Simplified%20Chinese-blue)](./README-ZH_CN.md)\
[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Purpose

This project aims to provide a robust and maintainable project structure for beginners in Django and DRF. It is designed based on the directory structure and libraries used by several renowned projects, and plans to use `cookiecutter` for easy and quick configuration to generate the basic project structure. This template can be used to comfortably start a new project or refactor an existing one.

## Development Plan

1. [x] Deploy basic project structure using `cookiecutter-django`
2. [x] Modify the structure according to other projects to make it more suitable for DRF's `restful` style framework
   - [x] Add `JWT` verification
   - [x] Update `user` management methods
   - [x] Add custom `middleware` for global exception handling
   - [x] Add `throttling` configuration
3. Wrap with `cookiecutter` for custom deployment
4. Support for more configuration items

## References

- [Cookiecutter Django](https://github.com/cookiecutter/cookiecutter-django)
- [Django REST Framework Simple JWT](https://github.com/jazzband/djangorestframework-simplejwt)
- [EvalAI](https://github.com/Cloud-CV/EvalAI/tree/master)
