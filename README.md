# El Precio Justo Valdemoro del Rey

Juego de "acierta el precio" con objetos antiguos, para jugar en la plaza del pueblo. Funciona completamente en el navegador, sin servidor ni backend — igual que el Bingo Musical VDR.

**Edición actual: Retro (pesetas)** — objetos y precios de los años 30 a 60, la época de nuestros abuelos. La versión anterior en euros (objetos de anticuario a precio de reventa actual) sigue disponible en `precio_justo_vdr_v2.json` por si se quiere volver a ella.

## Cómo jugar

1. **Configuración**: se elige cuántos equipos juegan (2 a 8) y el nombre de cada uno. Una vez pulsado "Comenzar Partida", esto queda bloqueado — no se puede cambiar a mitad de partida.
2. Sale el primer objeto: se ve su imagen y su nombre (nunca su precio), y una voz en off lee su descripción en voz alta.
3. **Los equipos dicen su precio por turnos, uno detrás de otro** (nunca todos a la vez):
   - En la **primera ronda** empieza el primer equipo de la lista de configuración.
   - En las **rondas siguientes** empieza el equipo que ganó la ronda anterior (el que se acercó más sin pasarse).
   - Si **nadie acertó** en una ronda, la siguiente la abre el equipo situado a la derecha del que la abrió.
   - El turno avanza siempre hacia la derecha, dando la vuelta al llegar al último equipo.
   - Un banner ("🎯 Turno de: …") indica en todo momento a quién le toca, con su casilla resaltada.
   - **No se puede repetir un precio que ya haya dicho otro equipo en la misma ronda** — si se intenta, aparece un aviso y hay que decir un precio distinto.
   - Cada equipo confirma su precio con el botón "Confirmar precio ✔" (o pulsando Enter) antes de pasar el turno al siguiente.
4. El botón **Resolver** solo se activa cuando **todos** los equipos han confirmado su precio.
5. Al pulsar Resolver:
   - Se revela el precio justo del objeto (en pesetas).
   - Se marca en verde el equipo que más se acercó **sin pasarse**.
   - Aparece un pop-up con el podio (hasta 3 equipos: 3, 2 y 1 puntos) con el precio que dijo cada uno.
   - Si todos los equipos se pasaron del precio, no se reparten puntos esa ronda.
6. El marcador global (arriba) se actualiza con los puntos acumulados de cada equipo.
7. Se pasa al siguiente objeto con "Siguiente objeto →".

## Cómo termina la partida

- **Automáticamente**, cuando se agotan los objetos del catálogo.
- **Manualmente**, pulsando "Terminar juego" en cualquier momento (pide confirmación).

En ambos casos aparece un pop-up con el equipo ganador (el de más puntos; si hay empate, se muestran todos los empatados) y la tabla final de puntuaciones.

## Instrucciones dentro del juego

Un botón flotante **"?"** en la esquina superior derecha, siempre visible, abre un pop-up con el resumen de las reglas — útil para repasar la mecánica de turnos con los presentadores antes de empezar.

## Persistencia

Todo se guarda en el `localStorage` del navegador: la configuración de equipos, el marcador, el objeto actual, de quién es el turno y los precios ya confirmados en la ronda en curso. Si se recarga la página a mitad de partida (por ejemplo, tras un corte de conexión), al volver a abrir el juego aparece un aviso para **continuar la partida en curso** o **descartarla y empezar una nueva**.

## Diseño

Pensado para verse bien proyectado en la plaza: fondo oscuro con acentos dorados/cobrizos (evocando una subasta de antigüedades), tipografía grande, y el precio revelado como una "etiqueta" bien visible. El equipo ganador de cada ronda se resalta en verde. Los botones **+ / −** para ajustar el precio usan un paso adaptado a la escala del objeto (1 peseta para objetos baratos, hasta 50 pesetas para los más caros), en vez de un paso fijo, para que ajustar el precio sea cómodo tanto en un cántaro de 3 pesetas como en una radio de 750.

## Voz en off

Se usa la Web Speech API del propio navegador (`SpeechSynthesis`), en español, a una velocidad reducida (0,85) para que se entienda bien en la plaza. Al mostrar cada objeto se intenta reproducir automáticamente; algunos navegadores bloquean el audio automático hasta la primera interacción del usuario, por lo que hay un botón **"🔊 Repetir descripción"** en la cabecera como respaldo. En Safari, si la voz deja de sonar, suele bastar con reiniciar el navegador (bug conocido del propio Safari con la cola de voces).

## Catálogo (`precio_justo_vdr_v3.json`)

Cada objeto incluye:

