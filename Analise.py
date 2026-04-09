import pandas as pd
import os

# 1. Configuração do Nome do Arquivo (Exatamente como aparece na sua pasta)
arquivo_entrada = 'Dados.csv'
arquivo_saida = 'resumo_consumo.csv'

print("--- Iniciando Processamento ---")

# 2. Verificação de Segurança
if os.path.exists(arquivo_entrada):
    try:
        # 3. Leitura dos Dados
        # sep=';' porque arquivos de logística costumam usar ponto e vírgula
        df = pd.read_csv(arquivo_entrada, sep=';', encoding='latin1')
        
        # 4. Padronização (Transforma todos os nomes de colunas em minúsculo)
        # Isso evita o erro de 'Data' vs 'data'
        df.columns = df.columns.str.lower()
        
        # 5. Tratamento da Data
        df['data'] = pd.to_datetime(df['data'], dayfirst=True)
        
        # 6. Geração do Resumo (Soma das saídas por produto)
        # Ajustado para os nomes das colunas que o Python agora lê em minúsculo
        resumo = df.groupby('produto')['saída'].sum()
        
        # 7. Exportação Final
        resumo.to_csv(arquivo_saida, sep=';', encoding='latin1')
        
        print("\n" + "="*40)
        print("✅ SUCESSO ABSOLUTO!")
        print(f"👉 O arquivo '{arquivo_saida}' foi criado.")
        print("👉 Agora você pode atualizar seu dashboard.")
        print("="*40)

    except Exception as e:
        print(f"\n❌ Ocorreu um erro técnico: {e}")
        print("Verifique se as colunas 'Produto', 'Saída' e 'Data' existem no CSV.")
else:
    print(f"\n❌ ERRO: O arquivo '{arquivo_entrada}' não foi encontrado.")
    print(f"Arquivos que o Python está vendo na pasta: {os.listdir('.')}")