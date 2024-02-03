#!/bin/bash
sysbench --test=cpu --cpu-max-prime=1000 --time=30 run

