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
        self._configs = {k: v for k, v in DEFAULT_CONFIGS.iteritems()}
        if not isinstance(update, dict):
            logging.warning('the update param is not a dict instance')
        else:
            self._update(update)

    def _update(self, update):
        '''Update the default config dict'''
        self._configs.update(update)

    def iteritems(self):
        '''iter config items'''
        return iter(
            [(k, self.__getattr__(k))
             for k, _ in self._configs.iteriterms()])

    def __getattr__(self, name):
        default = self._configs.get(name, None)
        return _get_from_env(name, default=default)


CONFIG = Config()
