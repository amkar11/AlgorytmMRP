import pandas as pd
ilosc_artykuly = int(input("Proszę podać ilość artykuły "))
for i in range(ilosc_artykuly):
    nazwa_produktu = input("Proszę wskazać nazwę produktu ")
    poziom_produktu = input("Proszę wskazać poziom produktu ")
    ilosc_wierszy = int(input("Ile tygodni trzeba na wykonanie zamówienia? "))
    columns = {"Tydzień":[i for i in range(1, ilosc_wierszy+1)], "Potrzeby brutto":0, "Wstępny zapas":0, "Potrzeby netto":0, "Wstępne zmontowanie":0, "Zaplanowany odbiór":0}
    row_labels = [i for i in range(1, ilosc_wierszy+1)]
    data = pd.DataFrame(data = columns, index=row_labels)
    def potrzeby_brutto():
        ilosc_dostarczen = int(input("Proszę wskazać ilość dostarczeń "))
        for i in range(ilosc_dostarczen):
            dzien_dostarczania = int(input("Proszę wskazać tydzień dostarczania produktu "))
            ilosc_produktow = int(input("Proszę wskazać ilość produktów "))
            data.loc[dzien_dostarczania, "Potrzeby brutto"] = ilosc_produktow
    potrzeby_brutto()
    def wstepny_zapas():
        ilosc_zapasu = int(input("Proszę wskazać wstępny zapas "))
        for index, row in data.iterrows():
            if ilosc_zapasu > 0:
                if row["Potrzeby brutto"] == 0:
                    data.loc[index, "Wstępny zapas"] = ilosc_zapasu
                elif row["Potrzeby brutto"] < ilosc_zapasu:
                    data.loc[index, "Wstępny zapas"] = ilosc_zapasu
                    ilosc_zapasu -= row["Potrzeby brutto"]
                elif row["Potrzeby brutto"] > ilosc_zapasu:
                    data.loc[index, "Wstępny zapas"] = ilosc_zapasu
                    ilosc_zapasu = 0
    wstepny_zapas()
    def potrzeby_netto():
        for index, row in data.iterrows():
            if data.loc[index, "Potrzeby brutto"] != 0:
                data.loc[index, "Potrzeby netto"] = data.loc[index, "Potrzeby brutto"] - data.loc[index, "Wstępny zapas"]
                if data.loc[index, "Potrzeby netto"] < 0:
                    data.loc[index, "Potrzeby netto"] = 0
    potrzeby_netto()
    def wstepne_zmontowanie():
        czas_zmontowania = int(input("Proszę podać czas zmontowania "))
        for index, row in data.iterrows():
            if index - czas_zmontowania >= 0 and index + czas_zmontowania in data.index:
                data.loc[index, "Wstępne zmontowanie"] = data.loc[index + czas_zmontowania, "Potrzeby netto"]
            else:
                data.loc[index, "Wstępne zmontowanie"] = 0
    wstepne_zmontowanie()
    def zaplanowany_odbiór():
        data["Zaplanowany odbiór"] = data["Potrzeby netto"]
    zaplanowany_odbiór()
    print(f"{nazwa_produktu}, poziom {poziom_produktu}")
    print(data.to_string(index=False))