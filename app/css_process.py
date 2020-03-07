import re

from functools import reduce

RE_ELEMENT = '<([a-zA-Z]+)'
RE_ELEMENT = re.compile(RE_ELEMENT, re.DOTALL)
RE_CLASS = 'class="(.*?)"'
RE_CLASS = re.compile(RE_CLASS, re.DOTALL)
RE_ID = 'id="(.*?)"'
RE_ID = re.compile(RE_ID, re.DOTALL)
RE_CSS_FILE = r'href="(.*?\.css).*?"'
RE_CSS_FILE = re.compile(RE_CSS_FILE, re.MULTILINE)


class CssProcess:
    RE_DESING = r'([\s\,#\.]*?\{.*?\}|([\s\,\.#]+[\-\:a-z0-9]+)+\s*?\{.*?\})'
    REPLACE_DIC = {"\n": "",
                   ", ": ",",
                   ": ": ":",
                   " {": "{",
                   "  ": ""}
    EXCEPT_ELEMENT = ['script', 'head', 'meta']
    EXCEPT_CLASS = ['adsbygoogle']
    _base = None
    _body = None

    def __init__(self, base, body):
        self._body = body
        self._base = base

    def get_except_list(self, val_list, except_list):
        new_list = list()
        for v in val_list:
            if v in except_list:
                continue
            new_list.append(v)
        return new_list

    def get_uniqe_list(self, val_list):
        return reduce(lambda x, y: x+[y] if y not in x else x, val_list, [])

    def get_element_list(self):
        element_list = RE_ELEMENT.findall(self._body)
        if not (element_list):
            return
        new_list = self.get_except_list(element_list, self.EXCEPT_ELEMENT)
        return self.get_uniqe_list(new_list)

    def get_class_list(self):
        new_list = list()
        class_list = RE_CLASS.findall(self._body)
        if not (class_list):
            return
        for cl in class_list:
            for nl in cl.split(' '):
                if nl:
                    new_list.append(nl)
        new_list = self.get_except_list(new_list, self.EXCEPT_CLASS)
        return self.get_uniqe_list(new_list)

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
            if self._base not in fl:
                file_list[index] = '{}{}'.format(self._base, fl)
                file_list[index] = file_list[index].replace('//', '/')
        return file_list

    def parse_css_element_on_body(self, material_list):
        style = list()
        for ml in material_list:
            RE_CSS_PARSE = r'[^\.\#]({cls}{frmt})'.format(
                cls='{}'.format(ml),
                frmt=self.RE_DESING
            )
            RE_CSS_PARSE = re.compile(RE_CSS_PARSE,
                                      re.MULTILINE | re.DOTALL | re.IGNORECASE)
            cs_list = RE_CSS_PARSE.findall(self._body)
            if not (cs_list):
                continue
            for cs in cs_list:
                tmp = cs[0]
                for i, j in self.REPLACE_DIC.items():
                    tmp = tmp.replace(i, j)
                style.append(tmp)
            # break

        return style

    def parse_css_id_on_body(self, material_list):
        style = list()
        for ml in material_list:
            RE_CSS_PARSE = r'(#{cls}{frmt})'.format(
                # cls='{}'.format(ml), frmt='[^"].*?\{.*?\}'
                cls='{}'.format(ml),
                frmt=self.RE_DESING
            )
            RE_CSS_PARSE = re.compile(RE_CSS_PARSE, re.MULTILINE | re.DOTALL)
            cs_list = RE_CSS_PARSE.findall(self._body)
            if not (cs_list):
                continue
            for cs in cs_list:
                tmp = cs[0]
                for i, j in self.REPLACE_DIC.items():
                    tmp = tmp.replace(i, j)
                style.append(tmp)

        return style

    def parse_css_class_on_body(self, material_list):
        style = list()
        for ml in material_list:
            RE_CSS_PARSE = r'(\.{cls}{frmt})'.format(
                cls='{}'.format(ml),
                frmt=self.RE_DESING
            )
            RE_CSS_PARSE = re.compile(RE_CSS_PARSE, re.MULTILINE | re.DOTALL)
            cs_list = RE_CSS_PARSE.findall(self._body)
            if not (cs_list):
                continue
            for cs in cs_list:
                tmp = cs[0]
                for i, j in self.REPLACE_DIC.items():
                    tmp = tmp.replace(i, j)
                style.append(tmp)
        return style
