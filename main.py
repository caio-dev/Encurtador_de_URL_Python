import pyshorteners

# Inserindo URL original
url = str(input('Insira a URL que deseja encurtar: '))

# Carregando a lib
s = pyshorteners.Shortener()

# Gera URL encurtada
url_final = s.tinyurl.short(url)

print("URL Encurtada: ", url_final)
