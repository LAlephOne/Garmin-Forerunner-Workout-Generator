#!/usr/bin/env python

class Distance(object):

    _METER = 1
    _KILOMETER = _METER * (10**3)
    _MARATHON = 42194.988
    _HALFMARATHON = 0.5 * _MARATHON
    _YARD = 0.9144
    _MILE = 1609.344
    UNITS = {
         'meter': _METER,
         'meters': _METER,
         'mts': _METER,
         'mt': _METER,
         'm': _METER,
         'marathon': _MARATHON,
         'marathons': _MARATHON,
         'halfmarathon': _HALFMARATHON,
         'half': _HALFMARATHON,
         'halfmarathons': _HALFMARATHON,
         'halfs': _HALFMARATHON,
         'halves': _HALFMARATHON,
         'kilo': _KILOMETER,
         'kilos': _KILOMETER,
         'kilometer': _KILOMETER,
         'kilometers': _KILOMETER,
         'km': _KILOMETER,
         'kms': _KILOMETER,
         'k': _KILOMETER,
         'yard': _YARD,
         'yards': _YARD,
         'yd': _YARD,
         'yds': _YARD,
         'miles': _MILE,
         'mls': _MILE,
         'ml': _MILE,
         'mi': _MILE
         }
    def __init__(self, s):
        try: self._meters, self._unit = s.split()
        except ValueError:
            self._meters = 1
            self._unit = s
        if self._unit not in self.UNITS:
            raise ValueError, "Unable to parse distance unit {0}".format(self._unit)
        self._convert(self._unit)

    def _convert(self, unit):
        self._meters = float(self._meters)
        if self.UNITS[unit] != 1:
            self._meters *= self.UNITS[unit]

    def meters():
        doc = "The meters distance."
        def fget(self):
            return self._meters
        def fset(self, value):
            self._meters = float(value)
        return locals()
    meters = property(**meters())

    def kilometers():
        doc = "The kilometers distance."
        def fget(self):
            return self._meters / self._KILOMETER
        def fset(self, value):
            self._meters = value
            self._convert('kilometers')
        return locals()
    kilometers = property(**kilometers())

    def marathons():
        doc = "The marathon distance."
        def fget(self):
            return self._meters / self._MARATHON
        def fset(self, value):
            self._meters = value
            self._convert('marathon')
        return locals()
    marathons = property(**marathons())

    def halfmarathons():
        doc = "The halfmarathon distance."
        def fget(self):
            return self._meters / self._HALFMARATHON
        def fset(self, value):
            self._meters = value
            self._convert('halfmarathon')
        return locals()
    halfmarathons = property(**halfmarathons())

    def yards():
        doc = "The yards distance."
        def fget(self):
            return self._meters / self._YARD
        def fset(self, value):
            self._meters = value
            self._convert('yards')
        return locals()
    yards = property(**yards())

    def miles():
        doc = "The miles distance."
        def fget(self):
            return self._meters / self._MILE
        def fset(self, value):
            self._meters = value
            self._convert('miles')
        return locals()
    miles = property(**miles())
