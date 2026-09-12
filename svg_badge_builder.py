#!/usr/bin/env python3
"""
svg-badge-builder: Generate standalone SVG badges locally.
"""
import argparse, sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception: pass

__version__ = "1.0.0"

COLOR_PRESETS = {
    "green": "#2ea44f", "blue": "#0969da", "red": "#cf222e",
    "yellow": "#d4a72c", "purple": "#8250df", "dark": "#24292f"
}

def generate_svg_badge(label, message, color="#2ea44f"):
    c = COLOR_PRESETS.get(color, color)
    l_w = max(40, len(label) * 7 + 14)
    m_w = max(40, len(message) * 7 + 14)
    total_w = l_w + m_w
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{total_w}" height="20" role="img" aria-label="{label}: {message}">
  <linearGradient id="s" x2="0" y2="100%"><stop offset="0" stop-color="#bbb" stop-opacity=".1"/><stop offset="1" stop-opacity=".1"/></linearGradient>
  <clipPath id="r"><rect width="{total_w}" height="20" rx="3" fill="#fff"/></clipPath>
  <g clip-path="url(#r)">
    <rect width="{l_w}" height="20" fill="#555"/>
    <rect x="{l_w}" width="{m_w}" height="20" fill="{c}"/>
    <rect width="{total_w}" height="20" fill="url(#s)"/>
  </g>
  <g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" text-rendering="geometricPrecision" font-size="110">
    <text x="{l_w*5}" y="140" transform="scale(.1)" fill="#fff">{label}</text>
    <text x="{(l_w + m_w/2)*10}" y="140" transform="scale(.1)" fill="#fff" font-weight="bold">{message}</text>
  </g>
</svg>"""
    return svg

def main():
    parser = argparse.ArgumentParser(description="🏷️ svg-badge-builder: Offline SVG Badge Generator")
    parser.add_argument("--label", default="build", help="Left side label")
    parser.add_argument("--message", default="passing", help="Right side message")
    parser.add_argument("--color", default="green", help="Right side color (green, blue, red, purple, hex)")
    parser.add_argument("--output", default="badge.svg", help="Output SVG filepath")
    args = parser.parse_args()
    
    svg = generate_svg_badge(args.label, args.message, args.color)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"✅ SVG badge generated successfully: {args.output} [{args.label} | {args.message}]")

if __name__ == "__main__":
    main()
