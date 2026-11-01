"""Generate the profile's stat and project cards as static SVGs from the GitHub API.

No third-party card services: the output only depends on GitHub itself.
Auth: GH_TOKEN / GITHUB_TOKEN env var, else `gh auth token`.
"""
import json
import os
import subprocess
import textwrap
import urllib.request
from pathlib import Path

USER = "manikanta-varaganti"
ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / "assets"

FEATURED = {
    "detection-of-motorcyclists-without-helmet": "Computer vision: detects motorcyclists riding without helmets.",
    "branch-predictor": "Branch predictor simulator (Smith N-bit, Bimodal, GShare, Hybrid) in Python 3.",
    "cache-simulator": "Generic cache simulator for any level of the memory hierarchy, in Python.",
    "internship-portal": "Web portal for managing internships.",
}

BG, PANEL, BORDER = "#1a1b26", "#16161e", "#292e42"
FG, BLUE, PURPLE, GREEN, ORANGE, RED, CYAN, COMMENT, YELLOW = (
    "#c0caf5", "#7aa2f7", "#bb9af7", "#9ece6a", "#ff9e64", "#f7768e", "#7dcfff", "#565f89", "#e0af68")
FONT = "JetBrains Mono, Fira Code, SF Mono, Menlo, Consolas, Courier New, monospace"
PALETTE = [BLUE, PURPLE, GREEN, ORANGE, CYAN, RED, YELLOW]


def token():
    t = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if t:
        return t
    return subprocess.check_output(["gh", "auth", "token"], text=True).strip()


TOKEN = token()


def api(path, data=None):
    url = path if path.startswith("http") else f"https://api.github.com{path}"
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json",
        "User-Agent": "profile-cards"}, data=data)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def esc(t):
    return str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def card(w, h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" font-family="{FONT}">'
            f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="10" fill="{PANEL}" stroke="{BORDER}" stroke-width="1.5"/>'
            f'{body}</svg>')


def stats_svg(stats):
    rows = [("stars earned", stats["stars"]), ("public repos", stats["repos"]),
            ("followers", stats["followers"]), ("on github since", stats["since"])]
    out = [f'<text x="26" y="36" font-size="14" fill="{COMMENT}">$ gh stats {USER}</text>']
    for i, (label, val) in enumerate(rows):
        y = 76 + i * 28
        out.append(f'<text x="26" y="{y}" font-size="15" fill="{FG}">{esc(label)}</text>')
        out.append(f'<line x1="{26 + len(label) * 9.2 + 10:.0f}" y1="{y-5}" x2="{455 - len(str(val)) * 10}" y2="{y-5}" stroke="{COMMENT}" stroke-dasharray="2 5"/>')
        out.append(f'<text x="469" y="{y}" font-size="17" font-weight="bold" text-anchor="end" fill="{CYAN}">{esc(val)}</text>')
    return card(495, 195, "".join(out))


def langs_svg(langs):
    total = sum(langs.values()) or 1
    top = sorted(langs.items(), key=lambda kv: -kv[1])[:6]
    shown = sum(v for _, v in top)
    out = [f'<text x="26" y="36" font-size="14" fill="{COMMENT}">$ gh langs --top {len(top)}</text>']
    x, bar_w = 26.0, 443.0
    out.append(f'<clipPath id="bar"><rect x="26" y="54" width="{bar_w:.0f}" height="12" rx="6"/></clipPath><g clip-path="url(#bar)">')
    for i, (_, v) in enumerate(top):
        w = bar_w * v / shown
        out.append(f'<rect x="{x:.1f}" y="54" width="{w + 0.5:.1f}" height="12" fill="{PALETTE[i % len(PALETTE)]}"/>')
        x += w
    out.append("</g>")
    for i, (name, v) in enumerate(top):
        col, row = i % 2, i // 2
        cx, cy = 26 + col * 225, 98 + row * 28
        out.append(f'<circle cx="{cx + 5}" cy="{cy - 5}" r="5" fill="{PALETTE[i % len(PALETTE)]}"/>')
        out.append(f'<text x="{cx + 18}" y="{cy}" font-size="14" fill="{FG}">{esc(name)}</text>')
        out.append(f'<text x="{cx + 205}" y="{cy}" font-size="14" text-anchor="end" fill="{COMMENT}">{100 * v / total:.1f}%</text>')
    out.append(f'<text x="26" y="184" font-size="11" fill="{COMMENT}"># by bytes, public non-fork repos</text>')
    return card(495, 195, "".join(out))


def project_svg(name, desc, lang, stars):
    lines = textwrap.wrap(desc, 56)[:2] or [""]
    out = [f'<text x="24" y="38" font-size="16" font-weight="bold" fill="{BLUE}">▸ {esc(name if len(name) <= 38 else name[:37] + "…")}/</text>']
    for i, ln in enumerate(lines):
        out.append(f'<text x="24" y="{66 + i * 20}" font-size="13" fill="{FG}">{esc(ln)}</text>')
    out.append(f'<circle cx="29" cy="115" r="5" fill="{GREEN}"/><text x="42" y="120" font-size="13" fill="{COMMENT}">{esc(lang or "n/a")}</text>')
    out.append(f'<text x="516" y="120" font-size="13" text-anchor="end" fill="{YELLOW}">★ {stars}</text>')
    return card(540, 136, "".join(out))


def main():
    user = api(f"/users/{USER}")
    repos = [r for r in api(f"/users/{USER}/repos?per_page=100&type=owner") if not r["fork"]]
    by_name = {r["name"]: r for r in repos}
    langs = {}
    for r in repos:
        for lang, n in api(f"/repos/{USER}/{r['name']}/languages").items():
            langs[lang] = langs.get(lang, 0) + n
    stats = {"stars": sum(r["stargazers_count"] for r in repos), "repos": user["public_repos"],
             "followers": user["followers"], "since": user["created_at"][:4]}
    (ASSETS / "stats.svg").write_text(stats_svg(stats))
    (ASSETS / "langs.svg").write_text(langs_svg(langs))
    (ASSETS / "projects").mkdir(exist_ok=True)
    for name, blurb in FEATURED.items():
        r = by_name.get(name)
        if r is None:
            print(f"skip {name}: not found")
            continue
        (ASSETS / "projects" / f"{name}.svg").write_text(
            project_svg(name, r.get("description") or blurb, r.get("language"), r["stargazers_count"]))
    print("stats:", stats, "| top langs:", sorted(langs, key=langs.get, reverse=True)[:6])


if __name__ == "__main__":
    main()
