<p align="center">
  <img width="612" height="344" src="https://media.istockphoto.com/photos/in-the-evening-creative-young-video-game-developer-works-on-a-desktop-picture-id1269257082?k=20&m=1269257082&s=612x612&w=0&h=Mye_TRDhGAPGFUOJzUngulazxi-pI_8DwRT3c_kosA4=">
</p>

## Desenvolvimento de jogos com Python

### Objetivos
O principal objetivo deste repositório é comentar as etapas de estudos que venho realizando em desenvolvimento de jogos e democratozar essa literatura em português para que várias pessoas consigam construir projetos. Vale salientar que, como uma "documentação" praticamente resumida, certas coisas não estarão presentes aqui, mas você pode pesquisar e encontrar o que deseja na documentação original. Ademais, as sprites utilizadas aqui não foram desenvolvidas por mim e estarão referenciadas no final desse readme.

### Importação e inicialização de biblioteca
Para que possamos inicializar um projeto em pygame, nada mais viável termos as ferramentas necessárias para criar do zero nosso projeto. Diante disso, esepra-se que você já possua instalado o framework Pygame, caso contrário, é só jogar o código abaixo no prompt do Python ou do Anaconda e esperar instalar na sua máquina.

```
pip install pygame
```
Em seguida, você já está pronto para importar a biblioteca e inicializar o projeto. Você fará isso toda vez que desenvolver um novo projeto de game em Python.
```
import pygame
pygame.init()
```
### Desenvolvimento de tela
O desenvolvimento de tela do game é uma etapa simples, mas que iremos interagir ao longo do projeto. Então, imagine comigo um pedaço de papel que será realizado uma redação, mais ou menos 30 linhas por exemplo, nessa folha, você precisa colocar o nome do local que você está fazendo a redação e dissertar, certo? É isto que iremos fazer logo embaixo:
```
//Aqui chamamos nossa biblioteca (local da redação), no display (nossa folha de redação) setamos um caption (título da redação)
pygame.display.set_caption('MEU PRIMEIRO JOGO")

//Apresentamos o tamanho da nossa tela de jogo
WINDOW_SIZE = (400, 400) 
```


<p align="center">
  <img width="320" height="320" src="https://github.com/wander-asb/game/blob/main/persona.gif?raw=true">
</p>
