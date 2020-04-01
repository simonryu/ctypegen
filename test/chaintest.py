# Copyright (c) 2020 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.
#
# DON'T EDIT THIS FILE. It was generated by
# ./ChainTest.py
# Please see AID/3558 for details on the contents of this file
#
from ctypes import * # pylint: disable=wildcard-import
from CTypeGenRun import * # pylint: disable=wildcard-import
# pylint: disable=unnecessary-pass,protected-access



class Globals(object):
   def __init__(self, dll):
      pass
def decorateFunctions( lib ):
   lib.callme.restype = c_int
   lib.callme.argtypes = [
      c_int,
      c_int,
      c_int ]

   lib.mockme.restype = c_int
   lib.mockme.argtypes = [
      c_int,
      c_int,
      c_int ]

   pass

functionTypes = {
   'callme': CFUNCTYPE( c_int, c_int
      , c_int
      , c_int
      ),
   'mockme': CFUNCTYPE( c_int, c_int
      , c_int
      , c_int
      ),
}


if __name__ == "__main__":
   test_classes()