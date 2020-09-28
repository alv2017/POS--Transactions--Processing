FROM mysql

RUN apt-get update
RUN apt-get -y install git
RUN apt-get -y install vim
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN pip3 install mysql-connector-python

RUN mkdir /opt/POS

RUN cd /opt/POS && git clone https://github.com/alv2017/POS--Transactions--Processing.git && \
	mv POS--Transactions--Processing POS_Transactions && \
	cd POS_Transactions && git pull origin master 
	
RUN cd /opt/POS/POS_Transactions/config && mv config_example.ini config.ini
	
RUN cp /opt/POS/POS_Transactions/db/sql/db_script.sql /docker-entrypoint-initdb.d/

ENV MYSQL_ROOT_PASSWORD=test123
