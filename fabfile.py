# -*- coding: utf-8 -*-
from fabric.api import task, local


@task
def server():
    local('honcho start')
