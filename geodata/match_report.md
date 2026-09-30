# Informe de ubicación de tramos

Generado por `scripts/geometry.py build`. Cada tramo de la tabla de Vialidad se ubicó sobre la traza de la
Red Vial Nacional 2025 (SIG Vial, DNV) buscando sus dos extremos.

- Tramos: 682
- Ubicados con confianza alta (los dos extremos anclados y el largo coincide): 442
- Ubicados por aproximación (interpolados o medidos en km desde un extremo anclado): 193
- Sin ubicar (no se dibujan): 47
- Con diferencia grande entre el largo dibujado y los km de la tabla: 29

## Sin ubicar

| Tramo | km tabla | Motivo |
|---|---|---|
| RN 1V03 · Buenos Aires · Emp. R.N. N° 3 - Rotonda Ex Indiada | 304.0 | sin ancla en un extremo y sin tramo vecino ubicado para medir |
| RN 252 · Buenos Aires · Rotonda V. Sarsfield - Emp. RN N° 3 | 6.0 | sin ancla en un extremo y sin tramo vecino ubicado para medir |
| RN A-001 · Buenos Aires · Puente La Noria - Emp. Avda. Lugones y Cantilo | 16.0 | ningún extremo del grupo pudo ubicarse sobre la traza |
| RN Au. Ezeiza Cañuelas · Buenos Aires · Fin AU Jorge Newbery - Cañuelas | 30.0 | la ruta no está en la capa de Vialidad |
| RN Av. Jorge Newbery · Buenos Aires · AU Riccheri (Dist. El Trébol) - AU Ezeiza - Cañuelas | 3.0 | la ruta no está en la capa de Vialidad |
| RN Puentes Riachuelo · Buenos Aires · Puente Alsina y accesos | 1.0 | la ruta no está en la capa de Vialidad |
| RN Puentes Riachuelo · Buenos Aires · Puente Avellaneda y accesos | 1.0 | la ruta no está en la capa de Vialidad |
| RN Puentes Riachuelo · Buenos Aires · Puente La Noria y accesos | 1.0 | la ruta no está en la capa de Vialidad |
| RN Puentes Riachuelo · Buenos Aires · Puente Pueyrredon y accesos | 1.0 | la ruta no está en la capa de Vialidad |
| RN Puentes Riachuelo · Buenos Aires · Puente Victorino de la Plaza y accesos | 1.0 | la ruta no está en la capa de Vialidad |
| RN 40 · Catamarca · Belén - Río Agua Clara | 11.0 | un extremo sin ancla y el largo no coincide (19 km sobre la traza) |
| RN 40 · Catamarca · Río Agua Clara - Río Las Cuevas | 36.0 | un extremo sin ancla y el largo no coincide (64 km sobre la traza) |
| RN 117 · Corrientes · Acc. Aeropuerto - Puente Internacional T. Neves | 5.0 | sin ancla en un extremo y sin tramo vecino ubicado para medir |
| RN 117 · Corrientes · Acc. a Paso de los Libres - Acc. Aeropuerto | 8.0 | sin ancla en un extremo y sin tramo vecino ubicado para medir |
| RN 121 · Corrientes · Acc. a Santo Tomé - Pte Internacional con Brasil | 8.0 | sin ancla en un extremo y sin tramo vecino ubicado para medir |
| RN 136 · Entre Ríos · Emp. RP 20 - Pte. Internacional General San Martín | 42.3 | sin ancla en un extremo y sin tramo vecino ubicado para medir |
| RN 11-AO11 · Formosa · Acc. a Pto. Pilcomayo | 11.0 | la ruta no está en la capa de Vialidad |
| RN 95 · Formosa · Fortín Lavalle - km 29,9 | 29.3 | medido en km desde un extremo, pero la traza de Vialidad se interrumpe en el medio |
| RN 73 · La Rioja · Anguinan - Fin del tramo | 8.0 | sin ancla en un extremo y sin tramo vecino ubicado para medir |
| RN 79 · La Rioja · Emp. RN N° 38 - Casa de Piedra | 126.0 | sin ancla en un extremo y sin tramo vecino ubicado para medir |
| RN S/N · Misiones · Pte. Internacional Posadas - Encarnación (Par) | 1.0 | la ruta no está en la capa de Vialidad |
| RN Vº RN 22 · Neuquén · Lte. Con Río Negro - Vinculación Autovía Norte | 6.86 | la ruta no está en la capa de Vialidad |
| RN Vº RN 22 · Neuquén · Vinculación Autovía Norte - Emp. RN 22 | 23.67 | la ruta no está en la capa de Vialidad |
| RN 40 · Río Negro · Inicio Circunv - Lte. Con Neuquen | 25.0 | sin ancla en un extremo y sin tramo vecino ubicado para medir |
| RN A026 · Río Negro · Acceso San Antonio Oeste (Km. 0,00 - Km 8,71) | 8.7 | sin ancla en un extremo y sin tramo vecino ubicado para medir |
| RN 51 · Salta · El Aybal - Campo Quijano | 22.0 | sin ancla en un extremo y sin tramo vecino ubicado para medir |
| RN 153 · San Juan · Media Agua - Pedernal | 38.0 | un extremo sin ancla y el largo no coincide (11 km sobre la traza) |
| RN 153 · San Juan · Pedernal - Km 57,80 | 20.0 | un extremo sin ancla y el largo no coincide (6 km sobre la traza) |
| RN 3 · Santa Cruz · Acc. Estancia Los Alamos - Acc. Estancia Moy Aike Chico km 2540 |  | sin ancla en un extremo y sin tramo vecino ubicado para medir |
| RN 3 · Santa Cruz · Antenas de telefónica km 2441 - Acc. Estancia Los Alamos |  | sin ancla en un extremo y sin tramo vecino ubicado para medir |
| RN 3 · Santa Cruz · PUENTE SOBRE RIO SANTA CRUZ (CTE. LUIS PIEDRABUENA) |  | los dos extremos caen en el mismo punto |
| RN 40 · Santa Cruz · Fin de pavimento ( km791.68) - Emp.RP73 |  | sin ancla en un extremo y sin tramo vecino ubicado para medir |
| RN 40 · Santa Cruz · Tres Lagos- Fin de pavimento ( km791.68) | 173.0 | sin ancla en un extremo y sin tramo vecino ubicado para medir |
| RN 98 · Santa Fe · Tostado - Lte. Sgo del Estero | 70.0 | los dos extremos caen en el mismo punto |
| RN A007 · Santa Fe · Emp. RN 11 - Calle Juan De Garay | 4.5 | sin ancla en un extremo y sin tramo vecino ubicado para medir |
| RN A007 · Santa Fe · Emp. RN 11 - Emp RN 1V11 | 2.7 | sin ancla en un extremo y sin tramo vecino ubicado para medir |
| RN A008 · Santa Fe · Emp. RN 9 - Acc. Sur a Puerto | 21.6 | sin ancla en un extremo y sin tramo vecino ubicado para medir |
| RN A008 · Santa Fe · Rio Parana - Emp. RN 9 | 8.19 | sin ancla en un extremo y sin tramo vecino ubicado para medir |
| RN 9 · Santiago del Estero · Ruta 9 (S) - Ruta 9 (N) | 4.0 | sin ancla en un extremo y sin tramo vecino ubicado para medir |
| RN Compl K · Tierra del Fuego, Antártida e Islas del Atlántico Sur · Emp. R. compl J - Emp. RP N° 30 |  | los dos extremos caen en el mismo punto |
| RN Región XII - Chile · Tierra del Fuego, Antártida e Islas del Atlántico Sur · Barcaza (Primera Angostura) |  | la ruta no está en la capa de Vialidad |
| RN Región XII - Chile · Tierra del Fuego, Antártida e Islas del Atlántico Sur · Monte Aymond - Integración Austral |  | la ruta no está en la capa de Vialidad |
| RN Región XII - Chile · Tierra del Fuego, Antártida e Islas del Atlántico Sur · San Sebastián - Paso Fronterizo |  | la ruta no está en la capa de Vialidad |
| RN 4V09 · Tucumán · EMP RPN°302 – Acceso a S. M. de Tucumán por Av. Benjamín Aráoz. |  | los dos extremos caen en el mismo punto |
| RN Ex 34 · Tucumán · Gdor. Garmendia - Lte. Salta | 28.0 | la ruta no está en la capa de Vialidad |
| RN Ex 34 · Tucumán · Lte. Sgo. Del Estero - Gdor. Garmendia | 39.0 | la ruta no está en la capa de Vialidad |
| RN Ex 9 · Tucumán · Acceso Norte a San Miguel de Tucumán | 1.3 | la ruta no está en la capa de Vialidad |

## Diferencias de largo

Largo dibujado contra km de la tabla, cuando difieren más de 3 km y más de 20%.

| Tramo | km tabla | km dibujado | Extremos |
|---|---|---|---|
| RN 22 · Río Negro · Allen - Cipolletti | 355.0 | 15.5 | localidad / intersección DNV |
| RN 40 · Salta · La Poma - La Quesera | 197.0 | 22.8 | localidad / localidad |
| RN 9 · Salta · Lte. Con Tucuman - Emp. RN 34 | 182.0 | 54.7 | límite / intersección DNV |
| RN 95 · Santa Fe · Villa Minetti - Lte. Con Chaco | 164.5 | 98.1 | intersección DNV / límite |
| RN 118 · Corrientes · San Miguel - Emp. RN 12 | 126.0 | 69.0 | localidad / cruce de rutas |
| RN 7 · Mendoza · Polvaredas - Punta de Vacas | 51.0 | 12.8 | localidad / localidad |
| RN 1S40 · Río Negro · Paso Flores - Emp. RN 23 | 80.0 | 47.3 | localidad / intersección DNV |
| RN 40 · Santa Cruz · Puente Blanco- El Turbio Viejo | 80.0 | 49.2 | localidad / localidad |
| RN 23 · Río Negro · Comallo - Pilcaniyeu | 56.0 | 32.7 | localidad / localidad |
| RN 3 · Santa Cruz · Emp. RN 288 - Estancia Ototel Aike *(dado de baja)* | 102.5 | 80.2 | intersección DNV / interpolado |
| RN 3 · Santa Cruz · Estancia Ototel Aike - Puesto Invernal Luis Trovato *(dado de baja)* | 76.0 | 59.4 | interpolado / interpolado |
| RN A019 · Córdoba · Avda. Circunvalación de Córdoba | 30.0 | 46.6 | fin de ruta / fin de ruta |
| RN 40 · Mendoza · Mendoza - Lte. Con San Juan | 76.0 | 92.5 | localidad / límite |
| RN 3 · Santa Cruz · Puesto invernal Luis Trovato - Guer Aike *(dado de baja)* | 75.0 | 58.6 | interpolado / localidad |
| RN 40 · Salta · La Quesera - Emp. RN 51 | 35.0 | 50.5 | localidad / intersección DNV |
| RN 40 · San Juan · Lte. Con Mendoza - Va. Media Agua | 33.0 | 20.3 | límite / intersección DNV |
| RN 40 · Santa Cruz · Casa Riera - Emp. RPN°37 | 45.0 | 55.6 | intersección DNV / intersección DNV |
| RN 7 · Mendoza · Punta De Vacas - Puente Del Inca | 26.0 | 15.6 | localidad / localidad |
| RN 131 · Entre Ríos · Emp. RP 11 - Emp. RN 12 | 41.0 | 31.8 | intersección DNV / intersección DNV |
| RN 22 · Neuquén · Plottier - Arroyito | 23.52 | 32.1 | localidad / localidad |
| RN 3 · Santa Cruz · Guer Aike- Río Gallegos *(dado de baja)* | 29.0 | 22.2 | localidad / localidad |
| RN 3 · Chubut · C.Rivadavia - Lte.Sta.Cruz | 17.31 | 24.1 | localidad / límite |
| RN 12 · Entre Ríos · Cerrito - Emp. RN 127 | 18.0 | 11.3 | localidad / intersección DNV |
| RN 40 · Santa Cruz · Río Olnie - Bajo Caracoles | 25.0 | 30.7 | localidad / localidad |
| RN 1v09 · Santa Fe · Emp. RN 178 - Lte. Con Córdoba | 22.5 | 28.1 | intersección DNV / límite |
| RN 12 · Misiones · Emp. RN 101 - Acc. a Puerto Iguazu | 14.0 | 10.2 | intersección DNV / localidad |
| RN 12 · Misiones · Acc. Aer. Posadas - Emp. RN 105 | 17.5 | 13.7 | interpolado / cruce de rutas |
| RN 64 · Santiago del Estero · La Banda - Sgo. Del Estero | 12.0 | 8.7 | intersección DNV / localidad |
| RN 36 · Córdoba · Emp. RN 8 - Int. RN A-005 | 5.0 | 8.2 | cruce de rutas / intersección DNV |

