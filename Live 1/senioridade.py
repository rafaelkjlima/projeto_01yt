nome = str(input('Qual seu nome: '))
s = int(input('Qual seu nivel de 0 a 12: '))

#classificado para jogar com a gente
if s > 6:
    print('legal podemos começar a conversa.')
    if s > 8:
        dev = str(input('quero tem perguntar, qual engine você tem maior experiencia? '))
        if dev.lower() == 'unreal':
            print('{} entreremos em contato em breve com você.'.format(nome))
        else:
            print('gostamos do seu perfil, porem estamos procurando outras experiencias. \n Obrigado por participar {}'.format(nome))

            #vamos repesar, "estagiario"
elif s > 2 and s <= 6:
    dev2 = str(input('tem experiencia com alguma engine de desenvolvimento? '))
    if dev2 != '':
        print('temos interesse em conhece-lo, melhor {}'.format(nome))
    else:
        print('lamento informar que temos outras preferencia de desenvolvedor para nossos projetos.')
        
else: #negado
    print('Obrigado por participar {} , porem estamos buscando outros perfis.'.format(nome))
    