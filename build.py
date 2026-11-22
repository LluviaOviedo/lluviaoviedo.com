#!/usr/bin/env python3
"""Genera index.html (español) y en/index.html (inglés) desde una sola plantilla.
Edita el contenido en CONTENT y ejecuta:  python3 build.py
"""
import html
import os
from urllib.parse import quote

SITE = "https://lluviaoviedo.com"
EMAIL = "raingogh@gmail.com"
PHONE_DISPLAY = "+52 55 1329 8857"
WA_NUMBER = "525513298857"

CONTENT = {
    "es": {
        "path": "/",
        "out": "index.html",
        "alt_lang": "en",
        "alt_label": "EN",
        "alt_path": "/en/",
        "title": "Lluvia Oviedo · Especialista en Marketing Digital",
        "desc": "Especialista en Marketing y Marketing Digital con 14 años de experiencia en estrategia, brand management, desarrollo de producto, retail y performance digital. CDMX.",
        "nav": ["Perfil", "Experiencia", "Formación", "Contacto"],
        "eyebrow": "Especialista en Marketing Digital",
        "hero_lead": "14 años convirtiendo estrategia en crecimiento: marcas más fuertes, campañas medibles y equipos alineados con el negocio.",
        "cta_primary": "Hablemos",
        "cta_secondary": "Ver experiencia",
        "location": "Ciudad de México",
        "available": "Disponible para nuevos proyectos",
        "stats": [
            ("14", "años de experiencia"),
            ("400%", "crecimiento de portafolio"),
            ("100+", "productos desarrollados"),
            ("38 MDP", "en ventas anuales"),
        ],
        "about_kicker": "Perfil",
        "about_title": "Estrategia, marca y <em>resultados</em>.",
        "about": [
            "Especialista en Marketing y Marketing Digital con 14 años de experiencia en estrategias de marketing, comunicación, brand management, desarrollo de productos, retail y campañas de performance digital.",
            "Experiencia liderando equipos multidisciplinarios, gestionando presupuestos y desarrollando estrategias comerciales enfocadas en la expansión del negocio, generación de nuevas oportunidades, ventas y crecimiento de marca. Profesional estratégica, orientada a resultados y con habilidades de liderazgo y visión de negocio.",
        ],
        "skills_title": "Habilidades",
        "skills": ["Management", "Marketing Digital", "Enfocada a objetivos", "Analítica", "Team Player", "Creativa", "Inglés Profesional"],
        "focus_title": "Áreas de especialidad",
        "focus": ["Brand Management", "Performance & Paid Media", "SEO / SEM", "Desarrollo de producto", "Retail", "Gestión de cuentas clave"],
        "exp_kicker": "Experiencia",
        "exp_title": "Trayectoria <em>profesional</em>",
        "now": "Actualidad",
        "jobs": [
            ("2025", None, "Key Account Manager", "Eyxo Agency",
             "Lidero la gestión integral de una cuenta clave junto a un equipo multidisciplinario distribuido en LATAM, asegurando una operación eficiente y orientada a resultados. Superviso entregas creativas, gestiono crisis y participo en la planificación estratégica. Identifico oportunidades de mejora y propongo acciones para escalar la operación y generar mayor valor para el cliente, manteniendo al equipo alineado con sus objetivos.",
             []),
            ("2021", "2025", "Gerente de Cuentas Digitales", "LUMIA Agency",
             "Lideré el desarrollo de campañas digitales, inversión en medios, control de pautas, seguimiento en redes sociales, cumplimiento de KPI’s y reporting. Respondía a las solicitudes de clientes generando nuevas oportunidades de negocio. Experiencia en industrias farmacéutica, automotriz, bebidas, nutrición deportiva, suplementos, juguetes y cementera.",
             []),
            ("2017", "2021", "Business Manager", "Actual Sales Agency",
             "Gestioné campañas digitales como Media Buyer y Content Manager, generando estrategias SEO/SEM, creación de contenidos y marketing en redes sociales. Amplié la cobertura a 20 nuevas zonas geográficas e integré 4 plataformas de push notifications.",
             ["+15% ROI", "+20% tráfico web", "100% de leads"]),
            ("2014", "2017", "Gerente de Mercadotecnia", "Green Carpet",
             "Supervisé áreas clave como administración, operaciones, logística, ventas y finanzas. Lideré estrategias de producto, precios, comunicación y coordinación con agencias, mejorando el posicionamiento de marca.",
             ["+400% portafolio", "+40% clientes", "+20% ventas"]),
            ("2012", "2014", "Jefe de Marca Propia", "Nutrisa",
             "Evalué y desarrollé nuevos productos con proveedores nacionales e internacionales; coordiné la logística, el catálogo online y la capacitación del personal en todos los productos de marca propia.",
             ["100+ productos en 2 años", "38 MDP ventas anuales", "+18% crecimiento"]),
        ],
        "edu_kicker": "Formación",
        "edu_title": "Formación <em>académica</em>",
        "edu": [
            ("2017 — 2019", "Maestría en Marketing", "Universidad de la Comunicación"),
            ("2002 — 2006", "Licenciatura en Comunicación Visual", "Universidad de la Comunicación"),
        ],
        "contact_kicker": "Contacto",
        "contact_title": "¿Tienes un proyecto o una oportunidad? <em>Conversemos.</em>",
        "contact_lead": "Escríbeme por correo o por WhatsApp y te respondo a la brevedad.",
        "email_label": "Correo electrónico",
        "wa_label": "WhatsApp",
        "wa_msg": "Hola Lluvia, vi tu portafolio en lluviaoviedo.com y me gustaría platicar contigo.",
        "form_title": "Envíame un mensaje",
        "f_name": "Nombre",
        "f_email": "Tu correo",
        "f_msg": "Mensaje",
        "f_send_mail": "Enviar por correo",
        "f_send_wa": "Enviar por WhatsApp",
        "f_subject": "Contacto desde lluviaoviedo.com",
        "f_hint": "Se abrirá tu app de correo o WhatsApp con el mensaje listo.",
        "copy": "Copiar",
        "copied": "¡Copiado!",
        "footer": "Todos los derechos reservados.",
        "back_top": "Volver arriba",
        "photo_alt": "Retrato de Lluvia Oviedo",
    },
    "en": {
        "path": "/en/",
        "out": "en/index.html",
        "alt_lang": "es",
        "alt_label": "ES",
        "alt_path": "/",
        "title": "Lluvia Oviedo · Digital Marketing Specialist",
        "desc": "Marketing and Digital Marketing Specialist with 14 years of experience in strategy, brand management, product development, retail and digital performance. Mexico City.",
        "nav": ["Profile", "Experience", "Education", "Contact"],
        "eyebrow": "Digital Marketing Specialist",
        "hero_lead": "14 years turning strategy into growth: stronger brands, measurable campaigns and teams aligned with the business.",
        "cta_primary": "Let’s talk",
        "cta_secondary": "See experience",
        "location": "Mexico City",
        "available": "Open to new opportunities",
        "stats": [
            ("14", "years of experience"),
            ("400%", "portfolio growth"),
            ("100+", "products developed"),
            ("MXN 38M", "in annual sales"),
        ],
        "about_kicker": "Profile",
        "about_title": "Strategy, brand and <em>results</em>.",
        "about": [
            "Marketing and Digital Marketing Specialist with 14 years of experience in marketing strategies, communications, brand management, product development, retail, and digital performance campaigns.",
            "Experienced in leading multidisciplinary teams, managing budgets, and developing business strategies focused on commercial expansion, new business opportunities, sales growth, and brand development. A strategic, results-driven professional with strong leadership skills and business acumen.",
        ],
        "skills_title": "Skills",
        "skills": ["Management", "Digital Marketing", "Goal-driven", "Analytical", "Team Player", "Creative", "Professional English"],
        "focus_title": "Areas of expertise",
        "focus": ["Brand Management", "Performance & Paid Media", "SEO / SEM", "Product Development", "Retail", "Key Account Management"],
        "exp_kicker": "Experience",
        "exp_title": "Professional <em>journey</em>",
        "now": "Present",
        "jobs": [
            ("2025", None, "Key Account Manager", "Eyxo Agency",
             "I lead the end-to-end management of a key client account, coordinating a multidisciplinary team across LATAM to ensure efficient operations and results-driven execution. I oversee creative deliverables, manage crisis situations and contribute to strategic planning, identifying growth opportunities and driving initiatives that deliver greater value to the client while keeping the team aligned with business objectives.",
             []),
            ("2021", "2025", "Digital Account Manager", "LUMIA Agency",
             "Led the development of digital campaigns, managed media investments, oversaw ad placements, monitored social media performance, tracked KPIs and prepared reports. Managed client requests and generated new business opportunities across pharmaceuticals, automotive, beverages, sports nutrition, supplements, toys and cement.",
             []),
            ("2017", "2021", "Business Manager", "Actual Sales Agency",
             "Managed digital campaigns as Media Buyer and Content Manager, developing SEO/SEM strategies, creating content and executing social media marketing initiatives. Expanded market reach to over 20 new geographic markets and integrated four push notification platforms.",
             ["+15% ROI", "+20% web traffic", "100% of lead targets"]),
            ("2014", "2017", "Marketing Manager", "Green Carpet",
             "Oversaw key business areas including administration, operations, logistics, sales and finance. Led product, pricing and communication strategies while coordinating external agencies, strengthening brand positioning.",
             ["+400% portfolio", "+40% client base", "+20% sales"]),
            ("2012", "2014", "Private Label Manager", "Nutrisa",
             "Evaluated and developed new products with national and international suppliers, coordinated logistics, managed the online catalog and trained staff on private label products.",
             ["100+ products in 2 years", "MXN 38M annual sales", "+18% YoY growth"]),
        ],
        "edu_kicker": "Education",
        "edu_title": "Academic <em>background</em>",
        "edu": [
            ("2017 — 2019", "Master’s Degree in Marketing", "Universidad de la Comunicación"),
            ("2002 — 2006", "Bachelor’s Degree in Visual Communication", "Universidad de la Comunicación"),
        ],
        "contact_kicker": "Contact",
        "contact_title": "Have a project or an opportunity? <em>Let’s talk.</em>",
        "contact_lead": "Reach out by email or WhatsApp and I’ll get back to you shortly.",
        "email_label": "Email",
        "wa_label": "WhatsApp",
        "wa_msg": "Hi Lluvia, I saw your portfolio at lluviaoviedo.com and would like to talk with you.",
        "form_title": "Send me a message",
        "f_name": "Name",
        "f_email": "Your email",
        "f_msg": "Message",
        "f_send_mail": "Send by email",
        "f_send_wa": "Send via WhatsApp",
        "f_subject": "Contact from lluviaoviedo.com",
        "f_hint": "Your email app or WhatsApp will open with the message ready to send.",
        "copy": "Copy",
        "copied": "Copied!",
        "footer": "All rights reserved.",
        "back_top": "Back to top",
        "photo_alt": "Portrait of Lluvia Oviedo",
    },
}

