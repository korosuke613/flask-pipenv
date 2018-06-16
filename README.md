```bash
docker run --rm -d -p 80:5000 -v $PWD:/app --name flask-container korosuke613/flask-pipenv 
```

```bash
sudo yum update
sudo yum install -y docker
sudo service docker start
sudo usermod -a -G docker ec2-user
```