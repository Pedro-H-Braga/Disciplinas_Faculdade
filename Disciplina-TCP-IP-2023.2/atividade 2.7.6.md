# Respostas da atividade sobre segurança em uma rede de switch
**Nome switch**: <br> 
`enable` >> `conf t` >> `hostname S1` <br> 
**Senha no switch**: <br> 
`enable` >> `conf t` >> `lina console 0` >> `password cisco` <br> 
**Senha modo privilegiado**: <br> 
`enable` >> `conf t` >> `enable secret class` <br> 
**banner para exibição**: <br> 
`enable` >> `conf t` >> `banner motd # Somente Acesso Autorizado. Infratores sofrerao as consequencias da lei. #` <br> 
**Salvando configurações**: <br> 
`enable` >> `copy running-config startup-config` <br> 


# Configurando conexão SSH
## Gerando par de chaves, mudar nome e domínio
- `crypto key generate rsa` -> Tem que ter um hostname no switch
- `ip domain-name ifrn.local` -> criando dominio numa rede local
- `crypto key generate rsa` -> 1024
## Numa conexão ssh precisa de usuario e senha
- `username admin secret 1234` -> criando usuario e senha para acesso ao switch
## Configurando modos de comunicação
- `line vty 0 15` -> deixando todas as vty com a mesma configuração
- `transport input ssh` -> modos de conexão
- `login local`
