# voe
 Virtual Observatory Events for Fast Radio Bursts

Layout:
- L4 will send a dictionary contiaining all the information needed to create a VOEvent to voe.
- voe will validate the dictionary, publish it to comet, publish it to a MongoDB
- voe will also be able to read the MongoDB to submit events to the TNS

Desired Features:
- easy installation through docker to compose the voe service, MongoDB, and comet service in one swoop
