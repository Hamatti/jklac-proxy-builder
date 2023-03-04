import os


decks = {}
formats = [folder for folder in os.listdir('.') if os.path.isdir(folder)]

for folder in formats:
    decks[folder] = [f for f in os.listdir(f'{folder}/') if os.path.isdir(os.path.join(folder, f)) and not f.startswith('.')]

html = '''
<html>
<head>
  <title>Proxy decks by formats</title>
</head>
<body>
<h1> Decks by formats </h1>
'''

for _format in decks:
    html += f"""
    <h2>{_format}</h2>
    <ul>"""

    for deck in decks[_format]:
        html += f'\n\t<li><a href="{_format}/{deck}/index.html">{deck}</a></li>'

    html += '\t\n</ul>'

html += '\n</body></html>'
print(html)
