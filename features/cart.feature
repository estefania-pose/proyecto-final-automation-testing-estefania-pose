@ui @regression
Feature: Carrito de compras en SauceDemo
  Como comprador autenticado
  Quiero agregar productos al carrito
  Para preparar mi compra

  Background:
    Given estoy en la pagina de login de SauceDemo
    When ingreso usuario "standard_user" y contrasena "secret_sauce"

  Scenario: Agregar un producto al carrito
    And agrego el producto "Sauce Labs Backpack" al carrito
    Then el contador del carrito muestra "1"