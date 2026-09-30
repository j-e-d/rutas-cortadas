# rutas-cortadas

Visualización del estado de las rutas nacionales argentinas, reconstruido desde el historial de
[j-e-d/estadorutas](https://github.com/j-e-d/estadorutas).

```
./build.sh [ruta al clon de estadorutas]   # genera site/data.json (por defecto ../estadorutas)
python3 -m http.server -d site             # ver en http://localhost:8000
```

- `scripts/history.py`: recorre el historial de git y escribe `build/rutas_changes.csv` y `build/rutas_snapshots.csv`.
- `scripts/viz_data.py`: convierte los cambios en `site/data.json` (horas por estado, causas, episodios).
- `site/index.html`: la página; carga `data.json`.

Un workflow de GitHub Actions reconstruye y publica en GitHub Pages una vez por día.
