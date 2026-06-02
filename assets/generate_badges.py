#!/usr/bin/env python3
"""
Generate animated SVG badges for Pool 1337
Placed in: assets/generate_badges.py
Output to: assets/badges/*.svg
"""
import os, json, glob

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BADGES_DIR = os.path.join(REPO_ROOT, "assets", "badges")
DAYS_DIR = os.path.join(REPO_ROOT, "days")

os.makedirs(BADGES_DIR, exist_ok=True)

modules = [
    {"id": "C00", "focus": "write() · loops · basic output", "ex": 9},
    {"id": "C01", "focus": "pointers · arrays · arithmetic", "ex": 9},
    {"id": "C02", "focus": "strings · strcpy · strlen", "ex": 13},
    {"id": "C03", "focus": "strcmp · strcat · comparison", "ex": 6},
    {"id": "C04", "focus": "base conversion · atoi · itoa", "ex": 6},
    {"id": "C05", "focus": "recursion · fibonacci · primes", "ex": 9},
    {"id": "C06", "focus": "argc / argv · program args", "ex": 4},
    {"id": "C07", "focus": "malloc · free · heap memory", "ex": 6},
    {"id": "C08", "focus": "structs · headers · guards", "ex": 0},
    {"id": "C09", "focus": "static libs · ar · Makefile", "ex": 0},
    {"id": "C10", "focus": "file I/O", "ex": 0},
    {"id": "C11", "focus": "function pointers", "ex": 0},
    {"id": "C12", "focus": "linked lists", "ex": 0},
    {"id": "C13", "focus": "binary trees", "ex": 0},
]

def scan_module(mod_id):
    """Scan days/Mod/ for .c files and count lines"""
    mod_path = os.path.join(DAYS_DIR, mod_id)
    files = []
    total_lines = 0
    if not os.path.isdir(mod_path):
        return files, 0
    for ex in sorted(os.listdir(mod_path)):
        ex_path = os.path.join(mod_path, ex)
        if not os.path.isdir(ex_path):
            continue
        for f in sorted(os.listdir(ex_path)):
            if f.endswith(".c"):
                filepath = os.path.join(ex_path, f)
                try:
                    with open(filepath, "r", encoding="utf-8", errors="ignore") as fh:
                        lines = len(fh.readlines())
                except:
                    lines = 0
                total_lines += lines
                files.append({"name": f"{ex}/{f}", "lines": lines})
    return files, total_lines

