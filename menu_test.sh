#!/bin/bash

function _menuPrincipal()
{
    cat banner.txt
    echo
    #echo "Please choose an option :"
    echo
    echo "1) Update checker"
    echo "2) Multiple machine search"
    echo "3) Single machine search"
    echo "4) Modify the checker and push the changes"
    echo "5) Quit"
    echo
    echo -n "Please choose an option :"
}

function _submenu1()
{
    echo
    echo "1) Normal"
    echo "2) Verbose"
    echo "3) Back to the main menu"
    echo
    echo -n "Please choose an option: "
}

function _submenu2()
{
    echo
    echo "1) Windows"
    echo "2) OSX"
    echo "3) Linux"
    echo "4) Linux TW"
    echo "5) Back to the main menu"
    echo
    echo -n "Please choose an option: "
}
function _submenu3()
{
    echo
    echo "1) Edit the taskcluster-worker-checker"
    echo "2) Push changes to the repo (experimental)"
    echo "3) Back to the main menu"
    echo
    echo -n "Please choose an option: "
}

opc=0
until [ $opc -eq 5 ]
do
    case $opc in
        '1') git pull;;
        2)
            opc1=0
            until [ $opc1 -eq 3 ]
            do
                case $opc1 in
                    1)  echo "Loading the Loading message"
                        python3 client.py -w win && python3 client.py -w osx && python3 client.py -w linux && python3 client.py -w linuxtw
                        ;;
                    2)  echo "following the white rabbit.."
                        python3 client.py -w win -v true && python3 client.py -w osx -v true && python3 client.py -w linux -v true && python3 client.py -w linuxtw -v true
                        ;;
                    3)
                        ;;
                    *)
                        _submenu1
                        ;;
                esac
                read opc1
            done
            _menuPrincipal
            ;;
        3)
            opc2=0
            until [ $opc2 -eq 5 ]
            do
                case $opc2 in
                    1)  clear
                        echo "Searching for Windows machines"
                        python3 client.py -w win -v true
                        ;;
                    2)  clear
                        echo "Searching for OSX machines"
                        python3 client.py -w osx -v true
                        ;;
                    3)  clear
                        echo "Searching for Linux machines"
                        python3 client.py -w linux -v true
                        ;;
                    4)  clear
                        echo "Searching for Linux TW machines"
                        python3 client.py -w linuxtw -v true
                        ;;
                    *)
                        _submenu2
                        ;;
                esac
                read opc2
            done
            _menuPrincipal
            ;;
        4)
          opc3=0
          until [ $opc3 -eq 3 ]
          do
              case $opc3 in
                  1) clear
                    echo "Modify the taskcluster-worker-checker"
                    pluma test1file.txt
                    ;;
                  2) clear
                    echo "Update the repository with the latest news"
                    Automation/experimental_push.sh
                    ;;
                 *)
                    _submenu3
                    ;;
                esac
                read opc3
            done
            _menuPrincipal
            ;;
        *)
            _menuPrincipal
            ;;
    esac
    read opc
done
