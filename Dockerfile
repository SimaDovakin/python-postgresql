FROM python:3.8

RUN useradd --create-home --shell /bin/bash app_user
WORKDIR /home/app_user

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

USER app_user
COPY . .

CMD ["bash"]

