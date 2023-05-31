package com.minikube.sample;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@EnableAutoConfiguration
public class MinikubeSampleApplication {

    public static void main(String[] args) {

        SpringApplication.run(MinikubeSampleApplication.class, args);
    }
}
