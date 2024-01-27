Código em Python feito para o programa de estágio da Tunts.Rocks. O programa processa dados de uma Google Sheet, calculando notas, situação do aluno, e notas finais para aprovação. Após processamento, a planilha é automaticamente atualizada com os resultados.
Para a realização do desafio, foi escolhido usar o gspread, que é uma API python para Google Sheets. A escolha foi feita baseado no tamanho e escopo do projeto.

Pré-requisitos

    Python 3.x
    Biblioteca gspread (pip install gspread)
    Uma Planilha Google com dados dos alunos, como fornecido pela Tunts.Rocks
    Uma conta de serviço do Google Cloud Platform com acesso à Planilha Google (credenciais fornecidas até conclusão do processo seletivo)

Usagem
    pip install gspread
    python grade_evaluator.py

Notas
Mesmo sendo a primeira vez que manipulo Sheets da Google, o processo foi relativamente simples. A API é muito bem documentada e o desafio foi bem explicado.
Futuras melhorias ao projeto podem incluir: uma GUI user-friendly, alteração do código para aceitar diversos formatos de tabela, testes automáticos e implementação de medidas de segurança em relação a chave da API.
