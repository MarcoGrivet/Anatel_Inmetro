#==============================================================================

   Projeto 31864 - ANATEL/INMETRO/DIMCI/MEDIÇÃO ANATEL
   
   Meta II   - Estudo e Proposição de Ontologias e Formatos para Coleta e 
   
			   Armazenamento de Dados e Registros do SGM
			   
   Produto I - Coleta de Dados Digitais : Recuperação de Legado
   
   Autor     - Marco Antonio Grivet Mattoso Maia
#============================================================================== 

=== OBJETIVO ===

Analisar os certificados em PDF e obter os chamados "parâmetros primários" destes
certificados, a saber:

	Tipo      - se PDF é textual ou imagem
	Categoria - laboratório de certificação	
	No. do certificado
	Equipamento
	Fabricante
	Modelo
	No. de série 
	Data de calibração

Uma planillha .xlsx é gerada no diretório dos certificados analisados contendo 
esses atributos.

Nesta versão apenas certificados dos laboratório abaixo estão sendo processados.
	Anritsu
	Bird
	Celplan
	CPqD
	CTJ
	INPE
	IPT
	Keysight
	Rodhe & Schwarz

Está sendo providenciado a inclusão dos laboratórios:
	FLIR
	PUCRS
	WaveControl
	
	
=== UTILIZAÇÃO ===

Para rodar este programa, recomenda-se o ambiente Visual Studio Code ou PyCharm.
As dependências de biblioteca podem ser instaladas no terminal de qualquer um 
destes ambientes através do comando:
	> pip install requirements.txt
	
O programa mestre a ser rodado chama-se Processor_Phase1.py	
		
Passo 1:
Alterar linhas 16 e 18 do arquivo Processor_Phase1.py para apontar para o 
diretório que contém os certificados em PDF (veja os comentários nas linhas 15 e 17)

Passo 2:
Alterar nas linhas 23 e 24 deste mesmo arquivo, os números iniciais e finais
dos certificados a serem processados. Certificados textuais demoram cerca de 1 seg
para serem processados enquanto que os flattened (imagem) demoram tipicamente 20 seg.
Assim para que o processamento não seja muito demorado em caso de testes iniciais,
esses limites foram impostos.

=== REPORT DE FALHAS ===

Nos casos em que o programa tenha um comportamento incorreto, favor enviar certificado
PDF para o email marcogrivet@gmail.com explicando brevemente a falha.


