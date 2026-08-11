# El Precio Justo Valdemoro del Rey

Juego de "acierta el precio" con objetos antiguos, para jugar en la plaza del pueblo. Funciona completamente en el navegador, sin servidor ni backend — igual que el Bingo Musical VDR.

## Cómo jugar

1. **Configuración**: se elige cuántos equipos juegan (2 a 8) y el nombre de cada uno. Una vez pulsado "Comenzar Partida", esto queda bloqueado — no se puede cambiar a mitad de partida.
2. Sale el primer objeto: se ve su imagen y su nombre (nunca su precio), y una voz en off lee su descripción en voz alta.
3. Los presentadores van introduciendo el precio que dice cada equipo.
4. El botón **Resolver** solo se activa cuando los precios de *todos* los equipos están rellenos.
5. Al pulsar Resolver:
   - Se revela el precio justo del objeto.
   - Se marca en verde el equipo que más se acercó **sin pasarse**.
   - Aparece un pop-up con el podio (hasta 3 equipos: 3, 2 y 1 puntos) con el precio que dijo cada uno.
   - Si todos los equipos se pasaron del precio, no se reparten puntos esa ronda.
6. El marcador global (arriba) se actualiza con los puntos acumulados de cada equipo.
7. Se pasa al siguiente objeto con "Siguiente objeto →".

## Cómo termina la partida

- **Automáticamente**, cuando se agotan los 16 objetos del catálogo.
- **Manualmente**, pulsando "Terminar juego" en cualquier momento (pide confirmación).

En ambos casos aparece un pop-up con el equipo ganador (el de más puntos; si hay empate, se muestran todos los empatados) y la tabla final de puntuaciones.

## Persistencia

Todo se guarda en el `localStorage` del navegador: el catálogo de objetos que quedan por jugar, la configuración de equipos, el marcador y el objeto actual. Si se recarga la página a mitad de partida (por ejemplo, tras un corte de conexión), al volver a abrir el juego aparece un aviso para **continuar la partida en curso** o **descartarla y empezar una nueva**.

## Diseño

Pensado para verse bien proyectado en la plaza: fondo oscuro con acentos dorados/cobrizos (evocando una subasta de antigüedades), tipografía grande, y el precio revelado como una "etiqueta" bien visible. El equipo ganador de cada ronda se resalta en verde.

## Voz en off

Se usa la Web Speech API del propio navegador (`SpeechSynthesis`), en español. Al mostrar cada objeto se intenta reproducir automáticamente; algunos navegadores bloquean el audio automático hasta la primera interacción del usuario, por lo que hay un botón **"🔊 Repetir descripción"** en la cabecera como respaldo.

## Catálogo (`precio_justo_vdr_v1.json`)

Cada objeto incluye:

| Campo | Descripción |
|---|---|
| `id` | Identificador único del objeto |
| `name` | Nombre mostrado en pantalla |
| `description` | Texto que lee la voz en off |
| `image` | Ruta local de la imagen (carpeta `imagenes/`) |
| `price` | Precio justo del objeto |

### Objetos actuales (16)

Todos son piezas rústicas y técnicas reales, con precios de referencia de un catálogo de antigüedades: cántaro de Cuenca, zoqueta de segador, cedazo de harina, trillo, radio Jicky, teléfono de sobremesa, carro de bueyes, ábaco de escuela, garlopa de carpintero, pala de horno, tenazas de brasero, tomavistas Capta-Movi, gaseosa La Revoltosa, máquina de coser Willcox & Gibbs, hoz y horca de madera.

### Ejemplo de objeto

```json
{
  "id": "obj16",
  "name": "Horca de Madera",
  "description": "Una horca de madera de labranza, de las que se usaban para mover y aventar la paja y la parva durante la trilla.",
  "image": "imagenes/horca.jpg",
  "price": 50
}
```

## Imágenes

Las fotografías de los objetos están en la carpeta `imagenes/`, con nombres descriptivos (`cantaro.jpg`, `hoz.JPG`, `maquina_de_coser.jpg`...) que coinciden con el campo `image` de cada objeto en el JSON.

## Uso local

```bash
npx serve .
# o bien
python3 -m http.server
```

No hay dependencias externas: todo el código (HTML, CSS y JavaScript) está en un único archivo `index.html`, sin librerías de terceros.
