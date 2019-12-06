NAME=flaskapp

run:
	sudo chown 1000:1000 -R ./mysql/data
	docker-compose build
	docker-compose up -d

stop:
	docker stop ${NAME}_uwsgi_1 ${NAME}_nginx_1 ${NAME}_mysql_1
	docker rm ${NAME}_uwsgi_1 ${NAME}_nginx_1 ${NAME}_mysql_1

reboot:
	make stop
	make run