ICON_MAIL = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5h16a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2Zm0 2v.4l8 5.1 8-5.1V7H4Zm16 2.8-7.46 4.75a1 1 0 0 1-1.08 0L4 9.8V17h16V9.8Z"/></svg>'
ICON_WA = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12.04 2a9.9 9.9 0 0 0-8.5 15l-1.4 5.1 5.24-1.37A9.9 9.9 0 1 0 12.04 2Zm0 18.1a8.2 8.2 0 0 1-4.18-1.15l-.3-.18-3.1.82.83-3.03-.2-.31a8.2 8.2 0 1 1 6.95 3.85Zm4.5-6.14c-.25-.12-1.46-.72-1.69-.8-.23-.09-.39-.13-.56.12-.16.25-.64.8-.78.97-.15.16-.29.18-.54.06a6.7 6.7 0 0 1-1.98-1.22 7.5 7.5 0 0 1-1.37-1.7c-.14-.25 0-.38.11-.5l.37-.44c.13-.15.17-.25.25-.42.08-.16.04-.31-.02-.43-.06-.13-.56-1.35-.77-1.85-.2-.48-.4-.42-.56-.43h-.48a.92.92 0 0 0-.66.31 2.8 2.8 0 0 0-.87 2.07 4.85 4.85 0 0 0 1.02 2.57c.12.17 1.76 2.68 4.26 3.76.6.26 1.06.41 1.42.52.6.19 1.14.16 1.57.1.48-.07 1.46-.6 1.67-1.18.2-.58.2-1.07.15-1.18-.06-.1-.23-.16-.48-.28Z"/></svg>'
ICON_PIN = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a7 7 0 0 1 7 7c0 5.25-7 13-7 13S5 14.25 5 9a7 7 0 0 1 7-7Zm0 4.5A2.5 2.5 0 1 0 12 11.5 2.5 2.5 0 0 0 12 6.5Z"/></svg>'
ICON_ARROW = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.3 5.3a1 1 0 0 1 1.4 0l6 6a1 1 0 0 1 0 1.4l-6 6a1 1 0 0 1-1.4-1.4l4.29-4.3H4a1 1 0 1 1 0-2h13.59L13.3 6.7a1 1 0 0 1 0-1.4Z"/></svg>'


