#Persistent
+F1:: ;Inicia Script (shift+f1)
SetMouseDelay, -1 ;Delay Mouse
SetTimer, EXEMPLO_DE_ROTINA_X_SEGUNDOS, 300 ;Executa a rotina de busca a cada x segundos...
Return

EXEMPLO_DE_ROTINA_X_SEGUNDOS:
CoordMode, Pixel, Screen  ;Ajusta para que a coordenada informada ao PixelSearch seja relativa à tela inteira do computador.
PixelSearch, PosX, PosY, 0, 0, 3000, 3000, 0xFF2929, 1, FAST RGB ;Busca um pixel vermelho com tonalidade hexadecimal !!NECESSARIO ALTERAR EFEITO DO MOB!! Variação até x tons. Área de busca x a partir do canto superior-esquerdo da tela.

if (ErrorLevel = 0) ;Se ErrorLevel continuar 0 depois do comando, o comando encontrou um pixel na cor das especificações.
{	
	Sleep, 300
	Funcao_Exemplo(PosX, PosY) ;Chama a função Funcao_Exemplo passando para ela os valores de PosX e PosY como sendo os parâmetros Posicao_X e Posicao_Y.
}
Else
{
	send, {f4} ; Caso não ache o pixel setado, pressiona atalho de teleporte
}
Return

;Posiciona o mouse em cima do pixel(mob) informado e executa skill
Funcao_Exemplo(Posicao_X, Posicao_Y)
{
	CoordMode, Mouse, Screen ; Ajusta para que a coordenada informada ao MouseMove seja relativa à tela inteira do computador.
	send, {f2} ; Pressiona tecla a setada
	MouseClick, Left,%Posicao_X%, %Posicao_Y%, , , , ; Clica com o botão esquerdo nas coordenadas armazenadas na variavel.
	Sleep, 300 ; Aguarda 300 milisegundos para teleportar
	send, {f4} ; Pressiona atalho de teleporte
}
^u::Pause ; Pausa Script (ctrl+U)
Return
