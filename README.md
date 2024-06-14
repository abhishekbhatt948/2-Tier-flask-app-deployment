# 2-Tier-flask-app-deployment
Project : 2-Tier Flask application deployment.

Part 1: Application Create.
  - Create MYsql Flask App which query to mysql database and show result.  // Create in Local repository.
  - Create Mysql Config file which have database and connect information.  // mysql Database.

  - Test both in local system Run Correctly or Not.
  - NOTE: Before move to next phase application must run.

Part 2: GitLab and Repository Deploy on Server.
  - here we used GitLab to deploy repository into remote server(AWS Cloud /EC2 Instance).
  - create repository into gitlab and upload your local repository files into gitlab using git push and pull method. (Makesure you know about how to works on Git). vai SSH or HTTPS.
  - in Gitlab have to create .gitlab-ci.yml configure files to deploy repository. here we only used Deploy stage becaz only transfer files using scp method.
    NOTE: before trying to move must have webserver on AWS/EC2 Instance. Here i am already create 2 webserver 1.K8s Master Node and 2. K8s-worker node. (you will get why this name.)
  - in gitlab project/setting/CI/CD/variables : you have to create variables such as $AWS_USERNAME, $AWS_INSTANCE_PUB_IP, $SSH_PRIVATE_KEY etc..., as per need.
  - once you transfer your source code files into master server. we start our deployment.
    
Part 3: Deployment Into Docker-Compose.
  - so here we deploy our application into Docker-compose.yml . how :-
  - first we required Dockerfile to build Images of our application. // Dockerfile is a configuration file to build package of any application which is your Images file.
  - after build we upload our Application Image files inot DOCKER-HUB regestry public paltform.
  - now Docker-compose is used to create multiple container from your deployment. for in our case we have flask app and mysql database. so we configure both in one file which is Docker-compose files , so when we        run docker-compose its create our container.
  - run docker-compose.yml .

 - our container is ready and app run on ip:port which we mentioned in files. ip takes from aws instance public ip .

Part 4 : App Deployment On Kubernetes.
  - so we have two webserver one master node and Worker Node.
  - Master node we used as control plane for k8s and worker node for running container/pods.
  - first we need to setup Cluster(is a combination of multiple server running in).
  - for setup cluster check files in folder K8s/installation.
  - once setup done. we come to deployment where we required menifest files. for our application. check ----> k8s folder.
  - update according your application. // must required changes ips/port/ password/database/ etc...
  - if you are going correctly your application run successfully.

Part 5 : Deployment using Helm Chart. 
  --
