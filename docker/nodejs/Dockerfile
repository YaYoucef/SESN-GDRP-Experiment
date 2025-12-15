FROM node:18-alpine

WORKDIR /app

COPY node-app/package.json .
RUN npm install

COPY node-app/ .
COPY data /data

CMD ["npm", "start"]
