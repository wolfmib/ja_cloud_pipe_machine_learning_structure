echo "delete the images clean.."
docker image prune -a


echo "clean docker sys prune"
docker system prune
