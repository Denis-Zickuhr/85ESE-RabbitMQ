#!/bin/bash

# Encontrar o PID do processo que está usando a porta 3306
pid=$(sudo lsof -t -i:3306)

# Encerrar o processo usando o PID
if [ -n "$pid" ]; then
    sudo kill -9 $pid
    echo "Processo com PID $pid encerrado."
else
    echo "Nenhum processo encontrado usando a porta 3306."
fi