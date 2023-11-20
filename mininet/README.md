# trabajo-practico-topologia
Topologia del trabajo practico

## Topología

La topología tendrá siempre dos hosts en los extremos (no customizable su cantidad). También dispondrá de una cantidad de switches variables, definada por parámetro, formando una cadena entre ellos.

## Prerrequisitos de instalacion en Ubuntu para mininet

```
sudo apt-get -y install xterm
```

## Instalación de mininet en Ubuntu

```
sudo apt-get install mininet
```

## Como correr la topologia 

Desde la consola ejecutar (por ejemplo con 2 switches):

```
python3 create_topology_from_scratch.py 2
```

El parámetro es referido a la cantidad de switches, y tiene que ser un número positivo, mayor a 1 y menor o igual a 10. Debe ser mayor a 1 porque como mínimo debe existir un switch entre los hosts extremos.

## Cómo utilizar mininet

Para correr la consola de un host:

```
h1 xterm &
```

## Logs creados

Se creará un archivo con la cantidad de switches definidos (pasados como parámetros al momento de la creación de la topología).

## Troubleshoot

En caso de que no corra mininet con un error relacionado a los controllers, intentar con este comando:

```
sudo fuser -k 6653/tcp
```
