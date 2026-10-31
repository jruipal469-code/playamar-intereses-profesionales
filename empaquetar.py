"""Empaqueta la aplicación sin dependencias ni conexiones externas.
Uso: python3 empaquetar.py
"""
from pathlib import Path
import base64
import hashlib
import re
import zipfile

raiz = Path(__file__).resolve().parent
dist = raiz / 'dist'
entrega = raiz / 'entrega'
entrega.mkdir(exist_ok=True)

def data_uri(nombre, mime):
    return 'data:' + mime + ';base64,' + base64.b64encode((dist / nombre).read_bytes()).decode('ascii')

html = (dist / 'index.html').read_text()
css = (dist / 'estilos.css').read_text()
for nombre in ['titillium-regular.woff', 'titillium-semibold.woff']:
    css = css.replace('./' + nombre, data_uri(nombre, 'font/woff'))
for nombre, mime in [('cabecera.webp', 'image/webp'), ('logo-playamar.svg', 'image/svg+xml')]:
    html = html.replace('./' + nombre, data_uri(nombre, mime))

partes = []
for nombre in ['datos.js', 'motor.js', 'app.js']:
    codigo = (dist / nombre).read_text()
    codigo = re.sub(r'^import .*?;\s*$', '', codigo, flags=re.MULTILINE)
    codigo = re.sub(r'\bexport\s+(?=const|function)', '', codigo)
    partes.append(codigo)
script = '\n(()=>{\n' + '\n'.join(partes) + '\n})();\n'
huella = base64.b64encode(hashlib.sha256(script.encode()).digest()).decode()
politica = "default-src 'none'; img-src data:; font-src data:; style-src 'unsafe-inline'; script-src 'sha256-" + huella + "'; connect-src 'none'; form-action 'none'; base-uri 'none'; object-src 'none'"
html = re.sub(r'(<meta http-equiv="Content-Security-Policy" content=")[^"]*(">)', lambda m: m[1] + politica + m[2], html)
html = html.replace(' <link rel="stylesheet" href="./estilos.css">', '<style>\n' + css + '\n</style>')
html = html.replace(' <script type="module" src="./app.js"></script>', '')
html = html.replace('</body>', '<script>' + script + '</script>\n</body>')
assert not re.search(r'\bimport\s.*?from\s', html)
assert 'src="./' not in html
(entrega / 'index.html').write_text(html)
(entrega / '.nojekyll').write_text('\n')
(entrega / 'LEEME.md').write_text((raiz / 'README.md').read_text())
(entrega / 'REVISION-LENGUAJE.md').write_text((raiz / 'REVISION-LENGUAJE.md').read_text())
with zipfile.ZipFile(raiz / 'Playamar-cuestionario-GitHub.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    for nombre in ['index.html', '.nojekyll', 'LEEME.md', 'REVISION-LENGUAJE.md']:
        z.write(entrega / nombre, nombre)
print('Paquete preparado:', raiz / 'Playamar-cuestionario-GitHub.zip')
print('Vista autónoma:', entrega / 'index.html')
