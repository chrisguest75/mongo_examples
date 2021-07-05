FROM node:14.17.1 as prod

ARG USERID=1001
ARG GROUPID=1001
RUN addgroup --system --gid $GROUPID nodeuser
RUN adduser --system --uid $USERID --gid $GROUPID nodeuser

WORKDIR /scratch
COPY package.json package-lock.json ./
COPY public public
COPY src src 

RUN npm ci --only=production && npm cache clean --force
USER nodeuser
ENV PORT 3001
ENV NODE_ENV production
EXPOSE 3001 
CMD [ "npm", "start" ]

