#!/usr/bin/python

# -*- coding: utf-8 -*-

from simplepam import authenticate

from shinken.log import logger
from shinken.basemodule import BaseModule

properties = {
    'daemons': ['webui', 'skonf', 'synchronizer'],
    'type': 'passwd_webui'
    }


# called by the plugin manager
def get_instance(plugin):
    logger.info("Instantiate an PAM/Passwd UI module for plugin %s" % plugin.get_name())

    instance = PAM_Webui(plugin)
    return instance


class PAM_Webui(BaseModule):
    def __init__(self, modconf):
        BaseModule.__init__(self, modconf)
        self.service_name = modconf.service_name
        if not self.service_name:
		self.service_name = "shinken"

    def init(self):
        logger.debug("Init pam auth module")

    # To load the webui application
    def load(self, app):
        self.app = app

    def check_auth(self, user, password):
	return authenticate(user,password, self.service_name)
