compose := "docker-compose.yaml"

start: 
	docker-compose -f ${compose} build
	docker-compose -f ${compose} up