def generate_module_svg(mod, files, lines_count):
    done = len(files) > 0
    ex_done = len(files)
    ex_total = mod["ex"]

    if done:
        fill = "#3fb950"
        stroke = "#238636"
        badge = "DONE"
        icon = "✅"
        progress_pct = 100
    else:
        fill = "#d29922"
        stroke = "#9e6a03"
        badge = "PLANNED"
        icon = "🟡"
        progress_pct = 0

    bar_width = int(120 * progress_pct / 100)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="340" height="64" viewBox="0 0 340 64">
  <defs>
    <filter id="glow-{mod['id']}">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <linearGradient id="grad-{mod['id']}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:{fill};stop-opacity:0.3" />
      <stop offset="100%" style="stop-color:{fill};stop-opacity:0.05" />
    </linearGradient>
  </defs>
  <style>
    .bg{{fill:#161b22;stroke:{stroke};stroke-width:1;}}
    .title{{fill:#c9d1d9;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;font-size:13px;font-weight:700;}}
    .meta{{fill:#8b949e;font-family:monospace;font-size:10px;}}
    .badge-bg{{fill:{fill};opacity:0.15;rx:10;}}
    .badge-txt{{fill:{fill};font-family:sans-serif;font-size:9px;font-weight:700;}}
    .bar-bg{{fill:#21262d;rx:3;}}
    .bar-fill{{fill:{fill};rx:3;filter:url(#glow-{mod['id']});}}
  </style>
  <rect class="bg" x="0" y="0" width="340" height="64" rx="12" />
  <rect fill="url(#grad-{mod['id']})" x="1" y="1" width="338" height="62" rx="11" opacity="0.5" />

  <text x="14" y="22" class="title">{icon} {mod['id']}</text>
  <text x="14" y="40" class="meta">{ex_done}/{ex_total} ex · {lines_count} lines</text>

  <rect class="badge-bg" x="260" y="10" width="70" height="22" rx="11" />
  <text x="295" y="25" text-anchor="middle" class="badge-txt">{badge}</text>

  <rect class="bar-bg" x="14" y="50" width="120" height="5" />
  <rect class="bar-fill" x="14" y="50" width="0" height="5">
    <animate attributeName="width" from="0" to="{bar_width}" dur="0.8s" fill="freeze" />
  </rect>
  <text x="140" y="55" class="meta">{progress_pct}%</text>
</svg>"""
    return svg

def generate_overall_svg(done_count, total_count, total_files, total_lines):
    pct = int(done_count / total_count * 100)
    bar_width = int(280 * pct / 100)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="420" height="140" viewBox="0 0 420 140">
  <defs>
    <linearGradient id="barGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#58a6ff">
        <animate attributeName="stop-color" values="#58a6ff;#3fb950;#58a6ff" dur="4s" repeatCount="indefinite" />
      </stop>
      <stop offset="100%" style="stop-color:#3fb950">
        <animate attributeName="stop-color" values="#3fb950;#58a6ff;#3fb950" dur="4s" repeatCount="indefinite" />
      </stop>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <style>
    .bg{{fill:#0d1117;stroke:#30363d;stroke-width:1;}}
    .title{{fill:#8b949e;font-family:-apple-system,sans-serif;font-size:15px;font-weight:600;}}
    .big{{fill:#fff;font-family:'Segoe UI',monospace;font-size:42px;font-weight:800;}}
    .sub{{fill:#58a6ff;font-family:monospace;font-size:14px;font-weight:600;}}
    .stat{{fill:#8b949e;font-family:monospace;font-size:12px;}}
    .bar-bg{{fill:#161b22;rx:6;}}
    .bar-fill{{fill:url(#barGrad);rx:6;filter:url(#glow);}}
  </style>
  <rect class="bg" x="0" y="0" width="420" height="140" rx="16" />

  <text x="20" y="32" class="title">🏊 POOL 1337 — LIVE PROGRESS</text>

  <text x="20" y="85" class="big">{pct}%</text>
  <text x="20" y="110" class="sub">{done_count}/{total_count} MODULES</text>

  <text x="220" y="85" class="stat">📁 {total_files} .c files</text>
  <text x="220" y="105" class="stat">📝 ~{total_lines} lines</text>

  <rect class="bar-bg" x="20" y="120" width="280" height="10" />
  <rect class="bar-fill" x="20" y="120" width="0" height="10">
    <animate attributeName="width" from="0" to="{bar_width}" dur="1.2s" fill="freeze" calcMode="spline" keySplines="0.4 0 0.2 1" />
  </rect>

  <circle cx="390" cy="28" r="4" fill="#3fb950">
    <animate attributeName="r" values="4;6;4" dur="2s" repeatCount="indefinite" />
    <animate attributeName="opacity" values="1;0.5;1" dur="2s" repeatCount="indefinite" />
  </circle>
  <text x="400" y="32" font-size="10" fill="#3fb950" font-family="sans-serif" font-weight="700">LIVE</text>
</svg>"""
    return svg

def generate_exercises_svg(total_ex, solved_ex):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="200" height="56" viewBox="0 0 200 56">
  <style>
    .bg{{fill:#161b22;stroke:#30363d;}}
    .num{{fill:#58a6ff;font-family:'Segoe UI',monospace;font-size:26px;font-weight:700;}}
    .label{{fill:#8b949e;font-family:sans-serif;font-size:11px;}}
  </style>
  <rect class="bg" x="0" y="0" width="200" height="56" rx="10" />
  <text x="16" y="36" class="num">{solved_ex}</text>
  <text x="60" y="26" class="label">EXERCISES</text>
  <text x="60" y="42" class="label">SOLVED</text>
  <circle cx="175" cy="28" r="5" fill="#3fb950">
    <animate attributeName="r" values="5;7;5" dur="2s" repeatCount="indefinite" />
  </circle>
</svg>"""
    return svg

def generate_norm_svg():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" width="160" height="36" viewBox="0 0 160 36">
  <style>
    .bg{fill:#161b22;stroke:#238636;stroke-width:1;}
    .dot{fill:#3fb950;}
    .txt{fill:#3fb950;font-family:sans-serif;font-size:11px;font-weight:700;}
  </style>
  <rect class="bg" x="0" y="0" width="160" height="36" rx="8" />
  <circle class="dot" cx="18" cy="18" r="5">
    <animate attributeName="opacity" values="1;0.4;1" dur="1.5s" repeatCount="indefinite" />
  </circle>
  <text x="34" y="22" class="txt">NORMINETTE OK</text>
</svg>"""
    return svg

# Main execution
total_files = 0
total_lines = 0
done_modules = 0
solved_exercises = 0

for mod in modules:
    files, lines = scan_module(mod["id"])
    total_files += len(files)
    total_lines += lines
    solved_exercises += len(files)
    if len(files) > 0:
        done_modules += 1

    svg = generate_module_svg(mod, files, lines)
    with open(os.path.join(BADGES_DIR, f"{mod['id']}.svg"), "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"✅ {mod['id']}: {len(files)} files, {lines} lines")

# Overall
overall = generate_overall_svg(done_modules, len(modules), total_files, total_lines)
with open(os.path.join(BADGES_DIR, "overall.svg"), "w", encoding="utf-8") as f:
    f.write(overall)

# Exercises
ex_svg = generate_exercises_svg(62, solved_exercises)
with open(os.path.join(BADGES_DIR, "exercises.svg"), "w", encoding="utf-8") as f:
    f.write(ex_svg)

# Norm
norm_svg = generate_norm_svg()
with open(os.path.join(BADGES_DIR, "norm.svg"), "w", encoding="utf-8") as f:
    f.write(norm_svg)

# Stats JSON for shields.io fallback
stats = {
    "schemaVersion": 1,
    "label": "Pool 1337",
    "message": f"{done_modules}/{len(modules)} modules",
    "color": "blue" if done_modules < len(modules) else "green",
    "cacheSeconds": 3600
}
with open(os.path.join(REPO_ROOT, "stats.json"), "w") as f:
    json.dump(stats, f, indent=2)

print(f"\n🎨 Generated {len(modules)+3} badges in assets/badges/")
print(f"📊 {done_modules}/{len(modules)} modules · {total_files} files · ~{total_lines} lines")
