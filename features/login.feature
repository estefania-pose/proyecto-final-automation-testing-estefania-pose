@ui @smoke
Feature: Autenticacion en SauceDemo
  Como usuario registrado
  Quiero iniciar sesion en la plataforma
  Para acceder al catalogo de productos

  Background:
    Given estoy en la pagina de login de SauceDemo

  Scenario: Login exitoso con credenciales validas
    When ingreso usuario "standard_user" y contrasena "secret_sauce"
    Then ingreso correctamente al inventario

  Scenario Outline: Login fallido con credenciales invalidas o bloqueadas
    When ingreso usuario "<usuario>" y contrasena "<clave>"
    Then visualizo un mensaje de error en pantalla

  Examples:
  | usuario         | password        |
  | locked_out_user | secret_sauce    |
  | usuario_malo    | password_malo   |
  | standard_user   | clave_incorrecta|