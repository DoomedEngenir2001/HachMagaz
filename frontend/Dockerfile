FROM node:alpine as build
# Copy custom Nginx configuration
COPY package.json package.json
# RUN npm install
# COPY . .
# RUN npm run build
# FROM nginx:stable-alpine
COPY  /dist /usr/share/nginx/html
COPY  nginx.conf /etc/nginx/conf.d/default.conf
# Copy project to nginx
COPY /dist /usr/share/nginx/html/
EXPOSE 5173
CMD ["nginx", "-g", "daemon off;"]