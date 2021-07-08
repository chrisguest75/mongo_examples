FROM node:14.17.1 as build

ARG USERID=1001
ARG GROUPID=1001
RUN addgroup --system --gid $GROUPID nodeuser
RUN adduser --system --uid $USERID --gid $GROUPID nodeuser

WORKDIR /scratch
COPY package.json package-lock.json ./
COPY public public
COPY src src 

RUN npm install
RUN npm run build

FROM nginx:1.21.0 as prod
COPY --from=build /scratch/build /usr/share/nginx/html

