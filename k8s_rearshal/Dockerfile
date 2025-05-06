# Use a modern Node.js base image
FROM node:18-alpine
# Set the working directory
WORKDIR /app
# Copy your application code
COPY app.js .
# Use a more flexible entrypoint
EXPOSE 8080
CMD ["node", "app.js"]

