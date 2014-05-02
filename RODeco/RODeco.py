#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File: main.py
# by BitK
# lu.k.philippe@gmail.com
#

import types


class RODecoException(Exception):
    pass


def RODeco(oldfunc, funcName="__unused", **kwargs):
    """Override a function with the decorated one.
    :param oldfunc: Function to override. All calls to this function will now call the decorated one.
    :param funcName: New name of the function. In case you need to access it afterwards.
    :param kwargs: Arguments of the function. Since all function calls will be overridden, the arg count MUST match.
    """
    def scopeError(newFuncName, oldFuncName):
        raise RODecoException("{} already exist in {} scope."
                              .format(newFuncName, oldFuncName))

    def wrapper(newfunc):

        if (oldfunc.__code__.co_argcount != newfunc.__code__.co_argcount):
            raise TypeError("{}() takes {} arguments ({} given)."
                            .format(oldfunc.__name__,
                                    oldfunc.__code__.co_argcount,
                                    newfunc.__code__.co_argcount))

        if funcName in oldfunc.__globals__:
            scopeError(newfunc.__name__, oldfunc.__name__)

        for item in oldfunc.__globals__.keys():
            if item in kwargs:
                globalscopeError(item, oldfunc.__name__)

        for item in kwargs:
            if item in newfunc.__code__.co_varnames:
                scopeError(item, newfunc.__name__)

        f = types.FunctionType(oldfunc.__code__,
                               oldfunc.__globals__,
                               name=oldfunc.__name__,
                               argdefs=oldfunc.__defaults__,
                               closure=oldfunc.__closure__)
        oldfunc.__globals__[funcName] = f

        oldfunc.__code__ = newfunc.__code__
        oldfunc.__globals__.update(kwargs)

        return newfunc

    return wrapper
