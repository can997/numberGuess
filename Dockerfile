FROM ubuntu
RUN apt-get update\
    && agt-get install -y python3
COPY guessNumber.py guessNumber
CMD ["python3","guessNumber/guessNumber.py]
