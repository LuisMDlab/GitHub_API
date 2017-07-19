# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 12:30:28 2017

@author: MlabL3P
"""

from github import Github
from config import token_dict
import csv

with open('SocialTeste.csv', encoding = "utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
              
        situacao = {'corrigido':'closed', 'reaberto':'open', 'aberto':'open'}
        
        label = {'imediato': '?', 'urgente': '?', 'alta': '?', 'normal': '?', 'baixa':'?', #Prioridade
                 'travamento':'?', 'grande': '?', 'pequeno':'?', 'mínimo':'?',  #Gravidade
                 'ajuste':'?','correção de erro':'?', 'Design':'?', 'Documentação':'', 'Estudo':'?', 'Geral':'?', 'Infra-estrutura':'?', 'Melhoria':'?' ,'Nova Funcionalidade': '?', 'Teste':'?'} #Categoria
        
        colaboradores = {'leogermani':Github(token_dict['token_leo']),
                         'luis':Github(token_dict['token_luis']),
                         'weryqyes':Github(token_dict['token_wery']),
                         'walison':Github(''),
                         'marcelf':Github(''),
                         'eduardo':Github(''),
                         'julianny':Github(''),
                         'rodrigo':Github(''),
                         'mbrunodm':Github(''),
                         'andre':Github(''),
                         '':'None'}
        
        repo = colaboradores[row['Relator']].get_organization('medialab-ufg').get_repo('test-issues')
        
       
        issue = repo.create_issue(title = row['Resumo'], body = 'Feito por ' + row['Relator'],\
                                  assignee = colaboradores[row['Atribuido']].get_user().login,\
                                  label = (label[row['Categoria']], label[row['Prioridade']], label[row['Gravidade']]))
        
        issue.edit(state=situacao[row['Resolução']])
