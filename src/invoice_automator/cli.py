import argparse
from pathlib import Path

def parse_args():
    p = argparse.ArgumentParser(description="Invoice Automator (CSV -> PDF)")
    p.add_argument("--csv", required=True, type=Path, help="Chemin du CSV d'entrée")
    p.add_argument("--out", required=True, type=Path, help="Dossier de sortie des PDF")
    return p.parse_args()

def main():
    args = parse_args()
    # Pour l'instant on ne fait que vérifier l'existence des chemins
    if not args.csv.exists():
        raise FileNotFoundError(f"CSV introuvable: {args.csv}")
    args.out.mkdir(parents=True, exist_ok=True)
    print(f"[OK] CSV détecté: {args.csv}")
    print(f"[OK] Dossier de sortie prêt: {args.out}")
    print("MVP à venir: lecture du CSV et génération PDF…")

if __name__ == "__main__":
    main()