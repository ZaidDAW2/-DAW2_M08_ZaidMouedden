/* ==========================================================================
   main.js — Mejoras progresivas
   La web funciona sin JavaScript. Cada función añade una mejora y comprueba
   primero que los elementos que necesita existen, así un cambio en el HTML
   no rompe el resto.
   ========================================================================== */

"use strict";

/* ---------- Tema claro / oscuro ---------- */
function initThemeToggle() {
  const button = document.querySelector(".theme-toggle");
  if (!button) return;

  const root = document.documentElement;

  const render = () => {
    const isDark = root.dataset.theme === "dark";
    button.setAttribute("aria-pressed", String(isDark));
    button.setAttribute("aria-label", isDark ? "Tema claro" : "Tema oscuro");
  };

  button.addEventListener("click", () => {
    root.dataset.theme = root.dataset.theme === "dark" ? "light" : "dark";
    try {
      localStorage.setItem("theme", root.dataset.theme);
    } catch {
      /* navegación privada o almacenamiento bloqueado: el tema no se recuerda */
    }
    render();
  });

  render();
}

/* ---------- Menú móvil ---------- */
function initMobileMenu() {
  const toggle = document.querySelector(".menu-toggle");
  const nav = document.getElementById("site-nav");
  if (!toggle || !nav) return;

  const setOpen = (open) => {
    toggle.setAttribute("aria-expanded", String(open));
    nav.classList.toggle("is-open", open);
  };

  toggle.addEventListener("click", () => {
    setOpen(toggle.getAttribute("aria-expanded") !== "true");
  });

  // Cierra al elegir un enlace
  nav.addEventListener("click", (event) => {
    if (event.target.closest("a")) setOpen(false);
  });

  // Cierra con Escape y devuelve el foco al botón
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && toggle.getAttribute("aria-expanded") === "true") {
      setOpen(false);
      toggle.focus();
    }
  });

  // Si se agranda la ventana a escritorio, resetea el estado
  window.matchMedia("(min-width: 48em)").addEventListener("change", (mq) => {
    if (mq.matches) setOpen(false);
  });
}

/* ---------- Enlace activo según la sección visible ---------- */
function initScrollSpy() {
  const links = document.querySelectorAll('.site-nav a[href^="#"]');
  if (!links.length || !("IntersectionObserver" in window)) return;

  const linkById = new Map();
  links.forEach((link) => linkById.set(link.hash.slice(1), link));

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        links.forEach((link) => link.removeAttribute("aria-current"));
        const active = linkById.get(entry.target.id);
        if (active) active.setAttribute("aria-current", "true");
      });
    },
    // La sección cuenta como activa cuando cruza la franja central de la pantalla
    { rootMargin: "-45% 0px -50% 0px" }
  );

  linkById.forEach((_, id) => {
    const section = document.getElementById(id);
    if (section) observer.observe(section);
  });
}

/* ---------- Filtro de proyectos por tecnología ---------- */
function initProjectFilter() {
  const container = document.querySelector("[data-filters]");
  const status = document.querySelector("[data-filter-status]");
  const projects = [...document.querySelectorAll(".project[data-tags]")];
  if (!container || projects.length < 2) return;

  // Recoge las etiquetas únicas de todos los proyectos
  const tags = [...new Set(projects.flatMap((p) => p.dataset.tags.split(/\s+/).filter(Boolean)))].sort();

  const LABELS = { html: "HTML", css: "CSS", javascript: "JavaScript", api: "API", sql: "SQL", java: "Java" };
  const label = (tag) => LABELS[tag] ?? tag.charAt(0).toUpperCase() + tag.slice(1);

  const makeButton = (value, text) => {
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "btn btn--ghost btn--sm";
    btn.dataset.filter = value;
    btn.textContent = text;
    btn.setAttribute("aria-pressed", "false");
    return btn;
  };

  const buttons = [makeButton("all", "Todos"), ...tags.map((t) => makeButton(t, label(t)))];
  container.append(...buttons);

  const apply = (filter) => {
    let visible = 0;
    projects.forEach((project) => {
      const match = filter === "all" || project.dataset.tags.split(/\s+/).includes(filter);
      project.hidden = !match;
      if (match) visible += 1;
    });
    buttons.forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.filter === filter)));
    if (status) status.textContent = `${visible} proyecto${visible === 1 ? "" : "s"} visible${visible === 1 ? "" : "s"}`;
  };

  container.addEventListener("click", (event) => {
    const btn = event.target.closest("button[data-filter]");
    if (btn) apply(btn.dataset.filter);
  });

  apply("all");
  container.hidden = false;
}

/* ---------- Copiar email al portapapeles ---------- */
function initCopyButtons() {
  if (!navigator.clipboard) return;

  document.querySelectorAll("[data-copy]").forEach((button) => {
    const original = button.textContent;
    button.hidden = false;

    button.addEventListener("click", async () => {
      try {
        await navigator.clipboard.writeText(button.dataset.copy);
        button.textContent = "¡Copiado!";
      } catch {
        button.textContent = "No se pudo copiar";
      }
      setTimeout(() => (button.textContent = original), 2000);
    });
  });
}

/* ---------- Año actual en el pie ---------- */
function initYear() {
  const el = document.querySelector("[data-year]");
  if (el) el.textContent = String(new Date().getFullYear());
}

/* ---------- Arranque ---------- */
initThemeToggle();
initMobileMenu();
initScrollSpy();
initProjectFilter();
initCopyButtons();
initYear();
