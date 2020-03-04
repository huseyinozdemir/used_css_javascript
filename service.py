import re

from functools import reduce


RE_CLASS = 'class="(.*?)"'
RE_CLASS = re.compile(RE_CLASS, re.DOTALL)
RE_ID = 'id="(.*?)"'
RE_ID = re.compile(RE_ID, re.DOTALL)


def get_class_list(body):
    class_list = RE_CLASS.findall(body)
    if not (class_list):
        return
    return reduce(lambda x,y: x+[y] if not y in x else x, class_list, [])

def get_id_list(body):
    id_list = RE_ID.findall(body)
    if not (id_list):
        return
    return reduce(lambda x,y: x+[y] if not y in x else x, id_list, [])

if __name__ == '__main__':
    body = """
 <html>
  <head>
   <title>
    The Dormouse's story
   </title>
  </head>
  <body>
   <p class="title">
    <b>
     The Dormouse's story
    </b>
   </p>
   <p id="once" class="story">
    Once upon a time there were three little sisters; and their names were
    <a class="sister" href="http://example.com/elsie" id="link1">
     Elsie
    </a>
    ,
    <a class="sister" href="http://example.com/lacie" id="link2">
     Lacie
    </a>
    and
    <a class="sister" href="http://example.com/tillie" id="link2">
     Tillie
    </a>
    ; and they lived at the bottom of a well.
   </p>
   <p id="since" class="story">
    ...
   </p>
  </body>
 </html>
    """
    print(get_class_list(body))
    print(get_id_list(body))
