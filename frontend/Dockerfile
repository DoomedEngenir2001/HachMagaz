FROM nginx:stable-alpine
# Copy custom Nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf
# Copy project to nginx
COPY /dist /usr/share/nginx/html/
EXPOSE 5173
CMD ["nginx", "-g", "daemon off;"]