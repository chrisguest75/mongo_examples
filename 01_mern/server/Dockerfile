FROM node:14.17.1 as prod

ARG USERID=1001
ARG GROUPID=1001
RUN addgroup --system --gid $GROUPID nodeuser
RUN adduser --system --uid $USERID --gid $GROUPID nodeuser

WORKDIR /scratch
COPY package.json package-lock.json ./
COPY server.js ./
COPY routes routes 
COPY db db 

RUN npm ci --only=production && npm cache clean --force
USER nodeuser
EXPOSE 3000 
CMD [ "node", "server.js" ]

