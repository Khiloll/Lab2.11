#!/usr/bin/env python3
# -*- coding: utf-8 -*-



def template_func(template):
    def replace_data(last_name, first_name):
        new_template = template.replace("%F%", last_name).replace("%N%", first_name)
        return new_template

    return replace_data

# Шаблон для приветствия
template = "Уважаемый %F%, %N%! Вы делаете работу по замыканиям функций."

# Создание замыкания
greeter = template_func(template)

# Ввод фамилии и имени
last_name = input("Введите фамилию: ")
first_name = input("Введите имя: ")

# Вызов внутренней функции для замены данных в шаблоне
result = greeter(last_name, first_name)

print(result)
