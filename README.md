# rutas-cortadas

Visualización del estado de las rutas nacionales argentinas, reconstruido desde el historial de
[j-e-d/estadorutas](https://github.com/j-e-d/estadorutas).

```
./build.sh [ruta al clon de estadorutas]   # genera site/data.json (por defecto ../estadorutas)
python3 -m http.server -d site             # ver en http://localhost:8000
```

- `scripts/history.py`: recorre el historial de git y escribe `build/rutas_changes.csv` y `build/rutas_snapshots.csv`.
- `scripts/viz_data.py`: convierte los cambios en `site/data.json` (horas por estado, causas, episodios).
- `site/index.html`: la página; carga `data.json` y `geo.json`.
- `site/geo.json`: la traza de cada tramo para el mapa. Está versionado: no se regenera en cada build.
- `scripts/geometry.py`: genera `site/geo.json` y `geodata/match_report.md`. Se corre a mano cuando cambia la
  lista de tramos (solo biblioteca estándar; `scripts/geolib.py` tiene la geometría):

  ```
  python3 scripts/geometry.py fetch                                        # baja las capas a geodata/raw/ (~150 MB)
  python3 scripts/geometry.py build ../estadorutas build/rutas_changes.csv # ~1 minuto
  ```

  La tabla de Vialidad no trae coordenadas ni progresivas, solo el nombre del tramo y su largo. El script ubica
  los dos extremos de cada tramo sobre la traza (límites provinciales, empalmes, localidades, postes
  kilométricos) y descarta lo que no cierra. `geodata/match_report.md` lista qué se ubicó con qué confianza,
  qué quedó afuera y dónde el largo dibujado no coincide con los km de la tabla.

## Fuentes

- Estado de las rutas: Vialidad Nacional, argentina.gob.ar/obras-publicas/vialidad-nacional/estado-de-las-rutas,
  vía [j-e-d/estadorutas](https://github.com/j-e-d/estadorutas).
- Trazas, postes kilométricos e intersecciones: Dirección Nacional de Vialidad, SIG Vial
  (sigvial.vialidad.gob.ar), capas Red Vial Nacional 2025, Postes Kilométricos 2025 e Intersecciones 2025.
  Datos públicos del Estado nacional; la capa no declara una licencia.
- Límites provinciales y localidades (BAHRA): Instituto Geográfico Nacional de la República Argentina
  (wms.ign.gob.ar). Las localidades solo se usan para ubicar tramos; no se publican.

Un workflow de GitHub Actions reconstruye y publica en GitHub Pages una vez por día.
