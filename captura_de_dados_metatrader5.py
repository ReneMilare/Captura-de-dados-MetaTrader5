# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 14:04:15 2020

@author: Rene Pereira Milare -> milarerp@gmail.com
"""
import MetaTrader5 as mt5
import datetime as dt
import pytz
import pandas as pd

def get_data_mt5(ativo, num_pregoes, time_frame):
    
    start = dt.date.today() - dt.timedelta(num_pregoes)
    end = dt.datetime.now() + dt.timedelta(1)
    
    ativo = str(ativo).upper()
    
    timezone = pytz.timezone('America/Sao_Paulo')
    
    date_from = dt.datetime(year=start.year, month=start.month, 
                            day=start.day, tzinfo=timezone)
    date_to = dt.datetime(year=end.year, month=end.month, 
                            day=end.day, tzinfo=timezone)
    
    dados = mt5.copy_rates_range(ativo, time_frame,
                                 date_from, date_to)
    
    df = pd.DataFrame(dados)
    df['time'] = pd.to_datetime(df['time'], unit='s')
        
    return df

def pregoes(ativo, num_pregoes, time_frame=mt5.TIMEFRAME_D1):
    if not mt5.initialize():
        print('Erro ao inicializar o MetaTrader.', mt5.last_error())
    
    if num_pregoes == -1:
        df = get_data_mt5(ativo, 99999, time_frame)
    else:
        df = get_data_mt5(ativo, num_pregoes, time_frame)
        
        pregoes_ = df.shape[0]
        while df.shape[0] < num_pregoes:
            pregoes_ += (num_pregoes - df.shape[0])
            df = get_data_mt5(ativo, pregoes_, time_frame)
        
    
    mt5.shutdown()
    
    nome_arquivo = 'dados_' + ativo.upper() + '_'+str(df.shape[0]) + \
        '_pregoes' + '.csv'
    
    df.to_csv(nome_arquivo, index=False)

    return df

''' Parâmetros '''
ATIVO = str(input('Nome do ativo: '))
PREGOES = int(input('Quantidade de pregões (-1 para máximo): '))

df = pregoes(ATIVO, PREGOES)
