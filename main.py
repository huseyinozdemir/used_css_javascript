from app.css_process import CssProcess

DOMAIN = 'https://www.eyzi.net/'


if __name__ == '__main__':
    body = """
 <html>
  <head>
   <title>
    The Dormouse's story
   </title>
   <link rel="canonical" href="https://www.pythontr.com" />
   <link rel="stylesheet" href="/css/main.min.css" type="text/css" />
   <link rel="preload" as="style" onload="this.rel='stylesheet'" href="https://www.eyzi.net/assets/css/font.awesome.min.css?display=swap&v=4" type="text/css">
   <style>
    div {
        background:#fff;
    }
    p {
        font-weight:10px;
    }
    .title{background-color:#fff;color:#000}
    .sister {
        margin: 0 auto;
        display: block;
        border: 2px solid #3bb8ea;
        overflow: hidden;
        border-radius: 14px;
    }
    .sister h1{
        margin: 0 auto;
    }
    #link1 {
        padding: 5px;
        background-color: #e4e4e4;
        margin: auto;
        margin-top: -5px;
        margin-bottom: 5px;
        border-radius: 0 0 6px 6px;
    }
    #link1 #link2 {
        padding: 5px;
        background-color: #e4e4e4;
        margin: auto;
        margin-top: -5px;
        margin-bottom: 5px;
        border-radius: 0 0 6px 6px;
    }
    #link2 {position: absolute;top: 0;left: 0;color: blue;}
    .story {
        position: absolute;
        width: 100%;
        bottom: 0;
        left: 0;
        right: 0;
        background: #000;
        background: rgba(0,0,0,0.7);
        color: #f9d327;
        transition: .5s ease;
        opacity: 0;
        font-size: 16px;
        padding: 1px;
        text-align: center;
        border-bottom-left-radius: 15px;
        border-bottom-right-radius: 15px;
        border-left: 2px solid;
        border-right: 2px solid;
        border-bottom: 2px solid;
    }
   </style>
  </head>
  <body>
  <div>
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
   </div>
  </body>
 </html>
    """
    cp = CssProcess(DOMAIN, body)
    print(cp.get_element_list())
    print(cp.get_css_file_list())
    class_list = cp.get_class_list()
    print(class_list)
    print(cp.parse_css_class_on_body(class_list))
    id_list = cp.get_id_list()
    print(id_list)
    print(cp.parse_css_id_on_body(id_list))
