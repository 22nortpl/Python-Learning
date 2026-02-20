nucleos = "ctacaatgtcagtatacccattgcattagccgg"

for i in range(0, len(nucleos), 3):
  codon = nucleos[i:i+3]
  if len(codon) == 3:
    print(codon)