## Ubicados por aproximación

| Tramo | km tabla | km dibujado | Extremos |
|---|---|---|---|
| RN 22 · Buenos Aires · Lte. La Pampa - Rio Colorado | 59.0 | 59.0 | límite / km desde ancla |
| RN 228 · Buenos Aires · Acc. a San Cayetano - Camp. A Belloq | 70.0 | 67.8 | intersección DNV / interpolado |
| RN 228 · Buenos Aires · Camp. A Belloq - Tres Arroyos | 15.0 | 14.5 | interpolado / localidad |
| RN 229 · Buenos Aires · Emp. R.N.3 - B. Marisol P. Alta | 15.0 | 14.9 | intersección DNV / extremo |
| RN 252 · Buenos Aires · Emp RN N° 3 - Puente La Niña | 2.0 | 2.0 | intersección DNV / km desde ancla |
| RN 3 · Buenos Aires · Avda. G. Torres - Emp. RN 33 | 12.0 | 10.1 | interpolado / cruce de rutas |
| RN 3 · Buenos Aires · CABA - Cañuelas | 44.0 | 47.1 | extremo / localidad |
| RN 3 · Buenos Aires · El Triángulo - Ex J. N. Granos | 5.0 | 4.2 | intersección DNV / interpolado |
| RN 3 · Buenos Aires · Ex J. N. Granos - Avda. G. Torres | 2.0 | 1.7 | interpolado / interpolado |
| RN 3 · Buenos Aires · Gonzalez Chavez - Tres Arroyos | 44.0 | 44.6 | interpolado / localidad |
| RN 3 · Buenos Aires · Juarez - Gonzalez Chavez | 47.0 | 47.6 | intersección DNV / interpolado |
| RN 33 · Buenos Aires · Emp. Ex RN N° 33 - La Viticola | 16.0 | 15.9 | interpolado / localidad |
| RN 33 · Buenos Aires · Emp. RN N° 3 - Emp. Ex RN N° 33 | 8.0 | 7.9 | intersección DNV / interpolado |
| RN 33 · Buenos Aires · Gral. Villegas - Lte. Santa Fe | 76.0 | 75.3 | localidad / extremo |
| RN 7 · Buenos Aires · CABA - Luján | 50.0 | 50.0 | km desde ancla / localidad |
| RN 9 · Buenos Aires · CABA - Campana | 65.0 | 63.1 | extremo / intersección DNV |
| RN A-017 · Buenos Aires · KM 47 (Ezeiza) - RP N° 210 (Guernica) | 15.0 | 15.3 | interpolado / extremo |
| RN A-017 · Buenos Aires · RN N° 3 (La Matanza) - KM 47 (Ezeiza) | 15.0 | 15.3 | intersección DNV / interpolado |
| RN 38 · Catamarca · Fín Avda. Circunvalación - Lte. Con Tucumán | 66.0 | 64.6 | interpolado / límite |
| RN 38 · Catamarca · Lte. Con La Rioja - Fin Avda. Circunvalación | 80.0 | 79.0 | límite / interpolado |
| RN 16 · Chaco · Pte. Gral. M. Belgrano - Emp. RN 11 | 16.0 | 16.2 | extremo / intersección DNV |
| RN 1S40 · Chubut · El Maiten - Emp. RP 70 | 12.2 | 12.4 | localidad / interpolado |
| RN 1S40 · Chubut · Emp. RP 70 - Emp. RN 40 | 19.6 | 19.8 | interpolado / intersección DNV |
| RN 3 · Chubut · Aº Verde - Pto.Madryn | 92.82 | 88.3 | extremo / localidad |
| RN 3 · Chubut · C.Rivadavia - Lte.Sta.Cruz | 17.31 | 24.1 | localidad / límite |
| RN 40 · Chubut · Acc.Cholila - El Bolson | 47.3 | 47.0 | intersección DNV / km desde ancla |
| RN 118 · Corrientes · San Miguel - Emp. RN 12 | 126.0 | 69.0 | localidad / cruce de rutas |
| RN 12 · Corrientes · Cuatro Bocas - Saladas | 69.0 | 69.6 | interpolado / intersección DNV |
| RN 12 · Corrientes · Goya - Cuatro Bocas | 76.0 | 76.6 | localidad / interpolado |
| RN 120 · Corrientes · Emp. RN 14 - Puente (Río Aguapey) | 30.0 | 30.2 | intersección DNV / interpolado |
| RN 120 · Corrientes · Puente (Río Aguapey) - Embalse Yaciretá | 27.0 | 27.2 | interpolado / extremo |
| RN 122 · Corrientes · Acc. a Yapeyú - Centro Yapeyú | 6.0 | 5.9 | extremo / localidad |
| RN 148 · Córdoba · Lte. C/San Luis - Emp RP 14 | 41.0 | 41.4 | extremo / intersección DNV |
| RN 19 · Córdoba · Cda. Jean Marie - Arroyito | 57.0 | 57.3 | interpolado / localidad |
| RN 19 · Córdoba · San Francisco - Cda. Jean Marie | 38.0 | 38.2 | localidad / interpolado |
| RN 36 · Córdoba · Emp. RN 8 - Int. RN A-005 | 5.0 | 8.2 | cruce de rutas / intersección DNV |
| RN 9 · Córdoba · Córdoba - Jesús María (entrada) | 40.0 | 39.8 | interpolado / localidad |
| RN 9 · Córdoba · Jesús María ( Entrada ) - Jesús María ( Salida ) | 8.0 | 7.7 | localidad / interpolado |
| RN 9 · Córdoba · Jesús María (salida) - Lte. Sgo del Estero | 155.0 | 148.6 | interpolado / límite |
| RN 9 · Córdoba · Pilar - Córdoba | 54.0 | 53.8 | intersección DNV / interpolado |
| RN A019 · Córdoba · Avda. Circunvalación de Córdoba | 30.0 | 46.6 | fin de ruta / fin de ruta |
| RN 12 · Entre Ríos · Cerrito - Emp. RN 127 | 18.0 | 11.3 | localidad / intersección DNV |
| RN 12 · Entre Ríos · Hernandarias - La Paz | 65.0 | 66.0 | intersección DNV / interpolado |
| RN 12 · Entre Ríos · La Paz - Lte. Corrientes | 46.0 | 46.7 | interpolado / límite |
| RN 131 · Entre Ríos · Emp. RP 11 - Emp. RN 12 | 41.0 | 31.8 | intersección DNV / intersección DNV |
| RN 135 · Entre Ríos · Emp. RN 14 - Pte. Internac. Gervasio Artigas | 14.65 | 14.7 | intersección DNV / extremo |
| RN 174 · Entre Ríos · Victoria - Rosario | 57.0 | 56.6 | intersección DNV / extremo |
| RN 18 · Entre Ríos · San Salvador - Emp. RN 14 | 62.0 | 62.1 | interpolado / intersección DNV |
| RN 18 · Entre Ríos · Villaguay - San Salvador | 30.0 | 30.0 | intersección DNV / interpolado |
| RN 11 · Formosa · Lucio Mansilla - Pte. San. Ignacio de Loyola | 189.75 | 189.5 | localidad / extremo |
| RN 81 · Formosa · Ing. Juarez - Km 25,5 | 35.1 | 35.1 | localidad / km desde ancla |
| RN 81 · Formosa · Juan Bazan - P. del Mortero | 24.3 | 24.8 | intersección DNV / interpolado |
| RN 81 · Formosa · Km. 25,5 - Lte. Con Salta | 25.5 | 25.5 | km desde ancla / límite |
| RN 81 · Formosa · Las Lomitas - J. G. Bazan | 30.8 | 30.8 | localidad / km desde ancla |
| RN 81 · Formosa · Pozo del Mortero - Laguna Yema | 27.6 | 28.1 | interpolado / localidad |
| RN 86 · Formosa · El Solitario - M. San Martin |  | 244.4 | localidad / extremo |
| RN 95 · Formosa · Km. 29,9 - Emp. RN 81 | 29.9 | 29.9 | km desde ancla / intersección DNV |
| RN 52 · Jujuy · Emp. RP 79 - Susques | 89.0 | 88.4 | intersección DNV / interpolado |
| RN 52 · Jujuy · Susques - Lte. con Chile | 105.0 | 104.9 | interpolado / frontera |
| RN 66 · Jujuy · El Cadillal - Emp. RN 34 | 34.0 | 33.9 | interpolado / intersección DNV |
| RN 66 · Jujuy · Emp. RN 9 - El Cadillal | 4.0 | 4.0 | intersección DNV / interpolado |
| RN 9 · Jujuy · Acc. a Dique La Ciénaga - Río Perico | 9.0 | 8.3 | localidad / interpolado |
| RN 9 · Jujuy · Emp. RN 52 - Paraje San Pedrito | 40.0 | 39.6 | intersección DNV / interpolado |
| RN 9 · Jujuy · Paraje San Pedrito - Acc. a Iturbe | 50.0 | 49.7 | interpolado / intersección DNV |
| RN 9 · Jujuy · Río Perico - S.S. de Jujuy | 23.0 | 21.4 | interpolado / localidad |
| RN 143 · La Pampa · Limay Mahuida - Río Salado | 56.2 | 56.3 | localidad / interpolado |
| RN 143 · La Pampa · Río Salado - Santa Isabel | 63.78 | 63.9 | interpolado / localidad |
| RN 151 · La Pampa · Pto. La Adelina - Algarrobo del Aguila | 47.9 | 48.2 | interpolado / localidad |
| RN 151 · La Pampa · Puelen - Pto. La Adelina | 65.74 | 66.2 | localidad / interpolado |
| RN 154 · La Pampa · Cotita Emp. RN 35 - Emp. RP 28 | 36.3 | 36.3 | intersección DNV / interpolado |
| RN 154 · La Pampa · Emp. RP 28 - Emp. RP 30 | 30.2 | 30.2 | interpolado / intersección DNV |
| RN 188 · La Pampa · Lte. Bs. As./La Pampa - Emp. R.P.7 | 50.35 | 50.1 | extremo / intersección DNV |
| RN 22 · La Pampa · Lte. Con Bs. As. - Lte. Con Río Negro | 63.71 | 61.0 | extremo / límite |
| RN 35 · La Pampa · Lte. Bs As - Bernasconi | 37.63 | 36.8 | extremo / localidad |
| RN 5 · La Pampa · Lte. Bs. As - Emp. R.P. 3 | 42.89 | 43.0 | extremo / intersección DNV |
| RN 40 · La Rioja · Cachiyuyal - Nonogasta | 24.0 | 23.9 | interpolado / localidad |
| RN 40 · La Rioja · Los Tambillos - Cachiyuyal | 18.0 | 17.1 | localidad / interpolado |
| RN 75 · La Rioja · La Rioja - Los Sauces | 18.0 | 17.6 | intersección DNV / interpolado |
| RN 75 · La Rioja · Los Sauces - Sanagasta | 14.0 | 13.8 | interpolado / localidad |
| RN 76 · La Rioja · Alto Jagüe - Queb. Santo Domingo | 35.0 | 36.4 | localidad / interpolado |
| RN 76 · La Rioja · Queb. Santo Domingo - Barrancas Blanca | 88.0 | 90.3 | interpolado / localidad |
| RN 78 · La Rioja · Campanas - Lte. Con Catamarca | 20.0 | 19.9 | localidad / km desde ancla |
| RN 142 · Mendoza · Jocoli - G. Grande | 35.0 | 34.9 | intersección DNV / km desde ancla |
| RN 145 · Mendoza · Cajón Grande - Lte. Internacional | 10.0 | 8.1 | localidad / interpolado |
| RN 145 · Mendoza · Paso Internacional El Pehuenche | 5.0 | 4.1 | interpolado / fin de ruta |
| RN 40 · Mendoza · A. Hondo - Pareditas | 67.0 | 57.3 | interpolado / localidad |
| RN 40 · Mendoza · Empalme RN 144 - A. Hondo | 96.0 | 82.0 | intersección DNV / interpolado |
| RN 40 · Mendoza · Mendoza - Lte. Con San Juan | 76.0 | 92.5 | localidad / límite |
| RN 7 · Mendoza · Lte.Con San Luis - Mendoza | 175.0 | 174.8 | límite / km desde ancla |
| RN 7 · Mendoza · Polvaredas - Punta de Vacas | 51.0 | 12.8 | localidad / localidad |
| RN 7 · Mendoza · Punta De Vacas - Puente Del Inca | 26.0 | 15.6 | localidad / localidad |
| RN 101 · Misiones · Acc. Aer. Iguazu - Empalme RN 12 | 6.0 | 6.1 | interpolado / cruce de rutas |
| RN 101 · Misiones · Bdo. De Irigoyen - San Antonio | 32.0 | 31.3 | extremo / localidad |
| RN 101 · Misiones · Empalme RP 19 - Lte. Parque Nacional Iguazu | 11.0 | 11.1 | intersección DNV / interpolado |
| RN 101 · Misiones · Lte. Parque Nacional Iguazu - Acc. Aer. Iguazu | 32.0 | 32.3 | interpolado / interpolado |
| RN 12 · Misiones · Acc. Aer. Posadas - Emp. RN 105 | 17.5 | 13.7 | interpolado / cruce de rutas |
| RN 12 · Misiones · Acc. a Puerto Iguazu - Puente Inter. Tancredo Neves | 3.0 | 1.2 | localidad / interpolado |
| RN 12 · Misiones · Emp. RN 101 - Acc. a Puerto Iguazu | 14.0 | 10.2 | intersección DNV / localidad |
| RN 12 · Misiones · Lte. Con Corrientes - Acc. Aer. Posadas | 13.2 | 10.3 | límite / interpolado |
| RN 12 · Misiones · Puente Inter. "Tancredo Neves" Puerto Iguazu (Arg) | 1.0 | 0.4 | interpolado / fin de ruta |
| RN 22 · Neuquén · Plottier - Arroyito | 23.52 | 32.1 | localidad / localidad |
| RN 231 · Neuquén · Aduana - Lte. con Chile | 16.53 | 15.7 | interpolado / frontera |
| RN 231 · Neuquén · Emp. RN 40 - Aduana | 14.94 | 14.7 | intersección DNV / interpolado |
| RN 237 · Neuquén · Arroyo Limay Chico - Emp. RN 40 | 67.36 | 65.9 | interpolado / intersección DNV |
| RN 237 · Neuquén · Piedra del Aguila - Arroyo Limay Chico | 118.79 | 116.7 | localidad / interpolado |
| RN 242 · Neuquén · Aduana - Lte. con Chile | 7.21 | 7.1 | interpolado / frontera |
| RN 242 · Neuquén · Las Lajas - Aduana | 51.63 | 51.1 | intersección DNV / interpolado |
| RN 1S40 · Río Negro · Paso Flores - Emp. RN 23 | 80.0 | 47.3 | localidad / intersección DNV |
| RN 22 · Río Negro · Allen - Cipolletti | 355.0 | 15.5 | localidad / intersección DNV |
| RN 23 · Río Negro · C. Oneli - Comallo | 41.0 | 41.6 | interpolado / localidad |
| RN 23 · Río Negro · Comallo - Pilcaniyeu | 56.0 | 32.7 | localidad / localidad |
| RN 23 · Río Negro · Ingeniero Jacobacci - C. Oneli | 47.0 | 47.9 | localidad / interpolado |
| RN 23 · Río Negro · Mtro. Ramos Mexia - Los Menucos | 89.0 | 88.2 | interpolado / intersección DNV |
| RN 23 · Río Negro · Valcheta - Mtro. Ramos Mexia | 104.0 | 103.1 | localidad / interpolado |
| RN A025 · Río Negro · Acceso Puerto S.A. Este (Km 0,00 - Km 28,14) | 28.0 | 27.9 | localidad / extremo |
| RN 34 · Salta · Lte. Con Sgo. Del Estero - Emp. RN 9 | 67.0 | 68.4 | extremo / intersección DNV |
| RN 34 · Salta · Torzalito - Lte. Con Jujuy | 20.0 | 20.0 | km desde ancla / límite |
| RN 40 · Salta · La Darsena - Seclantas | 105.0 | 95.4 | interpolado / localidad |
| RN 40 · Salta · La Poma - La Quesera | 197.0 | 22.8 | localidad / localidad |
| RN 40 · Salta · La Quesera - Emp. RN 51 | 35.0 | 50.5 | localidad / intersección DNV |
| RN 40 · Salta · Lte. Con Tucuman - La Darsena | 57.0 | 52.9 | límite / interpolado |
| RN 68 · Salta · Talapampa - Rio Ancho | 61.4 | 61.0 | localidad / km desde ancla |
| RN 9 · Salta · Emp. RN 34 - Torzalito | 125.0 | 122.6 | intersección DNV / interpolado |
| RN 9 · Salta · Lte. Con Tucuman - Emp. RN 34 | 182.0 | 54.7 | límite / intersección DNV |
| RN 9 · Salta · Torzalito - Acc. Salta | 48.0 | 47.1 | interpolado / localidad |
| RN 150 · San Juan · Jachal - Rodeo | 40.0 | 39.6 | localidad / interpolado |
| RN 150 · San Juan · Rodeo - Las Flores | 23.0 | 23.1 | interpolado / intersección DNV |
| RN 20 · San Juan · Caucete - Acc. Oeste SJ | 22.0 | 22.0 | localidad / km desde ancla |
| RN 20 · San Juan · Km 578 - Km 582 (circunvalación) | 4.0 | 2.8 | km / extremo |
| RN 40 · San Juan · Lte. Con Mendoza - Va. Media Agua | 33.0 | 20.3 | límite / intersección DNV |
| RN 40 · San Juan · Matagusanos - Talacasto | 35.0 | 37.9 | interpolado / intersección DNV |
| RN 40 · San Juan · San Juan - Matagusanos | 16.0 | 17.4 | localidad / interpolado |
| RN 288 · Santa Cruz · Punta Quilla - Emp. RN º 3 | 41.0 | 41.0 | localidad / km desde ancla |
| RN 3 · Santa Cruz · Acc Reserva Laguna Azul-Paso Fronterizo Integracion Austral km2673 |  | 12.8 | km / km |
| RN 3 · Santa Cruz · Acc. Estancia Moy Aike Chico km 2540 - Guer Aike |  | 42.7 | km / localidad |
| RN 3 · Santa Cruz · Chimen Aike -Acc.Reserva Laguna Azul Km 2660 |  | 42.9 | intersección DNV / km |
| RN 3 · Santa Cruz · Emp. RN 288 - Estancia Ototel Aike *(dado de baja)* | 102.5 | 80.2 | intersección DNV / interpolado |
| RN 3 · Santa Cruz · Emp. RN 288 - Pje. Lemarchand *(dado de baja)* | 107.0 | 99.6 | intersección DNV / interpolado |
| RN 3 · Santa Cruz · Empalme Aeropuerto-Chimen Aike |  | 11.0 | intersección DNV / intersección DNV |
| RN 3 · Santa Cruz · Empalme RN N° 288 - Empalme RP 9 |  | 35.7 | intersección DNV / intersección DNV |
| RN 3 · Santa Cruz · Estancia Ototel Aike - Puesto Invernal Luis Trovato *(dado de baja)* | 76.0 | 59.4 | interpolado / interpolado |
| RN 3 · Santa Cruz · Guer Aike- Río Gallegos *(dado de baja)* | 29.0 | 22.2 | localidad / localidad |
| RN 3 · Santa Cruz · Guer Aike-Empalme Aeropuerto |  | 21.5 | localidad / intersección DNV |
| RN 3 · Santa Cruz · Pje. Lemarchand - Güer Aike *(dado de baja)* | 106.0 | 98.6 | interpolado / localidad |
| RN 3 · Santa Cruz · Puesto invernal Luis Trovato - Guer Aike *(dado de baja)* | 75.0 | 58.6 | interpolado / localidad |
| RN 40 · Santa Cruz · 28 de Noviembre - Tapi Aike |  | 76.2 | localidad / intersección DNV |
| RN 40 · Santa Cruz · Bajada De Miguez - Emp. RP 11 | 28.0 | 27.2 | interpolado / intersección DNV |
| RN 40 · Santa Cruz · Bajo Caracoles - Río Ecker | 46.0 | 49.1 | localidad / interpolado |
| RN 40 · Santa Cruz · Casa Riera - Emp. RPN°37 | 45.0 | 55.6 | intersección DNV / intersección DNV |
| RN 40 · Santa Cruz · El Cerrito - Bajada de Miguez | 35.0 | 34.1 | intersección DNV / interpolado |
| RN 40 · Santa Cruz · El Turbio Viejo- 28 de Noviembre |  | 18.6 | localidad / localidad |
| RN 40 · Santa Cruz · El Turbio-La Esperanza *(dado de baja)* |  | 171.0 | localidad / intersección DNV |
| RN 40 · Santa Cruz · Emp. R.N. N°3 (Chimen Aike) - Punta Loyola |  | 25.2 | intersección DNV / localidad |
| RN 40 · Santa Cruz · Emp.RP73 -Emp. RP29 |  | 30.4 | intersección DNV / intersección DNV |
| RN 40 · Santa Cruz · Gobernador Gregores - Casa Riera |  | 70.1 | localidad / intersección DNV |
| RN 40 · Santa Cruz · Puente Blanco- El Turbio *(dado de baja)* |  | 49.2 | localidad / localidad |
| RN 40 · Santa Cruz · Puente Blanco- El Turbio Viejo | 80.0 | 49.2 | localidad / localidad |
| RN 40 · Santa Cruz · Río Ecker - Perito Moreno | 74.0 | 79.0 | interpolado / localidad |
| RN 40 · Santa Cruz · Río Olnie - Bajo Caracoles | 25.0 | 30.7 | localidad / localidad |
| RN 40 · Santa Cruz · Tapi Aike - La Esperanza |  | 76.1 | intersección DNV / intersección DNV |
| RN 168 · Santa Fe · Santa Fe - Parana | 17.0 | 18.1 | localidad / extremo |
| RN 174 · Santa Fe · Rosario - Victoria | 2.6 | 2.6 | intersección DNV / extremo |
| RN 178 · Santa Fe · Lte. Con Bs. As. - Emp. RN 33 | 69.0 | 68.6 | extremo / intersección DNV |
| RN 19 · Santa Fe · Santo Tomé - San francisco | 127.63 | 129.6 | intersección DNV / extremo |
| RN 1v09 · Santa Fe · Emp. RN 178 - Lte. Con Córdoba | 22.5 | 28.1 | intersección DNV / límite |
| RN 33 · Santa Fe · Lte. Con Bs.As. - Rufino | 22.0 | 23.0 | extremo / localidad |
| RN 7 · Santa Fe · Lte. Con Bs.As. - Lte. Con Cordoba | 56.13 | 57.2 | extremo / límite |
| RN 8 · Santa Fe · Lte. Con Santafe - Lte. Con Cordoba | 118.0 | 112.7 | extremo / límite |
| RN 9 · Santa Fe · Gral. Lagos - Rosario | 9.0 | 9.2 | interpolado / interpolado |
| RN 9 · Santa Fe · Lte. Con Bs. As. - Gral. Lagos | 50.0 | 51.5 | extremo / interpolado |
| RN 9 · Santa Fe · Rosario - Carcaraña | 39.63 | 40.8 | interpolado / localidad |
| RN 95 · Santa Fe · Villa Minetti - Lte. Con Chaco | 164.5 | 98.1 | intersección DNV / límite |
| RN 34 · Santiago del Estero · Antilla - Rosario De La Frontera | 70.4 | 70.3 | km desde ancla / km desde ancla |
| RN 34 · Santiago del Estero · Garmendia - Antilla | 39.2 | 39.2 | km desde ancla / km desde ancla |
| RN 34 · Santiago del Estero · Pozo Hondo - Garmendia | 66.0 | 66.0 | localidad / km desde ancla |
| RN 64 · Santiago del Estero · La Banda - Sgo. Del Estero | 12.0 | 8.7 | intersección DNV / localidad |
| RN 3 · Tierra del Fuego, Antártida e Islas del Atlántico Sur · Cabo Espíritu Santo - San Sebastián | 87.77 | 86.8 | extremo / localidad |
| RN 3 · Tierra del Fuego, Antártida e Islas del Atlántico Sur · La Herradura - Rancho Hambre | 11.0 | 10.2 | interpolado / intersección DNV |
| RN 3 · Tierra del Fuego, Antártida e Islas del Atlántico Sur · Puente Justicia - Tolhuin | 16.2 | 16.5 | interpolado / localidad |
| RN 3 · Tierra del Fuego, Antártida e Islas del Atlántico Sur · Río Grande - Puente Justicia | 83.85 | 85.6 | intersección DNV / interpolado |
| RN 3 · Tierra del Fuego, Antártida e Islas del Atlántico Sur · Tolhuin - La Herradura | 56.0 | 53.3 | localidad / interpolado |
| RN Compl A · Tierra del Fuego, Antártida e Islas del Atlántico Sur · Emp. RN 3 - Ea. Maria Luisa | 66.0 | 64.8 | intersección DNV / km desde ancla |
| RN Compl B · Tierra del Fuego, Antártida e Islas del Atlántico Sur · Emp. RN 3 - Puesto Radman | 70.0 | 69.2 | intersección DNV / extremo |
| RN Compl J · Tierra del Fuego, Antártida e Islas del Atlántico Sur · Emp. RN 3 - Puesto Moat | 91.0 | 88.7 | intersección DNV / extremo |
| RN 38 · Tucumán · J.B. Alberdi - Aguilares | 17.31 | 17.2 | interpolado / intersección DNV |
| RN 38 · Tucumán · Lte. Con Catamarca - J.B. Alberdi | 49.61 | 49.4 | límite / interpolado |
| RN 40 · Tucumán · Acc. a la Ciudad Sagrada de Quilmes - Colalao del Valle | 15.0 | 14.8 | interpolado / localidad |
| RN 40 · Tucumán · Lte. Catamarca - Acc. a la Ciudad Sagrada de Quilmes | 14.0 | 13.8 | límite / interpolado |
| RN 65 · Tucumán · Alpachiri - Campamento D.N.V. | 21.67 | 21.3 | localidad / km desde ancla |
| RN 65 · Tucumán · Campamento D.N.V. - Lte. Con Catamarca | 7.1 | 5.6 | km desde ancla / km desde ancla |
| RN 9 · Tucumán · Las Talitas - Acc. a El Cadillal | 13.21 | 13.1 | interpolado / localidad |
| RN 9 · Tucumán · San Cayetano - Acc. a Las Talitas | 12.0 | 11.9 | localidad / interpolado |
| RN A016 · Tucumán · Aerop. Internacional - Acc. a Alderetes | 2.07 | 3.0 | extremo / localidad |

