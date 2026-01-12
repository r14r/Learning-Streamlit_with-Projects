#!/usr/bin/env python3
import os
import re
import html
import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT
SITE = BASE / 'site'
ASSETS = SITE / 'assets'

LEVELS = [
    ('beginner', '01_Beginner', 'Beginner'),
    ('advanced', '02_Advanced', 'Advanced'),
    ('expert', '03_Expert', 'Expert'),
]

STEP_RE = re.compile(r'^\s*-\s*(?:\[\s*\]\s*)?(?:\*\*)?Step\s+(\d+)(?:\*\*)?\s*:\s*(.*)$', re.IGNORECASE)
TIPPS_RE = re.compile(r'^##\s*Step\s+(\d+)\b', re.IGNORECASE)
WIDGET_RE = re.compile(r'\bst\.(\w+)\b')


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        return path.read_text(encoding='latin-1')


def format_title(dirname: str) -> str:
    parts = dirname.split('_')
    out = []
    for part in parts:
        if part.isdigit():
            out.append(part)
        else:
            out.append(part.capitalize())
    return ' '.join(out)


def parse_todo_steps(todo_text: str):
    steps = {}
    current = None
    buffer = []

    for line in todo_text.splitlines():
        match = STEP_RE.match(line)
        if match:
            if current is not None:
                steps[current] = '\n'.join(buffer).strip()
            current = int(match.group(1))
            desc = match.group(2).strip()
            buffer = [desc] if desc else []
            continue

        if current is not None:
            if line.strip() == '':
                buffer.append('')
            elif line.startswith('  ') or line.startswith('\t'):
                buffer.append(line.strip())
            elif line.startswith('- '):
                buffer.append(line.strip())
    if current is not None:
        steps[current] = '\n'.join(buffer).strip()
    return steps


def parse_tipps_sections(tipps_text: str):
    steps = {}
    current = None
    buffer = []

    lines = tipps_text.splitlines()
    for line in lines:
        match = TIPPS_RE.match(line)
        if match:
            if current is not None:
                steps[current] = '\n'.join(buffer).strip()
            current = int(match.group(1))
            buffer = []
            continue
        if current is not None:
            buffer.append(line)
    if current is not None:
        steps[current] = '\n'.join(buffer).strip()
    return steps


def md_inline(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', text)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank" rel="noopener">\1</a>', text)
    return text


def md_to_html(md: str) -> str:
    lines = md.splitlines()
    html_lines = []
    in_code = False
    in_ul = False

    for line in lines:
        if line.strip().startswith('```'):
            if not in_code:
                if in_ul:
                    html_lines.append('</ul>')
                    in_ul = False
                html_lines.append('<pre><code>')
                in_code = True
            else:
                html_lines.append('</code></pre>')
                in_code = False
            continue

        if in_code:
            html_lines.append(html.escape(line))
            continue

        if re.match(r'^---+$', line.strip()):
            if in_ul:
                html_lines.append('</ul>')
                in_ul = False
            html_lines.append('<hr>')
            continue

        if line.startswith('#'):
            if in_ul:
                html_lines.append('</ul>')
                in_ul = False
            level = len(line) - len(line.lstrip('#'))
            level = min(level, 4)
            content = line[level:].strip()
            html_lines.append(f'<h{level}>{md_inline(content)}</h{level}>')
            continue

        list_match = re.match(r'^\s*-\s+(.*)$', line)
        if list_match:
            if not in_ul:
                html_lines.append('<ul>')
                in_ul = True
            html_lines.append(f'<li>{md_inline(list_match.group(1).strip())}</li>')
            continue

        if line.strip() == '':
            if in_ul:
                html_lines.append('</ul>')
                in_ul = False
            continue

        if in_ul:
            html_lines.append('</ul>')
            in_ul = False

        html_lines.append(f'<p>{md_inline(line.strip())}</p>')

    if in_ul:
        html_lines.append('</ul>')
    if in_code:
        html_lines.append('</code></pre>')

    return '\n'.join(html_lines)


def rel_link(from_path: Path, to_path: Path) -> str:
    return os.path.relpath(to_path, from_path.parent).replace(os.sep, '/')


