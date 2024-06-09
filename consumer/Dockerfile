FROM golang:1.20-alpine

WORKDIR /app

COPY go.mod ./
RUN go mod download

COPY . .

RUN go get -u github.com/segmentio/kafka-go

RUN go build -o main .

CMD ["./main"]