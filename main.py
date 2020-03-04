from app.css_process import CssProcess

DOMAIN = 'https://www.eyzi.net/'


if __name__ == '__main__':
    body = open('input/test.html', 'r').read()
    cp = CssProcess(DOMAIN, body)
    element_list = cp.get_element_list()
    print(element_list)
    print(cp.parse_css_element_on_body(element_list))
    print("----------------------")
    class_list = cp.get_class_list()
    print(class_list)
    print(cp.parse_css_class_on_body(class_list))
    print("----------------------")
    id_list = cp.get_id_list()
    print(id_list)
    print(cp.parse_css_id_on_body(id_list))
    print("----------------------")
    print(cp.get_css_file_list())