## Ubicados con confianza alta

| Tramo | km tabla | km dibujado | Extremos |
|---|---|---|---|
| RN 12 · Buenos Aires · Zarate - Lte. Entre Rios | 32.0 | 28.1 | intersección DNV / límite |
| RN 188 · Buenos Aires · Junín - Lte. La Pampa | 243.0 | 239.0 | localidad / límite |
| RN 188 · Buenos Aires · Pergamino - Junín | 82.0 | 86.5 | localidad / localidad |
| RN 188 · Buenos Aires · San Nicolás - Pergamino | 74.0 | 70.5 | localidad / localidad |
| RN 193 · Buenos Aires · Int. RN Nº 9 - Int. RN Nº 8 | 32.0 | 31.6 | intersección DNV / intersección DNV |
| RN 205 · Buenos Aires · Cañuelas - Emp. RN 3 | 1.0 | 3.3 | localidad / intersección DNV |
| RN 205 · Buenos Aires · Cañuelas - Int. RP 51 | 116.0 | 121.8 | localidad / intersección DNV |
| RN 205 · Buenos Aires · Int. RP 51 - Bolivar | 128.0 | 128.2 | intersección DNV / intersección DNV |
| RN 22 · Buenos Aires · Empalme R.N.3 - Medanos | 14.0 | 13.9 | intersección DNV / localidad |
| RN 22 · Buenos Aires · Medanos - Lte.con La Pampa | 60.0 | 62.8 | localidad / límite |
| RN 226 · Buenos Aires · Mar del Plata - Olavarria | 297.0 | 296.3 | intersección DNV / localidad |
| RN 226 · Buenos Aires · Olavarria - Gral. Villegas | 325.0 | 323.7 | localidad / localidad |
| RN 228 · Buenos Aires · Necochea - Acc. a San Cayetano | 55.0 | 53.1 | localidad / intersección DNV |
| RN 249 · Buenos Aires · Emp. R.N.3 - Emp. R.N. 229 P. Alta | 20.0 | 19.3 | cruce de rutas / intersección DNV |
| RN 3 · Buenos Aires · Azul - Chillar | 54.0 | 61.8 | localidad / localidad |
| RN 3 · Buenos Aires · Bajo Hondo - Emp. RN 229 | 18.0 | 16.6 | localidad / intersección DNV |
| RN 3 · Buenos Aires · Cañuelas - Azul | 246.0 | 232.2 | localidad / localidad |
| RN 3 · Buenos Aires · Chillar - Juarez | 41.0 | 40.8 | localidad / intersección DNV |
| RN 3 · Buenos Aires · Cnel. Dorrego - Bajo Hondo | 58.0 | 58.6 | localidad / localidad |
| RN 3 · Buenos Aires · Emp. RN 22 - Tte.Origone | 37.0 | 37.0 | intersección DNV / localidad |
| RN 3 · Buenos Aires · Emp. RN N° 229 - El Triángulo | 7.0 | 7.7 | intersección DNV / intersección DNV |
| RN 3 · Buenos Aires · Emp. RN N° 33 - Emp. RN N° 22 | 21.0 | 22.8 | cruce de rutas / intersección DNV |
| RN 3 · Buenos Aires · Pedro Luro - Stroeder | 73.0 | 76.5 | localidad / localidad |
| RN 3 · Buenos Aires · Stroeder - Patagones | 82.0 | 80.1 | localidad / localidad |
| RN 3 · Buenos Aires · Tres Arroyos - Cnel. Dorrego | 100.0 | 100.8 | localidad / localidad |
| RN 3 · Buenos Aires · Tte.Origone - Pedro Luro | 52.0 | 50.8 | localidad / localidad |
| RN 33 · Buenos Aires · Guamini - Trenque Lauquen | 124.0 | 124.4 | localidad / localidad |
| RN 33 · Buenos Aires · La Viticola - Tornquist | 45.0 | 47.1 | localidad / localidad |
| RN 33 · Buenos Aires · Pigüé - Guamini | 65.0 | 66.7 | localidad / localidad |
| RN 33 · Buenos Aires · Tornquist - Pigüé | 58.0 | 60.1 | localidad / localidad |
| RN 33 · Buenos Aires · Trenque Lauquen - Gral. Villegas | 117.0 | 114.2 | localidad / localidad |
| RN 35 · Buenos Aires · Bahía Blanca - Nueva Roma | 30.0 | 31.7 | localidad / localidad |
| RN 35 · Buenos Aires · Nueva Roma - San Germán | 43.0 | 41.3 | localidad / localidad |
| RN 35 · Buenos Aires · San Germán - Lte. La Pampa | 44.0 | 44.3 | localidad / límite |
| RN 5 · Buenos Aires · Lujan - Lte. La Pampa | 458.0 | 458.4 | intersección DNV / límite |
| RN 7 · Buenos Aires · Luján - Lte. Santa Fe | 308.0 | 306.6 | localidad / límite |
| RN 8 · Buenos Aires · Pilar - Lte. Santa Fe | 226.0 | 234.9 | intersección DNV / límite |
| RN 9 · Buenos Aires · Campana - Lte. Santa Fe | 160.0 | 161.5 | intersección DNV / límite |
| RN A-017 · Buenos Aires · RP N° 40(Merlo) - RN N° 3 (La Matanza) | 17.0 | 18.4 | intersección DNV / intersección DNV |
| RN Au. Riccheri · Buenos Aires · AV. Gral. Paz - Aeropuerto Ezeiza | 14.0 | 15.1 | intersección DNV / localidad |
| RN 157 · Catamarca · Emp. RN 60 - Lte. Sgo. Del Estero | 92.0 | 95.3 | intersección DNV / límite |
| RN 40 · Catamarca · Emp. RN 60 - Belén | 87.0 | 84.2 | intersección DNV / localidad |
| RN 40 · Catamarca · Río Las Cuevas - Santa María | 88.0 | 87.7 | localidad / localidad |
| RN 40 · Catamarca · Santa María -Lte. Con Tucumán | 14.0 | 12.8 | localidad / límite |
| RN 60 · Catamarca · Cortaderas - Lte. Int. Con Chile | 103.0 | 103.0 | localidad / frontera |
| RN 60 · Catamarca · Emp. RN 157 - Emp RP 33 | 109.0 | 111.1 | intersección DNV / intersección DNV |
| RN 60 · Catamarca · Emp. RN 38 - Lte. Con La Rioja | 42.0 | 42.9 | intersección DNV / límite |
| RN 60 · Catamarca · Emp. RP 33 - Emp. RN 38 | 60.0 | 60.7 | intersección DNV / intersección DNV |
| RN 60 · Catamarca · Fiambalá - Cortaderas | 94.0 | 94.9 | localidad / localidad |
| RN 60 · Catamarca · Lte. Con Córdoba - Emp. RN 157 | 9.0 | 8.1 | límite / intersección DNV |
| RN 60 · Catamarca · Lte. Con La Rioja - Tinogasta | 70.0 | 66.5 | límite / localidad |
| RN 60 · Catamarca · Tinogasta - Fiambalá | 46.0 | 48.0 | localidad / localidad |
| RN 64 · Catamarca · Lte. Con Sgo. Del Estero - Lte. Con Tucuman | 56.0 | 55.9 | límite / límite |
| RN 11 · Chaco · Lte. Con Sta. Fe - Resistencia | 77.0 | 73.4 | límite / localidad |
| RN 11 · Chaco · Resistencia - Lte. Con Formosa | 95.0 | 98.6 | localidad / límite |
| RN 16 · Chaco · Emp. RN 11 - Emp. RN 95 | 180.0 | 158.5 | intersección DNV / intersección DNV |
| RN 16 · Chaco · Emp. RN 95 - Pampa del Infierno | 80.0 | 83.0 | intersección DNV / intersección DNV |
| RN 16 · Chaco · Lte. Sgo. Del Estero - Lte. Con Salta | 18.0 | 17.7 | límite / límite |
| RN 16 · Chaco · Pampa del Infierno - Lte. Sgo. Del Estero | 52.0 | 62.1 | intersección DNV / límite |
| RN 89 · Chaco · Avia Terai - Gral. Pinedo | 87.0 | 87.4 | intersección DNV / localidad |
| RN 89 · Chaco · Gral. Pinedo -Lte. Sgo. Del Estero | 48.0 | 48.8 | localidad / límite |
| RN 95 · Chaco · Emp. RN 16 - Emp. RP 9 | 67.0 | 54.8 | intersección DNV / intersección DNV |
| RN 95 · Chaco · Emp. RP 3 - Lte. Con Formosa | 10.0 | 9.5 | intersección DNV / límite |
| RN 95 · Chaco · Emp. RP 9 - Emp. RP 3 | 116.0 | 111.7 | intersección DNV / intersección DNV |
| RN 95 · Chaco · Lte. Con Sta. Fe - Emp. RN 16 | 158.0 | 164.4 | límite / intersección DNV |
| RN 1S40 · Chubut · Lte. con Rio Negro - El Maiten | 7.0 | 6.2 | límite / localidad |
| RN 25 · Chubut · Las Plumas - Los Altares | 103.0 | 102.2 | localidad / localidad |
| RN 25 · Chubut · Los Altares - Paso de Indios | 57.0 | 56.3 | localidad / localidad |
| RN 25 · Chubut · Paso de Indios - Tecka | 164.0 | 161.2 | localidad / intersección DNV |
| RN 25 · Chubut · Rawson - Las Plumas | 205.0 | 207.0 | localidad / localidad |
| RN 259 · Chubut · Emp. RN 40 - Esquel | 13.6 | 11.6 | intersección DNV / localidad |
| RN 259 · Chubut · Esquel - Trevelin | 21.63 | 23.7 | localidad / localidad |
| RN 259 · Chubut · Trevelin - Lte. Con Chile | 39.95 | 39.3 | localidad / frontera |
| RN 26 · Chubut · C. Rivadavia - Sarmiento | 138.0 | 137.4 | intersección DNV / localidad |
| RN 26 · Chubut · Sarmiento - Emp. RN 40 | 72.7 | 71.3 | localidad / intersección DNV |
| RN 260 · Chubut · Emp. RN 40 - Lte. Con Chile | 105.41 | 106.0 | cruce de rutas / frontera |
| RN 3 · Chubut · Garayalde - C.Rivadavia | 178.0 | 176.6 | localidad / localidad |
| RN 3 · Chubut · Pto.Madryn - Trelew | 62.87 | 60.0 | localidad / intersección DNV |
| RN 3 · Chubut · Trelew - Garayalde | 198.0 | 195.6 | intersección DNV / localidad |
| RN 40 · Chubut · Emp. RN 259 - Acc. a Cholila | 105.0 | 104.4 | intersección DNV / intersección DNV |
| RN 40 · Chubut · Emp. RN 26 - Gob.Costa | 178.0 | 178.4 | intersección DNV / localidad |
| RN 40 · Chubut · Gob.Costa - Tecka | 83.7 | 83.2 | localidad / localidad |
| RN 40 · Chubut · Lte. Sta. Cruz - Rio Mayo | 37.3 | 38.3 | límite / localidad |
| RN 40 · Chubut · Rio Mayo - Emp. RN 26 | 53.4 | 52.5 | localidad / intersección DNV |
| RN 40 · Chubut · Tecka - Emp. RN 259 | 84.4 | 83.8 | localidad / intersección DNV |
| RN 118 · Corrientes · Saladas - Santa Rosa | 68.0 | 55.1 | intersección DNV / localidad |
| RN 118 · Corrientes · Santa Rosa - San Miguel | 59.0 | 63.3 | localidad / localidad |
| RN 119 · Corrientes · Emp. RN 14 y 127 - Km 70 | 70.0 | 69.8 | intersección DNV / km |
| RN 119 · Corrientes · Km. 70 - Mercedes | 39.0 | 39.5 | km / intersección DNV |
| RN 12 · Corrientes · Corrientes - Itatí | 60.0 | 64.5 | intersección DNV / intersección DNV |
| RN 12 · Corrientes · Esquina - Goya | 114.0 | 109.6 | localidad / localidad |
| RN 12 · Corrientes · Itatí - Ituzaingó | 167.0 | 166.3 | intersección DNV / localidad |
| RN 12 · Corrientes · Ituzaingo - Lte. Con Misiones | 69.0 | 69.2 | localidad / límite |
| RN 12 · Corrientes · Lte. Entre Ríos - Esquina | 37.12 | 37.5 | límite / localidad |
| RN 12 · Corrientes · Saladas - Corrientes | 90.0 | 83.9 | intersección DNV / intersección DNV |
| RN 123 · Corrientes · Desmochado - Emp. RN 12 | 31.0 | 28.2 | localidad / cruce de rutas |
| RN 123 · Corrientes · Emp. RN 12 - Mercedes | 73.0 | 77.8 | cruce de rutas / localidad |
| RN 123 · Corrientes · Mercedes - Emp. RN 14 | 110.0 | 104.5 | localidad / intersección DNV |
| RN 127 · Corrientes · Lte. Con Entre Ríos - Emp. RN 14 y 119 | 32.0 | 30.5 | límite / intersección DNV |
| RN 14 · Corrientes · Bompland - Paso de los Libres | 28.0 | 24.8 | localidad / intersección DNV |
| RN 14 · Corrientes · Cuatro Bocas - Bompland | 63.0 | 65.6 | localidad / localidad |
| RN 14 · Corrientes · Gdor. Virasoro - Lte. Con Misiones | 37.0 | 37.0 | localidad / límite |
| RN 14 · Corrientes · Lte. Entre Ríos - Cuatro Bocas | 62.0 | 62.6 | límite / localidad |
| RN 14 · Corrientes · Paso de los Libres - Yapeyú | 55.0 | 54.7 | intersección DNV / intersección DNV |
| RN 14 · Corrientes · Santo Tomé - Gdor. Virasoro | 63.0 | 62.0 | localidad / localidad |
| RN 14 · Corrientes · Yapeyú - Santo Tomé | 132.0 | 131.0 | intersección DNV / localidad |
| RN 158 · Córdoba · General Deheza - Rio Cuarto | 66.0 | 63.0 | localidad / intersección DNV |
| RN 158 · Córdoba · Int. RN 19 (San Francisco) - Int. RP 13 (Las Varillas) | 76.0 | 76.0 | intersección DNV / intersección DNV |
| RN 158 · Córdoba · Int. RP 13 - Villa Maria | 78.0 | 80.2 | intersección DNV / intersección DNV |
| RN 158 · Córdoba · Villa Maria - General Deheza | 66.0 | 66.4 | intersección DNV / localidad |
| RN 19 · Córdoba · Arroyito - Tránsito | 16.0 | 13.7 | localidad / localidad |
| RN 19 · Córdoba · Río Primero - Córdoba | 52.0 | 59.3 | localidad / intersección DNV |
| RN 19 · Córdoba · Tránsito - Río Primero | 43.0 | 42.9 | localidad / localidad |
| RN 20 · Córdoba · Córdoba - Emp RN 38 | 27.0 | 23.8 | intersección DNV / intersección DNV |
| RN 20 · Córdoba · Villa Dolores - Lte. C/San Luis | 17.0 | 17.1 | intersección DNV / límite |
| RN 20 · Córdoba · Villa Dolores - Lte. Con San Luis | 17.0 | 17.1 | intersección DNV / límite |
| RN 35 · Córdoba · Acc. a Sampacho (int. RP 24) - Int. RN 8 (Santa Catalina) | 41.0 | 42.9 | intersección DNV / intersección DNV |
| RN 35 · Córdoba · Acc. a Vicuña Mackena - Acc. a Sampacho (int. RP 24) | 40.0 | 37.6 | localidad / intersección DNV |
| RN 35 · Córdoba · Acc. a del Campillo (int. RP 27) - Acc. a Vicuña Mackena | 55.0 | 55.1 | intersección DNV / localidad |
| RN 35 · Córdoba · Lte. Con La Pampa -Acc. a del Campillo (int. RP 27) | 66.0 | 68.6 | límite / intersección DNV |
| RN 36 · Córdoba · Río Cuarto - Córdoba | 216.0 | 208.1 | localidad / localidad |
| RN 38 · Córdoba · Acc. a la Cumbre - Cruz del Eje - Lte. C/ La Rioja | 89.0 | 88.3 | localidad / límite |
| RN 38 · Córdoba · Bialet Masse (Int.RP E55) - Int.RP E66 | 37.0 | 40.2 | intersección DNV / intersección DNV |
| RN 38 · Córdoba · Int.RN 20 - Bialet Masse (Int.RP E55) | 27.0 | 26.6 | cruce de rutas / intersección DNV |
| RN 38 · Córdoba · Int.RP E66 - Acc. a la Cumbre - Cruz del Eje | 58.0 | 54.2 | intersección DNV / localidad |
| RN 60 · Córdoba · Int RP 16 / Acc. a Dean Funes - Quilino | 27.0 | 27.9 | intersección DNV / intersección DNV |
| RN 60 · Córdoba · Int. RN 9 - Int RP 16 / Acc. a Dean Funes | 49.0 | 48.9 | intersección DNV / intersección DNV |
| RN 60 · Córdoba · Quilino - Lte. C/Catamarca | 78.0 | 80.5 | intersección DNV / límite |
| RN 7 · Córdoba · Lte. C/Santa Fe - Lte. C/San Luis | 221.0 | 220.1 | límite / límite |
| RN 8 · Córdoba · Acc. a La Carlota - Int. RN 36 | 95.0 | 95.4 | intersección DNV / intersección DNV |
| RN 8 · Córdoba · Int. RN 36 - Int. RP 24 (Acc, a Sampacho) | 55.0 | 54.2 | intersección DNV / intersección DNV |
| RN 8 · Córdoba · Int. RP 24 (Acc.a Sampacho) - Lte. con San Luis | 44.0 | 43.7 | intersección DNV / límite |
| RN 8 · Córdoba · Lte. C/Santa Fe -Acc. a La Carlota | 98.0 | 97.6 | límite / intersección DNV |
| RN 9 · Córdoba · Lte. C/Santa Fe - Pilar | 246.0 | 245.4 | límite / intersección DNV |
| RN A005 · Córdoba · Emp RN 8 -Emp RN 36 | 11.0 | 11.3 | intersección DNV / intersección DNV |
| RN 12 · Entre Ríos · Ceibas - Gualeguay | 70.0 | 71.1 | intersección DNV / intersección DNV |
| RN 12 · Entre Ríos · Complejo Zarate Brazo Largo - Ceibas | 48.0 | 41.7 | localidad / intersección DNV |
| RN 12 · Entre Ríos · Emp. RN 131 - Paraná | 43.6 | 42.5 | intersección DNV / intersección DNV |
| RN 12 · Entre Ríos · Emp. RP 39 - Nogoyá | 47.0 | 46.4 | intersección DNV / localidad |
| RN 12 · Entre Ríos · Emp.RN 127 - Hernandarias | 33.8 | 33.8 | intersección DNV / intersección DNV |
| RN 12 · Entre Ríos · Galarza - Emp. RP 39 | 43.0 | 43.1 | localidad / intersección DNV |
| RN 12 · Entre Ríos · Gualeguay - Galarza | 46.0 | 46.1 | intersección DNV / localidad |
| RN 12 · Entre Ríos · Nogoyá - Emp. RN 131 | 64.0 | 64.3 | localidad / intersección DNV |
| RN 12 · Entre Ríos · Paraná - Cerrito | 44.36 | 36.6 | intersección DNV / localidad |
| RN 127 · Entre Ríos · Emp. RN 12 - Emp. RP 6 | 77.0 | 75.5 | intersección DNV / intersección DNV |
| RN 127 · Entre Ríos · Emp. RP 6 - Federal | 58.6 | 59.8 | intersección DNV / localidad |
| RN 127 · Entre Ríos · Federal - Miñones | 34.0 | 34.6 | localidad / localidad |
| RN 127 · Entre Ríos · La Hierra - Lte. Corrientes | 26.3 | 27.1 | localidad / límite |
| RN 127 · Entre Ríos · Miñones - La Hierra | 33.8 | 32.6 | localidad / localidad |
| RN 130 · Entre Ríos · Emp. RN 14 - Villaguay | 82.0 | 81.7 | intersección DNV / intersección DNV |
| RN 14 · Entre Ríos · Ceibas - Lte. Corrientes | 343.0 | 343.1 | intersección DNV / límite |
| RN 18 · Entre Ríos · Paraná - Villaguay | 135.0 | 135.0 | intersección DNV / intersección DNV |
| RN A015 · Entre Ríos · Emp. RN 14 - Acc. a Salto Grande | 14.67 | 13.3 | intersección DNV / localidad |
| RN 81 · Formosa · Formosa - Las Lomitas | 285.0 | 286.9 | intersección DNV / localidad |
| RN 81 · Formosa · Laguna Yema - Los Chiriguanos | 29.0 | 28.8 | localidad / intersección DNV |
| RN 81 · Formosa · Los Chiriguanos - Ing. Juarez | 46.0 | 44.3 | intersección DNV / localidad |
| RN 86 · Formosa · C. Zalazar - El Remanso | 34.79 | 35.0 | localidad / intersección DNV |
| RN 86 · Formosa · Clorinda - El Cogoik | 169.0 | 167.7 | intersección DNV / intersección DNV |
| RN 86 · Formosa · El Cogoik - Villa Gral. Güemes | 30.0 | 28.6 | intersección DNV / localidad |
| RN 86 · Formosa · El Remanso -Guadalcazar | 86.27 | 85.3 | intersección DNV / intersección DNV |
| RN 86 · Formosa · Fortin Leyes - San Martin 2 | 31.27 | 31.6 | localidad / localidad |
| RN 86 · Formosa · San Martin 2 - C. Zalazar | 63.23 | 63.7 | localidad / localidad |
| RN 86 · Formosa · Villa Gral. Güemes - Fortin Leyes | 28.0 | 28.5 | localidad / localidad |
| RN 95 · Formosa · Emp. RN 81 - Villa. Gral Güemes | 63.6 | 63.2 | intersección DNV / intersección DNV |
| RN 34 · Jujuy · Acc. a San Pedro -Lte. Con Salta | 91.0 | 93.8 | localidad / límite |
| RN 34 · Jujuy · Lte. Con Salta - Acc. Norte a San Pedro | 37.0 | 44.1 | límite / localidad |
| RN 40 · Jujuy · Lte. Con Salta - Emp. RN 9 | 408.0 | 399.6 | límite / intersección DNV |
| RN 52 · Jujuy · Emp. RN 9- Purmamarca | 3.5 | 3.2 | intersección DNV / localidad |
| RN 52 · Jujuy · Purmamarca - Emp. RP 79 | 59.0 | 57.5 | localidad / intersección DNV |
| RN 9 · Jujuy · Abra Pampa - Lte. C/Bolivia | 71.0 | 74.4 | localidad / frontera |
| RN 9 · Jujuy · Acc. a Iturbe - Abra Pampa | 60.0 | 58.8 | intersección DNV / localidad |
| RN 9 · Jujuy · Lte. Salta - Acc. a Dique La Ciénaga | 13.6 | 12.8 | límite / localidad |
| RN 9 · Jujuy · S.S. de Jujuy -Yala | 14.0 | 14.1 | localidad / localidad |
| RN 9 · Jujuy · Volcán - Emp. RN 52 | 20.0 | 20.1 | localidad / intersección DNV |
| RN 9 · Jujuy · Yala - Volcán | 31.0 | 26.1 | localidad / localidad |
| RN IV66 · Jujuy · Emp. RN 66 - Emp.RN 34 | 11.0 | 12.7 | intersección DNV / intersección DNV |
| RN 143 · La Pampa · Emp. RN 152 - Emp. RP 20 | 56.06 | 55.8 | intersección DNV / intersección DNV |
| RN 143 · La Pampa · Emp. RP 20 - Limay Mahuida | 92.48 | 92.3 | intersección DNV / localidad |
| RN 143 · La Pampa · Santa Isabel - Lte. Mendoza | 34.14 | 33.3 | localidad / límite |
| RN 151 · La Pampa · Algarrobo del Aguila - Emp. RN 143 | 6.23 | 5.9 | localidad / intersección DNV |
| RN 151 · La Pampa · Lte. Río Negro - Puelen | 45.7 | 45.2 | límite / localidad |
| RN 152 · La Pampa · El Carancho (Emp.RN 143) - Lihuel Calel | 77.17 | 78.4 | intersección DNV / localidad |
| RN 152 · La Pampa · Emp. RN 232 - Casa De Piedra | 93.28 | 93.2 | intersección DNV / localidad |
| RN 152 · La Pampa · Emp. RN 35 - Gral. Acha | 29.42 | 29.2 | intersección DNV / localidad |
| RN 152 · La Pampa · Gral. Acha - El Carancho (Emp. RN 143) | 42.3 | 42.5 | localidad / intersección DNV |
| RN 152 · La Pampa · Lihuel Calel - Puelches | 34.41 | 33.7 | localidad / localidad |
| RN 152 · La Pampa · Puelches - Emp. RN 232 | 16.04 | 15.4 | localidad / intersección DNV |
| RN 154 · La Pampa · Emp. RP 30 - La Adela Emp. RN 22 | 70.26 | 70.2 | intersección DNV / intersección DNV |
| RN 188 · La Pampa · Emp. R.P.7 - Realico Emp. RN.35 | 30.15 | 30.0 | intersección DNV / intersección DNV |
| RN 188 · La Pampa · Rancul - Lte. San Luis | 38.11 | 39.6 | localidad / límite |
| RN 188 · La Pampa · Realico Emp. R.N.35 - Rancul | 38.46 | 38.3 | intersección DNV / localidad |
| RN 1V143 · La Pampa · Emp. RP 10 - Emp. RN 143 | 12.1 | 12.1 | intersección DNV / intersección DNV |
| RN 232 · La Pampa · Emp. RN 152 - Emp. RP 30 | 36.19 | 36.5 | intersección DNV / intersección DNV |
| RN 232 · La Pampa · Emp. RP 30 - Lte. Rio Negro | 39.04 | 39.4 | intersección DNV / límite |
| RN 35 · La Pampa · Ataliva Roca - Emp. RN 5 | 48.88 | 46.2 | localidad / intersección DNV |
| RN 35 · La Pampa · Bernasconi - Peru | 42.57 | 44.0 | localidad / localidad |
| RN 35 · La Pampa · E. Castex (emp. RP 102) - Emp. RP 4 | 25.28 | 25.3 | intersección DNV / intersección DNV |
| RN 35 · La Pampa · Emp. RN 152- Ataliva Roca | 31.04 | 31.9 | intersección DNV / localidad |
| RN 35 · La Pampa · Emp. RN 5 - Winifreda | 41.68 | 44.6 | intersección DNV / intersección DNV |
| RN 35 · La Pampa · Emp. RP 2 - Lte. Córdoba | 34.15 | 34.3 | intersección DNV / límite |
| RN 35 · La Pampa · Emp. RP 4 - Emp. RP 2 | 39.76 | 40.0 | intersección DNV / intersección DNV |
| RN 35 · La Pampa · Peru - Emp. RN 152 | 44.38 | 43.3 | localidad / intersección DNV |
| RN 35 · La Pampa · Winifreda - E. Castex (emp. RP 102) | 35.47 | 35.6 | intersección DNV / intersección DNV |
| RN 5 · La Pampa · Emp. R.P. 3 - Santa Rosa | 41.33 | 41.4 | intersección DNV / intersección DNV |
| RN 141 · La Rioja · Emp. RN 79 - Lte. Con San Juan | 80.0 | 80.0 | intersección DNV / límite |
| RN 150 · La Rioja · Emp. RN 38 - Lte. Con San Juan | 86.0 | 87.6 | intersección DNV / límite |
| RN 38 · La Rioja · Chamical - Patquia | 67.0 | 66.1 | intersección DNV / localidad |
| RN 38 · La Rioja · Emp. RN 75 - Emp. RP 5 | 5.0 | 5.1 | intersección DNV / intersección DNV |
| RN 38 · La Rioja · La Rioja - Lte. Con Catamarca | 84.0 | 83.7 | intersección DNV / límite |
| RN 38 · La Rioja · Lte. Con Córdoba - Chamical | 77.0 | 77.6 | límite / intersección DNV |
| RN 38 · La Rioja · Patquia - La Rioja | 67.0 | 68.8 | localidad / intersección DNV |
| RN 40 · La Rioja · Lte. Con San Juan - Villa Unión | 53.0 | 51.0 | límite / intersección DNV |
| RN 40 · La Rioja · Nonogasta - Lte. Con Catamarca | 163.0 | 147.4 | localidad / límite |
| RN 40 · La Rioja · Villa Unión - Los Tambillos | 49.0 | 48.3 | intersección DNV / localidad |
| RN 60 · La Rioja · Aimogasta - Lte. Con Catamarca | 45.0 | 44.6 | localidad / límite |
| RN 60 · La Rioja · Villa Mazan - Aimogasta | 31.0 | 31.7 | localidad / localidad |
| RN 73 · La Rioja · Emp. RN 75 -Pampa de la Viuda | 18.0 | 17.9 | intersección DNV / localidad |
| RN 74 · La Rioja · Los Colorados - Nonogasta | 80.0 | 79.7 | localidad / intersección DNV |
| RN 74 · La Rioja · Patquia - Los Colorados | 33.0 | 32.9 | intersección DNV / localidad |
| RN 75 · La Rioja · Aminga - Aimogasta | 35.0 | 34.7 | localidad / intersección DNV |
| RN 75 · La Rioja · Huaco - Aminga | 41.0 | 40.8 | localidad / localidad |
| RN 75 · La Rioja · Sanagasta - Huaco | 15.0 | 15.7 | localidad / localidad |
| RN 76 · La Rioja · Acc. a Talampaya - Pagancillo | 29.0 | 28.7 | localidad / localidad |
| RN 76 · La Rioja · Barrancas Blanca - Lte. Con Chile | 25.81 | 24.0 | localidad / frontera |
| RN 76 · La Rioja · Emp. RN 150 - Acc. a Talampaya | 58.0 | 58.5 | intersección DNV / localidad |
| RN 76 · La Rioja · Pegancillo - Villa Unión | 25.0 | 29.1 | localidad / localidad |
| RN 76 · La Rioja · Villa Unión - Vinchina | 68.0 | 68.9 | localidad / localidad |
| RN 76 · La Rioja · Vinchina - Alto Jagüe | 30.0 | 33.5 | localidad / localidad |
| RN 77 · La Rioja · Lte. Con Córdoba - Emp. RN 79 | 77.0 | 76.5 | límite / intersección DNV |
| RN 78 · La Rioja · Emp. RN 40 - Famatina | 9.0 | 11.2 | intersección DNV / localidad |
| RN 78 · La Rioja · Famatina - Campanas | 49.0 | 46.4 | localidad / localidad |
| RN 79 · La Rioja · Emp. RN 141 - S. Rita de Catuna | 45.0 | 44.9 | intersección DNV / localidad |
| RN 79 · La Rioja · Lte. Con San Luis - Emp. RN 141 | 85.0 | 84.2 | límite / intersección DNV |
| RN 79 · La Rioja · S. Rita de Catuna - Emp. RN N° 38 | 72.0 | 72.1 | localidad / intersección DNV |
| RN 143 · Mendoza · Carmensa - San Rafael | 114.0 | 109.2 | intersección DNV / localidad |
| RN 143 · Mendoza · Lte. Con La Pampa - Carmensa | 106.0 | 106.6 | límite / intersección DNV |
| RN 143 · Mendoza · San Rafael - Pareditas | 104.0 | 108.1 | localidad / intersección DNV |
| RN 144 · Mendoza · Las Salinas - El Sosneado | 56.0 | 60.9 | localidad / intersección DNV |
| RN 144 · Mendoza · San Rafael - Las Salinas | 70.0 | 59.1 | intersección DNV / localidad |
| RN 145 · Mendoza · Bardas Blancas - Las Loicas | 35.0 | 34.4 | localidad / localidad |
| RN 145 · Mendoza · Las Loicas - Cajón Grande | 30.0 | 26.8 | localidad / localidad |
| RN 146 · Mendoza · Lte. con San Luis - Monte Coman | 124.0 | 121.3 | límite / localidad |
| RN 146 · Mendoza · San Rafael - Monte Coman | 57.51 | 54.6 | intersección DNV / localidad |
| RN 149 · Mendoza · Uspallata - Lte. Con San Juan | 60.0 | 60.6 | intersección DNV / límite |
| RN 153 · Mendoza · Lte. Con San Juan - Int. RN 149 | 54.5 | 51.2 | límite / intersección DNV |
| RN 188 · Mendoza · General Alvear - Malargue | 230.0 | 224.6 | localidad / intersección DNV |
| RN 188 · Mendoza · Lte. Con San Luis - Gral. Alvear | 111.0 | 111.5 | límite / localidad |
| RN 40 · Mendoza · Bardas Blancas - Malargüe | 62.7 | 66.1 | localidad / localidad |
| RN 40 · Mendoza · Emp. RP 221 - La Pasarela | 49.4 | 48.4 | intersección DNV / localidad |
| RN 40 · Mendoza · La Pasarela - Bardas Blancas | 56.7 | 56.3 | localidad / localidad |
| RN 40 · Mendoza · Lte. Con Neuquen - Emp. RP 221 | 35.7 | 35.1 | límite / intersección DNV |
| RN 40 · Mendoza · Malargüe - Emp. RN 144 | 58.3 | 60.0 | localidad / intersección DNV |
| RN 40 · Mendoza · Pareditas - Tunuyan | 37.8 | 41.2 | localidad / localidad |
| RN 40 · Mendoza · Tunuyan - Mendoza | 87.0 | 80.8 | localidad / localidad |
| RN 7 · Mendoza · Empalme RN 40 - Potrerillos | 46.0 | 40.5 | intersección DNV / intersección DNV |
| RN 7 · Mendoza · Potrerillos - Uspallata | 50.0 | 52.1 | intersección DNV / localidad |
| RN 7 · Mendoza · Puente Del Inca - Las Cuevas | 13.8 | 14.0 | localidad / localidad |
| RN 7 · Mendoza · Tunel Internacional | 4.45 | 4.0 | localidad / fin de ruta |
| RN 7 · Mendoza · Uspallata - Polvaredas | 40.0 | 40.5 | localidad / localidad |
| RN 101 · Misiones · Piñalito Norte - Emp. RP 19 | 29.7 | 29.4 | localidad / intersección DNV |
| RN 101 · Misiones · San Antonio - Piñalito Norte | 27.0 | 27.3 | localidad / localidad |
| RN 105 · Misiones · Posadas - San José | 35.0 | 34.4 | localidad / intersección DNV |
| RN 12 · Misiones · Eldorado - Emp. RN 101 | 86.35 | 86.7 | intersección DNV / intersección DNV |
| RN 12 · Misiones · Emp. RN 105 - Santa Ana | 33.0 | 33.1 | cruce de rutas / localidad |
| RN 12 · Misiones · Santa Ana - Eldorado | 161.0 | 159.4 | localidad / intersección DNV |
| RN 14 · Misiones · Campo Grande - San Vicente | 61.0 | 61.9 | intersección DNV / localidad |
| RN 14 · Misiones · Emp. RP 17 - Bernardo De Irigoyen | 11.0 | 10.8 | intersección DNV / localidad |
| RN 14 · Misiones · Gramado - Piñalito | 35.0 | 32.3 | intersección DNV / localidad |
| RN 14 · Misiones · Lte. Con Corrientes - San José | 7.3 | 4.8 | límite / localidad |
| RN 14 · Misiones · Oberá - Campo Grande | 40.0 | 38.9 | intersección DNV / intersección DNV |
| RN 14 · Misiones · Piñalito - Emp. RP 17 | 21.5 | 23.9 | localidad / intersección DNV |
| RN 14 · Misiones · San José - Oberá | 77.0 | 80.1 | localidad / intersección DNV |
| RN 14 · Misiones · San Vicente - Gramado | 74.6 | 73.0 | localidad / intersección DNV |
| RN 22 · Neuquén · Arroyito - Zapala | 136.4 | 135.5 | localidad / intersección DNV |
| RN 234 · Neuquén · Rinconada - Emp. RN 237 | 57.44 | 57.5 | localidad / cruce de rutas |
| RN 237 · Neuquén · Arroyito - Piedra del Aguila | 174.43 | 174.7 | intersección DNV / localidad |
| RN 40 · Neuquén · Catan Lil - Zapala | 120.32 | 131.6 | localidad / localidad |
| RN 40 · Neuquén · Chos Malal - Lte. con Mendoza | 116.21 | 125.0 | localidad / límite |
| RN 40 · Neuquén · Emp. RN 231 - Lago Villarino | 43.77 | 47.4 | intersección DNV / localidad |
| RN 40 · Neuquén · Lago Villarino- San Martín de los Andes | 43.16 | 48.2 | localidad / localidad |
| RN 40 · Neuquén · Las Lajas - Chos Malal | 142.27 | 156.4 | localidad / localidad |
| RN 40 · Neuquén · Lte. con Río Negro - Emp. RN 231 | 68.46 | 74.5 | límite / intersección DNV |
| RN 40 · Neuquén · Rinconada - Catan Lil | 35.45 | 39.6 | intersección DNV / localidad |
| RN 40 · Neuquén · San Martín de los Andes - Rinconada | 66.01 | 70.8 | localidad / intersección DNV |
| RN 40 · Neuquén · Zapala - Las Lajas | 49.01 | 56.1 | localidad / localidad |
| RN 151 · Río Negro · Cipolletti - Lte Con La Pampa | 147.0 | 150.3 | intersección DNV / límite |
| RN 1S40 · Río Negro · Emp. RN 23 - Límite con Chubut | 149.0 | 147.6 | intersección DNV / límite |
| RN 22 · Río Negro · Chimpay - Allen | 146.0 | 155.2 | localidad / localidad |
| RN 22 · Río Negro · Río Colorado - Chimpay | 193.0 | 186.6 | localidad / localidad |
| RN 23 · Río Negro · Emp. RN 3 - Valcheta | 78.0 | 77.2 | intersección DNV / localidad |
| RN 23 · Río Negro · Los Menucos - Maquinchao | 71.0 | 71.4 | intersección DNV / intersección DNV |
| RN 23 · Río Negro · Maquinchao - Ingeniero Jacobacci | 69.0 | 73.4 | intersección DNV / localidad |
| RN 23 · Río Negro · Pilcaniyeu - Emp. RN 40 | 64.0 | 61.7 | localidad / intersección DNV |
| RN 232 · Río Negro · Lte. Con La Pampa - Emp. RN 22 | 40.0 | 40.3 | límite / cruce de rutas |
| RN 250 · Río Negro · Emp. RN 3 - Gral. Conesa | 112.0 | 110.5 | intersección DNV / localidad |
| RN 250 · Río Negro · Gral. Conesa - Pomona | 145.0 | 147.0 | localidad / localidad |
| RN 250 · Río Negro · Pomona - Emp. RN 22 | 28.0 | 28.4 | localidad / intersección DNV |
| RN 251 · Río Negro · Emp.RN 22 - Gral.Conesa | 119.0 | 117.0 | intersección DNV / localidad |
| RN 251 · Río Negro · Gral. Conesa - S.A.Oeste | 84.0 | 82.6 | localidad / localidad |
| RN 3 · Río Negro · San Antonio Oeste - Sierra Grande | 125.0 | 134.2 | localidad / localidad |
| RN 3 · Río Negro · Sierra Grande - Lte. Con Chubut | 40.0 | 40.2 | localidad / límite |
| RN 3 · Río Negro · Viedma - San Antonio Oeste | 185.0 | 167.8 | localidad / localidad |
| RN 40 · Río Negro · El Bolsón - Villa Mascardi | 90.0 | 86.2 | localidad / localidad |
| RN 40 · Río Negro · Villa Mascardi - S.C. De Bariloche | 28.8 | 33.2 | localidad / localidad |
| RN 16 · Salta · El Quebrachal - Emp. RN 9/34 | 129.0 | 128.8 | localidad / intersección DNV |
| RN 16 · Salta · Lte. Con Chaco - El Quebrachal | 71.5 | 75.4 | límite / localidad |
| RN 34 · Salta · Embarcación - Gral. E. Mosconi | 79.5 | 78.6 | localidad / localidad |
| RN 34 · Salta · Gral. E. Mosconi - Tartagal | 10.0 | 9.5 | localidad / intersección DNV |
| RN 34 · Salta · Lte. Con Jujuy - Pichanal | 40.0 | 39.7 | límite / localidad |
| RN 34 · Salta · Pichanal - Embarcación | 19.9 | 19.1 | localidad / localidad |
| RN 34 · Salta · Tartagal - Lte. Con Bolivia | 57.0 | 54.0 | intersección DNV / frontera |
| RN 40 · Salta · Cachi - La Poma | 52.12 | 53.7 | localidad / localidad |
| RN 40 · Salta · San Antonio De Los Cobres - Lte. Con Jujuy | 27.76 | 24.0 | localidad / límite |
| RN 40 · Salta · Seclantas - Cachi | 29.0 | 28.2 | localidad / localidad |
| RN 50 · Salta · Acc. a Oran - Lte. Con Bolivia | 46.0 | 48.3 | localidad / frontera |
| RN 50 · Salta · Emp. RN 34 - Acc. a Oran | 28.0 | 23.7 | intersección DNV / localidad |
| RN 51 · Salta · Campo Quijano - San Antonio De Los Cobres | 134.0 | 132.0 | localidad / localidad |
| RN 51 · Salta · San Antonio De Los Cobres - Paso De Sico | 143.0 | 133.3 | localidad / localidad |
| RN 68 · Salta · Emp. RN 40 - Talapampa | 94.5 | 91.5 | intersección DNV / localidad |
| RN 81 · Salta · Lte. Con Formosa - Emp. RN 34 | 182.0 | 182.1 | límite / intersección DNV |
| RN 86 · Salta · Tonono - Tartagal | 33.8 | 32.4 | localidad / intersección DNV |
| RN 9 · Salta · Vaqueros - Lte. Con Jujuy | 37.5 | 36.4 | localidad / límite |
| RN 141 · San Juan · Lte.Con La Rioja - Bermejo | 58.0 | 59.8 | límite / localidad |
| RN 149 · San Juan · Calingasta - Pachaco | 42.0 | 41.1 | intersección DNV / intersección DNV |
| RN 149 · San Juan · Emp. RP 436 - Las Flores | 102.0 | 98.0 | intersección DNV / intersección DNV |
| RN 149 · San Juan · Lte. Con Mendoza - Calingasta | 91.0 | 90.4 | límite / intersección DNV |
| RN 149 · San Juan · Pachaco - Emp. RP 436 | 50.0 | 49.8 | intersección DNV / intersección DNV |
| RN 150 · San Juan · Arrequintin - Lte. Con Chile | 56.0 | 49.8 | localidad / frontera |
| RN 150 · San Juan · Emp. RN 40 - Jachal | 13.0 | 10.1 | intersección DNV / localidad |
| RN 150 · San Juan · Ischigualasto - Huaco | 85.0 | 83.3 | localidad / intersección DNV |
| RN 150 · San Juan · Las Flores - Arrequintin | 37.0 | 37.3 | intersección DNV / localidad |
| RN 150 · San Juan · Lte. Con La Rioja - Ischigualasto | 21.0 | 17.4 | límite / localidad |
| RN 153 · San Juan · Km 57,80 - Lte. Con Mendoza | 42.0 | 43.6 | km / límite |
| RN 20 · San Juan · Encon - Las Casuarinas | 60.0 | 59.3 | localidad / intersección DNV |
| RN 20 · San Juan · Las Casuarinas - Caucete | 26.0 | 26.8 | intersección DNV / localidad |
| RN 20 · San Juan · Lte. Con S.Luis - Encon | 56.0 | 55.7 | límite / localidad |
| RN 40 · San Juan · Huaco - Lte. Con La Rioja | 62.0 | 61.0 | intersección DNV / límite |
| RN 40 · San Juan · Jachal - Huaco | 40.0 | 38.9 | intersección DNV / intersección DNV |
| RN 40 · San Juan · Talacasto -Tucunuco | 57.0 | 56.3 | intersección DNV / localidad |
| RN 40 · San Juan · Tucunuco - Jachal | 34.0 | 33.9 | localidad / intersección DNV |
| RN 40 · San Juan · Va. Media Agua-Acc. Sur San Juan | 51.0 | 53.2 | intersección DNV / localidad |
| RN A014 · San Juan · Av. De Circunvalación | 15.0 | 15.9 | fin de ruta / fin de ruta |
| RN 146 · San Luis · Emp. RN 7 - Lte. Con Mendoza | 93.0 | 95.6 | intersección DNV / límite |
| RN 146 · San Luis · Lujan - Emp. RN 147 | 120.0 | 117.7 | intersección DNV / intersección DNV |
| RN 147 · San Luis · Emp.RN V146 - La Chañarienta | 118.0 | 118.0 | intersección DNV / intersección DNV |
| RN 188 · San Luis · Lte. Con La Pampa - Lte. Con Mendoza | 127.0 | 126.2 | límite / límite |
| RN 20 · San Luis · Lte. Con Cordoba - Lte. Con San Juan | 198.0 | 197.2 | límite / límite |
| RN 7 · San Luis · Lte. Con Córdoba - Lte. Con Mendoza | 211.0 | 211.7 | límite / límite |
| RN 79 · San Luis · Emp. RN 20 - Lte. Con La Rioja | 40.0 | 40.8 | intersección DNV / límite |
| RN 8 · San Luis · Lte. Cordoba - Villa Mercedes | 33.0 | 33.1 | límite / intersección DNV |
| RN V146 · San Luis · Emp. RN 147 - Emp. RN 7 | 9.87 | 9.8 | intersección DNV / intersección DNV |
| RN 281 · Santa Cruz · Puerto Deseado - EMP. RN Nº 3 | 125.0 | 125.7 | intersección DNV / intersección DNV |
| RN 288 · Santa Cruz · Emp. RN 3 - Estancia La Julia | 77.4 | 73.1 | intersección DNV / localidad |
| RN 288 · Santa Cruz · Estancia La Julia - Tres Lagos | 144.0 | 144.2 | localidad / localidad |
| RN 293 · Santa Cruz · Emp. RN 40 - Lte.Con Chile | 9.94 | 9.8 | intersección DNV / frontera |
| RN 3 · Santa Cruz · Caleta Olivia - Fitz Roy | 76.0 | 75.5 | localidad / localidad |
| RN 3 · Santa Cruz · El Salado - Puerto San Julián | 69.5 | 69.8 | localidad / localidad |
| RN 3 · Santa Cruz · Fitz Roy - Tres Cerros | 134.0 | 131.5 | localidad / localidad |
| RN 3 · Santa Cruz · Lte. Con Chubut - Caleta Olivia | 58.12 | 53.0 | límite / localidad |
| RN 3 · Santa Cruz · Puerto San Julian- Emp. RN 288 | 129.0 | 127.6 | localidad / intersección DNV |
| RN 3 · Santa Cruz · Río Gallegos- Monte Aymond *(dado de baja)* | 63.0 | 65.7 | localidad / localidad |
| RN 3 · Santa Cruz · Tres Cerros - El Salado | 66.5 | 68.8 | localidad / localidad |
| RN 3 · Santa Cruz · Tres Cerros - Puerto San Julian *(dado de baja)* | 136.0 | 138.6 | localidad / localidad |
| RN 40 · Santa Cruz · Bajo Caracoles - Perito Moreno *(dado de baja)* | 129.0 | 128.0 | localidad / localidad |
| RN 40 · Santa Cruz · Bella Vista- Puente Blanco | 78.0 | 78.7 | localidad / localidad |
| RN 40 · Santa Cruz · Casa Riera - Las Horquetas *(dado de baja)* | 45.0 | 48.3 | intersección DNV / localidad |
| RN 40 · Santa Cruz · Emp. RP 11 - Tres Lagos | 130.0 | 134.8 | intersección DNV / localidad |
| RN 40 · Santa Cruz · Emp. RP29 - Gobernador Gregores | 64.0 | 63.9 | intersección DNV / localidad |
| RN 40 · Santa Cruz · Emp. RPN°37 - Río Olnie | 75.0 | 69.6 | intersección DNV / localidad |
| RN 40 · Santa Cruz · Empalme RP43- Limite con Chubut *(dado de baja)* | 84.0 | 87.1 | intersección DNV / límite |
| RN 40 · Santa Cruz · Gobernador Gregores - Tamel Aike *(dado de baja)* | 103.0 | 103.4 | localidad / localidad |
| RN 40 · Santa Cruz · Guer Aike- Bella Vista | 85.0 | 80.3 | intersección DNV / localidad |
| RN 40 · Santa Cruz · La Esperanza - El Cerrito | 69.0 | 66.4 | intersección DNV / intersección DNV |
| RN 40 · Santa Cruz · Las Horquetas - Río Olnie *(dado de baja)* | 75.0 | 76.9 | localidad / localidad |
| RN 40 · Santa Cruz · Perito Moreno - Lte. Chubut *(dado de baja)* | 88.0 | 88.2 | localidad / límite |
| RN 40 · Santa Cruz · Perito Moreno- Límite con Chubut | 84.0 | 88.2 | localidad / límite |
| RN 40 · Santa Cruz · Tamel Aike - Bajo Caracoles *(dado de baja)* | 123.0 | 122.7 | localidad / localidad |
| RN 40 · Santa Cruz · Tres Lagos -Gdor. Gregores *(dado de baja)* | 173.0 | 171.9 | localidad / localidad |
| RN 40 · Santa Cruz · Tres Lagos- Gobernador Gregores *(dado de baja)* | 173.0 | 171.9 | localidad / localidad |
| RN 11 · Santa Fe · Arocena - Santa Fe | 52.0 | 50.7 | intersección DNV / intersección DNV |
| RN 11 · Santa Fe · Rosario - San Lorenzo | 17.26 | 14.3 | intersección DNV / localidad |
| RN 11 · Santa Fe · San Lorenzo - Arocena | 86.0 | 80.9 | localidad / intersección DNV |
| RN 11 · Santa Fe · Santa Fe - Lte. Con Chaco | 482.0 | 474.1 | intersección DNV / límite |
| RN 173 · Santa Fe · Emp. RN 11 - Puerto Aragon | 5.68 | 5.6 | intersección DNV / localidad |
| RN 175 · Santa Fe · Emp. RN 11 - Puerto San Martin | 3.0 | 2.4 | intersección DNV / localidad |
| RN 178 · Santa Fe · Acc. a Villa Eloisa - Las Rosas | 58.0 | 57.6 | intersección DNV / localidad |
| RN 178 · Santa Fe · Emp.RN 33 - Acc. a Villa Eloisa | 30.0 | 31.1 | intersección DNV / intersección DNV |
| RN 1v09 · Santa Fe · Roldan - Emp. RN 178 | 69.0 | 61.8 | localidad / intersección DNV |
| RN 1v09 · Santa Fe · Rosario - Roldan | 16.0 | 17.8 | intersección DNV / localidad |
| RN 33 · Santa Fe · Rufino - Zavalla | 235.0 | 231.8 | localidad / localidad |
| RN 33 · Santa Fe · Zavalla - Rosario | 19.0 | 19.9 | localidad / localidad |
| RN 34 · Santa Fe · Emp. RN A-012 - Emp. RN Nº 19 | 206.0 | 174.6 | intersección DNV / intersección DNV |
| RN 34 · Santa Fe · Emp. RN N° 19 - Lte. Con Sgo. Del Estero | 209.0 | 212.0 | intersección DNV / límite |
| RN 34 · Santa Fe · Rosario - Emp. RN A-012 | 16.0 | 14.1 | intersección DNV / intersección DNV |
| RN 9 · Santa Fe · Carcaraña - Lte. Con Cordoba | 63.5 | 61.0 | localidad / límite |
| RN 95 · Santa Fe · Ceres - Tostado | 81.28 | 79.9 | intersección DNV / localidad |
| RN 95 · Santa Fe · Tostado - Villa Minetti | 71.3 | 67.9 | localidad / intersección DNV |
| RN 98 · Santa Fe · Vera - Tostado | 155.0 | 173.3 | intersección DNV / localidad |
| RN A009 · Santa Fe · Puerto Reconquista - Emp. RN 11 | 12.0 | 11.5 | localidad / intersección DNV |
| RN A012 · Santa Fe · Alto Nivel RN 9(S) - Emp.RN 9 | 42.0 | 41.8 | intersección DNV / intersección DNV |
| RN A012 · Santa Fe · Emp. RN 9 (O) - San Lorenzo | 25.0 | 23.8 | intersección DNV / localidad |
| RN 157 · Santiago del Estero · Frías - Llavalle | 50.0 | 48.7 | intersección DNV / localidad |
| RN 157 · Santiago del Estero · Lavalle - Lte. Con Tucumán | 32.0 | 35.4 | localidad / límite |
| RN 16 · Santiago del Estero · El Caburé - Lte. Con Chaco | 96.0 | 96.8 | localidad / límite |
| RN 16 · Santiago del Estero · Lte. Con Chaco - El Caburé | 70.0 | 66.6 | límite / localidad |
| RN 34 · Santiago del Estero · La Banda - Pozo Hondo | 77.0 | 76.6 | intersección DNV / localidad |
| RN 34 · Santiago del Estero · Lte. Con Santa Fe - La Banda | 321.0 | 321.5 | límite / intersección DNV |
| RN 64 · Santiago del Estero · Puerta Chiquita - Lte. Con Catamarca | 25.0 | 26.1 | localidad / límite |
| RN 64 · Santiago del Estero · Santa Catalina - Puerta Chiquita | 9.8 | 7.7 | localidad / localidad |
| RN 64 · Santiago del Estero · Santiago Del Estero - Santa Catalina | 58.7 | 63.5 | localidad / localidad |
| RN 89 · Santiago del Estero · Lte. Con Chaco - Quimilí | 71.47 | 71.2 | límite / intersección DNV |
| RN 89 · Santiago del Estero · Quimilí - Suncho Corral | 112.0 | 107.4 | intersección DNV / localidad |
| RN 89 · Santiago del Estero · Suncho Corral - Emp RN 34 | 28.0 | 32.5 | localidad / intersección DNV |
| RN 9 · Santiago del Estero · Loreto - Santiago Del Estero | 60.0 | 59.9 | intersección DNV / localidad |
| RN 9 · Santiago del Estero · Lte. Con Córdoba - Río Saladillo | 97.0 | 95.2 | límite / localidad |
| RN 9 · Santiago del Estero · Río Saladillo - Loreto | 68.0 | 69.2 | localidad / intersección DNV |
| RN 9 · Santiago del Estero · Santiago Del Estero - Lte Con Tucuman | 85.0 | 85.4 | localidad / límite |
| RN 98 · Santiago del Estero · Bandera - Los Tableros | 13.0 | 12.8 | intersección DNV / localidad |
| RN 98 · Santiago del Estero · Los Tableros - Pinto | 47.0 | 45.9 | localidad / intersección DNV |
| RN 3 · Tierra del Fuego, Antártida e Islas del Atlántico Sur · Rancho Hambre - Ushuaia | 43.45 | 42.9 | intersección DNV / intersección DNV |
| RN 3 · Tierra del Fuego, Antártida e Islas del Atlántico Sur · San Sebastián - Río Grande | 79.44 | 79.3 | localidad / intersección DNV |
| RN 3 · Tierra del Fuego, Antártida e Islas del Atlántico Sur · Ushuaia - Bahía Lapataia | 18.0 | 17.7 | intersección DNV / localidad |
| RN Compl I · Tierra del Fuego, Antártida e Islas del Atlántico Sur · Emp. RN 3 - Limite Con Chile | 11.0 | 10.6 | intersección DNV / frontera |
| RN 157 · Tucumán · Bella Vista - S. M. de Tucumán (Av. Jujuy) | 18.62 | 18.4 | localidad / localidad |
| RN 157 · Tucumán · Lte. Sgo. Del Estero - Monteagudo | 47.71 | 43.9 | límite / intersección DNV |
| RN 157 · Tucumán · Monteagudo - Simoca | 30.26 | 30.1 | intersección DNV / localidad |
| RN 157 · Tucumán · Simoca - Bella Vista | 26.32 | 26.7 | localidad / localidad |
| RN 1V38 · Tucumán · Acc. a Aguilares - Acc. a Concepción | 6.0 | 7.1 | intersección DNV / intersección DNV |
| RN 1V38 · Tucumán · Acc. a Concepción - Acc. a Monteros | 24.0 | 23.6 | intersección DNV / localidad |
| RN 1V38 · Tucumán · Acc. a Monteros - Emp RN 38 | 19.0 | 20.3 | localidad / intersección DNV |
| RN 1V38 · Tucumán · Rio Marapa - Acc. a Aguilares | 21.0 | 19.0 | localidad / intersección DNV |
| RN 1V65 · Tucumán · Int. R.N.N°1V38 - Int. R.N.N°38 Concepción | 3.0 | 2.9 | cruce de rutas / cruce de rutas |
| RN 38 · Tucumán · Aguilares - Concepción | 9.47 | 9.5 | intersección DNV / intersección DNV |
| RN 38 · Tucumán · Concepción - Monteros | 24.62 | 23.4 | intersección DNV / localidad |
| RN 38 · Tucumán · Famaillá - S. M. de Tucumán | 31.0 | 30.6 | localidad / localidad |
| RN 38 · Tucumán · Monteros - Famaillá | 15.65 | 15.1 | localidad / localidad |
| RN 40 · Tucumán · Colalao del Valle - Lte. Con Salta | 8.0 | 9.4 | localidad / límite |
| RN 65 · Tucumán · Int. R.N.N°38 Concepción - Alpachiri | 18.33 | 17.2 | intersección DNV / localidad |
| RN 9 · Tucumán · Acc. a El Cadillal - Lte. Con Salta | 57.0 | 56.6 | localidad / límite |
| RN 9 · Tucumán · Lte. Con Sgo. Del Estero - San Andres | 61.35 | 61.2 | límite / localidad |
| RN 9 · Tucumán · San Andres - S. M. de Tucumán (san Cayetano) | 3.8 | 4.2 | localidad / localidad |
| RN A016 · Tucumán · Acc. a Alderetes- S. M. de Tucumán | 4.68 | 3.7 | localidad / localidad |