def render_page(title, nav_html, main_html, root_prefix):
    return f'''<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" href="{root_prefix}assets/styles.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:wght@400;600;700&family=Space+Grotesk:wght@400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/aos@2.3.4/dist/aos.css">
</head>
<body>
  <div class="site">
    <aside class="sidebar">
      <div class="brand">
        <div class="brand-title">Streamlit Workshop</div>
        <div class="brand-subtitle">Learning-Streamlit_with-Projects</div>
      </div>
      <div class="nav-search">
        <input id="nav-search" type="search" placeholder="Projekt oder Step suchen...">
        <div class="nav-search-hint">Tipp: Tippe z.B. "api" oder "step 3"</div>
      </div>
      {nav_html}
    </aside>
    <main class="main">
      {main_html}
    </main>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/aos@2.3.4/dist/aos.js"></script>
  <script src="{root_prefix}assets/app.js"></script>
</body>
</html>'''


def build_nav(structure, current_path, current_file: Path):
    nav_parts = ['<nav class="nav">']
    for level_key, level_title, projects in structure:
        level_open = current_path.startswith(f'{level_key}/')
        nav_parts.append(f'<details class="nav-level" {"open" if level_open else ""}>')
        nav_parts.append(f'<summary>{html.escape(level_title)}</summary>')
        nav_parts.append('<div class="nav-level-items">')
        for project in projects:
            proj_open = current_path.startswith(f'{level_key}/{project["slug"]}/')
            nav_parts.append(f'<details class="nav-project" {"open" if proj_open else ""}>')
            nav_parts.append(f'<summary>{html.escape(project["title"])}</summary>')
            nav_parts.append('<ul>')

            def link_item(label, target_path, is_active):
                target_file = SITE / target_path
                href = rel_link(current_file, target_file)
                cls = ' class="active"' if is_active else ''
                nav_parts.append(f'<li><a{cls} href="{href}">{html.escape(label)}</a></li>')

            link_item('Projekt', project['paths']['project'], current_path == project['paths']['project'])
            for step in project['steps']:
                link_item(f"Step {step['num']}", step['path'], current_path == step['path'])
            link_item('App', project['paths']['app'], current_path == project['paths']['app'])
            nav_parts.append('</ul>')
            nav_parts.append('</details>')
        nav_parts.append('</div>')
        nav_parts.append('</details>')
    nav_parts.append('</nav>')
    return '\n'.join(nav_parts)


def summarize_app(app_text: str):
    lines = [line for line in app_text.splitlines() if line.strip()]
    widgets = sorted(set(WIDGET_RE.findall(app_text)))
    imports = []
    functions = 0
    classes = 0
    data_sources = set()
    try:
        tree = ast.parse(app_text)
        for node in tree.body:
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                seg = ast.get_source_segment(app_text, node)
                if seg:
                    imports.append(seg)
            elif isinstance(node, ast.FunctionDef):
                functions += 1
            elif isinstance(node, ast.ClassDef):
                classes += 1
    except SyntaxError:
        pass
    import_names = []
    for item in imports:
        parts = re.split(r'\s+', item)
        if parts:
            if parts[0] == 'import' and len(parts) > 1:
                import_names.append(parts[1].split(',')[0])
            elif parts[0] == 'from' and len(parts) > 1:
                import_names.append(parts[1])
    app_lower = app_text.lower()
    if 'requests' in app_lower or 'httpx' in app_lower:
        data_sources.add('HTTP API')
    if 'yfinance' in app_lower:
        data_sources.add('Yahoo Finance')
    if 'pandas' in app_lower and ('read_csv' in app_lower or 'read_excel' in app_lower):
        data_sources.add('Datei (CSV/Excel)')
    if 'st.file_uploader' in app_lower:
        data_sources.add('Upload')
    if 'sqlite3' in app_lower or 'sqlalchemy' in app_lower:
        data_sources.add('Datenbank')
    if 'openai' in app_lower or 'anthropic' in app_lower or 'ollama' in app_lower:
        data_sources.add('LLM API')
    return {
        'lines': len(lines),
        'widgets': widgets[:8],
        'imports': sorted(set(import_names))[:6],
        'functions': functions,
        'classes': classes,
        'data_sources': sorted(data_sources),
    }


