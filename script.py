import os


def checkforprogram(directory, targetp):

    # Função que checa em um item dado, se X string existe nela
    # Também recebe o caminho para quando achar, printar uma mensagem personalizada
    def check(p_targetp, p_item, p_path):
        if p_targetp in p_item:
            print(f"Achouu!\n{p_targetp} no caminho {p_path}")

    try:
        dirlist = os.listdir(directory)
        # Cria uma lista baseada nos elementos encontrados em "dir"

        if os.path.exists(directory):
            for item in dirlist:
                itemdir = os.path.join(directory, item)
                # Caminho do item atual, criado ao juntar o diretório passado pelo parâmetro com o item atual

                # Se for um diretório checa e faz uma chamada recursiva para verificar o mesmo
                if os.path.isdir(itemdir):
                    check(targetp, item, itemdir)
                    checkforprogram(itemdir, targetp)

                # Se for um arquivo apenas checa
                elif os.path.isfile(itemdir):
                    check(targetp, item, itemdir)

    except Exception as e:
        print(f'Ocorreu um erro: {e}')


targetP = str(input("Digite o programa alvo: "))
caminho1 = "C:/Program Files"
caminho2 = "C:/Program Files (x86)"

checkforprogram(caminho1, targetP)
checkforprogram(caminho2, targetP)
