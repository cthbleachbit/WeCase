#!/usr/bin/env python3
from sys import stderr
from copy import deepcopy
from configparser import ConfigParser


class WConfigParser():

    ITEM = {
        "section": "", "type": None,
        "name": "", "alias": "",
        "default": None
    }

    def __init__(self, schema, config, section=""):
        super(WConfigParser, self).__setattr__("loaded", False)
        self._section = section
        self._config_path = config
        self._options = []
        self._config = ConfigParser()
        self._config.read(config)
        self.__parse__(schema)
        super(WConfigParser, self).__setattr__("loaded", True)

    def __parse__(self, schema):
        schema = open(schema)

        config_item = deepcopy(self.ITEM)
        for line in schema:
            if line.strip() == "":
                if config_item:
                    self._options.append(config_item)
                    config_item = deepcopy(self.ITEM)
                continue

            name, value = line.replace("\n", "").split("=")
            name = name.strip()
            value = value.strip()

            try:
                config_item[name] = value
            except KeyError:
                print("Invaild line: %s" % line, file=stderr)
        schema.close()

    def _get_option(self, name):
        for i in self._options:
            if i["name"] == name or i["alias"] == name:
                return i

    def __setattr__(self, attr, value):
        if not self.loaded:
            super(WConfigParser, self).__setattr__(attr, value)
        else:
            if not self._config.has_section(self._section):
                self._config[self._section] = {}
            self._config[self._section][attr] = str(value)

    def __getattr__(self, attr):
        option = self._get_option(attr)
        if not option:
            raise AttributeError("WConfigParser object has no attribute '%s'" % attr)

        type = eval(option["type"])
        try:
            value = self._config[self._section][attr]
        except KeyError:
            value = option["default"]

        if type is str:
            return value
        else:
            return type(eval(value))

    def save(self):
        # TODO: Create and check the lock file during writing
        with open(self._config_path, "w+") as config_file:
            config_file.seek(0)
            config_file.write("# WeCase Configuration File, by WeCase Project.\n")
            config_file.write("# DO NOT EDIT ON NORMAL PURPOSE.\n\n")
            self._config.write(config_file)