def build_assets():
    ASSETS.mkdir(parents=True, exist_ok=True)
    styles = """:root {
  --bg: #f5f0e8;
  --bg-alt: #f0e2d0;
  --ink: #1f1a16;
  --accent: #0f6f6b;
  --accent-soft: #e2b07d;
  --card: #fff8ef;
  --line: #e2c8a8;
  --shadow: 0 18px 40px rgba(31, 26, 22, 0.12);
}

body {
  font-family: "Space Grotesk", "Segoe UI", sans-serif;
  background: radial-gradient(circle at top left, #f8efe5 0%, #f3dfc6 45%, #f1d7b1 100%);
  color: var(--ink);
  min-height: 100vh;
}

.site {
  display: grid;
  grid-template-columns: 320px 1fr;
  min-height: 100vh;
}

.sidebar {
  position: sticky;
  top: 0;
  height: 100vh;
  overflow-y: auto;
  padding: 24px 20px 40px;
  background: linear-gradient(160deg, #fff7ee 0%, #f7e7d2 60%, #f0d3a8 100%);
  border-right: 1px solid var(--line);
}

.brand {
  padding: 16px 16px 24px;
  border-radius: 18px;
  background: var(--card);
  box-shadow: var(--shadow);
  margin-bottom: 20px;
}

.brand-title {
  font-family: "Fraunces", serif;
  font-size: 20px;
  letter-spacing: 0.5px;
}

.brand-subtitle {
  font-size: 12px;
  color: #5a4b3f;
}

.nav details {
  margin-bottom: 10px;
}

.nav summary {
  cursor: pointer;
  font-weight: 600;
  padding: 8px 10px;
  border-radius: 10px;
  background: rgba(255, 255, 255, 0.6);
}

.nav-level-items {
  margin-top: 8px;
  padding-left: 6px;
}

.nav-project summary {
  font-weight: 500;
  background: rgba(255, 255, 255, 0.4);
}

.nav ul {
  list-style: none;
  margin: 8px 0 0 0;
  padding-left: 12px;
}

.nav a {
  display: block;
  padding: 6px 8px;
  border-radius: 8px;
  color: #2a2018;
}

.nav a:hover {
  background: rgba(15, 111, 107, 0.12);
}

.nav a.active {
  background: rgba(15, 111, 107, 0.2);
  color: #0a4d4a;
  font-weight: 600;
}

.nav-search {
  background: rgba(255, 255, 255, 0.7);
  padding: 12px;
  border-radius: 14px;
  margin: 16px 0 20px;
  box-shadow: 0 12px 24px rgba(31, 26, 22, 0.08);
}

.nav-search input {
  width: 100%;
  border: 1px solid rgba(15, 111, 107, 0.2);
  border-radius: 10px;
  padding: 8px 10px;
  background: #fff;
}

.nav-search-hint {
  margin-top: 6px;
  font-size: 11px;
  color: #6a5847;
}

.main {
  padding: 32px 40px 80px;
}

.hero {
  background: var(--card);
  padding: 32px;
  border-radius: 24px;
  box-shadow: var(--shadow);
  margin-bottom: 28px;
}

.hero h1 {
  font-family: "Fraunces", serif;
  font-size: 36px;
  margin-bottom: 8px;
}

.meta {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
  font-size: 13px;
  color: #5a4b3f;
}

.section-card {
  background: var(--card);
  padding: 24px;
  border-radius: 20px;
  box-shadow: var(--shadow);
  margin-bottom: 24px;
}

.tabs {
  display: flex;
  gap: 10px;
  margin-bottom: 16px;
}

.tab-btn {
  border: none;
  background: rgba(15, 111, 107, 0.08);
  padding: 8px 16px;
  border-radius: 999px;
  font-weight: 600;
  cursor: pointer;
}

.tab-btn.active {
  background: var(--accent);
  color: #fff;
}

.tab-panel {
  display: none;
}

.tab-panel.active {
  display: block;
}

.md h1, .md h2, .md h3, .md h4 {
  font-family: "Fraunces", serif;
  margin-top: 18px;
}

.md pre {
  background: #1f1a16;
  color: #f7e7d2;
  padding: 14px;
  border-radius: 12px;
  overflow-x: auto;
}

.md code {
  background: rgba(15, 111, 107, 0.12);
  padding: 2px 6px;
  border-radius: 6px;
}

.badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: rgba(15, 111, 107, 0.12);
  color: #0a4d4a;
  padding: 4px 10px;
  border-radius: 999px;
  font-size: 12px;
  font-weight: 600;
}

.step-grid {
  display: grid;
  gap: 16px;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
}

.code-block {
  background: #1f1a16;
  color: #f7e7d2;
  padding: 18px;
  border-radius: 16px;
  overflow-x: auto;
}

.nav-inline {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.nav-inline a {
  background: rgba(15, 111, 107, 0.08);
  padding: 8px 14px;
  border-radius: 999px;
  font-weight: 600;
  color: #0a4d4a;
}

.summary-grid {
  display: grid;
  gap: 12px;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
}

.summary-card {
  background: rgba(255, 255, 255, 0.6);
  padding: 12px 14px;
  border-radius: 14px;
  border: 1px solid rgba(15, 111, 107, 0.12);
}

@media (max-width: 980px) {
  .site {
    grid-template-columns: 1fr;
  }
  .sidebar {
    position: relative;
    height: auto;
  }
  .main {
    padding: 24px;
  }
}
"""

    app_js = """document.addEventListener('DOMContentLoaded', () => {
  const tabContainers = document.querySelectorAll('[data-tabs]');
  tabContainers.forEach(container => {
    const buttons = container.querySelectorAll('.tab-btn');
    const panels = container.querySelectorAll('.tab-panel');
    if (!buttons.length) return;
    const activate = (index) => {
      buttons.forEach((btn, idx) => btn.classList.toggle('active', idx === index));
      panels.forEach((panel, idx) => panel.classList.toggle('active', idx === index));
    };
    buttons.forEach((btn, idx) => {
      btn.addEventListener('click', () => activate(idx));
    });
    activate(0);
  });

  if (window.AOS) {
    AOS.init({
      duration: 650,
      easing: 'ease-out-cubic',
      once: true,
    });
  }

  const navSearch = document.getElementById('nav-search');
  if (navSearch) {
    navSearch.addEventListener('input', (event) => {
      const query = event.target.value.toLowerCase().trim();
      const items = document.querySelectorAll('.nav li');
      items.forEach((item) => {
        const text = item.textContent.toLowerCase();
        const matches = !query || text.includes(query);
        item.style.display = matches ? '' : 'none';
      });
    });
  }
});
"""

    (ASSETS / 'styles.css').write_text(styles, encoding='utf-8')
    (ASSETS / 'app.js').write_text(app_js, encoding='utf-8')


