FROM golang:1.21.3-alpine3.18
WORKDIR ./app
COPY ./example-backend .
RUN go build && \
	go test ./... && \
	rm -rf /var/lib/apt/lists/* && \
	adduser -S locall 
EXPOSE 8080
ENV REQUEST_ORIGIN=http://localhost:3000
USER locall
CMD ["./server"]