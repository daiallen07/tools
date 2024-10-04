#dogker install script
sudo apt install docker.io -y
sudo apt install docker-compose -y
docker pull docker.io/kalilinux/kali-rolling
docker run --tty --interactive kalilinux/kali-rolling


#after you get into the docker terminal, run apt update
#then run the script
