@echo off
:: ctp, i.e.create post
:: call create_post.py
:: if %1=--draft create draft
if "%2"=="" (
    python .\pyScripts\create_post.py %1
) else if "%1"=="--draft" (
    python .\pyScripts\create_post.py %2 "True"
) else (
    echo \033[31mwrong command arguments\033[0m
)