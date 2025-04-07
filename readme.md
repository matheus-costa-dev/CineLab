# CineLab: Análise Exploratória de Star Wars Episódio IV 🚀

Bem-vindo ao **CineLab**, um repositório dedicado à análise de dados do universo cinematográfico, começando pelo clássico *Star Wars: Episódio IV - Uma Nova Esperança*.

## 📌 Sobre o Projeto

Este projeto realiza uma análise exploratória dos dados do filme Star Wars Episódio IV, obtidos através da API pública SWAPI (Star Wars API). O objetivo é extrair insights interessantes sobre personagens, planetas, naves espaciais e outros elementos do universo Star Wars.

## 🛠️ Estrutura do Repositório

```
CineLab/
├── datasets/                  # Dados brutos e processados
│   └── starwars_4/            # Dados específicos do Episódio IV
├── notebooks/
│   └── analise_exploratoria.ipynb  # Análise exploratória em Jupyter Notebook
├── reports/
│   └── analise_sw4.html       # Relatório renderizado em HTML (Quarto)
└── scripts/
    └── get_swapi_data.py      # Script para coletar dados da SWAPI
```

## 🔍 Análises Realizadas

1. **Exploração dos dados** do Episódio IV
2. **Estatísticas descritivas** sobre personagens
3. **Visualizações** de relações entre elementos do filme
4. **Insights** sobre o universo Star Wars

## 🚀 Como Reproduzir a Análise

1. **Obter os dados**:
   ```bash
   python scripts/get_swapi_data.py
   ```

2. **Executar a análise exploratória**:
   - Abra o Jupyter Notebook `notebooks/analise_exploratoria.ipynb`
   - Execute as células sequencialmente

3. **Gerar o relatório HTML** (se usando Quarto):
   ```bash
   quarto render reports/analise_sw4.qmd
   ```

## 📊 Tecnologias Utilizadas

- Python 3
- Jupyter Notebook
- Quarto (para relatórios)
- Bibliotecas:
  - pandas
  - matplotlib/seaborn
  - requests (para API SWAPI)

## 🤝 Como Contribuir

Contribuições são bem-vindas! Siga estes passos:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-analise`)
3. Commit suas mudanças (`git commit -m 'Adiciona análise de X'`)
4. Push para a branch (`git push origin feature/nova-analise`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
---

Desenvolvido por [Matheus Costa](https://github.com/matheus-costa-dev)  [Yasmin Pellegrine]()
📧 Contato: [dev.matheuspc@gmail.com](mailto:[dev.matheuspc@gmail.com) [email@gmail.com](mailto:[yasmin@gmail.com)