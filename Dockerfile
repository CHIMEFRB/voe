FROM python:3.12-slim as BASE

COPY . /voe
WORKDIR /voe

SHELL ["/bin/bash", "-c"]

RUN pip install .

CMD ["bash"]