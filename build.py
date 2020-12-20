import sys

try: 
    decklist = sys.argv[1]
except IndexError as e:
    print('Proxy builder for manual images')
    print("Usage: python build.py [decklist]")
    exit(1)

image_nodes = []
with open(decklist, 'r') as cards:
    for i, line in enumerate(cards):
        line = line.strip()
        if not line: continue
        amount, url = line.split(' ')
        for i in range(int(amount)):
            image_node = f'<img src="{url}" />'
            image_nodes.append(image_node)

styles = """body,
  html,
  img,
  a {
    border: none !important;
    margin: 0 !important;
    padding: 0 !important;
  }

  img {
    height: 316px !important;
    margin: 0 1px 1px 0 !important;
    width: 230px !important;
  }
"""
html = f"""<html>
<head>
  <style>
  {styles}
</style>
<body>
{''.join(image_nodes)}
</body>
</html>"""

print(html)