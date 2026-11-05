# Analisando dados de veículos

Aplicativo web interativo, feito com Streamlit, para explorar visualmente um conjunto de dados de anúncios de venda de carros.

## Para que serve

O app carrega o arquivo `vehicles.csv` e gera gráficos interativos com poucos cliques. Ele ajuda a entender rapidamente como se distribuem a quilometragem dos veículos e a relação entre quilometragem e preço, sem precisar escrever código.

## Funcionalidades

- **Histograma da quilometragem:** o botão "Criar histograma" mostra a distribuição da coluna `odometer`, com a frequência de veículos em cada faixa de quilometragem.
- **Gráfico de dispersão:** o botão "Criar Gráfico de Dispersão" relaciona `odometer` (eixo X) e `price` (eixo Y), para identificar tendências e valores atípicos.
- **Gráficos interativos:** os gráficos usam Plotly e permitem zoom, deslocamento, seleção de áreas e consulta dos valores ao passar o mouse.
- **Exibição sob demanda:** cada gráfico só é gerado quando o botão correspondente é clicado.

## Tecnologias

- Python
- Streamlit
- Pandas
- Plotly Express

## Estrutura do projeto

- `app.py`: código do aplicativo (ajuste o nome conforme o seu arquivo)
- `vehicles.csv`: base de dados de anúncios de veículos
- `requirements.txt`: dependências do projeto

## Como executar

1. Instale as dependências:

   pip install streamlit pandas plotly

2. Coloque o arquivo `vehicles.csv` na mesma pasta do aplicativo.

3. Inicie o app:

   streamlit run app.py

4. Abra no navegador o endereço exibido no terminal (normalmente [http://localhost:8501](https://projeto-sprint-5-gips.onrender.com/)).

## Dados esperados

O arquivo `vehicles.csv` deve ser separado por vírgulas e conter, no mínimo, as colunas `odometer` (quilometragem) e `price` (preço).
