#!/usr/bin/env python3
import json
import os
import argparse
from jinja2 import Environment, FileSystemLoader
import pdfkit
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15

def generate_key_pair(output_dir):
    key = RSA.generate(2048)
    public_key = key.publickey().export_key()

    with open(os.path.join(output_dir, "public.pem"), "wb") as f:
        f.write(public_key)
    return key

def sign_pdf(pdf_path, key):
    with open(pdf_path, "rb") as f:
        data = f.read()
    
    h = SHA256.new(data)
    signature = pkcs1_15.new(key).sign(h)
    
    with open(pdf_path + ".sig", "wb") as f:
        f.write(signature)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to leaderboard.json")
    parser.add_argument("--output", required=True, help="Directory to save PDFs")
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)
    
    with open(args.input, "r") as f:
        data = json.load(f)

    env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")))
    template = env.get_template("certificate.html")
    
    key = generate_key_pair(args.output)
    
    for player in data.get("leaderboard", []):
        html_content = template.render(
            name=player["name"],
            domain=player["domain"],
            rank=player["rank"],
            nation=player["nation"],
            points=player["points"]
        )
        
        safe_name = ''.join(ch if ch.isalnum() else '-' for ch in player['name'].lower()).strip('-') or 'player'
        pdf_filename = f"{safe_name}-certificate.pdf"
        pdf_path = os.path.join(args.output, pdf_filename)
        
        options = {
            'page-size': 'A4',
            'orientation': 'Landscape',
            'margin-top': '0mm',
            'margin-right': '0mm',
            'margin-bottom': '0mm',
            'margin-left': '0mm',
        }
        
        try:
            pdfkit.from_string(html_content, pdf_path, options=options)
            sign_pdf(pdf_path, key)
            print(f"Generated and signed certificate for {player['name']}")
        except Exception as e:
            raise RuntimeError(f"Could not generate PDF for {player['name']}: {e}") from e

if __name__ == "__main__":
    main()
