#!/usr/bin/env python3
"""
μFIFA World Cup 2026 - Profile Validator
-----------------------------------------
Checks that a profile file in /profile/ meets all required structure rules.
Used by both the pre-commit hook (locally) and GitHub Actions CI (on PR).

Exit codes:
  0 - all checks passed
  1 - one or more checks failed
"""

import sys
import os
import re

# ── Colour helpers (disabled in CI if NO_COLOR is set) ──────────────────────
USE_COLOR = (os.environ.get("NO_COLOR") is None and sys.stdout.isatty()) or os.environ.get("GITHUB_ACTIONS") == "true"

def red(s):    return f"\033[31m{s}\033[0m" if USE_COLOR else s
def green(s):  return f"\033[32m{s}\033[0m" if USE_COLOR else s
def yellow(s): return f"\033[33m{s}\033[0m" if USE_COLOR else s
def bold(s):   return f"\033[1m{s}\033[0m"  if USE_COLOR else s

# ── Required top-level sections (## headings) ──────────────────────────────
REQUIRED_TOP_SECTIONS = [
    "## FIFA World Cup Corner",
    "## Portfolio Highlights",
]

# ── Required sections (must appear as #### headings) ────────────────────────
REQUIRED_SECTIONS = [
    "#### My Nation & Why:",
    "#### Supporting Team in the Real World Cup 2026:",
    "#### All-Time Favourite Player:",
    "#### Best Player Right Now:",
    "#### Past World Cup Memories:",
    "#### 2026 Predictions:",
    "#### μFIFA World Cup 2026 - Tournament Goals:",
    "#### History of Open Source and Collaborative Contributions:",
    "#### History of Community Engagement:",
    "#### Domain Profiles:",
    "#### Tools, Workflows & Automations:",
    "#### Public Portfolio & Recognition:",
    "#### Education and Proof of Work:",
    "#### History of Leadership:",
    "#### Networking:",
    "#### Career Plan:",
    "#### Profile Card:",
]

# ── Rules ────────────────────────────────────────────────────────────────────

def check_filename(path):
    """File must be named <something>@mulearn.md"""
    name = os.path.basename(path)
    if not re.match(r'^.+@mulearn\.md$', name, re.IGNORECASE):
        return False, f"File must be named <your-muid>@mulearn.md - got '{name}'"
    return True, f"Filename is valid: {name}"


def check_header(lines):
    """First line must be # Name (...), second ### line must contain 'FIFA Nation:'"""
    if not lines:
        return False, "File is empty"
    if not lines[0].startswith("# "):
        return False, f"First line must start with '# Full Name ...' - got: {lines[0][:60]!r}"
    
    header_line = next((l for l in lines[:5] if l.startswith("### ") and "FIFA Nation:" in l), None)
    if not header_line:
        return False, "Missing '### Squad Domain: ... | FIFA Nation: ...' line in the first 5 lines"
    
    squad_domain_keywords = ["Coder", "Maker", "Designer", "Strategist"]
    if not any(g in header_line for g in squad_domain_keywords):
        return False, f"Squad Domain line must include at least one of: {', '.join(squad_domain_keywords)}"
    
    return True, "Header and Squad Domain/Nation line found"


def check_about_me(content):
    """About Me blockquote must exist and be at least 200 characters"""
    # Capture all consecutive > lines after ### About Me
    about_match = re.search(r'### About Me\s*\n+((?:>.*\n?)+)', content)
    if not about_match:
        return False, "'### About Me' section with a blockquote (>) is missing"
    
    # Strip leading > from each line and join
    raw_block = about_match.group(1)
    quote_text = re.sub(r'^>\s?', '', raw_block, flags=re.MULTILINE).strip()
    
    if len(quote_text) < 200:
        return False, f"About Me must be at least 200 characters - currently {len(quote_text)} characters"
    
    return True, f"About Me is {len(quote_text)} characters ✓"


def check_top_sections(content):
    """Top-level ## section headings (FIFA World Cup Corner, Portfolio Highlights) must be present"""
    errors = []
    for section in REQUIRED_TOP_SECTIONS:
        # Match flexibly: allow optional emoji or extra characters between ## and the heading text
        # e.g. "## ⚽ FIFA World Cup Corner" and "## FIFA World Cup Corner" both match
        heading_text = re.escape(section.lstrip('## ').strip())
        pattern = re.compile(
            r'^##\s+.*?' + heading_text,
            re.MULTILINE
        )
        if not pattern.search(content):
            errors.append(f"Missing top-level section: {section}")
    if errors:
        return False, errors
    return True, "Top-level sections present"


def check_sections(content):
    """All required #### sections must be present"""
    errors = []
    for section in REQUIRED_SECTIONS:
        if section not in content:
            errors.append(f"Missing section: {section}")
    
    if errors:
        return False, errors
    return True, "All required sections present"


