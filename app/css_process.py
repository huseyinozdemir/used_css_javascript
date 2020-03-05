import re

from functools import reduce

RE_ELEMENT = '<([a-zA-Z]+)'
RE_ELEMENT = re.compile(RE_ELEMENT, re.DOTALL)
RE_CLASS = 'class="(.*?)"'
RE_CLASS = re.compile(RE_CLASS, re.DOTALL)
RE_ID = 'id="(.*?)"'
RE_ID = re.compile(RE_ID, re.DOTALL)
RE_CSS_FILE = 'href="(.*?\.css).*?"'
RE_CSS_FILE = re.compile(RE_CSS_FILE, re.MULTILINE)


class CssProcess:
    REPLACE_DIC = {"\n": "",
                   ", ": ",",
                   ": ":":",
                   " {":"{",
                   "  ": ""}
    EXCEPT_ELEMENT = ['script']
    _base = None
    _body = None

    def __init__(self, base, body):
        self._body = body
        self._base = base

    def get_uniqe_list(self, val_list):
        return reduce(lambda x, y: x+[y] if y not in x else x, val_list, [])

    def get_element_list(self):
        element_list = RE_ELEMENT.findall(self._body)
        if not (element_list):
            return
        return self.get_uniqe_list(element_list)

    def get_class_list(self):
        class_list = RE_CLASS.findall(self._body)
        if not (class_list):
            return
        return self.get_uniqe_list(class_list)

    def get_id_list(self):
        id_list = RE_ID.findall(self._body)
        if not (id_list):
            return
        return self.get_uniqe_list(id_list)

    def get_css_file_list(self):
        file_list = RE_CSS_FILE.findall(self._body)
        if not (file_list):
            return
        file_list = self.get_uniqe_list(file_list)
        for index, fl in enumerate(file_list):
            if not self._base in fl:
                file_list[index] = '{}{}'.format(self._base, fl)
                file_list[index] = file_list[index].replace('//', '/')
        return file_list

    def parse_css_element_on_body(self, material_list):
        style = list();
        for ml in material_list:
            if ml in self.EXCEPT_ELEMENT:
                continue
            RE_CSS_PARSE = '[^\.\#]({cls}{frmt})'.format(
                #cls='{}'.format(ml), frmt='[\s|a-z0-9]*?\{.*?\}'
                cls='{}'.format(ml), frmt='[\sa-z0-9]*?\{.*?\}'
            )
            RE_CSS_PARSE = re.compile(RE_CSS_PARSE, re.MULTILINE|re.DOTALL|re.IGNORECASE)
            cs_list = RE_CSS_PARSE.findall(self._body)
            if not (cs_list):
                continue
            for cs in cs_list:
                tmp = cs
                for i, j in self.REPLACE_DIC.items():
                    tmp = tmp.replace(i, j);
                style.append(tmp)

        return style

    def parse_css_id_on_body(self, material_list):
        style = list();
        for ml in material_list:
            RE_CSS_PARSE = '({cls}{frmt})'.format(
                cls='#{}'.format(ml), frmt='[^"].*?\{.*?\}'
            )
            RE_CSS_PARSE = re.compile(RE_CSS_PARSE, re.MULTILINE|re.DOTALL)
            cs_list = RE_CSS_PARSE.findall(self._body)
            if not (cs_list):
                continue
            for cs in cs_list:
                tmp = cs
                for i, j in self.REPLACE_DIC.items():
                    tmp = tmp.replace(i, j);
                style.append(tmp)

        return style

    def parse_css_class_on_body(self, material_list):
        style = list();
        for ml in material_list:
            RE_CSS_PARSE = '({cls}{frmt})'.format(
                cls='\.{}'.format(ml), frmt='.*?\{.*?\}'
            )
            RE_CSS_PARSE = re.compile(RE_CSS_PARSE, re.MULTILINE|re.DOTALL)
            cs_list = RE_CSS_PARSE.findall(self._body)
            if not (cs_list):
                continue
            for cs in cs_list:
                tmp = cs
                for i, j in self.REPLACE_DIC.items():
                    tmp = tmp.replace(i, j);
                style.append(tmp)

        return style
