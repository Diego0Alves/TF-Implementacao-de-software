# TF01 - 

## Aluno
- **Nome.** Diego Alves da Silva
- **RA.** 6324649
- **Curso** Análise e Desenvolvimento de Sitemas

## Empresa Fictícia
- **Nome:** TechFix
- **Ramo:** Tecnologia da informação
- **Descrição:** TechFix é uma empresa de assistência técnica para problemas de software ou hardware

## Como Executar

### Pré-requisitos
- Ubuntu 20.04+ ou similar
- Acesso sudo

### Instalação

```bash
# Clone o repositório
git clone https://github.com/Diego0Alves/TF-Implementacao-de-software
```
```bash
cd TF-Implementacao-de-software/TF01
```
# Execute o script de instalação

```bash
chmod +x scripts/install.sh
sudo ./scripts/install.sh
```

Acesso:

Pagina inicial do site: http://localhost

Páginas disponíveis:
/ (Home)
/sobre.html
/servicos.html
/contato.html

Configurações Aplicadas

Nginx configurado com virtual host personalizado

Logs personalizados em /var/log/nginx/

Permissões configuradas para usuário atual

Página 404 customizada

Comandos Úteis

```bash
# Verificar status do Nginx
sudo systemctl status nginx
```
```bash
# Ver logs de acesso
sudo tail -f /var/log/nginx/access.log
```
```bash
# Ver logs de erro
sudo tail -f /var/log/nginx/error.log
```