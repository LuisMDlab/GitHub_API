# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 12:30:28 2017
@author: LuisMDlab
"""
#Insert Issues into GitHub Python Script.

from github import Github #Connect with GitHub API module.
from config import token_dict #External file with a colaborators tokens dict.
import csv
import time

#Import issue info from csv. (Exported of MANTIS)
with open('Issue_Teste.csv', encoding = "utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #Info Comparation between  dicts and csv.
        situacao = {'corrigido':'closed', 'reaberto':'open', 'aberto':'open'}
        
        label = {'urgente':'piority:critical', 'alta':'piority:high', 'normal':'piority:medium', 'baixa':'piority:low', #Prioridade
                 
                 'Ajuste':'Bug','Correção de Erro':'Bug', 'Design':'Interface', 'Documentação':'Docs', 'Estudo':'Estudo',\
                 'Infra-estrutura':None, 'Melhoria':'Improvement' ,'Nova Funcionalidade':'NewFeature', 'Teste':None, #Categoria
                 
                 'atribuido':'dev:ready', 'novo':None, 'resolvido':'dev:validation', 'retorno':'dev:inprogress'} #Estado
        
        #Colaborators Dict, with Github object.
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
        #Repository Connection. (Access Tokens of repository users owners is needed)
        repo = colaboradores[row['Relator']].get_organization('medialab-ufg').get_repo('test-issues')
        
        try:#Create issue with assignee
            #Conditional chain to avoid "None" values from csv.
            if label[row['Prioridade']] == None:
                issue = repo.create_issue(title = row['Resumo'],\
                                          body = row['Resumo'],\
                                          assignee = colaboradores[row['Atribuido']].get_user().login,\
                                          labels = [label[row['Categoria']], label[row['Estado']]])
            elif label[row['Categoria']] == None:
                issue = repo.create_issue(title = row['Resumo'],\
                                          body = row['Resumo'],\
                                          assignee = colaboradores[row['Atribuido']].get_user().login,\
                                          labels = [label[row['Prioridade']], label[row['Estado']]])
            elif label[row['Estado']] == None:
                issue = repo.create_issue(title = row['Resumo'],\
                                          body = row['Resumo'],\
                                          assignee = colaboradores[row['Atribuido']].get_user().login,\
                                          labels = [label[row['Prioridade']], label[row['Categoria']]])
            else:
                issue = repo.create_issue(title = row['Resumo'],\
                                          body = row['Resumo'],\
                                          assignee = colaboradores[row['Atribuido']].get_user().login,\
                                          labels = [label[row['Prioridade']], label[row['Categoria']], label[row['Estado']]])
        except:#Create issue without assignee
            #Conditional chain to avoid "None" values from csv.
            if label[row['Prioridade']] == None:
                issue = repo.create_issue(title = row['Resumo'],\
                                          body = row['Resumo'],\
                                          labels = [label[row['Categoria']], label[row['Estado']]])
            elif label[row['Categoria']] == None:
                issue = repo.create_issue(title = row['Resumo'],\
                                          body = row['Resumo'],\
                                          labels = [label[row['Prioridade']], label[row['Estado']]])
            elif label[row['Estado']] == None:
                issue = repo.create_issue(title = row['Resumo'],\
                                          body = row['Resumo'],\
                                          labels = [label[row['Prioridade']], label[row['Categoria']]])
            else:
                issue = repo.create_issue(title = row['Resumo'],\
                                          body = row['Resumo'],\
                                          labels = [label[row['Prioridade']], label[row['Categoria']], label[row['Estado']]])
        time.sleep(3) #Avoid API Stop or Block.
