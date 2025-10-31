# 🌤️ Assistente Virtual Meteorológico

Um assistente virtual que recebe comandos de voz para fornecer informações sobre as condições climáticas em tempo real, ajudando o usuário a se planejar para o dia.

## ⚡ Funcionalidades

O assistente reconhece e executa os seguintes comandos:

- **Mostrar previsão de hoje** – informa o clima atual e a previsão para as próximas horas.  
- **Vai chover amanhã?** – consulta dados meteorológicos e responde sobre a possibilidade de chuva.  
- **Qual a temperatura atual?** – apresenta a temperatura ambiente e a sensação térmica.  
- **Atualizar dados meteorológicos** – força a atualização das informações climáticas para garantir precisão.  

## 📂 Estrutura do Projeto

```
Assistente_Virtual_Meteorologico/
│
├─ audios/ # Áudios de teste dos comandos
├─ temp/ # Pasta temporária para gravações
├─ assistente.py # Script principal do assistente
├─ transcritor.py # Responsável por transcrever áudio em texto
├─ testes.py # Testes automatizados com os áudios
├─ config.json # Configurações de comandos
├─ requirements.txt # Dependências do projeto
└─ pycache/ # Cache do Python (não subir ao GitHub)
```

## 🛠️ Dependências

Recomenda-se criar um ambiente virtual Python e instalar as dependências:

```bash
python -m venv venv
```

### Ativando o ambiente virtual

Windows:
```bash
venv\Scripts\activate
```

Linux/Mac:
```bash
source venv/bin/activate
```

### Instalando dependências
```bash
pip install -r requirements.txt
```

### Principais pacotes usados
- torch e torchaudio
- transformers
- pyaudio
- nltk

### Recursos do NLTK
Para o NLTK, baixe os recursos necessários:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

## 🚀 Uso

### Rodando o assistente ao vivo
```bash
python assistente.py
```

O programa abrirá o microfone e exibirá a mensagem:

```
Fale alguma coisa...
```

Diga um dos comandos reconhecidos e o assistente executará a ação correspondente.

### Rodando os testes com áudios gravados
```bash
python testes.py
```

Valida se cada áudio corresponde corretamente ao comando esperado. Exemplo de retorno:

```
.....
----------------------------------------------------------------------
Ran 5 tests in 5.736s
OK
```

Observação: o primeiro teste valida a inicialização do modelo, seguido dos quatro comandos meteorológicos.

## 🔑 Configuração da API

Para obter dados meteorológicos em tempo real:

1. Crie uma conta gratuita no OpenWeatherMap.
2. Gere uma API Key (chave única).
3. Insira a chave no código (API_KEY) ou em config.json.

## ⚠️ Observações
Certifique-se de criar a pasta temp antes de rodar o assistente.

Para otimizar o reconhecimento de voz, use áudios de boa qualidade e fale claramente.

O assistente não possui interface web; toda interação é via terminal/microfone.

__pycache__ e arquivos .pyc não devem ser enviados ao GitHub.

A pasta temp pode ser adicionada ao .gitignore para evitar arquivos temporários.

### .gitignore
```
# Python
__pycache__/
*.py[cod]
*.pyo
*.pyd
venv/
env/
temp/

# Jupyter Notebook
.ipynb_checkpoints

# Sistema
.DS_Store
Thumbs.db
```