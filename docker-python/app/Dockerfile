FROM python:3.9.21

WORKDIR /usr/src/app

RUN pip install --no-cache-dir \
    beautifulsoup4 \
    pandas \
    ipykernel \
    requests \
    mysql \
    mysql-connector-python \
    scikit-learn

RUN echo "alias ll='ls -al'" >> /root/.bashrc

CMD ["tail", "-f", "/dev/null"]