def check_sections_not_empty(content, lines):
    """Each required section must have at least one non-empty, non-placeholder line after it"""
    warnings = []
    
    placeholder_patterns = [
        r'^\s*-\s*$',                          # bare dash
        r'^\s*-\s*\.\.\.\s*$',                 # - ...
        r'^\s*-\s*N/A\s*$',                    # - N/A
        r'^\s*-\s*TBD\s*$',                    # - TBD
        r'^\s*-\s*write about your self',       # copy-pasted from old template (variant)
        r'^\s*-\s*write about yourself',          # copy-pasted from old template
        r'^\s*>\s*Who are you',                 # un-edited About Me prompt
    ]

    section_pattern = re.compile(r'^(#{1,4} .+)$', re.MULTILINE)
    section_positions = [(m.start(), m.group(1)) for m in section_pattern.finditer(content)]

    for i, (pos, heading) in enumerate(section_positions):
        if heading not in REQUIRED_SECTIONS:
            continue
        # Content between this heading and the next
        end = section_positions[i + 1][0] if i + 1 < len(section_positions) else len(content)
        body = content[pos + len(heading):end].strip()

        if not body:
            warnings.append(f"Section appears empty: {heading}")
            continue

        # Check if body is only placeholder lines
        body_lines = [l for l in body.splitlines() if l.strip() and not l.strip().startswith("<!--")]
        non_placeholder = [
            l for l in body_lines
            if not any(re.match(p, l, re.IGNORECASE) for p in placeholder_patterns)
            and not l.strip().startswith("*If you're just starting")
            and not l.strip().startswith("- *If you're just starting")
        ]

        if not non_placeholder:
            warnings.append(f"Section looks unfilled (only placeholder text): {heading}")

    if warnings:
        return "warn", warnings
    return True, "All sections have content"


def check_profile_card(content):
    """Profile card img src must be updated from the placeholder"""
    placeholder = "yourname@mulearn"
    img_match = re.search(r'src="https://mulearn\.org/embed/rank/([^"]+)"', content)
    if not img_match:
        return False, "Profile Card img tag is missing or malformed - check the Profile Card section"
    if placeholder in img_match.group(1):
        return False, "Profile Card still has the placeholder URL - replace 'yourname@mulearn' with your actual MUID"
    return True, f"Profile Card embed found: {img_match.group(1)}"


def check_mulearn_id_consistency(path, content):
    """The MUID in the filename should match the one in the profile card src"""
    filename_muid = os.path.basename(path).replace(".md", "").replace(".MD", "")
    img_match = re.search(r'src="https://mulearn\.org/embed/rank/([^"]+)"', content)
    if not img_match:
        return True, "Skipped MUID consistency check (no img found)"
    
    card_muid = img_match.group(1)
    if filename_muid.lower() != card_muid.lower():
        return False, (
            f"MUID mismatch: filename is '{filename_muid}' "
            f"but profile card uses '{card_muid}' - they must match"
        )
    return True, f"MUID is consistent: {filename_muid}"


# --- NEW CHECKS FOR PHASE 1 ---
def check_urls(content):
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
    for url in urls:
        if "localhost" in url or "127.0.0.1" in url:
            return False, f"Found local URL which is not allowed: {url}"
    return True, "URLs are valid."

def check_emails(content):
    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)
    for email in emails:
        if email.endswith("@example.com"):
            return False, f"Placeholder email found: {email}"
    return True, "Emails are valid."

# Add to runner:
# We need to insert these checks into the checks list in validate()

def check_image_dimensions(content):
    # Check for img tags and warn if height/width is missing or too large
    imgs = re.findall(r'<img[^>]+>', content)
    for img in imgs:
        width = re.search(r'width=["\'](\d+)["\']', img)
        height = re.search(r'height=["\'](\d+)["\']', img)
        if width and int(width.group(1)) > 800:
            return False, "Image width must not exceed 800px"
        if height and int(height.group(1)) > 800:
            return False, "Image height must not exceed 800px"
    return True, "Image dimensions are valid."
# ── Runner ───────────────────────────────────────────────────────────────────

def validate(path):
    print(bold(f"\nμFIFA Profile Validator → {os.path.basename(path)}"))
    print("─" * 55)

    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(red(f"✗ File not found: {path}"))
        return False

    lines = content.splitlines()
    passed = True
    has_warnings = False

    checks = [
        ("Filename",             lambda: check_filename(path)),
        ("Header",               lambda: check_header(lines)),
        ("About Me length",      lambda: check_about_me(content)),
        ("Top-level sections",   lambda: check_top_sections(content)),
        ("Required sections",    lambda: check_sections(content)),
        ("Section content",      lambda: check_sections_not_empty(content, lines)),
        ("Profile Card",         lambda: check_profile_card(content)),
        ("MUID consistency",     lambda: check_mulearn_id_consistency(path, content)),
        ("URL Formats",          lambda: check_urls(content)),
        ("Email Formats",        lambda: check_emails(content)),
        ("Image Dimensions",     lambda: check_image_dimensions(content)),
    ]

    for label, fn in checks:
        result = fn()
        status, detail = result[0], result[1]

        if status is True:
            print(green(f"  ✓ {label}"))
        elif status == "warn":
            has_warnings = True
            print(yellow(f"  ⚠ {label}"))
            items = detail if isinstance(detail, list) else [detail]
            for item in items:
                print(yellow(f"      → {item}"))
        else:
            passed = False
            print(red(f"  ✗ {label}"))
            items = detail if isinstance(detail, list) else [detail]
            for item in items:
                print(red(f"      → {item}"))

    print("─" * 55)
    if passed and not has_warnings:
        print(green("  All checks passed. You're on the pitch! ⚽\n"))
    elif passed and has_warnings:
        print(yellow("  Passed with warnings - fill in the flagged sections before your PR.\n"))
    else:
        print(red("  Validation failed. Fix the errors above before submitting your PR.\n"))

    return passed


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python3 {sys.argv[0]} <profile_file.md> [<file2.md> ...]")
        sys.exit(1)

    all_passed = True
    for filepath in sys.argv[1:]:
        if not validate(filepath):
            all_passed = False

    sys.exit(0 if all_passed else 1)

