import pandas as pd
from twilio.rest import Client

account_sid = "AC142733e2f787f03ee4a1214db1289427"
auth_token  = "483760022e390acb23cc004c152adc55"
client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'Em {mes} alguém bateu a meta. O vendedor {vendedor} conseguiu vender {vendas}')
        message = client.messages.create(
            to="+5518996693647",
            from_="+17123838356",
            body=f'Em {mes} alguém bateu a meta. O vendedor {vendedor} conseguiu vender {vendas}')

        print(message.sid)