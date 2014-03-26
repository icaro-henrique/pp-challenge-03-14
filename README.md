pp-challenge-03-14
==================

Repositório para armazenamento dos resultados da atividade de Pair Programming do LIS em Março de 2014

Atividades
==========

<h3>24/03 - Manhã</h3>

<b>Instalação</b>

1) No Windows, instalar o Python 3 (remover versões anteriores) adicioná-lo ao PATH do Windows

2) Instalar o editor Sublime Text 3

3) Procurar e instalar o plugin "Package Control" para o Sublime Text

4) Instalar o pacote "SublimeREPL" pelo "Package Control"

5) Fazer um "hello world" em Python e rodar pelo "SublimeREPL"

<b>Linguagem</b>

1) Informar o valor da soma de dois números passados por parâmetro de entrada do programa (e.g. python sum.py 5 7)

2) Hello IO. Dar "hello" para um nome que está em um arquivo do sistema (realizar leitura do arquivo)

3) Contador de vogais. Conta a quantidade de cada vogal (separadamente) em uma palavra digitada e retorna o total no fim

<b>Design</b>

1) Ler um overview sobre o que é Pep8 em Python

2) Instalar o plugin "Pep8 Python Lint" pelo "Package Control"

2.1) Este plugin é compatível apenas com o Sublime Text 2, baixe a versão "Portable", instale o "Package Control" da versão do Sublime Text 2 e instale o "Pep8 Python Lint"

3) Usando o plugin, ajustar todos os scripts feitos anteriormente para estarem de acordo com o Pep8

3.1) Ao salvar algum arquivo Python, os problemas da Pep8 são mostrados na tela, ajustar o código para que fique de acordo com todos eles

4) Criar uma conta no GitHub e instalar o TortoiseGIT

5) Clonar o repositório "https://github.com/icaro-henrique/pp-challenge-03-14.git"

6) Colocar os scripts desenvolvidos em uma pasta com o nome da equipe (e.g. "leao")

5) Criar um branch com o seu nome (e.g. "icaro-henrique")

6) Realizar um commit e push da pasta com o scripts deste branch

7) Iniciar um pull request do seu branch

<h3>25/03 - Tarde</h3>

<b>Algoritmos</b>

1) n-ésimo número de Fibonacci

    e.g.
    F10 = 55
    F12 = 144

2) Bubble sort de uma lista de números passados por parâmetro de entrada do programa

    e.g. python bubble_sort.py 3 4 2 1 -> [1, 2, 3, 4]
<b>Programas</b>

1) Fazer um leitor de RSS que a partir do link do feed imprime o nome do mesmo e as 3 primeiras entradas (título, link e descrição)

2) Jogo de par ou ímpar, entrada do programa é 1 ou 2 e se quer "par" ou "impar", sorteia um valor e retorna o resultado

    e.g. python par_impar.py par 2 -> Voce (par) 2 x 1 Adversario (impar), voce perdeu!
3) Cifra de César. A partir de um texto de entrada e uma chave numérica "n", mover cada letra do texto "n" caracteres para frente no alfabeto (não precisa ser case sensitive)

    e.g.: python caesar.py ABEVZ 2 -> CDGZB (usando alfabeto brasileiro)
<b>Equipe Força, Batata, Triângulo</b>

1) Comunicação UDP. Criar um servidor e um cliente que receberão e enviarão, respectivamente, mensagens por um socket UDP. Mensagem vazia denota o fim da comunicação

<b>Equipe Leão, Sol</b>

1) Filtro de "pacotes de rede" e distribuição de carga. A partir de pacotes gerados, realizar as seguintes operações:

1.1) Definir uma estrutura de um "Servidor_UDP" e de "Servidor_HTTP" que devem realizar o seguinte

1.1.1) Servidores UDP, ao receberem uma mensagem, imprimem a mesma na tela, juntamente com o endereço de quem a enviou (source_ip).
  
    e.g.
    Pacote recebido: | udp | 219.90.20.135 | 25.117.51.251 | ppto2srjmxxkxwNJ |
    Mensagem: 219.90.20.135: ppto2srjmxxkxwNJ
1.1.2) Servidores HTTP, ao receberem uma mensagem, concatenam o seu conteúdo em um arquivo do sistema no formato a seguir: <dd-mm-yyyy hh:mm:ss> - <source_ip> - <dest_ip> - <content> - <id_servidor> (obs: Arquivo é limpo a cada nova execução)

    e.g.
    Pacote recebido: | tcp | 219.90.20.135 | 25.117.51.251 | ppto2srjmxxkxwNJ |
    Linha adicionada: 24-03-2014 15:47:34 - 219.90.20.135 - 25.117.51.251 -ppto2srjmxxkxwNJ - http_1
2.1) Criar uma estrutura de um "Roteador" que deve realizar o seguinte roteamento dos pacotes:

2.1) Pacotes do tipo "tcp" são descartados

2.2) Pacotes "udp" devem ser repassados para um "Servidor_UDP" que os processará

2.3) Pacotes "http" devem ser repassados para um "Servidor_HTTP" que os processará

2.4) O roteador deve manter um log de cada encaminhamento de pacote e ele deve ser apresentado no final da execução

    e.g.
    Pacote UDP enviado para: udp_1
    Pacote UDP enviado para: udp_2
    Pacote HTTP enviado para: http_1
    Pacote UDP enviado para: udp_1
    Pacote TCP descartado
    Pacote HTTP enviado para: http_2
3.1) Cada tipo de servidor (UDP e HTTP) deve ter duas instâncias e no momento que o roteador encaminhar as mensagens, a instância alvo será escolhida seguindo um algoritmo de Round-Robin (alternando entre as instâncias de cada tipo)

    e.g.
    Pacote udp -> Roteador -> Round-Robin -> Servidor_UDP_1
    Pacote udp -> Roteador -> Round-Robin -> Servidor_UDP_2
    Pacote http -> Roteador -> Round-Robin -> Servidor_HTTP_1
    Pacote udp -> Roteador -> Round-Robin -> Servidor_UDP_1
    Pacote http -> Roteador -> Round-Robin -> Servidor_HTTP_2
    Pacote udp -> Roteador -> Round-Robin -> Servidor_UDP_2
4.1) O gerador de pacotes já foi implementado e fornecido para uso no programa. Verificar o script "net_packet.py" no repositório para instruções de uso

    