| Campo | Descripción |
|---|---|
| `id` | Identificador único del objeto |
| `name` | Nombre mostrado en pantalla |
| `description` | Texto que lee la voz en off |
| `image` | Ruta local de la imagen (carpeta `imagenes/`) |
| `price` | Precio justo del objeto, en pesetas |
| `estimated` | `true` si el precio es una estimación razonada (ver metodología abajo); no aparece si el precio está tomado directamente de una fuente documentada |
| `priceNote` | Breve justificación del precio, visible solo en el JSON (no se muestra en el juego) |

El JSON también incluye a nivel general `"currency": "pesetas"` y `"era": "1930-1969"`.

### Metodología de precios en pesetas

Poner precio en pesetas de la época a objetos antiguos es mucho más difícil que mirar su precio de reventa actual, porque la mayoría de aperos rurales nunca se vendieron con un precio de catálogo documentado — los hacía el carpintero, el herrero o el alfarero del pueblo por encargo. Por eso cada objeto sigue uno de estos dos criterios:

- **Dato real documentado**: para objetos manufacturados de marca (radio, teléfono, gramola, máquina Singer) se ha partido de referencias históricas contrastadas: una radio instalada en un pueblo en 1924 costó 300 pesetas; la cuota anual de abonado telefónico particular era de 30 pesetas en los años 50 (300 en 1886); el jornal de un peón antes de la Guerra Civil era de 9,20 pesetas al día, con el pan a 0,65 ptas/kg. Estos datos actúan como referencia para situar el precio de objetos similares en su década.
- **Estimación razonada** (`estimated: true`, la mayoría del catálogo): para los aperos y objetos artesanales, el precio se calcula a partir del trabajo que habría llevado fabricarlos — desde 3-6 pesetas para una pieza sencilla de un rato de carpintero, hasta cientos de pesetas para una gran construcción como un carro de bueyes (semanas de trabajo de carpintero y herrero, una de las mayores inversiones de una familia labradora de la época).

### Objetos actuales (36)

Un repaso variado de la vida rural de los años 30 a 60: cántaro de Cuenca, zoqueta de segador, cedazo de harina, trillo, radio Jicky, teléfono de sobremesa, carro de bueyes, ábaco de escuela, garlopa de carpintero, pala de horno, tenazas de brasero, tomavistas Capta-Movi, gaseosa La Revoltosa, máquina de coser Singer 15K, hoz, horca de madera, yugo de bueyes, bieldo, celemín, sulfatadora de cobre, rueca de hilar, almirez de bronce, plancha de carbón, candil de aceite, velón de aceite, romana de pesar, bota de vino, arado de madera, molino de café de pared, gramola "La Voz de su Amo", brasero de latón, criba de madera, farolillo de aceite, orza de barro, garrafa forrada de mimbre y balanza de platillos.

Dos objetos de la edición anterior se sustituyeron por versiones con época documentada: la máquina de coser Willcox & Gibbs (1890, fuera de rango) se cambió por una **Singer 15K de 1940**, y el gramófono sin fecha se cambió por una **gramola "La Voz de su Amo" de 1940**.

### Ejemplo de objeto

```json
{
  "id": "obj17",
  "name": "Yugo de Bueyes",
  "description": "Un yugo de madera de encina, tallado a mano hacia 1900, que se colocaba sobre el cuello de los bueyes para engancharlos al carro o al arado y que tirasen juntos.",
  "image": "imagenes/yugo_bueyes.jpg",
  "price": 35,
  "estimated": true,
  "priceNote": "Yugo de bueyes tallado a mano, trabajo esmerado de carpintero."
}
```

## Imágenes

Las fotografías de los objetos están en la carpeta `imagenes/`, con nombres descriptivos que coinciden con el campo `image` de cada objeto en el JSON.

### Añadir objetos nuevos en el futuro

Para ampliar el catálogo más adelante:
1. Buscar objetos en `todocoleccion.net` (permite el acceso automatizado, a diferencia de otras tiendas de antigüedades) — cada ficha da nombre, descripción, precio de reventa actual y una URL de imagen directa, y suele traer "Lotes similares" con más candidatos ya listos.
2. Generar un `download_map.json` con el nombre de archivo local y la URL de cada imagen nueva.
3. Ejecutar el script de descarga correspondiente (`descargar_imagenes.py` para añadir imágenes nuevas sin tocar las existentes, o `sustituir_imagenes.py` si el objetivo es reemplazar una imagen ya existente) en el propio ordenador — no es posible descargar los archivos de imagen directamente desde el asistente, solo leer su información.
4. Subir las imágenes descargadas a la carpeta `imagenes/` de Drive.

## Uso local

```bash
npx serve .
# o bien
python3 -m http.server
```

No hay dependencias externas: todo el código (HTML, CSS y JavaScript) está en un único archivo `index.html`, sin librerías de terceros.
