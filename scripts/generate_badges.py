#!/usr/bin/env python3
import json
import os
import argparse
import re

def generate_svg(name, rank, domain, output_dir):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="200" height="50">
  <rect width="200" height="50" fill="#333" rx="5"/>
  <text x="10" y="20" fill="#fff" font-family="Arial" font-size="14">{name}</text>
  <text x="10" y="40" fill="#f1c40f" font-family="Arial" font-size="12">Rank: {rank} | {domain}</text>
</svg>"""
    os.makedirs(output_dir, exist_ok=True)
    filename = f"{name.lower().replace(' ', '-')}-badge.svg"
    with open(os.path.join(output_dir, filename), "w") as f:
        f.write(svg)
    print(f"Generated badge for {name}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    with open(args.input, "r") as f:
        content = f.read()

    # Parse individual rankings from markdown
    # Format: | 1 | Sachin | Coder | India | 1000 | [Profile](...) |
    match = re.search(r'## Individual Rankings.*?(?=\n##|$)', content, re.DOTALL)
    if match:
        table = match.group(0)
        lines = table.split("\n")
        for line in lines:
            if line.startswith("|") and not "Rank" in line and not "---" in line:
                parts = [p.strip() for p in line.split("|")]
                if len(parts) >= 6 and parts[1].isdigit():
                    rank = parts[1]
                    name = parts[2]
                    domain = parts[3]
                    generate_svg(name, rank, domain, args.output)
                    
    # Also generate leaderboard.json
    data = {"leaderboard": []}
    if match:
        table = match.group(0)
        lines = table.split("\n")
        for line in lines:
            if line.startswith("|") and not "Rank" in line and not "---" in line:
                parts = [p.strip() for p in line.split("|")]
                if len(parts) >= 6 and parts[1].isdigit():
                    rank = parts[1]
                    name = parts[2]
                    domain = parts[3]
                    nation = parts[4]
                    points = parts[5]
                    data["leaderboard"].append({
                        "rank": rank,
                        "name": name,
                        "domain": domain,
                        "nation": nation,
                        "points": points
                    })
    with open(os.path.join(args.output, "leaderboard.json"), "w") as f:
        json.dump(data, f, indent=2)
    print("Generated leaderboard.json")

if __name__ == "__main__":
    main()
