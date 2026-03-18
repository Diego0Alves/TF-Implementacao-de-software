FROM node:18-alpine

RUN npm install -g http-server

WORKDIR /app
COPY . .

EXPOSE 3000

CMD ["http-server", "-p", "3000", "-c-1"]