def render(lang, c):
    e = html.escape
    wa_link = f"https://wa.me/{WA_NUMBER}?text={quote(c['wa_msg'])}"
    nav_ids = ["perfil", "experiencia", "formacion", "contacto"] if lang == "es" else ["profile", "experience", "education", "contact"]

    nav = "".join(f'<a href="#{i}">{e(t)}</a>' for i, t in zip(nav_ids, c["nav"]))
    stats = "".join(
        f'<div class="stat reveal"><span class="stat-n">{e(n)}</span><span class="stat-l">{e(l)}</span></div>'
        for n, l in c["stats"]
    )
    about = "".join(f"<p>{e(p)}</p>" for p in c["about"])
    skills = "".join(f"<li>{e(s)}</li>" for s in c["skills"])
    focus = "".join(f"<li>{e(s)}</li>" for s in c["focus"])

    jobs = []
    for i, (start, end, role, company, text, wins) in enumerate(c["jobs"]):
        period = f"{start} — {end or c['now']}"
        current = ' current' if end is None else ''
        wins_html = ""
        if wins:
            wins_html = '<ul class="wins">' + "".join(f"<li>{e(w)}</li>" for w in wins) + "</ul>"
        jobs.append(f'''
        <article class="job reveal{current}">
          <div class="job-dot" aria-hidden="true"></div>
          <div class="job-period">{e(period)}</div>
          <div class="job-card">
            <h3>{e(role)}</h3>
            <p class="job-company">{e(company)}</p>
            <p class="job-text">{e(text)}</p>
            {wins_html}
          </div>
        </article>''')
    jobs_html = "".join(jobs)

    edu = "".join(
        f'<div class="edu-card reveal"><span class="edu-years">{e(y)}</span><h3>{e(d)}</h3><p>{e(s)}</p></div>'
        for y, d, s in c["edu"]
    )

    canonical = SITE + c["path"]
    alt_url = SITE + c["alt_path"]
    og_locale = "es_MX" if lang == "es" else "en_US"

    jsonld = f'''{{"@context":"https://schema.org","@type":"Person","name":"Lluvia Oviedo","jobTitle":"{c['eyebrow']}","url":"{canonical}","image":"{SITE}/assets/lluvia-oviedo.jpg","email":"mailto:{EMAIL}","address":{{"@type":"PostalAddress","addressLocality":"Ciudad de México","addressCountry":"MX"}},"alumniOf":"Universidad de la Comunicación"}}'''

    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(c["title"])}</title>
