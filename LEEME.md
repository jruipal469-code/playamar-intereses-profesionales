# Cuestionario de intereses · Playamar te orienta

Aplicación lista para GitHub Pages, sin instalación, servidor propio ni servicios de pago. Mantiene el logotipo oficial del IES Playamar, la tipografía Titillium, los colores de la web y la imagen de Autorientación. No utiliza Sites ni H5P.

## Probarla antes de publicarla

Abre `entrega/index.html` en Chrome, Edge, Firefox o Safari. Es un archivo autónomo: incluye el cuestionario, el diseño, las fuentes, el logo y la imagen. No requiere conexión para responder y calcular resultados. Los enlaces para volver a la web sí necesitan internet.

También puedes descomprimir `Playamar-cuestionario-GitHub.zip` y abrir su `index.html` con doble clic. No subas el ZIP sin descomprimirlo.

## Publicarla en GitHub Pages

1. En tu cuenta de GitHub, crea un repositorio nuevo llamado, por ejemplo, `playamar-intereses`. Para usar GitHub Pages con una cuenta gratuita, elige un repositorio público.
2. Descomprime el paquete `Playamar-cuestionario-GitHub.zip`.
3. En el repositorio, selecciona **Add file → Upload files** y sube el archivo **index.html** y **LEEME.md**. El `index.html` debe quedar directamente en la raíz del repositorio, no dentro de otra carpeta. Incluye `.nojekyll` si aparece entre los archivos; si no, puedes crearlo después con **Add file → Create new file**, darle ese nombre y añadir un salto de línea.
4. Guarda la subida con **Commit changes**.
5. Abre **Settings → Pages**. En **Build and deployment**, selecciona **Deploy from a branch**; elige **main** y **/(root)**. Pulsa **Save**.
6. Cuando termine la publicación, GitHub mostrará el enlace de la aplicación en **Settings → Pages → Visit site**. La primera publicación puede tardar unos minutos.
7. Abre ese enlace y prueba **Comenzar el cuestionario**. Esa es la dirección que se enlazará desde la página Autorientación de WordPress.

Si el archivo descargado se llama `index.html.txt`, cambia el nombre a `index.html` antes de subirlo.

Instrucciones contrastadas el 31/10/2026 con la documentación de GitHub:
- [Crear un sitio de GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)
- [Configurar la fuente de publicación](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)

## Qué hace

- 80 actividades en ocho bloques de diez, con lenguaje adaptado a adolescentes y un ejemplo visible en cada una.
- Dos respuestas mutuamente excluyentes: «Me interesa» / «No me interesa».
- Indicación de progreso y aviso de preguntas pendientes.
- Revisión de respuestas antes y después de consultar resultados.
- Cinco puntuaciones de 0 a 16, con barras y texto accesible.
- Mayor puntuación y siguiente puntuación distinta, incluyendo todos sus empates.
- Interpretación específica para todas las áreas iguales y para todas las respuestas negativas.
- Impresión de resultados y guardado como PDF a través del diálogo de impresión del navegador. En móvil, la opción disponible depende del navegador y del sistema.
- Enlaces de vuelta a la web, Autorientación y las enseñanzas.

## Qué significa el resultado

Es una exploración de intereses, no una evaluación de competencias, aptitudes ni idoneidad para una profesión. No hay umbrales inventados de «alto», «medio» o «bajo», comparaciones con otros alumnos ni porcentajes de capacidad. Cada «Me interesa» suma un punto al área que figura en la Tabla I del documento original.

Se conservan las 80 actividades, su numeración y la asignación original, incluidas algunas correspondencias que pueden resultar poco intuitivas: por ejemplo, el ítem 18 pertenece a Ciencia y tecnología. No se han redistribuido según una interpretación propia.

## Origen del cuestionario

«Test para la identificación de intereses vocacionales y profesionales», elaborado por las psicólogas Malca de Goldenberg y Magali Merchán. Documento facilitado por el Departamento de Orientación del IES Playamar.

