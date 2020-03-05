# used_css_javascript
The used CSS Javascript list

## INSTALL
pip install -r requirements.txt

## PARSE
```
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
```

## USAGE
```
    python main.py http://abc.com/page.html http://abc.com
```
