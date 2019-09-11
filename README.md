# mini-curso-blockchain

## O que é Bitcoin?

Bitcoin é uma criptomoeda, descentralizada e que não necessita de terceiros para funcionar. Isso significa que você não depende de bancos, grandes corporações ou governos para movimentar seu dinheiro. Com o Bitcoin, o dinheiro é realmente seu. O Bitcoin é baseado em uma rede descentralizada segura chamada Blockchain criada por Satoshi Nakamoto.

## Quem é Satoshi Nakamoto?

**Satoshi Nakamoto** *(中本哲史 Nakamoto Satoshi)* é o pseudônimo utilizado pela pessoa ou pessoas que criaram a moeda virtual bitcoin. Há diversas teorias a respeito de quem poderia estar por trás da verdadeira identidade de Satoshi Nakamoto, mas por enquanto são apenas especulações.
Em 2008, Nakamoto apresentou o [conceito bitcoin](https://bitcoin.org/bitcoin.pdf) no grupo de discussões chamado The Cryptography Mailing. Em 2009, lançou a rede bitcoin que começa a funcionar com o lançamento do primeiro cliente bitcoin open source e a emissão das primeiras bitcoins.

# Dinâmicas de alinhamento

As dinâmicas são atividades lúdicas que demonstram algumas funcionalidades do bitcoin e os problemas que ele pode resolver, levando o participante a fazer ligações mais palpáveis aos conceitos, facilitando o entendimento quando entrarmos em termos e algoritmos mais complexos.

## Do mundo físico ao digital (A troca da maçã)

Nós estamos sentados em um banco no parque Ibirapuera. É um belo dia. Eu tenho uma maçã comigo, e dou ela pra você.

Você agora tem um maçã e eu tenho zero maçãs. Muito simples, certo?

Minha maçã esta fisicamente sendo coloca em sua mão. Você sabe que aconteceu. Eu estava lá, você estava lá — você a tocou.
Não precisamos de uma terceira pessoa para nos ajudar na transferência. Não precisamos de um Juiz entre nós para confirmar 
que a maçã passou de um para o outro.
A maçã agora é sua! Eu não posso de entregar outra maça porque não tenho mais nenhuma. Eu não tenho controle sobre ela mais. 
A maçã saiu de minha posse. Agora você tem total controle sobre a maçã. Você pode entregar a maçã para um amigo se quiser, então o seu amigo pode entregar para o amigo dele, e por ai vai.

Agora, digamos que eu tenha uma maçã digital. Vou te entregar minha maçã digital. Agora a coisa fica interessante.

Como você sabe que a maçã digital que costumava ser minha, agora é sua e somente sua? Pense nisso por um instante. É um pouco mais complicado, certo? Como você sabe que eu não mandei esta maçã por email em anexo para meu tio. Ou para meu amigo João. Ou minha amiga Lua também?

Talvez eu tenha feito algumas cópias daquela maçã em meu computador. Talvez eu tenha colocado a maçã para download na internet para um milhão de pessoas baixarem.

Como você pode ver, essa troca digital é um problema. Enviar maçãs digitais não parece igual a enviar maçãs físicas.
Aqui temos um grande problema da computação chamado “gasto duplo” ou “double-spending problem”.
Uma solução para este problema séria fazer um registro da troca em um livro digital. Assim alguém rastreia nossas maçãs e podemos ficar mais tranquilos, problema resolvido!
Ainda temos dois problemas aqui:
Alguém em posse do livro digital, pode criar quantas maçãs quiser.
Não é a mesma coisa que o nosso dia no parque Ibirapuera onde só estávamos você e eu. Alguém com controle do livro é como colocar um Juiz no meio de nossa troca.
Mas como eu posso trocar minha maçã digital com você desta maneira usual?
E se eu desse este livro para todo mundo? No lugar do livro ficar com apenas umas pessoa, ele estaria no computador de todo mundo. Todas as trocas que já aconteceram, de todos os tempos, em maçãs digitais, serão gravados nele.
Você não pode enganar, Eu não posso enviar maçãs que eu não tenho, porque então não seria capaz de sincronizar com todas as outras pessoas no sistema. Seria um sistema difícil de vencer. Especialmente se ficar muito grande.
Ainda mais, não é controlado por uma única pessoa, então eu sei que ninguém pode decidir por dar mais maçãs digitais a si mesmo. As regras do sistema já foram definidas no inicio.
E os códigos e regras são abertos, você pode participar da rede também — atualizando o livro e certificando-se de que tudo fosse feito. Para o problema, você poderia obter 25 maçãs digitais como recompensa. Na verdade, essa é a única maneira de criar mais maçãs digitais no sistema.

## Generais Bizantinos

O problema dos generais bizantinos trata sobre as armadilhas e desafios que existem ao tentar coordenar ações de comunicação dentro de uma rede cujos pares não são totalmente confiáveis. Foi proposto em 1982 por Marshall Pease, Robert Shostak e Leslie Lamport, e desde então virou um problema bastante visto em aulas de computação, e tido por muitos como algo sem solução.

Um breve resumo: o problema mostra uma situação hipotética de batalha, onde dois generais planejam atacar uma cidade. Cada um deles tem um exército acampado em uma montanha, tendo um vale separando os dois. Eles precisam trocar mensagens, mas a única forma de fazê-lo é através do vale – o qual está cercado de forças inimigas, sendo pouco provável que um mensageiro não seja capturado lá.

O problema em questão está em conseguir achar uma maneira de chegar a um consenso para resolver o problema. Uma das soluções propostas é a de nomear um dos generais como líder, cabendo a este a responsabilidade de avisar o segundo general sobre a hora do ataque. O problema é conseguir chegar a um algoritmo que permita a ambos concluir, de forma correta e inequívoca, “vamos atacar na hora marcada!”

Um exemplo da falta de solução do problema é: o primeiro general pode começar enviando uma mensagem “Ataque às 09:00 em 4 de agosto.” No entanto, uma vez enviada, o primeiro general não tem ideia se o mensageiro entregou ou não. Essa incerteza pode levar o primeiro general a hesitar a atacar, devido ao risco de ser o único atacante. Isso gera um problema que mesmo um número infinito de confirmações não conseguiria eliminar. Esse sempre foi o calcanhar de Aquiles das redes descentralizadas.

## Lavando louça na republica

Leo, Júlio, Maria e Elsa são quatro estudantes que moram na mesma república em Ouro Preto. Como em quase toda república espalhada pelo Brasil, é uma guerra na hora de saber quem vai lavar as vasilhas sujas de Miojo. Os estudantes tentaram implantar um sistema de revezamento, mas foi um fracasso felomenal: Júlio é o maior malandro, Leo distraído, Maria coincidentemente nunca está em casa na sua vez de lavar as vasilhas. Elsa é maior cri-cri e toda vez que tem visita pra jantar na vez dela lavar a louça ela argumenta que ficou em desvantagem, que trabalhou mais que os outros e quer descontar o trabalho extra na outra semana. No fim ninguém entra em acordo e é a senhoria que tem que decidir com mão de ferro quem vai lavar as vasilhas.
Pra resolver a este problema a senhoria teve uma ideia simples, porém genial: ela inventou de dar fichinhas coloridas a cada um dos estudantes (cada estudante com sua cor) e construiu um longo tubo transparente e indestrutível que ela chumbou ao chão da sala (tá bom, a ideia não era tão simples assim, mas vai seguindo o raciocínio).

Quando um estudante termina de lavar as vasilhas ele deposita uma fichinha no tubo pra ficar registrado que ele cumpriu com sua parte no revezamento. Pra evitar trapaças só é possível colocar uma fichinha no tubo se três dos quatro estudantes estiverem presentes, pois na tampa do tubo tem quatro cadeados onde cada estudante tem a chave para um deles.
Cada fichinha só pode ser colocada no tubo com o consentimento de pelo menos mais dois estudantes, que só permitem que isso aconteça depois de checarem que a pessoa realmente lavou as vasilhas e deixou a cozinha limpa. Como o tubo é inviolável e indestrutível, cada fichinha vale como registro eterno de que aquela louça foi lavada naquele dia. E basta uma olhadinha no tubo pra saber quem é o próximo a ter que lavar as vasilhas. É o tubo da verdade!

Infelizmente, o sistema só funciona se todos forem honestos. Se dois dos estudantes resolverem agir de má fé e se recusarem a abrir seus cadeados pro cara que acabou de lavar as vasilhas, o sistema deixa de funcionar. Agora, esse risco seria diminuído se morassem nessa república 1000 estudantes em vez de 4, pois as chances de que 50% estivessem agindo de má fé cairiam consideravelmente.
Mas claro, um tubo com 1000 cadeados na sala seria impraticável. Onde a galera vai dormir no carnaval? E se a gente pudesse usar a tecnologia pra utilizar este mesmo princípio no mundo virtual?
Bom, essa tecnologia existe e se chama blockchain. O blockchain nada mais é que um grande arquivão, consultável e transparente como nosso tubo, onde a gente pode “empilhar” registros da mesma maneira que os estudantes de Ouro Preto empilhavam fichinhas. A estes registros nós damos o nome de blocos. E à essa cadeia de blocos damos o nome de…. blockchain! Tchãrã!

Assim como acontecia com as fichinhas no tubo, uma vez um registro é adicionado ao blockchain ele não pode ser retirado nunca mais, passa a ser verdade eterna e absoluta! 

# Passo a passo estrutura blockchain

## Hash

Hash é uma valor numérico de comprimento fixo que identifica unicamente um dado.

`primeira-hash.py`:
```
import hashlib

hashlib.sha256(b'ufscar').hexdigest()
```
Usando o sha256, mesmo algoritmo de hash usado no Bitcoin, temos uma hash com 64 caracteres.
```
hashlib.sha256(b'universidade federal de sao carlos').hexdiges()
```
Alterando para um dado maior, ainda temos uma hash de comprimento igual a anterior, porem unicamente diferente. Sendo assim podemos usar dados pequenos ou enormes e sempre obteremos uma hash de comprimento fixo.

## Block
`block.py`

## Genesis Block

## Links de referência
- https://foxbit.com.br/o-que-e-bitcoin/
- https://en.wikipedia.org/wiki/History_of_bitcoin
- https://medium.com/@fguisso/desvendando-o-blockchain-a0dd2632ee3b
- https://www.criptofacil.com/como-o-bitcoin-resolveu-um-dos-maiores-problemas-da-computacao-descentralizada/
- https://www.collectifbam.fr/projets/realisations/blockchain-vaisselle/resume
- https://medium.com/codando/eli5-explicando-o-blockchain-para-m%CC%B7a%CC%B7c%CC%B7o%CC%B7n%CC%B7h%CC%B7e%CC%B7i%CC%B7r%CC%B7o%CC%B7s%CC%B7-crian%C3%A7as-de-cinco-anos-132c877b8f3f
- https://www.freecodecamp.org/news/how-does-blockchain-really-work-i-built-an-app-to-show-you-6b70cd4caf7d/
- https://blockchaindemo.io/
- https://medium.com/coinmonks/building-a-simple-blockchain-data-structure-with-python-e7ebd448647a
- https://blockchaindemo.io/
- https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b
- https://www.freecodecamp.org/news/how-does-blockchain-really-work-i-built-an-app-to-show-you-6b70cd4caf7d/
