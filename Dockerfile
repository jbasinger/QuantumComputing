FROM python
RUN pip install -U pip && pip install qiskit qiskit[visualization]
WORKDIR /code
ENTRYPOINT ["/bin/bash"]