<meta name="description" content="{e(c["desc"])}">
<meta name="theme-color" content="#0a0a0d">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="es" href="{SITE}/">
<link rel="alternate" hreflang="en" href="{SITE}/en/">
<link rel="alternate" hreflang="x-default" href="{SITE}/">
<meta property="og:type" content="profile">
<meta property="og:title" content="{e(c["title"])}">
<meta property="og:description" content="{e(c["desc"])}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/assets/og.jpg">
<meta property="og:locale" content="{og_locale}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..600;1,9..144,300..600&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
<script type="application/ld+json">{jsonld}</script>
</head>
<body>
<div class="bg" aria-hidden="true"><div class="orb o1"></div><div class="orb o2"></div><div class="orb o3"></div><div class="grain"></div></div>

<header class="topbar" id="top">
  <a class="logo" href="{c["path"]}" aria-label="Lluvia Oviedo">LO<span>.</span></a>
  <nav class="nav" aria-label="Main">{nav}</nav>
  <a class="lang" href="{c["alt_path"]}" hreflang="{c["alt_lang"]}" lang="{c["alt_lang"]}">{c["alt_label"]}</a>
</header>

<main>
  <section class="hero">
    <div class="hero-text">
      <p class="eyebrow reveal"><span class="pulse"></span>{e(c["available"])}</p>
      <h1 class="reveal"><span class="first">Lluvia</span><span class="last">Oviedo</span></h1>
      <p class="role reveal">{e(c["eyebrow"])}</p>
      <p class="lead reveal">{e(c["hero_lead"])}</p>
      <div class="actions reveal">
        <a class="btn primary" href="#{nav_ids[3]}">{e(c["cta_primary"])} {ICON_ARROW}</a>
        <a class="btn ghost" href="#{nav_ids[1]}">{e(c["cta_secondary"])}</a>
      </div>
      <p class="loc reveal">{ICON_PIN} {e(c["location"])}</p>
    </div>
    <figure class="portrait reveal">
      <div class="portrait-frame">
        <picture>
          <source srcset="/assets/lluvia-oviedo.webp" type="image/webp">
          <img src="/assets/lluvia-oviedo.jpg" width="900" height="1200" alt="{e(c["photo_alt"])}" fetchpriority="high">
        </picture>
      </div>
      <div class="badge"><span>14</span><small>{e(c["stats"][0][1])}</small></div>
    </figure>
  </section>

  <section class="stats" aria-label="Highlights">{stats}</section>

  <section class="section about" id="{nav_ids[0]}">
    <div class="sec-head reveal"><span class="kicker">01 — {e(c["about_kicker"])}</span><h2>{c["about_title"]}</h2></div>
    <div class="about-grid">
      <div class="about-text reveal">{about}</div>
      <div class="about-side reveal">
        <h3>{e(c["focus_title"])}</h3>
        <ul class="tags">{focus}</ul>
        <h3>{e(c["skills_title"])}</h3>
        <ul class="tags soft">{skills}</ul>
      </div>
    </div>
  </section>

  <section class="section" id="{nav_ids[1]}">
    <div class="sec-head reveal"><span class="kicker">02 — {e(c["exp_kicker"])}</span><h2>{c["exp_title"]}</h2></div>
    <div class="timeline">{jobs_html}
    </div>
  </section>

  <section class="section" id="{nav_ids[2]}">
    <div class="sec-head reveal"><span class="kicker">03 — {e(c["edu_kicker"])}</span><h2>{c["edu_title"]}</h2></div>
    <div class="edu-grid">{edu}</div>
  </section>

  <section class="section contact" id="{nav_ids[3]}">
    <div class="contact-wrap reveal">
      <div class="contact-info">
        <span class="kicker">04 — {e(c["contact_kicker"])}</span>
        <h2>{c["contact_title"]}</h2>
        <p class="lead">{e(c["contact_lead"])}</p>
        <div class="channels">
          <div class="channel">
            <a class="channel-main" href="mailto:{EMAIL}?subject={quote(c["f_subject"])}">
              <span class="ic">{ICON_MAIL}</span>
              <span><small>{e(c["email_label"])}</small><strong>{EMAIL}</strong></span>
            </a>
            <button class="copy" type="button" data-copy="{EMAIL}" data-done="{e(c["copied"])}">{e(c["copy"])}</button>
          </div>
          <div class="channel">
            <a class="channel-main wa" href="{wa_link}" target="_blank" rel="noopener">
              <span class="ic">{ICON_WA}</span>
              <span><small>{e(c["wa_label"])}</small><strong>{PHONE_DISPLAY}</strong></span>
            </a>
            <button class="copy" type="button" data-copy="{PHONE_DISPLAY}" data-done="{e(c["copied"])}">{e(c["copy"])}</button>
          </div>
        </div>
      </div>
      <form class="contact-form" id="contact-form" data-email="{EMAIL}" data-wa="{WA_NUMBER}" data-subject="{e(c["f_subject"])}">
        <h3>{e(c["form_title"])}</h3>
        <label><span>{e(c["f_name"])}</span><input name="name" required autocomplete="name"></label>
        <label><span>{e(c["f_email"])}</span><input name="email" type="email" autocomplete="email"></label>
        <label><span>{e(c["f_msg"])}</span><textarea name="message" rows="4" required></textarea></label>
        <div class="form-actions">
          <button class="btn primary" type="submit" value="mail">{ICON_MAIL} {e(c["f_send_mail"])}</button>
          <button class="btn wa-btn" type="submit" value="wa">{ICON_WA} {e(c["f_send_wa"])}</button>
        </div>
        <p class="hint">{e(c["f_hint"])}</p>
      </form>
    </div>
  </section>
</main>

<footer class="footer">
  <p>© <span id="year">2026</span> Lluvia Oviedo. {e(c["footer"])}</p>
  <a href="#top">{e(c["back_top"])} ↑</a>
</footer>

<a class="wa-float" href="{wa_link}" target="_blank" rel="noopener" aria-label="WhatsApp">{ICON_WA}</a>
<script src="/assets/main.js" defer></script>
</body>
</html>
'''


if __name__ == "__main__":
    root = os.path.dirname(os.path.abspath(__file__))
    for lang, c in CONTENT.items():
        out = os.path.join(root, c["out"])
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            f.write(render(lang, c))
        print("wrote", c["out"])
