# lightsOnRep
  Lights on Rep is an IOT project that solves the problem of alerting humans that they have an email so they won’t miss important business or school mail through their Gmail account. Several people tend to be late to get to their next destination or never have a reminder to email professors back. 

  In this project, I will be using hardware that connects to the internet and serves some sort of service/solves a problem. Lights on Rep helps the user identify their messages by using Red LED lights. The red light stays on for 5 seconds to represent that you have an email. Five seconds may seem long, however, it stays on long enough so you don’t feel like you’ve missed your message and may feel the need to go back and check. 
  
  This project will eventually form into the original idea which was intended to make a vanity mirror that displays messages through a plexiglass (which has a cost of $400). However, this project was projected to cost less than $60 and only cost $56.13 in total. It is connected to the internet and uses a pub-sub/cloud protocol MQTT (a lightweight IOT protocol that has low bandwidth and is used for smaller devices. The monitor is connected to the raspberry pi, then the raspberry pi is connected to the internet through a Wi-Fi chip that publishes data. The internet then transfers data to DNS, then that information is sent to an IP address, then data is sent to the server/broker then the data is subscribed (user is notified) and displayed.
