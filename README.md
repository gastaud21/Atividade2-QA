Aluno Rodrigo Duarte Gastaud

Foram feitos dois testes:

Desenvolvimento de testes funcionais em nível de sistema para testar a aplicação web desenvolvida:
Feature: Compra de produto no SauceDemo

  Scenario: Comprar um item com sucesso
    Given que o usuário está logado no SauceDemo
    When ele adiciona um item ao carrinho
    And finaliza a compra com dados válidos
    Then ele deve ver a mensagem de confirmação da compra



Desenvolvimento de testes unitários para testar o código-fonte da aplicação web desenvolvida.

Feature: Login no site SauceDemo

  Scenario: Login com usuário e senha válidos
    Given que o usuário está na página de login do SauceDemo
    When ele insere um nome de usuário e senha válidos
    And ele envia o formulário de login
    Then ele deve ser redirecionado para a página de inventário
