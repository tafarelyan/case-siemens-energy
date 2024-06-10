package main

import (
	"context"
	"fmt"

	"github.com/segmentio/kafka-go"
)

func main() {
	topic := "siemens_energy"
	brokerAddress := "kafka:9092"

	r := kafka.NewReader(kafka.ReaderConfig{
		Brokers:   []string{brokerAddress},
		Topic:     topic,
		MaxBytes:  10e6, // 10MB
	})

	defer r.Close()

	for {
		m, err := r.ReadMessage(context.Background())
		if err == nil {
			fmt.Printf("Mensagem no offset %d: %s\n", m.Offset, string(m.Value))
		}
	}
}