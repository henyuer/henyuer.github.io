---
layout: post
title: "assignment2-fast-layers计算时cython及其配置问题"
date: 2024-08-18 14:50:01 +0800
categories: [cs231n]
tags: [cython, google colab]
---

在 cs231n assignment2 的 fast layers 计算时，发生如下报错：

```python
NameError: name 'col2im_6d_cython' is not defined
```

## 相关知识

#### cython 是什么

Cython 是一个能够将 Python 代码转换为 C 代码的编译器，可以通过这种方式提高 Python 代码的执行速度。
cython 库 是 python 的一个第三方库。

#### colab 机制

colab 实际上相当于远程服务器给用户提供了虚拟机，我们自己的 cs231n 的文件，则存储在 google 云盘上，而每次运行所需要的库，实际上存储在 colab 的内存里面，一旦会话重启，相当于关闭了原有的虚拟机，再次打开另一个虚拟机，所以之前加载的库需要重新加载，诸如 numpy，cython 等库。不过这些命令 cs231n 前面的文件都写好，我们不必操心。

要想让云服务器那边的虚拟机执行相关的命令，只需要在代码中写入命令即可，不过注意 jupyter 的命令行命令格式要在正常命令前面加上`!`或`%`等字符,仅谈印象，详情请谷歌，像下面：

```bash
%cd /content/drive/My\ Drive/$FOLDERNAME/cs231n/
!python setup.py build_ext --inplace
%cd /content/drive/My\ Drive/$FOLDERNAME/
```

这个命令就是 cd 到指定文件夹，执行`python setup.py build_ext --inplace`命令，再 cd 回原目录

## 问题解决

我这里是 2023 春的代码，执行完

```bash
%cd /content/drive/My\ Drive/$FOLDERNAME/cs231n/
!python setup.py build_ext --inplace
%cd /content/drive/My\ Drive/$FOLDERNAME/
```

有两个报错：

```python
C:\Users\29402\anaconda3\lib\site-packages\Cython\Compiler\Main.py:381: FutureWarning: Cython directive 'language_level' not set, using '3str' for now (Py3). This has changed from earlier releases! File: C:\Users\29402\Desktop\cs231n\assignment2\cs231n\im2col_cython.pyx
```

{% highlight cython %}
Error compiling Cython file:

---

...
cdef int N = x.shape[0]
cdef int C = x.shape[1]
cdef int H = x.shape[2]
cdef int W = x.shape[3]

    cdef int HH = (H + 2 * padding - field_height) / stride + 1

---

im2col_cython.pyx:19:60: Cannot assign type 'double' to 'int'
（以下类似报错重复三次，略）
{% endhighlight %}

第一个报错似乎是 cython 库本身的问题，版本警告，还不算错误,在相关文件`im2col_cython.pyx`的顶部加入代码`# cython: language_level=3`,警告消失。
贴一个 cython 库的链接，应该是在讨论相关 bug：[github cython issues](https://github.com/cython/cython/issues/5484)

第二个报错才是导致 nameerror 的罪魁祸首，之前我以为是一个小错误，带着 c++的直觉，觉得类型转换顶多算一个警告，编译器会自动转换，没想到是它导致文件编译失败。之前我还一直以为是环境配置或者路径导入的问题，使得命名无法引用。

直到我在自己的 conda 的 python 环境里，先`conda install cython`装好 cython 库，
再在目标目录下执行`python setup.py build_ext --inplace`,结果跑出一模一样的错误，才意识到不是环境的问题，就是下面的错误有问题

那么只要把`/`全部改为`//`,结果就全是 int 型，再一跑，错误没了，成功跑通，目录下也成功出现几个`im2col_cython.cpython-310-x86_64-linux-gnu.so`等文件。

当然，最后别忘了重启会话，这样新文件才能发挥作用，下面的 nameerror 才能消失。
