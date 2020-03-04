import re

from functools import reduce

RE_CLASS = 'class="(.*?)"'
RE_CLASS = re.compile(RE_CLASS, re.DOTALL)
RE_ID = 'id="(.*?)"'
RE_ID = re.compile(RE_ID, re.DOTALL)


class CssProcess:
    _body = None

    def __init__(self, body):
        self._body = body

    def get_class_list(self):
        class_list = RE_CLASS.findall(self._body)
        if not (class_list):
            return
        return reduce(lambda x, y: x+[y] if y not in x else x, class_list, [])

    def get_id_list(self):
        id_list = RE_ID.findall(self._body)
        if not (id_list):
            return
        return reduce(lambda x, y: x+[y] if y not in x else x, id_list, [])
