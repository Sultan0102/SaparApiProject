# develop stage
FROM node:16.16-alpine as develop-stage
WORKDIR /app
COPY ./sapar/package*.json ./
RUN npm install
COPY ./sapar .
# build stage
FROM develop-stage as build-stage
RUN npm run build

# production stage
FROM nginx:1.15.7-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]