import tkinter as tk
from tkinter import messagebox

#Dados da Pokédex
pokedex = {
    'fire': [
        {'nome': 'Charmander', 'info': 'Charmander é um Pokémon do tipo Fogo da primeira geração. Seu corpo laranja e a chama na ponta da cauda representam sua saúde e energia.'},
        {'nome': 'Cyndaquil', 'info': 'Cyndaquil é um Pokémon do tipo Fogo da segunda geração. Ele é pequeno, com chamas que surgem de suas costas quando está em perigo.'},
        {'nome': 'Torchic', 'info': 'Torchic é um Pokémon do tipo Fogo da terceira geração. Ele tem um espírito corajoso e, quando evolui, se torna um grande lutador.'},
        {'nome': 'Chimchar', 'info': 'Chimchar é um Pokémon do tipo Fogo da quarta geração. Ele é ágil e rápido, inspirado no comportamento de macacos.'},
        {'nome': 'Tepig', 'info': 'Tepig é um Pokémon do tipo Fogo da quinta geração. Ele é pequeno, mas muito determinado e cheio de energia.'},
        {'nome': 'Fennekin', 'info': 'Fennekin é um Pokémon do tipo Fogo da sexta geração. Ele tem um temperamento ardente e gosta de manipular o fogo.'},
        {'nome': 'Litten', 'info': 'Litten é um Pokémon do tipo Fogo da sétima geração. Ele é um felino com um forte senso de independência.'},
        {'nome': 'Scorbunny', 'info': 'Scorbunny é um Pokémon do tipo Fogo da oitava geração. Ele é muito energético e adora correr.'},
        {'nome': 'Fuecoco', 'info': 'Fuecoco é um Pokémon do tipo Fogo da nona geração. Ele tem um temperamento tranquilo e adora comer.'},
    ],
    'water': [
        {'nome': 'Squirtle', 'info': 'Squirtle é um Pokémon do tipo Água da primeira geração. Ele é um pequeno tartaruga com uma habilidade incrível de lançar água.'},
        {'nome': 'Totodile', 'info': 'Totodile é um Pokémon do tipo Água da segunda geração. Ele é um dinossauro aquático muito enérgico e curioso.'},
        {'nome': 'Mudkip', 'info': 'Mudkip é um Pokémon do tipo Água da terceira geração. Ele é um pequeno anfíbio com habilidades aquáticas impressionantes.'},
        {'nome': 'Piplup', 'info': 'Piplup é um Pokémon do tipo Água da quarta geração. Ele é um pinguim orgulhoso e determinado.'},
        {'nome': 'Oshawott', 'info': 'Oshawott é um Pokémon do tipo Água da quinta geração. Ele tem uma concha como espada e é muito corajoso.'},
        {'nome': 'Froakie', 'info': 'Froakie é um Pokémon do tipo Água da sexta geração. Ele é ágil e capaz de se camuflar na água.'},
        {'nome': 'Popplio', 'info': 'Popplio é um Pokémon do tipo Água da sétima geração. Ele é brincalhão e possui grande talento para o circo.'},
        {'nome': 'Sobble', 'info': 'Sobble é um Pokémon do tipo Água da oitava geração. Ele é tímido e possui habilidades de camuflagem.'},
        {'nome': 'Quaxly', 'info': 'Quaxly é um Pokémon do tipo Água da nona geração. Ele tem um estilo calmo e elegante, com grande habilidade em natação.'},
    ],
      'grass': [
        {'nome': 'Bulbasaur', 'info': 'Bulbasaur é um Pokémon do tipo Planta/Veneno da primeira geração. Ele tem uma planta crescendo em suas costas e pode atacar com ela.'},
        {'nome': 'Chikorita', 'info': 'Chikorita é um Pokémon do tipo Planta da segunda geração. Ela tem uma folha grande na cabeça e é muito amigável.'},
        {'nome': 'Treecko', 'info': 'Treecko é um Pokémon do tipo Planta da terceira geração. Ele é ágil e capaz de se mover rapidamente pelas árvores.'},
        {'nome': 'Turtwig', 'info': 'Turtwig é um Pokémon do tipo Planta da quarta geração. Sua carapaça de tortuga está cheia de energia e pode gerar raízes fortes.'},
        {'nome': 'Snivy', 'info': 'Snivy é um Pokémon do tipo Planta da quinta geração. Ele é rápido e possui um estilo elegante e estratégico.'},
        {'nome': 'Chespin', 'info': 'Chespin é um Pokémon do tipo Planta da sexta geração. Ele tem uma casca espinhosa e é muito protetor.'},
        {'nome': 'Rowlet', 'info': 'Rowlet é um Pokémon do tipo Planta/Voador da sétima geração. Ele é uma coruja com grandes olhos e muito silencioso.'},
        {'nome': 'Grookey', 'info': 'Grookey é um Pokémon do tipo Planta da oitava geração. Ele é muito travesso e adora bater em troncos com seu bastão.'},
        {'nome': 'Sprigatito', 'info': 'Sprigatito é um Pokémon do tipo Planta da nona geração. Ele é um felino com grande agilidade e habilidades naturais em camuflagem.'},
    ],
    'extra': [
        {'nome': 'Pokébola', 'info': 'A Pokébola é usada para capturar e armazenar Pokémon. Você a joga em um Pokémon selvagem após enfraquecê-lo.'},
        {'nome': 'Poção', 'info': 'A Poção recupera o HP do seu Pokémon durante ou fora das batalhas. Muito útil em jornadas longas!'},
        {'nome': 'TM', 'info': 'Os TMs são máquinas técnicas em forma de disco, usadas para ensinar golpes aos Pokémon. '},
        {'nome': 'Revive', 'info': 'Revive é um item que ressuscita um Pokémon desmaiado com metade de seu HP.'},
        {'nome': 'Bicicleta', 'info': 'A Bicicleta permite que você se mova mais rapidamente pelo mapa. Ideal para viagens longas!'},
        {'nome': 'Rare Candy', 'info': 'O Rare Candy aumenta o nível do seu Pokémon instantaneamente. Um atalho para evoluções!'}
    ]
} 