def main():
    SITE.mkdir(exist_ok=True)
    build_assets()

    structure = []
    for level_key, level_dir, level_label in LEVELS:
        level_path = BASE / level_dir
        projects = []
        for project_dir in sorted(level_path.iterdir()):
            if not project_dir.is_dir():
                continue
            todo_path = project_dir / 'TODO.md'
            tipps_path = project_dir / 'TIPPS.md'
            app_path = project_dir / 'app' / 'app.py'

            todo_text = read_text(todo_path) if todo_path.exists() else ''
            tipps_text = read_text(tipps_path) if tipps_path.exists() else ''

            steps_desc = parse_todo_steps(todo_text)
            steps_tipps = parse_tipps_sections(tipps_text)
            step_numbers = sorted(set(steps_desc.keys()) | set(steps_tipps.keys()))

            app_text = read_text(app_path) if app_path.exists() else ''
            summary = summarize_app(app_text) if app_text else None

            projects.append({
                'slug': project_dir.name,
                'title': format_title(project_dir.name),
                'level': level_key,
                'paths': {},
                'steps': [
                    {'num': num, 'desc': steps_desc.get(num, ''), 'tipps': steps_tipps.get(num, '')}
                    for num in step_numbers
                ],
                'todo_text': todo_text,
                'tipps_text': tipps_text,
                'app_text': app_text,
                'summary': summary,
            })
        structure.append((level_key, level_label, projects))

    for level_key, _level_title, projects in structure:
        for project in projects:
            project_base = SITE / level_key / project['slug']
            project_base.mkdir(parents=True, exist_ok=True)
            project['paths']['project'] = f'{level_key}/{project["slug"]}/index.html'
            project['paths']['app'] = f'{level_key}/{project["slug"]}/app.html'
            for step in project['steps']:
                step['path'] = f'{level_key}/{project["slug"]}/step-{step["num"]:02d}.html'

    for level_key, level_title, projects in structure:
        for project in projects:
            project_base = SITE / level_key / project['slug']
            project_page = project_base / 'index.html'
            app_page = project_base / 'app.html'
            root_prefix = rel_link(project_page, SITE / 'assets' / 'styles.css').replace('assets/styles.css', '')

            nav_html = build_nav(structure, project['paths']['project'], project_page)

            todo_html = md_to_html(project['todo_text'] or 'Keine TODO.md gefunden.')
            tipps_html = md_to_html(project['tipps_text'] or 'Keine TIPPS.md gefunden.')

            step_cards = ''.join([
                f'<a class="box" href="{rel_link(project_page, SITE / step["path"])}"><strong>Step {step["num"]}</strong><p>{html.escape(step["desc"] or "Beschreibung fehlt")}</p></a>'
                for step in project['steps']
            ])

            summary_html = ''
            if project['summary']:
                summary = project['summary']
                summary_html = f'''
<section class="section-card" data-aos="fade-up">
  <h2>App Kurzprofil</h2>
  <div class="summary-grid">
    <div class="summary-card"><strong>Zeilen</strong><div>{summary['lines']}</div></div>
    <div class="summary-card"><strong>Funktionen</strong><div>{summary['functions']}</div></div>
    <div class="summary-card"><strong>Klassen</strong><div>{summary['classes']}</div></div>
    <div class="summary-card"><strong>Widgets</strong><div>{', '.join(summary['widgets']) or '—'}</div></div>
    <div class="summary-card"><strong>Imports</strong><div>{', '.join(summary['imports']) or '—'}</div></div>
    <div class="summary-card"><strong>Quellen/APIs</strong><div>{', '.join(summary['data_sources']) or '—'}</div></div>
  </div>
</section>
'''

            main_html = f'''
<section class="hero" data-aos="fade-up">
  <h1>{html.escape(project['title'])}</h1>
  <div class="meta">
    <span class="badge">Level: {html.escape(level_title)}</span>
    <span class="badge">Projektpfad: {html.escape(str(project_base.relative_to(BASE)))}</span>
  </div>
</section>

<section class="section-card" data-aos="fade-up" data-tabs>
  <div class="tabs">
    <button class="tab-btn">TODO.md</button>
    <button class="tab-btn">TIPPS.md</button>
  </div>
  <div class="tab-panel md">{todo_html}</div>
  <div class="tab-panel md">{tipps_html}</div>
</section>

{summary_html}

<section class="section-card" data-aos="fade-up">
  <h2>Steps</h2>
  <div class="step-grid">
    {step_cards}
    <a class="box" href="{rel_link(project_page, app_page)}"><strong>App</strong><p>Finale Streamlit-App ansehen.</p></a>
  </div>
</section>
'''

            project_page.write_text(render_page(project['title'], nav_html, main_html, root_prefix), encoding='utf-8')

            nav_html = build_nav(structure, project['paths']['app'], app_page)
            last_step = project['steps'][-1]['path'] if project['steps'] else None
            last_label = None
            if project['steps']:
                last_step_info = project['steps'][-1]
                last_label = f"Step {last_step_info['num']}"
                if last_step_info['desc']:
                    last_label += f": {last_step_info['desc'].splitlines()[0][:28]}"
            app_nav = '<div class="nav-inline">'
            app_nav += f'<a href="{rel_link(app_page, project_page)}">Zurueck zum Projekt</a>'
            if last_step:
                label_text = last_label or 'Letzter Step'
                app_nav += f'<a href="{rel_link(app_page, SITE / last_step)}">{html.escape(label_text)}</a>'
            app_nav += '</div>'

            app_html = f'''
<section class="hero" data-aos="fade-up">
  <h1>{html.escape(project['title'])} — App</h1>
  <div class="meta">
    <span class="badge">Level: {html.escape(level_title)}</span>
    <span class="badge">Datei: app/app.py</span>
  </div>
  {app_nav}
</section>

<section class="section-card" data-aos="fade-up">
  <h2>app.py</h2>
  <pre class="code-block"><code>{html.escape(project['app_text'] or 'Keine app.py gefunden.')}</code></pre>
</section>
'''

            app_page.write_text(render_page(project['title'] + ' App', nav_html, app_html, root_prefix), encoding='utf-8')

            for idx, step in enumerate(project['steps']):
                step_file = project_base / f'step-{step["num"]:02d}.html'
                step_title = f"{project['title']} — Step {step['num']}"
                desc_html = md_to_html(step['desc'] or 'Beschreibung fehlt.')
                tipps_html = md_to_html(step['tipps'] or 'Keine Tipps fuer diesen Schritt gefunden.')

                prev_path = project['steps'][idx - 1]['path'] if idx > 0 else project['paths']['project']
                next_path = project['steps'][idx + 1]['path'] if idx + 1 < len(project['steps']) else project['paths']['app']
                prev_label = 'Projekt' if idx == 0 else f"Step {project['steps'][idx - 1]['num']}"
                next_label = 'App' if idx + 1 >= len(project['steps']) else f"Step {project['steps'][idx + 1]['num']}"
                if idx > 0 and project['steps'][idx - 1]['desc']:
                    prev_label += f": {project['steps'][idx - 1]['desc'].splitlines()[0][:28]}"
                if idx + 1 < len(project['steps']) and project['steps'][idx + 1]['desc']:
                    next_label += f": {project['steps'][idx + 1]['desc'].splitlines()[0][:28]}"

                nav_inline = f'''
<div class="nav-inline">
  <a href="{rel_link(step_file, SITE / prev_path)}">Zurueck zu {html.escape(prev_label)}</a>
  <a href="{rel_link(step_file, SITE / next_path)}">Weiter zu {html.escape(next_label)}</a>
</div>
'''

                step_html = f'''
<section class="hero" data-aos="fade-up">
  <h1>{html.escape(step_title)}</h1>
  <div class="meta">
    <span class="badge">Level: {html.escape(level_title)}</span>
    <span class="badge">Projekt: {html.escape(project['title'])}</span>
  </div>
  {nav_inline}
</section>

<section class="section-card" data-aos="fade-up">
  <h2>Was zu tun ist</h2>
  <div class="md">{desc_html}</div>
</section>

<section class="section-card" data-aos="fade-up">
  <h2>Tipps & Code</h2>
  <div class="md">{tipps_html}</div>
</section>
'''
                nav_html = build_nav(structure, step['path'], step_file)
                step_file.write_text(render_page(step_title, nav_html, step_html, root_prefix), encoding='utf-8')

    index_path = SITE / 'index.html'
    root_prefix = rel_link(index_path, SITE / 'assets' / 'styles.css').replace('assets/styles.css', '')

    nav_html = build_nav(structure, '', index_path)

    level_cards = []
    for level_key, level_title, projects in structure:
        items = ''.join([
            f'<li><a href="{level_key}/{p["slug"]}/index.html">{html.escape(p["title"])}</a></li>'
            for p in projects
        ])
        level_cards.append(f'''
    <div class="section-card" data-aos="fade-up">
      <h2>{html.escape(level_title)}</h2>
      <ul>{items}</ul>
    </div>
    ''')

    main_html = f'''
<section class="hero" data-aos="fade-up">
  <h1>Streamlit Projects Explorer</h1>
  <p>Waehle ein Projekt links in der Navigation aus oder starte hier im Level-Ueberblick.</p>
</section>
{''.join(level_cards)}
'''

    index_path.write_text(render_page('Streamlit Projects Explorer', nav_html, main_html, root_prefix), encoding='utf-8')


if __name__ == '__main__':
    main()
