# Message brokers VS Message queue
Keeping up with the demands of modern applications is getting more difficult by the day. We now have large volumes of data and information constantly being exchanged online. Some of these exchanges heavily depend on the computers' resources, network speed, and transmission mode. With these exchange comes challenges such as data breaches, data loss, transmission failures, etc. Fortunately, one solution to the challenges highlighted above is a message broker.

## What is a message broker?
A message broker is software that aids communication between services, systems, or applications. They can also route, store, and deliver information to a specified destination. Message brokers foster stable and asynchronous communication between systems. In summary, the essence of a message broker is to provide a stable and reliable means for applications to communicate. **Sounds great, right?** Let's learn some more.
**
## Essential components of a message broker
- **Message**: the bits of information we want to send.
- **Queue**: this is the data structure that describes how the broker executes messages. It is based on FIF0 (First-In-First-Out). A perfect example is a queue at a grocery store.
- **Producer**: is the application that sends the message(s) to the message broker. They are also referred to as publishers.
- **Consumer**: is the application that receives the message(s) from the message broker. They are also referred to as subscribers.
  
- **Topic**: This is a folder used by message brokers to store messages.

## What is a message queue?
Imagine you have two running systems: The first system sends four messages to the second system. Have you ever wondered how the other system knows the message to transmit first from the queue? Let's find out!

A message queue offers an endpoint that enables software components to connect to the queue to send and receive messages and a small buffer that temporarily stores messages. For instance, suppose there are four people in a queue; the first person in the queue is the first person to be attended to. A message queue works the same way as a regular one; the only difference is our message queue contains messages, not people.

## Messaging patterns of message brokers
Message brokers use **two** common messaging styles.
- **Point-to-point**: This messaging style is based on a one-to-one relationship between the sender and receiver of the message. Once a message is sent, it is consumed once. This style is primarily used when one needs an action to be performed once and a sort of guarantee is required. A perfect example is a system that handles financial transactions.
![alt text](https://prosper-django-bucket.s3.us-east-2.amazonaws.com/mephis-1.jpg)

  
- **Publish-Subscribe**: In this style, messages are sent to a topic, after which the message is broadcasted to all endpoints subscribed to that topic. Here, the sender of the message(publisher) does not know anything about the receiver(subscriber). When do I use this messaging style? Imagine a telecommunications company wanting to inform its subscribers about a new feature. Everyone subscribed to that company will receive a notification and decide whether they're interested.
  
![alt text](https://prosper-django-bucket.s3.us-east-2.amazonaws.com/memphis-2.jpg)
  
## What are the metrics of using a message broker?
- **It facilitates asynchronous communication**: Unlike APIs, when you send a message to a system, you don't have to wait for a response. Your message is added to the queue where another system can easily pick it up and execute it, saving us time.
- **Improved interaction between components**: Publishers can send messages whether the consumers are present or not. The only requirement is a working message broker. Consumers can also do the same.
- **Increased Reliability by ensuring message transmission**: Message brokers have an in-built redelivering mechanism that is triggered whenever a failure occurs when delivering messages to a consumer. A failed message is re-sent almost immediately or at some other time(if specified). It also supports the routing of not delivered messages - referred to as the dead-letter mechanism.
  
## Challenges of using a message broker
- **Increased system complexity**: Introducing a message broker into a system is challenging. Due to this, there are several things you must take into account, such as data consistency issues, security issues, and maintenance of the network between components.
- **Debugging can be tedious**: Due to its complexity, locating the source of an error can be challenging as each service has its logs. Hence, the need to add a message-tracing feature is necessary.
  
## Examples of message brokers
Over the years, several message brokers have sprung up. Here are some popular and effective ones. **Memphis, NATS Jetstream, Apache Kafka, RabbitMQ, and Amazon SQS.**

**Here are some main features:**
- **Memphis**: Memphis is the future of conventional message brokers. It offers an ecosystem that supports the reliable and rapid development of queue-based applications that involve large volumes of data, modern protocols, etc. Looking for a simple, cloud-native and robust message broker? **Memphis** is your best bet.
  
- **Kafka**: Kafka is an open-source, distributed event streaming platform that is used as a replacement for conventional message brokers. The key features of Kafka are high scalability, high availability, low latency, and permanent storage.
  
- **Amazon Simple Queue Services**: Amazon Simple Queue Service(ASQS) is a distributed queue service that can receive, store, and send messages between systems. ASQS is designed to handle many tasks without losing any message. It also allows the developer to use custom SSE keys for protecting the queues from data breaches.
- **RabbitMQ**: This is an open-source message broker software that is widely used. It supports several programming languages and thrives in cloud environments. Some of its key features are distributed deployment, asynchronous messaging, and enterprise and cloud readiness.
- **Redis**: Remote Dictionary Server is a fast, distributed, open-source data store used as a message broker. Redis provides support for various data structures (abstract) such as maps, lists, sets, etc. Redis's key features include data persistence, high availability, easy scalability, and an in-memory database.
  
## When to use message brokers?
- **Safeguarding sensitive information**: If your platform requires data transfer between systems, issues related to a data breach are bound to arise. To tackle this challenge, a message broker should be introduced as it offers end-to-end encryption.

- **Notifications on mobile applications**: Modern applications have push notifications. Let's imagine you are developing a telecommunications application. Every phone connected to the network can subscribe to some message broker's topic. In that way, whenever a message is sent to the topic, all subscribers will be notified.
- **E-commerce systems**: For online businesses, implementing an effective and reliable payment system is vital. Message brokers are needed to ensure that messages are consumed once, hence, enhancing order fulfillment.
## Similarities between message brokers and message queues
From the previous definition, a message queue is simply a storage mechanism for messages. At the same time, a message broker is a mechanism that facilitates communication between systems. How are they related? A message queue is just a data structure or a container - a way to store messages until they are consumed. A message broker is a separate component that manages queues. In essence, message brokers use message queues to transmit information between all interested parties.

## Message queues vs. Message brokers: Differences
A queue is a data structure based on FIFO(First-In-First-Out). A message queue orders the way information is to be transmitted. i.e., the first message in the queue should be the first message to be consumed/executed by the consumer. A message queue oversees the ordering of transmitted tasks; they are not interested in the information contained in the task. On the other hand, message brokers are more interested in the conversion, transmission, and routing of data between services. As a result, they can access the information carried through them. **What's the difference?** The queue is the storage for produced data until it is ready to be consumed, while the message broker executes tasks according to the order described by the message queue.
# Conclusion
A message queue is a medium used by applications to send messages. It is not interested in the information contained in the task. The message broker receives the information contained in the message queue, translates it, and delivers it to the specified receiver.**