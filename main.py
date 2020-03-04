from app.css_process import CssProcess


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
    cp = CssProcess(body)
    print(cp.get_class_list())
    print(cp.get_id_list())
