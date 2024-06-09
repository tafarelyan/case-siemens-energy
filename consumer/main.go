package main

import (
	"context"
	"fmt"
	"log"

	"github.com/segmentio/kafka-go"
)

func main() {
	topic := "siemens_energy"
	brokerAddress := "kafka:9092"

	r := kafka.NewReader(kafka.ReaderConfig{
		Brokers:   []string{brokerAddress},
		Topic:     topic,
		Partition: 0,
		MaxBytes:  10e6, // 10MB
	})

	for {
		m, err := r.ReadMessage(context.Background())
		if err != nil {
			break
		}
		fmt.Printf("Mensagem no offset %d: %s = %s\n", m.Offset, string(m.Key), string(m.Value))
	}

	if err := r.Close(); err != nil {
		log.Fatal("failed to close reader:", err)
	}

}