/* 

FAZENDO BACKUP NO MYSQL WORKBENCH (Data Export)


ONDE CLICAR:
   - No menu superior, vá em: Server -> Data Export 
   (OU na aba "Administration" no canto inferior esquerdo -> Data Export).

O QUE SELECIONAR E POR QUÊ:

   [A] Tabela / Banco de Dados (Object Selection):
       - Marque a caixinha do banco de dados que deseja salvar (ex: 'empresa').
       - Por quê? Isso diz ao Workbench de qual banco ele deve extrair os dados.

   [B] Formato de Exportação (Export Options):
       - Marque: "Export to Self-Contained File"
       - Por quê? Essa opção junta a estrutura e todos os dados em um ÚNICO 
         arquivo de texto (.sql). É a forma mais simples de guardar e transportar.
       - A outra opção ("Export to Dump Project Folder") cria vários arquivos 
         separados por tabela, o que costuma ser desnecessário para o dia a dia.

   [C] Opções Adicionais (Canto inferior direito):
       - Marque: "Include Create Schema"
       - Por quê? Essa opção adiciona a instrução 'CREATE DATABASE' no início 
         do arquivo. Se você precisar restaurar esse backup em outro computador 
         onde o banco ainda não existe, o MySQL cria o banco sozinho antes de 
         povoar as tabelas.

FINALIZANDO:
   - Clique no botão de reticências (...) para escolher a pasta no PC e o nome do arquivo.
   - Clique em "Start Export" (canto inferior direito).
   - Aguarde a barra carregar até 100% ("Export Completed").

*/