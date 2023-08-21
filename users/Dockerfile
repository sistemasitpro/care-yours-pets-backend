# Dockerfile for NestJS
FROM node:18-alpine AS nest-builder
WORKDIR /app
COPY . .
RUN npm install
RUN npm run build
