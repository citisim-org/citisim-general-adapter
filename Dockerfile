FROM python:3.6
RUN wget -qO- http://pike.esi.uclm.es/add-pike-repo.sh | sh 
RUN wget -q "http://keyserver.ubuntu.com:11371/pks/lookup?op=get&search=0xB6391CB2CFBA643D" -O- wget -O-  | apt-key add -
RUN echo "deb http://zeroc.com/download/Ice/3.7/debian9 stable main" > /etc/apt/sources.list.d/zeroc.list
RUN apt-get update -y
RUN apt-get install python3-zeroc-ice -y
RUN apt-get install libcitisim -y
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN mv /usr/lib/python3/dist-packages/IcePy*.so /usr/lib/python3/dist-packages/IcePy.so
CMD ["bash"]
