from PIL import Image

def separateRGB(img):

	#print('Iniciando separação de imagem...')
	#Pegamos cada 'Valor' em pixels
	data = img.getdata()
	#print('Data:', data)

	#Vamos então suprimir cada uma das bandas((255, 120, 65) -> (0, 120, 0) para G)
	r = [(d[0], 0, 0) for d in data]
	g = [(0, d[1], 0) for d in data]
	b = [(0, 0, d[2]) for d in data]

	#invertido = [(255 - d[0], 255 - d[1], 255 - d[2]) for d in data]

	#Salva imagens em R, G e B
	img.putdata(r)
	img.save('Imagens/R.png')
	img.putdata(g)
	img.save('Imagens/G.png')
	img.putdata(b)
	img.save('Imagens/B.png')
	#img.putdata(invertido)
	#img.save('Imagens/Negativo.png')

	#print('Conversão Completa!')

	return r, g, b

def main():
	#imgName = input("Digite o nome da imagem com sua devida extensão: ")
	imgName = 'rainbow.png'

	img = Image.open(imgName)

	#print('Carregando a imagem...\n')

	#print('Imagem:', imgName, '\n')

	r, g, b = separateRGB(img)


if __name__ == "__main__":
	main()