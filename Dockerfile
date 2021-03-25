FROM python:3.9 as builder

WORKDIR /usr/src/Rest_News

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update
RUN apt upgrade -y && apt install -y postgresql gcc python3-dev musl-dev
RUN pip install --upgrade pip

COPY . .

COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --weel-dir /usr/src/Rest_News/wheels -r requirements.txt

FROM python:3.9

RUN mkdir -p /home/Rest_News

RUN groupadd restnews
RUN useradd -m -g restnews admin -p Password
RUN usermod -aG restnews admin

ENV HOME=/home/Rest_News
ENV APP_HOME=/home/Rest_News/web

RUN mkdir $APP_HOME
WORKDIR %APP_HOME

RUN apt update && apt install -y netcat

COPY --from=builder /usr/src/Rest_News/wheels /wheels
COPY --from=builder /usr/src/Rest_News/requirements.txt .
RUN pip install --no-cache /wheels/*

COPY ./entrypoint.sh $APP_HOME
COPY . $APP_HOME

RUN chown -R admin:admin

USER admin

ENTRYPOINT ["/home/Rest_New/web/entrypoint.sh"]