#!/bin/sh


getpid(){
    PID=$(pgrep -f "python manage.py run")
    if [ "x$?" != "x0" ]
    then
        PID=''
    fi
    echo $PID
}


start()
{
    echo 'start ...'

    PID=$(getpid)
    if [ "x$PID" != "x" ]
    then
        echo "nimitz is running"
        exit 0
    fi
<<<<<<< HEAD:run.sh
    filepath=$(cd "$(dirname "$0")";pwd)
    cd $filepath
    nohup python manage.py run &
=======

    nohup python sweb.py &
>>>>>>> 8e16c726511b17e5765306090a1e222b112d1b39:sweb.sh
    sleep 1
}

stop()
{
    echo 'stop ...'
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

case $1 in
    start)
        start
        ;;
    stop)
        stop
        ;;
    restart)
        echo "restart ..."
        stop
        start
        ;;
    status)
        getpid
        ;;
esac






