#!/usr/bin/env python3
import sys
from urllib import request

from app.css_process import CssProcess

ERROR_NO_TARGET = 'python main.py http://abc.com/page.html http://abc.com'

# debug 1
DEBUG = 0

# static file
# body = open('input/test.html', 'r').read()


def set_out(input_list):
    result = ''
    for il in input_list:
        result += il
    return result

if __name__ == '__main__':
    if DEBUG:
        body = open('input/test.html', 'r').read()
    else:
        if len(sys.argv) < 2:
            sys.stderr.write('{}\n'.format(ERROR_NO_TARGET))
            sys.exit(2)
        if len(sys.argv) > 1:
            target = sys.argv[1:][0]
            body = request.urlopen(target).read().decode('utf-8')
            domain = sys.argv[2:][0]

    cp = CssProcess(domain, body)
    element_list = cp.get_element_list()
    class_list = cp.get_class_list()
    id_list = cp.get_id_list()
    out = ''
    out += set_out(cp.parse_css_element_on_body(element_list))
    out += set_out(cp.parse_css_class_on_body(class_list))
    out += set_out(cp.parse_css_id_on_body(id_list))

    print(out)
