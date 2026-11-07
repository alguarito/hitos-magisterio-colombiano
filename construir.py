"""Arma la versión autónoma (un solo archivo, logo incrustado) a partir de fuente/linea-de-tiempo.html."""
import base64, pathlib
raiz = pathlib.Path(__file__).resolve().parent
html = (raiz / "fuente" / "linea-de-tiempo.html").read_text(encoding="utf-8")
logo = base64.b64encode((raiz / "assets" / "logo-sutev.png").read_bytes()).decode()
salida = html.replace("../assets/logo-sutev.png", "data:image/png;base64," + logo)
assert "../assets/" not in salida
(raiz / "index.html").write_text(salida, encoding="utf-8")
print("ok", len(salida), "bytes")
