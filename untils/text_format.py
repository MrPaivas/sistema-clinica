def format_text(dict):
    formated_text = f"""Nova Consulta! Consultório: {dict.get('consultorio', 'nenhum')}, Paciente: {dict.get('paciente', 'nenhum')}, Estagiário: {dict.get('estagiario', 'nenhum')}"""
    return formated_text