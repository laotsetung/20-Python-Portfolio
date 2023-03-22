<b>verip</b>

  simples app que busca a Geolocalização do IP, utilizando um script linux (verip) que chama a aplicação Python eu posso simplesmente digitar no terminal
  
<b>verip (ENDEREÇO_DE_IP)</b>
  
  Usando a lib requests para conseguir informações basicas do IP a partir de um arquivo JSON, 
  resgatamos além do Pais e Continente obtemos Latitude e Longitude, e com esses dados fazemos uma nova busca mais refinada.

Usando a lib: Nominatim do pacote 'geopy' para tentar resgatar informações exatas de local como Cidade e até mesmo Rua. (Aproximadamente) 
A maioria das excessões de erro foram adicionadas, como por exemplo verificação de IP válido.
...porém o app ainda contém bugs e vai simplesmente travar ocasionalmente.

***Mais do que tudo, isto é só um aquecimento em programação e também um aprendizado da plataforma git / github
