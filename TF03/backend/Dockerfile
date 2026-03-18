FROM node:18-alpine

WORKDIR /app

# package.json and package-lock.json are in repo root
COPY package.json package-lock.json* ./
RUN npm install

# Backend source is in backend/ folder
COPY backend/. ./

EXPOSE 5000

CMD ["node", "app.js"]