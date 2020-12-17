#!/bin/bash

# setup colors
NC='\033[0m' # No Color
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[1;34m'

# getting env vars
set -o allexport
source .env
set +o allexport

echo ";----------------------------;"
echo "; Docker compose bash script ;"
echo ";----------------------------;"
echo "Usage:"
echo "    ./docker-shell.sh <service_name> (default: web)"
echo "Ex:"
echo "    ./docker-shell.sh nginx"
echo ""
CONTAINER_NAME=web
if [[ -n $1 ]]; then
    CONTAINER_NAME=$1
fi

FULLNAME=${COMPOSE_PROJECT_NAME}_${CONTAINER_NAME}

echo -e "${YELLOW}opening bash for container: ${BLUE}${FULLNAME}.${NC}"

docker exec -i -t ${FULLNAME} /bin/bash
if [ $? -eq 0 ]; then
    echo -e "${GREEN}closed bash for ${FULLNAME}.${NC}"
else
    echo -e "${RED}Open bash for ${FULLNAME} has failed! \nPlease, check you service name and your COMPOSE_PROJECT_NAME env variable.${NC}"
fi
