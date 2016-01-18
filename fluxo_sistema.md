
## Fluxo do Sistema:

- Cadastro de Categorias: (carro, moto, caminhão, ...)  
    -- Informar a categoria e o CNH dela  
        ex: Nome: Moto , CNH : A   
        ex: Nome: Carro , CNH : B,C  
- Cadastro de Veículos da locadora  
    -- Informar Modelo, categoria, quilometragem atual  
        ex: Modelo: Palio, Categoria: (selectBox), Quilometragem: 10        
    - o checkbox disponível informa que aquele veículo esta disponível para locação.  
- Cadastro do Cliente que deseja fazer a locação  
    -- Informar dados do Cliente:  
       ex: Nome: Lucas, CPF : 12345678901, CNH: A, B   
    -- campo Email e Telefone são opcionais   
    -- caso o cliente deseje efetuar uma reserva o email deverá ser obrigatório  
- Cadastrar uma locação ( irá basicamente associar um veículo a um cliente informando a data inicial e final da locação e o valor)  
    -- Informa o Cliente, o Veículo, Data Inicial e Final da locação, valor  
  
- Registrando Devolução   
    -- Para registrar uma devolução entre na página de Locação e clique na opção "devolução"  
    -- o Sistema irá redicionar para a pagina de devolução onde precisara informar somente o km_rodado  
  
--Efetuar Reserva  
    -- O Sistema permite que o cliente faça uma reserva do veículo quando o mesmo estiver em uso.  
    -- Existem duas formas:  
        -- Entrando na página de veículos irá aparecer uma opção "Reserva" caso o veículo estaja indisponível  
        -- Entrando na página de reserva clicar no botão "Nova Reserva", a lista de veículos mostrar somente os veículos que estão alugados no momento.  
    -- Informe o nome para a sua reserva e salve.  
    -- Assim que o veículo for devolvido, você recebera no email cadastrado a notificação de reserva disponível.  
    -- Quando o cliente confirmar a reserva ou desistir, o usuário devera editar a reservar emarcar o checkbox "Finalizada".  
  
  
Um demo do sistema pode ser acessado no link abaixo: 
  
[https://locadora-lucasfarias.herokuapp.com/](https://www.github.com)  

