import requests 

def main():
  #zip code (CEP) input
  cep_input = input('Digite o seu CEP: ')
  
  #check if zip code has 8 numbers, if not error msg
  if len(cep_input) != 8:
    print('CEP Inválido')
    exit()
  
  request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))
  adress_data = request.json() 
  
  #show de json requests response, if cep not exist error msg
  if 'erro' not in adress_data: 
    print('CEP : {}'.format(adress_data['cep']))
    print('Bairro : {}'.format(adress_data['bairro']))
    print('Complemento : {}'.format(adress_data['complemento']))
    print('Localidade : {}'.format(adress_data['localidade']))
    print('Estado : {}'.format(adress_data['uf']))
    
    
    #print(request.json())
  else: 
    print('CEP Inválido')
if __name__ == '__main__':
  main()