    # --- LÓGICA DE LEITURA DE DADOS REAIS ---
    file_path = os.path.join(data_path, 'raw_sweep.csv')
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Ficheiro de dados CSV não encontrado em: {file_path}")

    # Lê o ficheiro CSV usando pandas
    raw_df = pd.read_csv(file_path)

    # Renomeia as colunas para os nomes que o modelo espera, se necessário
    # raw_df.rename(columns={
    #     'Frequency_GHz': 'frequency_GHz', 
    #     'S21_Magnitude_dB': 's21_magnitude'
    # }, inplace=True) 
    # O código que escrevemos no 'model.py' está à espera de 'frequency_GHz' e 's21_magnitude'
    # Como as colunas no CSV estão capitalizadas, vamos forçar a renomeação:
    raw_df.columns = raw_df.columns.str.lower()
    raw_df.rename(columns={'s21_magnitude_db': 's21_magnitude'}, inplace=True)
    # ------------------------------------
