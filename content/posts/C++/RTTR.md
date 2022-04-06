---
title: "C++动态反射库RTTR"
date: 2022-04-04T22:18:09+08:00
draft: false
tags: [ "反射" ]
categories: [ "C++" ]
---

![](images/avatar.jpg)

## 1 C++动态反射库——[RTTR](https://github.com/rttrorg/rttr)简介

## 2 基本使用

## 3 底层实现

### 3.1 类

#### 3.1.1 类注册

#### 3.1.2 类实例化

### 3.2 函数

#### 3.2.1 函数注册

#### 3.2.2 函数调用

遍历，利用名字匹配及参数匹配。

```c++
variant type::invoke(string_view name, instance obj, std::vector<argument> args) const
{
    const auto raw_t = get_raw_type();
    const auto& methvec = raw_t.m_type_data->m_class_data.m_methods;
    for (auto mit = methvec.crbegin() ; mit != methvec.crend() ; ++mit)
    {
        const auto& meth = *mit ;
        if ( meth.get_name() == name &&
             detail::compare_with_arg_list::compare(meth.get_parameter_infos(), args))
        {
            return meth.invoke_variadic(obj, args);
        }
    }

    return variant();
}
```

### 3.3 属性

#### 3.3.1 属性注册

#### 3.3.2 属性访问

