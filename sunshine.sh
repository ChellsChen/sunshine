#!/bin/sh

# cd $(dirname $(readlink $0))/baichuan-web


if [ -L "$0" ]
    then
    cd $(dirname $(readlink $0))/baichuan-web
else
    filepath=$(cd "$(dirname "$0")"; pwd)
    cd $filepath/baichuan-web
fi


getpid(){
    PID=$(pgrep -f "python manage.py")
    if [ "x$?" != "x0" ]
    then
        PID=''
    fi
    echo $PID
}


start()
{
    echo '\033[31m start ... \033[0m'

    PID=$(getpid)
    if [ "x$PID" != "x" ]
    then
        echo "\033[34m manage.py is running"
        exit 0
    fi

    python manage.py run &
}

stop()
{
    echo '\033[31m stop ... \033[0m'
    PID=$(getpid)
    while [ "x$PID" != "x" ]
    do
        for p in $PID;
        do
            kill $p
        done
        sleep 1
        PID=$(getpid)
    done
}

initdb()
{
    if [ ! -d "db" ]
    then
        mkdir db
    fi
    echo "\033[34m init user.db ...\033[0m"
    python manage.py createdb
}



case $1 in
    start)
        start
        ;;
    stop)
        stop
        ;;
    restart)
        echo "\033[31m restart ... \033[0m"
        stop
        start
        ;;
    status)
        getpid
        ;;
    initdb)
        initdb
        ;;
esac






