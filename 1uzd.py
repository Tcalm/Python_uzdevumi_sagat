"""
Uzrakstiet programmu definējot klasi,lai veselu skaitli pārveidotu par romiešu ciparu.

1)Ar kādiem cipariem ikdienā tiek strādāts? Arābu ...pavisam 10 ...0- 9  21
2)Romiešu cipariem... I, V, X, D, C, M cipari veido skaitli XXI
3)Kas ir klase?
"""
class AAA:
    #defineju konstruktoru
    def __init__(self):
        self.roma_sk={
            1:"I",
            4:"IV",
            5:"V",
            9:"IX",
            10: 'X', 
            40: 'XL', 
            50: 'L', 
            90: 'XC', 
            100: 'C', 
            400: 'CD', 
            500: 'D', 
            900: 'CM', 
            1000: 'M'
        }
        # metode, funkcija, kura veiks pārveidošanu.
    def to_roman(self, num): 
        result = "" 
        for value, numeral in sorted(self.roma_sk.items(), key=lambda x: x[0], reverse=True): 
            while num >= value: 
                result += numeral 
                num -= value  #num=num-value
        return result

# Izveidoju objektu
kk=AAA()
skaitlis=21
# izsaucam klases iekšējo funkciju (metode)
rom_sks=kk.to_roman(skaitlis)
print(f"{skaitlis} romiešu ciparos ir {rom_sks}")