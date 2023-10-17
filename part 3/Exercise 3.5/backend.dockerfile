FROM golang
WORKDIR ./app
RUN adduser -S backend
USER backend 
COPY ./example-backend .
RUN go build
RUN go test ./...
EXPOSE 8080
CMD ["./server"]