La versión actual adapta el lenguaje de los 80 enunciados para adolescentes y añade un ejemplo explicativo por actividad. Mantiene la numeración, las dos opciones de respuesta y la clave de puntuación del original. No es una transcripción literal ni se ha establecido su equivalencia psicométrica con el original. En el ítem 56, «productos ecuatorianos» se adapta a «productos de tu país» y se utiliza el aceite de oliva como ejemplo cercano. Los ejemplos no son preguntas adicionales ni suman puntos.

La transcripción de origen se conserva en `dist/datos.js`, bajo `itemsOriginales`, para facilitar la revisión del Departamento. `REVISION-LENGUAJE.md` permite comparar cada enunciado original con su adaptación y su ejemplo. Las explicaciones de áreas y los ejemplos de profesiones de los resultados son una síntesis orientativa añadida, no la reproducción completa de la Tabla II ni una oferta educativa verificada.

La imagen procede de la cabecera de Autorientación de la web del centro. El logotipo es el utilizado en la cabecera oficial de [iesplayamar.es](https://iesplayamar.es/). Las fuentes Titillium se han tomado de los recursos de la web de BlogsAverroes del centro. Se mantienen integrados para evitar consultas externas durante el cuestionario.

## Respuestas y privacidad

La aplicación no pide nombres ni correos, no incluye formularios de envío, analítica, cookies ni almacenamiento local de respuestas. Las respuestas existen solo en memoria durante la sesión de la página. Recargarla o cerrarla las borra. El informe se imprime localmente; no se envía a Orientación.

El alojamiento puede registrar peticiones de visita según sus propias condiciones. La aplicación no incluye las respuestas en direcciones web ni solicitudes de red. No hay integración con cuentas de alumnado ni con servicios de IA.

## Editar y mantener

Los archivos editables están en `dist/`: `index.html`, `estilos.css`, `app.js`, `datos.js`, `motor.js` y los recursos gráficos. La carpeta `entrega/` contiene la versión autónoma lista para publicar.

Para probar los archivos modulares hace falta servir `dist/` con un servidor local; abrir ese `index.html` directamente como archivo puede bloquear las importaciones. Para probar sin servidor, utiliza siempre `entrega/index.html`.

Pruebas del cálculo: `node --test test.mjs`.

Generar de nuevo el paquete y el archivo autónomo después de editar: `python3 empaquetar.py`.

No se ha publicado en GitHub ni se ha cambiado la página de WordPress. Esta versión incorpora la revisión lingüística solicitada; el siguiente paso, tras revisar el contenido, es publicar el paquete en tu repositorio y utilizar la URL que GitHub devuelva.

## Comprobaciones realizadas

- Seis pruebas automáticas: cobertura de los 80 ítems, exclusividad de asignación a un área, puntuación individual, empates, respuestas negativas y rechazo de cuestionarios incompletos.
- Recorrido completo en navegador, incluida la versión autónoma empaquetada: perfil de prueba con resultados 16/7/3/2/1 y prueba previa con cinco áreas empatadas a 16.
- Validación de preguntas pendientes, conservación de respuestas al volver atrás y reinicio.
- Revisión visual en ordenador y a 390 píxeles de ancho, sin desbordamiento horizontal.
- Vista de impresión de un informe de ejemplo: dos páginas con las cinco puntuaciones y las orientaciones.
- El archivo autónomo se ha comprobado servido localmente por HTTP. La apertura directa con doble clic no se ha podido verificar mediante el navegador de pruebas, que no permite direcciones `file://`; el archivo se entrega con todos sus recursos integrados y sin importaciones externas.
- La publicación final en GitHub Pages queda pendiente hasta subirlo a tu repositorio.

Revisión de lenguaje del 31/10/2026: 80 enunciados adaptados y 80 ejemplos explicativos; clave de puntuación conservada.
