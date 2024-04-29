# frb-voe
 Virtual Observatory Events for Fast Radio Bursts

Layout:
- observatory (L4) will send an HTML request contiaining all the information needed to create a VOEvent to voe.
- voe will validate the dictionary using Pydantic, publish it to comet and save it to a MongoDB
- voe will periodically check the MongoDB for new subscribers and for newly retracted FRBs
- voe will also be able to submit FRBs from the MongoDB to the TNS through a CLI

Desired Features:
- easy installation through docker to compose the voe service, MongoDB, and comet service in one swoop
