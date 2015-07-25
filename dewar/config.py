# -*- coding: utf-8 -*-
import os
import json
import logging


def _get_from_env(name, default=None):
    '''Get config from environ variable

    :param name: the name of environ variable
    :param default: the value return if there is no match environ variable
    '''
    raw_value = os.environ.get(name, default)
    if raw_value is not None:
        try:
            return json.loads(raw_value)
        except (ValueError, TypeError):
            return raw_value


class Config(object):
    '''
    A class to help manage config.

    :param update: The dict to update default config.
    '''

    def __init__(self, update=None):
        self._configs = {}
        self._init_keys()
        if update:
            if not isinstance(update, dict):
                logging.warning('the update param is not a dict instance')
            else:
                self._update(update)

    def keys(self):
        return self._configs.keys()

    def iteritems(self):
        '''iter config items'''
        return iter(
            [(k, self.__getattr__(k))
             for k, _ in self._configs.iteriterms()])

    def __getattr__(self, name):
        if not name.startswith('DEWAR_'):
            name = ''.join(['DEWAR_', name])
        default = self._configs.get(name, None)
        return _get_from_env(name, default=default)

    def __getitem__(self, name):
        return self.__getattr__(name)

    def _update(self, update):
        '''Update the default config dict'''
        self._configs.update(update)

    def _init_keys(self):
        for k in os.environ:
            if k.startswith('DEWAR_'):
                self._configs.setdefault(k[6:], None)


CONFIG = Config()
