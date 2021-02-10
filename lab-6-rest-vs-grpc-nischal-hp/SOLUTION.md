
|  Method 	| Local  	| Same-Zone  	|  SameReg/Diff Zone 	| Europe |
|---------- |---------- |-------------- |-----------------------|--------|
|   REST add	|  2.65 ms 	|  3.58 ms 	|    3.06 ms	| 280.91 ms |
|   gRPC add	|  0.54 ms 	|  0.656 ms 	|  0.741 ms  	| 144.57 ms |
|   REST img	|  3.66 ms 	|  22.53 ms 	|  22.54 ms 	| 1161.3 ms |
|   gRPC img	|  4.8 ms     |  8.2 ms 	|   10.11 ms	| 171.45 ms |
|   PING        |  0.040 ms      | 0.341 ms     |  0.367 ms     | 138.85 ms |


You should examine your results and provide a short paragraph with your observations of the performance difference between REST and gRPC. You should explicitly comment on the role that network latency plays -- it's useful to know that REST makes a new TCP connection for each query while gRPC makes a single TCP connection that is used for all the queries.

## Results:

### 1) Local :
In this test, gRPC was significantly faster than REST when executing the add service, but was a bit slower when executing the image service. This shows that gRPC is designed more for low-latency and hence it is suitable for add function, since it is a light weight function. 

Another reason is that, even when running on a localhost gRPC serializes the data, whereas REST does not do that and hence is faster.

The ping result is 0.040 ms, which means it's very fast.

### 2) Same-Zone :
In this test, gRPC outperformed REST for both the add and the image service. This happens because, there is increased network latency compared to the previous test, as the client and server are running are on two different machines which are physically distant from each other. 

When the network latency increases, gRPC outperforms REST; since gRPC makes a single TCP connection that is used for all the queries. Whereas REST makes a new TCP connection for each query, and this causes REST to perform slowly.

The ping result is 0.341 ms, which is slightly more than running on localhost. But it is still faster.

### 3) SameReg/Diff Zone  :
The results obtained in this test, were similar to the results obtained in the previous test. This goes on to show that it does not matter whether client and server are running in the same-zone or in a diff-zone, as long as they are in the same region.

Similar to the previous test, gRPC outperformed REST for both the add and the image service. This happens because of increased network latency, as the client and server are running are on two different machines which are physically distant from each other.When the network latency increases, gRPC outperforms REST; since gRPC makes a single TCP connection that is used for all the queries. Whereas REST makes a new TCP connection for each query, and this causes REST to perform slowly.

The ping result is 0.367 ms, which is almost the same as previous test. Thus, having two machines in the same-zone of diff-zone does not really matter.

### 4) Europe : 
This test is performed for 100 iterations, unlike other tests which are performed for 1000 iterations. This is to keep the running time manageable.

When the client and server are very distant from each other, that is one being in US and the other being in Europe, even then gRPC outperforms REST just like the previous two tests. This once again boils down to network latency. Since, REST API creates a new TCP connection for every request, this delays the response time. This becomes particularly problematic for heavy-weight calls and also when the distance between client and server is very large, like in this scenario. gRPC creates a single TCP connection that is used for all the queries; hence it overcomes this drawback.

The difference between REST and gRPC is very large for image function specifically. This highlights the advantage of using gRPC over REST for heavy-weight functions.

The ping result is 138.85 ms, which means it's very slow, compared to the other tests. This results in overall poor network latency.

### Conclusion: 
gRPC is preferable to be used over REST for heavy-weight functions, as long as client and server are running on two different machines. 
However, for light-weight functions like the add function, REST can also be used; as the response time difference is not that much. It is also easier to code for REST, than for gRPC.
