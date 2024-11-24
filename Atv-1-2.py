import pandas as pd
import matplotlib.pyplot as plt


url = "https://raw.githubusercontent.com/woota/covid19br/master/cases-brazil-cities.csv"

                                                     # Carregar os dados
df = pd.read_csv(url)

                                                     # Remover linhas com informações totais por estado (cidades identificadas como "TOTAL")
df = df[~df['city'].str.contains('TOTAL', na=False)]

                                                     # Criar colunas auxiliares para estado e cidade
df['state'] = df['city_ibge_code'].astype(str).str[:2]  

                                                     # 1. Cidade com mais casos de covid
cidade_mais_casos = df.loc[df['confirmed'].idxmax()]
print(f"1. Cidade com mais casos de covid: {cidade_mais_casos['city']} com {cidade_mais_casos['confirmed']} casos.")

                                                     # 2. Cidade com menos casos de covid
cidade_menos_casos = df.loc[df['confirmed'].idxmin()]
print(f"2. Cidade com menos casos de covid: {cidade_menos_casos['city']} com {cidade_menos_casos['confirmed']} casos.")

                                                     # 3. Estado com mais casos de covid
estado_mais_casos = df.groupby('state')['confirmed'].sum().idxmax()
casos_estado_mais = df.groupby('state')['confirmed'].sum().max()
print(f"3. Estado com mais casos de covid: {estado_mais_casos} com {casos_estado_mais} casos.")

                                                     # 4. Estado com menos casos de covid
estado_menos_casos = df.groupby('state')['confirmed'].sum().idxmin()
casos_estado_menos = df.groupby('state')['confirmed'].sum().min()
print(f"4. Estado com menos casos de covid: {estado_menos_casos} com {casos_estado_menos} casos.")

                                                     # 5. Cidade com mais mortes por covid
cidade_mais_mortes = df.loc[df['deaths'].idxmax()]
print(f"5. Cidade com mais mortes por covid: {cidade_mais_mortes['city']} com {cidade_mais_mortes['deaths']} mortes.")

                                                     # 6. Cidade com menos mortes por covid
cidade_menos_mortes = df.loc[df['deaths'].idxmin()]
print(f"6. Cidade com menos mortes por covid: {cidade_menos_mortes['city']} com {cidade_menos_mortes['deaths']} mortes.")

                                                     # 7. Estado com mais mortes por covid
estado_mais_mortes = df.groupby('state')['deaths'].sum().idxmax()
mortes_estado_mais = df.groupby('state')['deaths'].sum().max()
print(f"7. Estado com mais mortes por covid: {estado_mais_mortes} com {mortes_estado_mais} mortes.")

                                                     # 8. Estado com menos mortes por covid
estado_menos_mortes = df.groupby('state')['deaths'].sum().idxmin()
mortes_estado_menos = df.groupby('state')['deaths'].sum().min()
print(f"8. Estado com menos mortes por covid: {estado_menos_mortes} com {mortes_estado_menos} mortes.")

                                                     # 9. Total de casos de covid no Brasil
total_casos = df['confirmed'].sum()
print(f"9. Total de casos de covid no Brasil: {total_casos}")

                                                     # 10. Total de mortes por covid no Brasil
total_mortes = df['deaths'].sum()
print(f"10. Total de mortes por covid no Brasil: {total_mortes}")

                                                     # 11. Gerar um gráfico barplot com 5 estados com mais mortes
top5_estados_mortes = df.groupby('state')['deaths'].sum().nlargest(5)
top5_estados_mortes.plot(kind='bar', color='red', title='Top 5 Estados com Mais Mortes por COVID-19')
plt.ylabel('Número de Mortes')
plt.xlabel('Estado')
plt.show()

                                                     # 12. Gerar um gráfico histograma com 5 estados com menos mortes
bottom5_estados_mortes = df.groupby('state')['deaths'].sum().nsmallest(5)
bottom5_estados_mortes.plot(kind='bar', color='blue', title='Top 5 Estados com Menos Mortes por COVID-19')
plt.ylabel('Número de Mortes')
plt.xlabel('Estado')
plt.show()
