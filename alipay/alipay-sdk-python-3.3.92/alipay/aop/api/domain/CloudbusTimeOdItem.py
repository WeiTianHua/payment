#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CloudbusTimeOdItem(object):

    def __init__(self):
        self._bus_od = None
        self._od = None
        self._time = None

    @property
    def bus_od(self):
        return self._bus_od

    @bus_od.setter
    def bus_od(self, value):
        self._bus_od = value
    @property
    def od(self):
        return self._od

    @od.setter
    def od(self, value):
        self._od = value
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value


    def to_alipay_dict(self):
        params = dict()
        if self.bus_od:
            if hasattr(self.bus_od, 'to_alipay_dict'):
                params['bus_od'] = self.bus_od.to_alipay_dict()
            else:
                params['bus_od'] = self.bus_od
        if self.od:
            if hasattr(self.od, 'to_alipay_dict'):
                params['od'] = self.od.to_alipay_dict()
            else:
                params['od'] = self.od
        if self.time:
            if hasattr(self.time, 'to_alipay_dict'):
                params['time'] = self.time.to_alipay_dict()
            else:
                params['time'] = self.time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CloudbusTimeOdItem()
        if 'bus_od' in d:
            o.bus_od = d['bus_od']
        if 'od' in d:
            o.od = d['od']
        if 'time' in d:
            o.time = d['time']
        return o


