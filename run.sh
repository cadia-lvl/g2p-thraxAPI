docker container stop g2p
docker container rm g2p
docker build . -t g2p:example --progress=plain
docker run -d --name=g2p -p 8080:8080 g2p:example
