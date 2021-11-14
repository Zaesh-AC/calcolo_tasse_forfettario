#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser(description="Shortcut per l'inseriemento dei valori")
parser.add_argument('--lordo', type=int, dest="lordo", action='store', help='Fatturato lordo')
parser.add_argument("--coef", "--cr", type=int, dest='cr', action='store', help="Coefficiente di redditività")
parser.add_argument("--aliquota", "--ali", type=int, dest='aliquota', action='store', help="Aliquota applicata")

args = parser.parse_args()

def calcolo_tasse(lordo, coeff_redditivita, aliquota):
    imponibile = lordo * (coeff_redditivita / 100)
    prev = imponibile * (25.72 / 100)
    imposta = (((imponibile - prev) * aliquota) / 100)
    netto = lordo - prev - imposta
    return (
        imponibile,
        prev,
        imposta,
        netto
    )

if __name__ == "__main__":
    lordo = args.lordo if args.lordo else int(input("Inserici lordo\n"))
    coeff_redditivita = args.cr if args.cr else int(input("Inserici coeff redditivita\n"))
    aliquota = args.aliquota if args.aliquota else int(input("Inserici aliquota\n"))

    imponibile, inps, imposta, netto = calcolo_tasse(lordo, coeff_redditivita, aliquota)

    print(f"Reddito imponibile: {imponibile}")
    print(f"Contributi previdenziali INPS: {inps}")
    print(f"Imposta: {imposta}")
    print(f"Netto: {netto}")
