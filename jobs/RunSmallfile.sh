#!/bin/bash

run_smallfile()
{
	cd /''Downloads/''smallfile
	case "$1" in
        create)
            python smallfile/smallfile_cli.py --operation create --threads 8  --file-size 64 --files $2 --top /$3 --pause 1000
            ;;
        append)
            python smallfile/smallfile_cli.py --operation append --threads 8  --file-size 64 --files $2 --top /$3 --pause 1000
            ;;
        read)
            python smallfile/smallfile_cli.py --operation read --threads 8  --file-size 64 --files $2 --top /$3 --pause 1000 -
            ;;
        rename)
            python smallfile/smallfile_cli.py --operation rename --threads 8  --file-size 64 --files $2 --top /$3 --pause 1000
            ;;
        mkdir)
            python smallfile/smallfile_cli.py --operation mkdir --threads 8  --file-size 64 --files $2 --top /$3 --pause 1000
            ;;
        rmdir)
            python smallfile/smallfile_cli.py --operation rmdir --threads 8  --file-size 64 --files $2 --top /$3 --pause 1000
            ;;
        delete-renamed)
            python smallfile/smallfile_cli.py --operation delete-renamed --threads 8  --file-size 64 --files $2 --top /$3 --pause 1000
            ;;
        ls-l)
            python smallfile/smallfile_cli.py --operation ls-l --threads 8  --file-size 64 --files $2 --top /$3 --pause 500
            ;;
	esac
}

source=${BASH_SOURCE[0]}
	if [ $source == $0 ]; then
		run_smallfile $1 $2 $3
	fi

