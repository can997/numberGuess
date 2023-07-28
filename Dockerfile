FROM ubuntu
RUN apt-get update\
    && apt-get install -y python3
COPY numberGuess.py /opt/guessNumber/numberGuess.py
WORKDIR /opt/guessNumber
CMD ["python3","numberGuess.py"]
