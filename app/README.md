## Sistema de Gestão de informações de sensores de campo

Este projeto foi desenvolvido para receber os dados enviados por sensores de campo que através de um controlador enviarão dados de 5 em 5 minutos. 

## Funcionalidades
- Interface gráfica para cadastro de  :
  Fabricantes, Unidade de Medida, Tipo de Sensor, Sensor e  Equipamentos
- Gestão de usuários e permissões.

## Api rest
- O controlador poderá enviar os dados para o RfControl através das rotas disponíveis em:
 api/v1/docs/swagger/

## Segurança
- O Administrador poderá fazer a gestão de usuários , definindo quem terá acesso a cada funcionalidade do sistema. 
- Essas permissões serão aplicadas também as rotas da api. 
- Para consumir as rotas api, será necessário ter um token jwt, que será gerado para o usuário através da rota :
api/v1/autenticacao/token

O token terá a duração de 1 dia. 

Para gerar o token será necessário fazer login com usuário e senha.

## Tecnologias utilizadas 
- Django
- django rest
- Postgresql (banco de dados)
- Nginx - Servidor web
- uwsgi - servidor wsgi
- certbot para https

