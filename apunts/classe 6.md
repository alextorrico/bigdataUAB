import pandas as pd

datasets = glob.glob('datasets/twitch_*') #aixo agafa tots els arxius que comnecin per twitch_/ glo.glob fa una llista de tots els datasets

llist = []

for data in datasets:
    df = pd.read_csv(data, "sep\t")
    df.loc[df['streamer_name']== "auronplay"]
    llista.append(df)

    print(df)
df.final = pd.concat(llista)
df_final.to_csv(f"{streamer}-dateset.csv", index=False)
