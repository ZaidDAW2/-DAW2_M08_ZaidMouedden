# Portfolio · Nombre Apellido

Web personal que funciona como **currículum y portfolio**: permite a una empresa entender mi perfil en menos de un minuto y comprobar, con proyectos reales, lo que sé hacer.

🔗 **Versión publicada:** https://usuario.github.io/portfolio/
📁 **Repositorio:** https://github.com/usuario/portfolio

---

## Objetivo

- Presentar mi perfil profesional, competencias, formación y experiencia.
- Mostrar proyectos reales con enlace al código y a la demo, indicando qué competencia demuestra cada uno.
- Ser cómodo de consultar desde móvil, tableta y escritorio.
- Mantenerse vivo: se actualiza cada vez que termino un proyecto o práctica.

## Tecnologías

| Área | Qué se usa |
|---|---|
| Estructura | HTML5 semántico (`header`, `nav`, `main`, `section`, `article`, `address`, `dl`, `time`…) |
| Estilos | CSS propio sin frameworks: variables (custom properties), Grid, Flexbox, `clamp()` para tipografía fluida, enfoque *mobile-first* |
| Interacción | JavaScript vanilla como mejora progresiva (la web funciona sin JS) |
| Publicación | GitHub Pages |

## Funcionalidades

- **Responsive** con tres puntos de corte (móvil, ~640px, ~1024px) y menú desplegable en móvil.
- **Tema claro/oscuro**: respeta la preferencia del sistema y recuerda la elección manual.
- **Filtro de proyectos** por tecnología, generado automáticamente a partir de las etiquetas de cada proyecto.
- **Navegación activa**: el menú marca la sección visible.
- **Copiar email** con un clic.
- **Accesibilidad**: enlace "saltar al contenido", foco visible, atributos ARIA en los controles, contraste AA, respeto a `prefers-reduced-motion`.
- **Imprimible**: al imprimir (o guardar como PDF) se oculta lo interactivo y queda un CV limpio.

## Estructura del proyecto

```
portfolio/
├── index.html              # Todo el contenido, en orden de lectura
├── css/
│   ├── tokens.css          # Variables: colores, tipografía, espaciado, temas
│   ├── base.css            # Reset, estilos de etiquetas y utilidades
│   ├── layout.css          # Contenedor, cabecera, navegación, secciones, pie
│   ├── components.css      # Piezas reutilizables: botones, tarjetas, tags, filtros
│   └── sections.css        # Estilos específicos de cada sección + impresión
├── js/
│   └── main.js             # Tema, menú móvil, scroll spy, filtro, copiar email
├── assets/
│   ├── favicon.svg
│   └── img/                # Capturas de proyectos (y foto opcional)
└── README.md
```

**Convenciones**

- CSS con nomenclatura **BEM** (`.bloque__elemento--modificador`).
- Ningún color ni tamaño "a mano": todo sale de `tokens.css`. Cambiar la identidad visual = editar un archivo.
- Cada función de `main.js` comprueba que sus elementos existen antes de actuar, así un cambio en el HTML no rompe el resto.

## Cómo verlo en local

No necesita instalación ni compilación.

**Opción 1 — abrir directamente:** doble clic en `index.html`.

**Opción 2 — servidor local** (recomendado, se comporta igual que la versión publicada):

```bash
git clone https://github.com/usuario/portfolio.git
cd portfolio

# Con Python
python3 -m http.server 8000
# o con Node
npx serve .
```

Después abre http://localhost:8000.

## Cómo añadir un proyecto

1. Guarda una captura en `assets/img/` (16:9, formato `.webp` o `.png`).
2. En `index.html`, dentro de `#proyectos`, copia un `<article class="card project">` existente.
3. Cambia título, descripción, línea **Demuestra**, enlaces y el atributo `data-tags` (en minúscula, separados por espacios). El filtro se actualiza solo.
4. Commit: `feat(proyectos): añade <nombre del proyecto>`.

## Despliegue

Publicado con **GitHub Pages** desde la rama `main`:

1. *Settings → Pages → Build and deployment*.
2. *Source*: **Deploy from a branch** · *Branch*: `main` · carpeta `/ (root)`.
3. En 1–2 minutos queda disponible en `https://usuario.github.io/portfolio/`.

Cada `push` a `main` vuelve a publicar la web automáticamente.

## Flujo de trabajo con Git

- `main`: versión publicada; siempre estable.
- `develop` (u otra rama por funcionalidad, p. ej. `feature/proyectos`): donde se trabaja. Se integra en `main` con *merge* cuando está lista.
- Mensajes de commit siguiendo [Conventional Commits](https://www.conventionalcommits.org/es/): `feat:`, `fix:`, `style:`, `docs:`, `refactor:`.

## Licencia

Código bajo licencia MIT. Los textos e imágenes personales son © Nombre Apellido.
