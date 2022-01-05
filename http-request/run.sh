for i in $(ls -F | grep /); do
    cd ./${i}
    ./run.sh &
    cd ..
done

exit_script() {
    echo "Printing something special!"
    echo "Maybe executing other commands!"
    trap - SIGINT SIGTERM # clear the trap
    kill -- -$$ # Sends SIGTERM to child/sub processes
    fuser -k 8080/tcp
    fuser -k 8000/tcp
    fuser -k 5000/tcp
    fuser -k 3000/tcp
}


trap exit_script SIGINT
trap exit_script SIGTERM
