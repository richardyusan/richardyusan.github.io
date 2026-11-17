---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* Bachelor of Economics

<!-- TODO (Richard): add university and year above, and a Work experience section, e.g.
Work experience
======
* 20XX - present: Role, Company
  * What you did
-->

Profile
======
Software developer based in Indonesia with a Bachelor of Economics and co-authored economic research. I focus on porting software to new platforms (Android, WebAssembly, online multiplayer) and on low-level tooling for laptops and PC firmware.

Skills
======
* **Languages:** C, C++, C#, Python, JavaScript (Node.js), BlitzBasic
* **Platforms:** Android (NDK), Web (Emscripten / WebAssembly), Windows, Linux, macOS (OpenCore)
* **Graphics & games:** OpenGL ES 2, gl4es, Raydium 3D engine, ODE physics, Epic Online Services
* **Systems:** ACPI / ASL, power management, OpenCore
* **Tooling:** source-to-source transpilers, Git & GitHub Actions

Selected projects
======
* **MultiHero ports**: BlitzBasic-to-C++ transpiler; Android, WebAssembly and online multiplayer versions of the Blitz3D fighting game.
* **ManiaDrive Android**: Android port of the 2006 Raydium racing game with touch and gamepad support, story mode and LAN multiplayer.
* **IdeaPad 14ALC6 tooling**: fan control, battery conservation mode, Wi-Fi power settings and Hackintosh EFI for the Lenovo IdeaPad 14ALC6.

Publications
======
<ul>
{% assign pubs = site.publications | sort: "date" | reverse %}
{% for p in pubs %}
  <li>{{ p.citation }}</li>
{% endfor %}
</ul>

Open-source repositories
======
<ul>
{% for r in site.data.repos %}
  <li><a href="{{ r.html_url }}"><strong>{{ r.name }}</strong></a>{% if r.language %} ({{ r.language }}){% endif %}{% if r.description %}: {{ r.description }}{% endif %}</li>
{% endfor %}
</ul>