#Função para mostrar pokémons da tipagem escolhida :O
def mostrar_geracoes(tipo):
    limpar_tela()
    label_info.config(text=f"Gerações do tipo {tipo.capitalize()}")

    for i, pokemon in enumerate(pokedex[tipo][:9]):
        nome = pokemon['nome'] if isinstance(pokemon, dict) else pokemon
        botao = tk.Button(janela, text=f"G{i+1} - {nome}", width=30,
                          command=lambda n=nome: perguntar_info(n))
        botao.pack(pady=2)

    botao_voltar = tk.Button(janela, text="Voltar ao início", bg="purple", fg="white", width=20, command=voltar_ao_inicio)
    botao_voltar.pack(pady=5)

#Itens extras
def mostrar_extras():
    limpar_tela()
    label_info.config(text="Itens Extras da Pokédex")

    for i, item in enumerate(pokedex['extra']):
        nome = item['nome']
        botao = tk.Button(janela, text=nome, width=30, command=lambda n=nome: perguntar_info(n))
        botao.pack(pady=2)

    botao_voltar = tk.Button(janela, text="Voltar ao início", bg="purple", fg="white", width=20, command=voltar_ao_inicio)
    botao_voltar.pack(pady=5)
    #Pergunta se deseja saber mais
def perguntar_info(pokemon):
    resposta = messagebox.askyesno("Quer saber mais?", f"Deseja saber as informações sobre {pokemon}?")
    if resposta:
        for tipo in ['fire', 'water', 'grass', 'extra']:
            for p in pokedex[tipo]:
                if isinstance(p, dict) and p['nome'] == pokemon:
                    messagebox.showinfo(pokemon, p['info'])
                    return
    else:
        messagebox.showinfo("Mistério...", "Sem spoilers, né? Tudo bem, o mistério fica no ar!")
        
#limpa os widgets da janela
def limpar_tela():
    for widget in janela.winfo_children():
        if widget not in [label_titulo, label_info]:
            widget.destroy()

     #Função para voltar ao início
def voltar_ao_inicio():
    limpar_tela()
    label_info.config(text=">>> Escolha uma Tipagem <<<")
    for tipo in ['fire', 'water', 'grass']:
        cor = {'fire': 'red', 'water': 'blue', 'grass': 'green'}[tipo]
        btn = tk.Button(janela, text=tipo.capitalize(), bg=cor, fg='white', width=20,
                        command=lambda t=tipo: mostrar_geracoes(t))
        btn.pack(pady=5)

    #Botão extra na cor dourada
    botao_extra = tk.Button(janela, text="Extras", bg="#F4B400", fg="black", width=20, command=mostrar_extras)
    botao_extra.pack(pady=5)

    #Janela principal
janela = tk.Tk()
janela.title("Pokédex Iniciante")
janela.geometry("400x600")

label_titulo = tk.Label(janela, text=">>> Bem-vindo à sua Pokédex Iniciante <<<", font=("Helvetica", 14, "bold"))
label_titulo.pack(pady=10)

label_info = tk.Label(janela, text=">>> Escolha uma Tipagem <<<", font=("Helvetica", 12))
label_info.pack(pady=10)

for tipo in ['fire', 'water', 'grass']:
    cor = {'fire': 'red', 'water': 'blue', 'grass': 'green'}[tipo]
    btn = tk.Button(janela, text=tipo.capitalize(), bg=cor, fg='white', width=20,
                    command=lambda t=tipo: mostrar_geracoes(t))
    btn.pack(pady=5)