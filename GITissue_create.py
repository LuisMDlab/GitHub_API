# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 12:30:28 2017
@author: MlabL3P
"""
#Script to Insert Issues into GitHub.

from github import Github #GitHub Module to connect with API.
from config import token_dict #External file with a dict of colaborators tokens.
import csv
import time

#Import issue info from csv. (Exported of MANTIS)
with open('Issue_Teste.csv', encoding = "utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #Comparation info dicts.
        situacao = {'corrigido':'closed', 'reaberto':'open', 'aberto':'open'}
        
        label = {'urgente':'piority:critical', 'alta':'piority:high', 'normal':'piority:medium', 'baixa':'piority:low', #Prioridade
                 
                 'Ajuste':'Bug','Correção de Erro':'Bug', 'Design':'Interface', 'Documentação':'Docs', 'Estudo':'Estudo',\
                 'Infra-estrutura':None, 'Melhoria':'Improvement' ,'Nova Funcionalidade':'NewFeature', 'Teste':None, #Categoria
                 
                 'atribuido':'dev:ready', 'novo':None, 'resolvido':'dev:validation', 'retorno':'dev:inprogress'} #Estado
        
        #Colaborators Dict.
        colaboradores = {'leogermani':Github(token_dict['token_leo']),
                         'luis':Github(token_dict['token_luis']),
                         'weryqyes':Github(token_dict['token_wery']),
                         'walison':Github(token_dict['token_wallison']),
                         'marcelf':Github(''),
                         'eduardo':Github(token_dict['token_eduardo']),
                         'julianny':Github(token_dict['token_julianny']),
                         'rodrigo':Github(token_dict['token_rodrigo']),
                         'mbrunodm':Github(token_dict['token_mbruno']),
                         'andre':Github(token_dict['token_andre']),
                         '':None}
        #Connection with repo. (Access Tokens of repository users owners is needed)
        repo = colaboradores[row['Relator']].get_organization('medialab-ufg').get_repo('test-issues')
        
        try:
            #create issue with assignee
            issue = repo.create_issue(title = row['Resumo'],\
                                      body = row['Resumo'],\
                                      assignee = colaboradores[row['Atribuido']].get_user().login,\
                                      labels = [label[row['Prioridade']], label[row['Categoria']], label[row['Estado']]])
        except:
            #create issue without assignee
            issue = repo.create_issue(title = row['Resumo'],\
                                      body = row['Resumo'],\
                                      labels = [label[row['Prioridade']], label[row['Categoria']], label[row['Estado']]])
        #Avoid API Stop.
        time.sleep(5)
